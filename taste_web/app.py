"""TasteMirror v2 — 23-Dimension Research Taste Explorer (Concept-Level Steering)"""
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

# All 23 dimensions with contrastive prompts for concept-level steering
ALL_DIMS = {
    # Original 6 (Evans & Foster)
    "strategic_orientation": {
        "label": "Strategic Orientation", "icon": "🧭", "group": "Evans & Foster Meta-Knowledge",
        "pos": "exploration", "neg": "understanding",
        "pos_prompt": "We explore radically new computational paradigms through open-ended evolutionary search, discovering novel architectures that transcend conventional design.",
        "neg_prompt": "We provide a systematic analysis and comprehensive understanding of existing model behavior, characterizing the mechanisms through careful empirical study.",
    },
    "theory_of_progress": {
        "label": "Theory of Progress", "icon": "📈", "group": "Evans & Foster Meta-Knowledge",
        "pos": "novelty", "neg": "engineering",
        "pos_prompt": "We introduce a fundamentally new concept that reimagines how we approach this problem, proposing a paradigm shift in the field.",
        "neg_prompt": "We engineer a robust system achieving state-of-the-art performance through careful optimization, ablation studies, and scalable implementation.",
    },
    "contribution_claim": {
        "label": "Contribution Claim", "icon": "🎯", "group": "Evans & Foster Meta-Knowledge",
        "pos": "framework", "neg": "performance",
        "pos_prompt": "We propose a theoretical framework that organizes and connects disparate phenomena, providing new conceptual tools for thinking about the problem.",
        "neg_prompt": "We achieve new state-of-the-art results, outperforming all baselines by significant margins on standard benchmarks.",
    },
    "epistemic_posture": {
        "label": "Epistemic Posture", "icon": "🔬", "group": "Evans & Foster Meta-Knowledge",
        "pos": "embrace", "neg": "problematize",
        "pos_prompt": "We enthusiastically develop and deploy new AI capabilities, building systems that push the boundaries of what machines can do.",
        "neg_prompt": "We critically examine the assumptions underlying current approaches, questioning whether the problem is well-defined and highlighting overlooked risks.",
    },
    "temporal_stance": {
        "label": "Temporal Stance", "icon": "⏳", "group": "Evans & Foster Meta-Knowledge",
        "pos": "long", "neg": "near",
        "pos_prompt": "We consider the long-term trajectory of intelligence, examining fundamental questions about the emergence of life, consciousness, and open-ended evolution.",
        "neg_prompt": "We address an immediate practical challenge with a deployable solution, focusing on near-term improvements to existing pipelines.",
    },
    "field_positioning": {
        "label": "Field Positioning", "icon": "🗺️", "group": "Evans & Foster Meta-Knowledge",
        "pos": "challenging", "neg": "advancing",
        "pos_prompt": "We challenge the dominant assumptions in the field, arguing that the community has been approaching this problem from the wrong angle entirely.",
        "neg_prompt": "We advance the state of the art in this well-established research direction, building incrementally on recent progress.",
    },
    # Sociology of Science
    "disciplinary_voice": {
        "label": "Disciplinary Voice", "icon": "🏛️", "group": "Sociology of Science",
        "pos": "humanities", "neg": "cs_formal",
        "pos_prompt": "Drawing on critical theory and interpretive analysis, we examine how power structures and social contexts shape the development and deployment of algorithmic systems.",
        "neg_prompt": "We formalize the problem as an optimization over a well-defined loss function, prove convergence guarantees, and validate empirically on standard benchmarks.",
    },
    "scope": {
        "label": "Scope", "icon": "🌐", "group": "Sociology of Science",
        "pos": "grand", "neg": "narrow",
        "pos_prompt": "We present a sweeping vision for the future of intelligence, connecting insights from biology, philosophy, and computer science to reconceptualize the nature of mind.",
        "neg_prompt": "We focus narrowly on improving attention mechanism efficiency for a specific class of sequence-to-sequence models on a targeted benchmark.",
    },
    "collaborative_stance": {
        "label": "Collaborative Stance", "icon": "🤝", "group": "Sociology of Science",
        "pos": "community", "neg": "solo",
        "pos_prompt": "We present this work as part of a growing community effort, building on shared infrastructure, open datasets, and collaborative protocols developed across multiple labs.",
        "neg_prompt": "We present a singular breakthrough insight that fundamentally changes how we think about this problem, introducing an entirely novel approach.",
    },
    "normative_load": {
        "label": "Normative Load", "icon": "⚖️", "group": "Sociology of Science",
        "pos": "prescriptive", "neg": "descriptive",
        "pos_prompt": "We argue that the AI research community must fundamentally change its approach, and we propose concrete policy recommendations and ethical guidelines.",
        "neg_prompt": "We objectively describe and measure the observed behavior of the system without making value judgments about whether it should be different.",
    },
    # Research Methodology
    "empirical_weight": {
        "label": "Empirical Weight", "icon": "🧫", "group": "Research Methodology",
        "pos": "data_first", "neg": "theory_first",
        "pos_prompt": "We conduct extensive experiments across multiple datasets and conditions, letting the empirical results guide our understanding of the phenomenon.",
        "neg_prompt": "We develop a theoretical framework grounded in first principles, deriving formal properties before validating key predictions experimentally.",
    },
    "reproducibility_stance": {
        "label": "Reproducibility Stance", "icon": "🧪", "group": "Research Methodology",
        "pos": "exploratory", "neg": "benchmark",
        "pos_prompt": "We conduct an exploratory qualitative investigation, using open-ended methods to discover unexpected phenomena and generate new hypotheses.",
        "neg_prompt": "We evaluate on standard benchmarks with fixed train/test splits, reporting mean and standard deviation across five random seeds for full reproducibility.",
    },
    "formalization_level": {
        "label": "Formalization Level", "icon": "📐", "group": "Research Methodology",
        "pos": "conceptual", "neg": "mathematical",
        "pos_prompt": "We develop a rich conceptual vocabulary and narrative framework for understanding the phenomenon, using metaphors and analogies to build intuition.",
        "neg_prompt": "We provide formal definitions, prove theorems about convergence and complexity bounds, and derive closed-form expressions for the key quantities.",
    },
    "iteration_speed": {
        "label": "Iteration Speed", "icon": "🔄", "group": "Research Methodology",
        "pos": "incremental", "neg": "one_shot",
        "pos_prompt": "This paper continues our multi-year research program, building on our previous findings to incrementally refine our understanding of the system.",
        "neg_prompt": "We present a complete standalone contribution that addresses a well-defined problem from scratch with a novel approach.",
    },
    # Creativity & Innovation
    "novelty_source": {
        "label": "Novelty Source", "icon": "💡", "group": "Creativity & Innovation",
        "pos": "bridging", "neg": "deepening",
        "pos_prompt": "We bridge insights from biology, physics, and computer science, combining concepts from artificial life, statistical mechanics, and deep learning in a novel synthesis.",
        "neg_prompt": "We push the boundaries of transformer architectures deeper, discovering new properties of attention mechanisms through careful ablation within the established paradigm.",
    },
    "problem_orientation": {
        "label": "Problem Finding vs Solving", "icon": "❓", "group": "Creativity & Innovation",
        "pos": "finding", "neg": "solving",
        "pos_prompt": "We identify a previously unrecognized problem that the research community has overlooked, revealing a fundamental gap in our understanding.",
        "neg_prompt": "We solve a well-known open problem in the field, providing an efficient algorithm with provable guarantees that improves on existing approaches.",
    },
    "risk_appetite": {
        "label": "Risk Appetite", "icon": "🌊", "group": "Creativity & Innovation",
        "pos": "speculative", "neg": "safe",
        "pos_prompt": "We speculatively explore the possibility that artificial systems could develop consciousness, proposing radical new frameworks that challenge conventional assumptions about mind.",
        "neg_prompt": "We make safe, incremental improvements to a well-established method, with thorough ablations ensuring each change contributes positively to the final result.",
    },
    "zeitgeist_alignment": {
        "label": "Zeitgeist Alignment", "icon": "⏰", "group": "Creativity & Innovation",
        "pos": "contrarian", "neg": "trending",
        "pos_prompt": "While the field rushes toward scaling large models, we argue for a return to fundamental principles of embodied cognition and morphological computation.",
        "neg_prompt": "We apply the latest large language model techniques to a timely problem, building on the recent wave of breakthroughs in foundation models.",
    },
    # Bourdieu
    "capital_strategy": {
        "label": "Capital Strategy", "icon": "🏆", "group": "Bourdieu's Field Theory",
        "pos": "disrupting", "neg": "prestige",
        "pos_prompt": "We challenge the established evaluation paradigms and propose that the community has been optimizing for the wrong metrics, calling for a fundamental rethinking.",
        "neg_prompt": "We publish results on the most prestigious benchmarks, achieving recognition from the top venues and building on work from leading research labs.",
    },
    "position_taking": {
        "label": "Position-Taking", "icon": "📍", "group": "Bourdieu's Field Theory",
        "pos": "heterodox", "neg": "orthodox",
        "pos_prompt": "We take a deliberately heterodox position, arguing against the mainstream consensus and proposing an alternative paradigm grounded in different assumptions.",
        "neg_prompt": "We work within the established paradigm, applying standard methods and evaluation protocols to advance the commonly accepted research agenda.",
    },
    # Meta-level
    "audience_awareness": {
        "label": "Audience Awareness", "icon": "🎭", "group": "Meta-Level",
        "pos": "outsiders", "neg": "insiders",
        "pos_prompt": "We write for a broad interdisciplinary audience, explaining technical concepts accessibly and connecting our work to societal implications that non-specialists can appreciate.",
        "neg_prompt": "We assume deep familiarity with recent advances in the specific subfield, using specialized notation and referencing prior work without extensive background.",
    },
    "narrative_mode": {
        "label": "Narrative Mode", "icon": "📖", "group": "Meta-Level",
        "pos": "story", "neg": "argument",
        "pos_prompt": "We tell the story of how we discovered an unexpected phenomenon, taking the reader on a journey from initial observations through failed attempts to the final insight.",
        "neg_prompt": "We present a tight logical argument: definition, theorem, proof. Each claim follows deductively from the previous, building an airtight case for our conclusion.",
    },
    "future_orientation": {
        "label": "Future Orientation", "icon": "🔮", "group": "Meta-Level",
        "pos": "could_be", "neg": "what_is",
        "pos_prompt": "We envision possible futures where artificial agents develop their own cultures, rituals, and forms of creativity, exploring what might emerge from open-ended evolution.",
        "neg_prompt": "We carefully measure and characterize the current state of the system, documenting what exists and how it behaves under controlled conditions.",
    },
}

