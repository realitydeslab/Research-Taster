"""TasteMirror — Interactive Research Taste Explorer"""
import json, torch, numpy as np, os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

app = Flask(__name__, static_folder='static')
CORS(app)

# Global state
MODEL = None
TOKENIZER = None
PROBES = {}
TASTE_DIRECTIONS = {}
RESEARCHER_PROFILES = {}
SCALER = None
PCA_MODEL = None
X_ALL = None
DATA = None
REPS = None

DIMS = {
    "strategic_orientation": {"options": ["exploration", "understanding", "infrastructure", "safety"],
                              "label": "Strategic Orientation", "icon": "🧭"},
    "theory_of_progress": {"options": ["novelty", "bridging", "questioning", "engineering", "scaling"],
                           "label": "Theory of Progress", "icon": "📈"},
    "contribution_claim": {"options": ["framework", "evidence", "mechanism", "performance"],
                           "label": "Contribution Claim", "icon": "🎯"},
    "epistemic_posture": {"options": ["embrace", "problematize", "validate"],
                          "label": "Epistemic Posture", "icon": "🔬"},
    "temporal_stance": {"options": ["near", "long", "mixed"],
                        "label": "Temporal Stance", "icon": "⏳"},
    "field_positioning": {"options": ["advancing", "challenging", "bridging"],
                          "label": "Field Positioning", "icon": "🗺️"},
}

STEERING_PAIRS = {
    "strategic_orientation": ("exploration", "understanding"),
    "temporal_stance": ("long", "near"),
    "epistemic_posture": ("embrace", "problematize"),
}

def init_model():
    global MODEL, TOKENIZER, PROBES, TASTE_DIRECTIONS, RESEARCHER_PROFILES
    global SCALER, PCA_MODEL, X_ALL, DATA, REPS
    
    print("Loading model...")
    model_path = "/workspace/models/Qwen3.5-9B"
    TOKENIZER = AutoTokenizer.from_pretrained(model_path)
    MODEL = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.bfloat16, device_map="auto")
    MODEL.eval()
    
    print("Loading data and representations...")
    with open("/workspace/research-taster/data/papers_meta_annotated.json") as f:
        all_data = json.load(f)
    rc = Counter(d["researcher"] for d in all_data)
    valid_r = {r for r, c in rc.items() if c >= 5}
    DATA = [d for d in all_data if d["researcher"] in valid_r]
    
    REPS = np.load("/workspace/research-taster/results/reps_Qwen3.5-9B.npz")["layer_12"]
    SCALER = StandardScaler()
    PCA_MODEL = PCA(n_components=256)
    X_ALL = PCA_MODEL.fit_transform(SCALER.fit_transform(REPS))
    
    # Train probes
    print("Training probes...")
    for dim in DIMS:
        labels = [d["meta_taste"].get(dim, "MISSING") for d in DATA]
        valid = {l for l, c in Counter(labels).items() if c >= 5 and l != "MISSING"}
        if len(valid) < 2:
            continue
        idx = [i for i, l in enumerate(labels) if l in valid]
        le = LabelEncoder()
        y = le.fit_transform([labels[i] for i in idx])
        clf = LogisticRegression(max_iter=2000)
        clf.fit(X_ALL[idx], y)
        PROBES[dim] = {"clf": clf, "le": le, "idx": idx}
    
    # Compute taste directions for steering
    print("Computing taste directions...")
    for dim, (pos, neg) in STEERING_PAIRS.items():
        labels = [d["meta_taste"].get(dim, "MISSING") for d in DATA]
        pos_idx = [i for i, l in enumerate(labels) if l == pos]
        neg_idx = [i for i, l in enumerate(labels) if l == neg]
        if len(pos_idx) >= 5 and len(neg_idx) >= 5:
            direction = REPS[pos_idx].mean(0) - REPS[neg_idx].mean(0)
            direction = direction / (np.linalg.norm(direction) + 1e-8)
            TASTE_DIRECTIONS[dim] = {
                "vector": torch.tensor(direction, dtype=torch.bfloat16).to(MODEL.device),
                "pos": pos, "neg": neg
            }
    
    # Compute researcher profiles
    print("Computing researcher profiles...")
    r2idx = {}
    for i, d in enumerate(DATA):
        r = d["researcher"]
        if r not in r2idx:
            r2idx[r] = []
        r2idx[r].append(i)
    
    for r, idxs in r2idx.items():
        centroid = X_ALL[idxs].mean(0)
        # Get dominant taste for each dimension
        profile = {}
        for dim in DIMS:
            if dim in PROBES:
                vals = Counter(DATA[i]["meta_taste"].get(dim, "?") for i in idxs)
                top = vals.most_common(1)[0]
                profile[dim] = {"value": top[0], "count": top[1], "total": len(idxs)}
        RESEARCHER_PROFILES[r] = {
            "centroid": centroid,
            "profile": profile,
            "n_papers": len(idxs),
        }
    
    print("Ready!")

