"""TasteMirror v2 — Interactive Research Taste Explorer with 23 Dimensions"""
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

# Original 6 dimensions
ORIG_DIMS = {
    "strategic_orientation": {
        "label": "Strategic Orientation", "icon": "🧭",
        "poles": ("exploration", "understanding"),
    },
    "theory_of_progress": {
        "label": "Theory of Progress", "icon": "📈",
        "poles": ("novelty", "engineering"),
    },
    "contribution_claim": {
        "label": "Contribution Claim", "icon": "🎯",
        "poles": ("framework", "performance"),
    },
    "epistemic_posture": {
        "label": "Epistemic Posture", "icon": "🔬",
        "poles": ("embrace", "problematize"),
    },
    "temporal_stance": {
        "label": "Temporal Stance", "icon": "⏳",
        "poles": ("long", "near"),
    },
    "field_positioning": {
        "label": "Field Positioning", "icon": "🗺️",
        "poles": ("challenging", "advancing"),
    },
}

# New 17 dimensions
NEW_DIMS = {
    "disciplinary_voice": {"label": "Disciplinary Voice", "icon": "🏛️", "poles": ("humanities_interpretive", "cs_formal")},
    "scope": {"label": "Scope", "icon": "🌐", "poles": ("narrow_focused", "grand_sweeping")},
    "collaborative_stance": {"label": "Collaborative Stance", "icon": "🤝", "poles": ("solo_genius", "community_building")},
    "normative_load": {"label": "Normative Load", "icon": "⚖️", "poles": ("descriptive_neutral", "prescriptive_activist")},
    "empirical_weight": {"label": "Empirical Weight", "icon": "🔬", "poles": ("theory_first", "data_first")},
    "reproducibility_stance": {"label": "Reproducibility Stance", "icon": "🧪", "poles": ("benchmark_driven", "exploratory_qualitative")},
    "formalization_level": {"label": "Formalization Level", "icon": "📐", "poles": ("mathematical", "conceptual_narrative")},
    "iteration_speed": {"label": "Iteration Speed", "icon": "🔄", "poles": ("one_shot", "incremental_program")},
    "novelty_source": {"label": "Novelty Source", "icon": "💡", "poles": ("combinatorial_bridging", "deepening_within")},
    "problem_orientation": {"label": "Problem Finding vs Solving", "icon": "🎯", "poles": ("problem_finding", "problem_solving")},
    "risk_appetite": {"label": "Risk Appetite", "icon": "🌊", "poles": ("safe_incremental", "wild_speculative")},
    "zeitgeist_alignment": {"label": "Zeitgeist Alignment", "icon": "⏰", "poles": ("rides_trends", "contrarian_ahead")},
    "capital_strategy": {"label": "Capital Strategy", "icon": "🏆", "poles": ("prestige_seeking", "field_disrupting")},
    "position_taking": {"label": "Position-Taking", "icon": "📍", "poles": ("orthodox", "heterodox")},
    "audience_awareness": {"label": "Audience Awareness", "icon": "🎭", "poles": ("insiders", "outsiders")},
    "narrative_mode": {"label": "Narrative Mode", "icon": "📖", "poles": ("argument_driven", "story_driven")},
    "future_orientation": {"label": "Future Orientation", "icon": "🔮", "poles": ("what_is", "what_could_be")},
}

ALL_DIMS = {**ORIG_DIMS, **NEW_DIMS}