# Ian Cheng's Four Worlding Arts (composite archetypes)
CHENG_ARCHETYPES = {
    "cartoonist": {
        "label": "Cartoonist", "icon": "🎨",
        "description": "Simplify, feel, meme. Reduces complexity into emotionally resonant forms. Seeks home via gut.",
        "pos_prompt": "We reduce the complexity of this problem into an instantly legible framework. If it moves us emotionally, it will move our audience. We distill everything to its most resonant signal — a character, a metaphor, a meme that captures the essence. Our work speaks to instinct before intellect.",
        "neg_prompt": "We present a comprehensive formal analysis with careful mathematical treatment, avoiding simplification and maintaining the full complexity of the theoretical landscape with rigorous notation throughout.",
        # Composite: scope(-), audience(+outsiders), narrative(+story), formalization(+conceptual), risk(-safe)
        "steering_recipe": {"scope": -4, "audience_awareness": 5, "narrative_mode": 5, "formalization_level": 5, "risk_appetite": -3, "empirical_weight": -3},
    },
    "director": {
        "label": "Director", "icon": "🎬",
        "description": "Structure, meaning, journey. Domesticates chaos into narrative containers. Seeks home via story.",
        "pos_prompt": "We structure this complex problem into a narrative journey. By choosing the right framing and backstory, we create conditions for the meaningful solution to reveal itself. Every element serves the throughline — excavating a fundamental truth about how order might overcome chaos, how individual and collective wants can realign.",
        "neg_prompt": "We take an exploratory, open-ended approach, letting the system surprise us without predetermined structure. There is no narrative arc — just tinkering and seeing what emerges from the interaction of components.",
        # Composite: narrative(+story), scope(+grand), normative(+prescriptive), position(-orthodox), collaborative(+community)
        "steering_recipe": {"narrative_mode": 5, "scope": 4, "normative_load": 4, "position_taking": -3, "collaborative_stance": 4, "future_orientation": -3},
    },
    "hacker": {
        "label": "Hacker", "icon": "🔓",
        "description": "Break interfaces, tinker, first principles. Strips systems to their Reality OS. Seeks surprise via gut.",
        "pos_prompt": "We strip away the interface packaging to reveal the core innovation underneath. By breaking down assumptions and playing with all the dials, we discover that the system's full range of expression far exceeds its designed purpose. Our hack cheats common sense assumptions about what should be possible — it's not science, but it works.",
        "neg_prompt": "We work within established paradigms, applying standard methods and evaluation protocols. We follow best practices and accepted conventions, building incrementally on the existing body of work without questioning its foundations.",
        # Composite: risk(+speculative), zeitgeist(+contrarian), capital(+disrupting), formalization(-mathematical), reproducibility(+exploratory)
        "steering_recipe": {"risk_appetite": 5, "zeitgeist_alignment": 4, "capital_strategy": 4, "formalization_level": -3, "reproducibility_stance": 4, "problem_orientation": 3},
    },
    "emissary": {
        "label": "Emissary", "icon": "🌍",
        "description": "Nurture, world, long-term autonomy. Gardens as though you'll live forever. Seeks surprise via story.",
        "pos_prompt": "We initiate and nurture a living system toward long-term autonomy. The unknowns are not problems to solve but content for our ongoing stream — energy to be transformed, information we don't already know. We must resist the craving for easy meaning and instead garden as though we'll live forever, absorbing surprises while maintaining coherent identity.",
        "neg_prompt": "We present a finite, self-contained contribution with clear boundaries. The work has a definitive conclusion and does not aspire to ongoing life beyond its publication. It answers a specific question and moves on.",
        # Composite: temporal(+long), future(+could_be), scope(+grand), epistemic(+embrace), novelty(+bridging), iteration(+incremental)
        "steering_recipe": {"temporal_stance": 5, "future_orientation": 5, "scope": 4, "epistemic_posture": 4, "novelty_source": 4, "iteration_speed": 4},
    },
}