def get_taste_vector(text):
    """Get hidden state vector for text"""
    inputs = TOKENIZER(text, return_tensors="pt", truncation=True, max_length=512)
    inputs = {k: v.to(MODEL.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = MODEL(**inputs, output_hidden_states=True)
    hidden = outputs.hidden_states[12][0].mean(dim=0).cpu().float().numpy()
    return hidden

def profile_text(text):
    """Get taste profile for text"""
    hidden = get_taste_vector(text)
    hidden_pca = PCA_MODEL.transform(SCALER.transform(hidden.reshape(1, -1)))
    
    profile = {}
    for dim, probe in PROBES.items():
        probs = probe["clf"].predict_proba(hidden_pca)[0]
        classes = probe["le"].classes_
        pred_idx = probs.argmax()
        profile[dim] = {
            "predicted": classes[pred_idx],
            "confidence": float(probs[pred_idx]),
            "all_probs": {c: float(p) for c, p in zip(classes, probs)},
            "label": DIMS[dim]["label"],
            "icon": DIMS[dim]["icon"],
        }
    
    # Find similar researchers
    similar = []
    for r, rdata in RESEARCHER_PROFILES.items():
        sim = float(cosine_similarity(hidden_pca, rdata["centroid"].reshape(1, -1))[0][0])
        similar.append({"name": r, "similarity": sim, "n_papers": rdata["n_papers"],
                       "profile": rdata["profile"]})
    similar.sort(key=lambda x: -x["similarity"])
    
    return profile, similar[:5], hidden_pca[0].tolist()

def steer_generate(text, steering, max_tokens=120):
    """Generate text with taste steering"""
    prompt = "Continue this research abstract:\n\n" + text + " We"
    inputs = TOKENIZER(prompt, return_tensors="pt").to(MODEL.device)
    
    handles = []
    for dim, scale in steering.items():
        if dim in TASTE_DIRECTIONS and abs(scale) > 0:
            direction = TASTE_DIRECTIONS[dim]["vector"]
            def make_hook(s, d):
                def hook_fn(module, input, output):
                    if isinstance(output, tuple):
                        h = output[0]
                        h = h + s * d.unsqueeze(0).unsqueeze(0)
                        return (h,) + output[1:]
                    return output + s * d.unsqueeze(0).unsqueeze(0)
                return hook_fn
            layer = MODEL.model.layers[12]
            h = layer.register_forward_hook(make_hook(scale, direction))
            handles.append(h)
    
    with torch.no_grad():
        output = MODEL.generate(
            **inputs, max_new_tokens=max_tokens,
            temperature=0.7, do_sample=True, top_p=0.9,
        )
    
    for h in handles:
        h.remove()
    
    generated = TOKENIZER.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return "We " + generated

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/profile', methods=['POST'])
def api_profile():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    profile, similar, vector = profile_text(text)
    return jsonify({
        "profile": profile,
        "similar_researchers": similar,
        "vector": vector[:10],  # first 10 PCs for visualization
    })

@app.route('/api/steer', methods=['POST'])
def api_steer():
    data = request.json
    text = data.get('text', '')
    steering = data.get('steering', {})
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Convert steering values to floats
    steering_float = {k: float(v) for k, v in steering.items()}
    
    generated = steer_generate(text, steering_float)
    
    # Also profile the generated text
    profile, similar, vector = profile_text(generated)
    
    return jsonify({
        "generated": generated,
        "profile": profile,
        "similar_researchers": similar,
    })

@app.route('/api/researchers', methods=['GET'])
def api_researchers():
    result = []
    for r, rdata in RESEARCHER_PROFILES.items():
        result.append({
            "name": r,
            "n_papers": rdata["n_papers"],
            "profile": rdata["profile"],
        })
    return jsonify(result)

@app.route('/api/steering_dims', methods=['GET'])
def api_steering_dims():
    result = {}
    for dim, info in TASTE_DIRECTIONS.items():
        result[dim] = {
            "pos": info["pos"],
            "neg": info["neg"],
            "label": DIMS[dim]["label"],
            "icon": DIMS[dim]["icon"],
        }
    return jsonify(result)

if __name__ == '__main__':
    init_model()
    app.run(host='0.0.0.0', port=7860, debug=False)