# Group dimensions for UI
DIM_GROUPS = {
    "Evans & Foster Meta-Knowledge": ["strategic_orientation", "theory_of_progress", "contribution_claim",
                                       "epistemic_posture", "temporal_stance", "field_positioning"],
    "Sociology of Science": ["disciplinary_voice", "scope", "collaborative_stance", "normative_load"],
    "Research Methodology": ["empirical_weight", "reproducibility_stance", "formalization_level", "iteration_speed"],
    "Creativity & Innovation": ["novelty_source", "problem_orientation", "risk_appetite", "zeitgeist_alignment"],
    "Bourdieu's Field Theory": ["capital_strategy", "position_taking"],
    "Meta-Level": ["audience_awareness", "narrative_mode", "future_orientation"],
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
    # Try extended annotated first
    ext_path = "/workspace/research-taster/data/papers_extended_annotated.json"
    orig_path = "/workspace/research-taster/data/papers_meta_annotated.json"
    
    if os.path.exists(ext_path):
        with open(ext_path) as f:
            all_data = json.load(f)
        print(f"  Loaded extended annotations from {ext_path}")
    else:
        with open(orig_path) as f:
            all_data = json.load(f)
        print(f"  Loaded original annotations from {orig_path}")
    
    rc = Counter(d["researcher"] for d in all_data)
    valid_r = {r for r, c in rc.items() if c >= 5}
    DATA = [d for d in all_data if d["researcher"] in valid_r]
    
    REPS = np.load("/workspace/research-taster/results/reps_Qwen3.5-9B.npz")["layer_12"]
    SCALER = StandardScaler()
    PCA_MODEL = PCA(n_components=256)
    X_ALL = PCA_MODEL.fit_transform(SCALER.fit_transform(REPS))
    
    # Train probes for all available dimensions
    print("Training probes...")
    
    def get_labels(dim):
        """Get labels from either meta_taste or extended_taste"""
        labels = []
        for d in DATA:
            val = d.get("meta_taste", {}).get(dim, None)
            if val is None:
                val = d.get("extended_taste", {}).get(dim, "MISSING")
            labels.append(val if val else "MISSING")
        return labels
    
    for dim, info in ALL_DIMS.items():
        labels = get_labels(dim)
        valid = {l for l, c in Counter(labels).items() if c >= 5 and l != "MISSING"}
        if len(valid) < 2:
            continue
        idx = [i for i, l in enumerate(labels) if l in valid]
        le = LabelEncoder()
        y = le.fit_transform([labels[i] for i in idx])
        clf = LogisticRegression(max_iter=2000)
        clf.fit(X_all[idx], y)
        PROBES[dim] = {"clf": clf, "le": le, "idx": idx}
        print(f"  Probe {dim}: {len(valid)} classes, {len(idx)} samples, acc={clf.score(X_all[idx], y):.3f}")
    
    # Compute taste directions for ALL steerable dimensions
    print("Computing taste directions...")
    for dim, info in ALL_DIMS.items():
        if "poles" not in info:
            continue
        pos, neg = info["poles"]
        labels = get_labels(dim)
        pos_idx = [i for i, l in enumerate(labels) if l == pos]
        neg_idx = [i for i, l in enumerate(labels) if l == neg]
        
        # Also try loading pre-computed direction
        steer_file = f"/workspace/research-taster/results/steer_dir_{dim}.npy"
        if os.path.exists(steer_file):
            direction = np.load(steer_file)
            TASTE_DIRECTIONS[dim] = {
                "vector": torch.tensor(direction, dtype=torch.bfloat16).to(MODEL.device),
                "pos": pos, "neg": neg,
            }
            print(f"  Loaded direction: {dim}")
        elif len(pos_idx) >= 3 and len(neg_idx) >= 3:
            direction = REPS[pos_idx].mean(0) - REPS[neg_idx].mean(0)
            direction = direction / (np.linalg.norm(direction) + 1e-8)
            TASTE_DIRECTIONS[dim] = {
                "vector": torch.tensor(direction, dtype=torch.bfloat16).to(MODEL.device),
                "pos": pos, "neg": neg,
            }
            print(f"  Computed direction: {dim}")
    
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
        profile = {}
        for dim in ALL_DIMS:
            if dim in PROBES:
                labels = get_labels(dim)
                vals = Counter(labels[i] for i in idxs if labels[i] != "MISSING")
                if vals:
                    top = vals.most_common(1)[0]
                    profile[dim] = {"value": top[0], "count": top[1], "total": len(idxs)}
        RESEARCHER_PROFILES[r] = {
            "centroid": centroid,
            "profile": profile,
            "n_papers": len(idxs),
        }
    
    print(f"Ready! {len(PROBES)} probes, {len(TASTE_DIRECTIONS)} steering directions")

def get_taste_vector(text):
    inputs = TOKENIZER(text, return_tensors="pt", truncation=True, max_length=512)
    inputs = {k: v.to(MODEL.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = MODEL(**inputs, output_hidden_states=True)
    hidden = outputs.hidden_states[12][0].mean(dim=0).cpu().float().numpy()
    return hidden

def profile_text(text):
    hidden = get_taste_vector(text)
    hidden_pca = PCA_MODEL.transform(SCALER.transform(hidden.reshape(1, -1)))
    
    profile = {}
    for dim, probe in PROBES.items():
        probs = probe["clf"].predict_proba(hidden_pca)[0]
        classes = probe["le"].classes_
        pred_idx = probs.argmax()
        info = ALL_DIMS.get(dim, {})
        profile[dim] = {
            "predicted": classes[pred_idx],
            "confidence": float(probs[pred_idx]),
            "all_probs": {c: float(p) for c, p in zip(classes, probs)},
            "label": info.get("label", dim),
            "icon": info.get("icon", ""),
        }
    
    similar = []
    for r, rdata in RESEARCHER_PROFILES.items():
        sim = float(cosine_similarity(hidden_pca, rdata["centroid"].reshape(1, -1))[0][0])
        similar.append({"name": r, "similarity": sim, "n_papers": rdata["n_papers"],
                       "profile": rdata["profile"]})
    similar.sort(key=lambda x: -x["similarity"])
    
    return profile, similar[:5], hidden_pca[0].tolist()

def steer_generate(text, steering, max_tokens=120):
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
    return jsonify({"profile": profile, "similar_researchers": similar, "vector": vector[:10]})

@app.route('/api/steer', methods=['POST'])
def api_steer():
    data = request.json
    text = data.get('text', '')
    steering = data.get('steering', {})
    if not text:
        return jsonify({"error": "No text provided"}), 400
    steering_float = {k: float(v) for k, v in steering.items()}
    generated = steer_generate(text, steering_float)
    profile, similar, vector = profile_text(generated)
    return jsonify({"generated": generated, "profile": profile, "similar_researchers": similar})

@app.route('/api/researchers', methods=['GET'])
def api_researchers():
    result = []
    for r, rdata in RESEARCHER_PROFILES.items():
        result.append({"name": r, "n_papers": rdata["n_papers"], "profile": rdata["profile"]})
    return jsonify(result)

@app.route('/api/steering_dims', methods=['GET'])
def api_steering_dims():
    result = {}
    for dim, info in TASTE_DIRECTIONS.items():
        dim_info = ALL_DIMS.get(dim, {})
        result[dim] = {
            "pos": info["pos"], "neg": info["neg"],
            "label": dim_info.get("label", dim),
            "icon": dim_info.get("icon", ""),
        }
    return jsonify(result)

@app.route('/api/dim_groups', methods=['GET'])
def api_dim_groups():
    return jsonify(DIM_GROUPS)

if __name__ == '__main__':
    init_model()
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port, debug=False)