DIM_GROUPS = {}
for dim, info in ALL_DIMS.items():
    g = info["group"]
    if g not in DIM_GROUPS:
        DIM_GROUPS[g] = []
    DIM_GROUPS[g].append(dim)

def get_hidden_state(text):
    inputs = TOKENIZER(text, return_tensors="pt", truncation=True, max_length=512)
    inputs = {k: v.to(MODEL.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = MODEL(**inputs, output_hidden_states=True)
    return outputs.hidden_states[12][0].mean(dim=0).cpu().float().numpy()

def init_model():
    global MODEL, TOKENIZER, PROBES, TASTE_DIRECTIONS, RESEARCHER_PROFILES
    global SCALER, PCA_MODEL, X_ALL, DATA, REPS
    
    print("Loading model...")
    model_path = "/workspace/models/Qwen3.5-9B"
    TOKENIZER = AutoTokenizer.from_pretrained(model_path)
    MODEL = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.bfloat16, device_map="auto")
    MODEL.eval()
    
    print("Loading data...")
    with open("/workspace/research-taster/data/papers_meta_annotated.json") as f:
        all_data = json.load(f)
    rc = Counter(d["researcher"] for d in all_data)
    valid_r = {r for r, c in rc.items() if c >= 5}
    DATA = [d for d in all_data if d["researcher"] in valid_r]
    
    REPS = np.load("/workspace/research-taster/results/reps_Qwen3.5-9B.npz")["layer_12"]
    SCALER = StandardScaler()
    PCA_MODEL = PCA(n_components=256)
    X_ALL = PCA_MODEL.fit_transform(SCALER.fit_transform(REPS))
    
    # Train probes for original 6 dims (have annotations)
    print("Training probes (original 6)...")
    for dim in ["strategic_orientation", "theory_of_progress", "contribution_claim",
                "epistemic_posture", "temporal_stance", "field_positioning"]:
        labels = [d["meta_taste"].get(dim, "MISSING") for d in DATA]
        valid = {l for l, c in Counter(labels).items() if c >= 5 and l != "MISSING"}
        if len(valid) < 2:
            continue
        idx = [i for i, l in enumerate(labels) if l in valid]
        le = LabelEncoder()
        y = le.fit_transform([labels[i] for i in idx])
        clf = LogisticRegression(max_iter=2000)
        clf.fit(X_ALL[idx], y)
        PROBES[dim] = {"clf": clf, "le": le}
        print(f"  {dim}: acc={clf.score(X_ALL[idx], y):.3f}")
    
    # Compute concept-level steering directions for ALL 23 dims
    print("Computing concept-level steering directions (23 dims)...")
    for dim, info in ALL_DIMS.items():
        pos_vec = get_hidden_state(info["pos_prompt"])
        neg_vec = get_hidden_state(info["neg_prompt"])
        direction = pos_vec - neg_vec
        norm = np.linalg.norm(direction)
        direction = direction / (norm + 1e-8)
        TASTE_DIRECTIONS[dim] = {
            "vector": torch.tensor(direction, dtype=torch.bfloat16).to(MODEL.device),
            "pos": info["pos"], "neg": info["neg"],
        }
        print(f"  {dim}: {info['neg']} → {info['pos']} (norm={norm:.2f})")
    
    # Researcher profiles
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
        for dim in PROBES:
            vals = Counter(DATA[i]["meta_taste"].get(dim, "?") for i in idxs)
            if vals:
                top = vals.most_common(1)[0]
                profile[dim] = {"value": top[0], "count": top[1], "total": len(idxs)}
        RESEARCHER_PROFILES[r] = {"centroid": centroid, "profile": profile, "n_papers": len(idxs)}
    
    # Compute Cheng archetype vectors
    print("Computing Cheng archetype vectors...")
    for arch_name, arch_info in CHENG_ARCHETYPES.items():
        pos_vec = get_hidden_state(arch_info["pos_prompt"])
        neg_vec = get_hidden_state(arch_info["neg_prompt"])
        direction = pos_vec - neg_vec
        norm = np.linalg.norm(direction)
        direction = direction / (norm + 1e-8)
        TASTE_DIRECTIONS[f"cheng_{arch_name}"] = {
            "vector": torch.tensor(direction, dtype=torch.bfloat16).to(MODEL.device),
            "pos": arch_name, "neg": f"not_{arch_name}",
        }
        print(f"  cheng_{arch_name}: norm={norm:.2f}")
    
    # Pre-compute Cheng 2×2 coordinates for all papers
    print("Computing Cheng 2×2 map for all papers...")
    CHENG_PAPER_MAP = []
    arch_vecs = {}
    for arch_name in ["cartoonist", "director", "hacker", "emissary"]:
        arch_vecs[arch_name] = TASTE_DIRECTIONS[f"cheng_{arch_name}"]["vector"].cpu().float().numpy()
    
    for paper in DATA:
        pid = paper.get("semantic_scholar_id") or paper.get("title", "")[:40]
        title = paper.get("title", "Unknown")
        researcher = paper.get("researcher", "Unknown")
        abstract = paper.get("abstract", "")[:200]
        
        # Get hidden state for this paper
        text = f"Title: {title}\nAbstract: {abstract}"
        try:
            h = get_hidden_state(text)
            sims = {}
            for arch_name, avec in arch_vecs.items():
                sims[arch_name] = float(cosine_similarity(h.reshape(1,-1), avec.reshape(1,-1))[0][0])
            
            # X axis: Home (-) ↔ Surprise (+)
            x = (sims["hacker"] + sims["emissary"]) - (sims["cartoonist"] + sims["director"])
            # Y axis: Gut (-) ↔ Story (+)
            y = (sims["director"] + sims["emissary"]) - (sims["cartoonist"] + sims["hacker"])
            
            CHENG_PAPER_MAP.append({
                "title": title, "researcher": researcher, "abstract": abstract,
                "x": round(x, 4), "y": round(y, 4),
                "sims": {k: round(v, 4) for k, v in sims.items()},
            })
        except Exception as e:
            print(f"  Skip {title[:30]}: {e}")
    
    print(f"  Mapped {len(CHENG_PAPER_MAP)} papers to Cheng 2×2")
    # Store globally
    app.config["CHENG_PAPER_MAP"] = CHENG_PAPER_MAP
    
    print(f"Ready! {len(PROBES)} probes, {len(TASTE_DIRECTIONS)} steering directions")

def classify_cheng(hidden_raw):
    """Classify text into Cheng's four worlding arts using cosine similarity to archetype vectors"""
    scores = {}
    for arch_name, arch_info in CHENG_ARCHETYPES.items():
        # Use the archetype's positive prompt vector as reference
        arch_vec = TASTE_DIRECTIONS[f"cheng_{arch_name}"]["vector"].cpu().float().numpy()
        sim = float(cosine_similarity(hidden_raw.reshape(1, -1), arch_vec.reshape(1, -1))[0][0])
        scores[arch_name] = sim
    
    # Softmax-like normalization
    import math
    temp = 3.0  # temperature
    exp_scores = {k: math.exp(v * temp) for k, v in scores.items()}
    total = sum(exp_scores.values())
    probs = {k: v / total for k, v in exp_scores.items()}
    
    top = max(probs, key=probs.get)
    return {
        "archetype": top,
        "scores": {k: round(v, 3) for k, v in probs.items()},
        "raw_sims": {k: round(v, 4) for k, v in scores.items()},
    }

def profile_text(text):
    hidden_raw = get_hidden_state(text)
    hidden_pca = PCA_MODEL.transform(SCALER.transform(hidden_raw.reshape(1, -1)))
    
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
    
    # Cheng archetype classification
    cheng = classify_cheng(hidden_raw)
    
    similar = []
    for r, rdata in RESEARCHER_PROFILES.items():
        sim = float(cosine_similarity(hidden_pca, rdata["centroid"].reshape(1, -1))[0][0])
        similar.append({"name": r, "similarity": sim, "n_papers": rdata["n_papers"],
                       "profile": rdata["profile"]})
    similar.sort(key=lambda x: -x["similarity"])
    
    return profile, similar[:5], hidden_pca[0].tolist(), cheng

def steer_generate(text, steering, max_tokens=150):
    prompt = "Continue this research abstract:\n\n" + text + " We"
    inputs = TOKENIZER(prompt, return_tensors="pt").to(MODEL.device)
    
    # Combine all steering into one vector, then normalize total magnitude
    combined = torch.zeros(REPS.shape[1], dtype=torch.bfloat16, device=MODEL.device)
    active_count = 0
    for dim, scale in steering.items():
        if dim in TASTE_DIRECTIONS and abs(scale) > 0:
            combined = combined + scale * TASTE_DIRECTIONS[dim]["vector"]
            active_count += 1
    
    # Cap total steering magnitude — max effective scale ~15 regardless of how many dials
    if active_count > 0:
        total_norm = combined.norm().item()
        max_norm = 15.0  # equivalent to one dial at 15
        if total_norm > max_norm:
            combined = combined * (max_norm / total_norm)
    
    handles = []
    if combined.norm().item() > 0.01:
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                h = output[0]
                h = h + combined.unsqueeze(0).unsqueeze(0)
                return (h,) + output[1:]
            return output + combined.unsqueeze(0).unsqueeze(0)
        h = MODEL.model.layers[12].register_forward_hook(hook_fn)
        handles.append(h)
    
    with torch.no_grad():
        output = MODEL.generate(**inputs, max_new_tokens=max_tokens, temperature=0.5, do_sample=True, top_p=0.9,
                                enable_thinking=False)
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
        return jsonify({"error": "No text"}), 400
    profile, similar, vector, cheng = profile_text(text)
    return jsonify({"profile": profile, "similar_researchers": similar, "vector": vector[:10], "cheng": cheng})

@app.route('/api/steer', methods=['POST'])
def api_steer():
    data = request.json
    text = data.get('text', '')
    steering = {k: float(v) for k, v in data.get('steering', {}).items()}
    if not text:
        return jsonify({"error": "No text"}), 400
    generated = steer_generate(text, steering)
    profile, similar, vector, cheng = profile_text(generated)
    return jsonify({"generated": generated, "profile": profile, "similar_researchers": similar, "cheng": cheng})

@app.route('/api/steering_dims', methods=['GET'])
def api_steering_dims():
    result = {}
    for dim, info in TASTE_DIRECTIONS.items():
        if dim.startswith("cheng_"):
            continue  # separate endpoint
        d = ALL_DIMS.get(dim, {})
        result[dim] = {"pos": info["pos"], "neg": info["neg"],
                       "label": d.get("label", dim), "icon": d.get("icon", "")}
    return jsonify(result)

@app.route('/api/cheng_archetypes', methods=['GET'])
def api_cheng():
    result = {}
    for name, info in CHENG_ARCHETYPES.items():
        result[name] = {
            "label": info["label"],
            "icon": info["icon"],
            "description": info["description"],
            "steering_recipe": info["steering_recipe"],
        }
    return jsonify(result)

@app.route('/api/cheng_map', methods=['GET'])
def api_cheng_map():
    return jsonify(app.config.get("CHENG_PAPER_MAP", []))

@app.route('/worlding')
def worlding_page():
    return send_from_directory('static', 'worlding.html')

@app.route('/api/steer_archetype', methods=['POST'])
def api_steer_archetype():
    """Steer using a Cheng archetype's composite recipe"""
    data = request.json
    text = data.get('text', '')
    archetype = data.get('archetype', '')
    intensity = float(data.get('intensity', 1.0))
    
    if not text or archetype not in CHENG_ARCHETYPES:
        return jsonify({"error": "Invalid input"}), 400
    
    recipe = CHENG_ARCHETYPES[archetype]["steering_recipe"]
    steering = {k: v * intensity for k, v in recipe.items()}
    
    generated = steer_generate(text, steering)
    profile, similar, vector, cheng = profile_text(generated)
    return jsonify({
        "generated": generated,
        "profile": profile,
        "similar_researchers": similar,
        "cheng": cheng,
        "archetype_used": archetype,
    })

@app.route('/api/dim_groups', methods=['GET'])
def api_dim_groups():
    return jsonify(DIM_GROUPS)

if __name__ == '__main__':
    init_model()
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port, debug=False)
