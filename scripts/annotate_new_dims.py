"""
Annotate 373 papers with 17 new taste dimensions using Qwen3.5-9B.
Then train probes and compute steering directions for all dimensions.
"""
import json, torch, numpy as np, os, re, sys
from transformers import AutoTokenizer, AutoModelForCausalLM
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from collections import Counter

# New dimensions to annotate
NEW_DIMS = {
    # Sociology of science
    "disciplinary_voice": {
        "question": "What disciplinary voice does this paper use?",
        "options": ["cs_formal", "humanities_interpretive", "mixed"],
        "description": "CS-style formal/technical vs humanities-style interpretive/critical",
        "poles": ("humanities_interpretive", "cs_formal"),
        "icon": "🏛️", "label": "Disciplinary Voice",
    },
    "scope": {
        "question": "What is the scope of claims in this paper?",
        "options": ["narrow_focused", "moderate", "grand_sweeping"],
        "description": "Narrow/focused contribution vs grand/sweeping claims",
        "poles": ("narrow_focused", "grand_sweeping"),
        "icon": "🌐", "label": "Scope",
    },
    "collaborative_stance": {
        "question": "What collaborative stance does this paper take?",
        "options": ["solo_genius", "team_effort", "community_building"],
        "description": "Individual heroic contribution vs community-building collaborative work",
        "poles": ("solo_genius", "community_building"),
        "icon": "🤝", "label": "Collaborative Stance",
    },
    "normative_load": {
        "question": "How normatively loaded is this paper?",
        "options": ["descriptive_neutral", "mildly_normative", "prescriptive_activist"],
        "description": "Purely descriptive/neutral vs prescriptive/activist with clear should-statements",
        "poles": ("descriptive_neutral", "prescriptive_activist"),
        "icon": "⚖️", "label": "Normative Load",
    },
    # Research methodology
    "empirical_weight": {
        "question": "What is the empirical weight of this paper?",
        "options": ["theory_first", "balanced", "data_first"],
        "description": "Theory-driven conceptual work vs data-driven empirical work",
        "poles": ("theory_first", "data_first"),
        "icon": "🔬", "label": "Empirical Weight",
    },
    "reproducibility_stance": {
        "question": "What is the reproducibility stance of this paper?",
        "options": ["benchmark_driven", "mixed_methods", "exploratory_qualitative"],
        "description": "Benchmark-driven quantitative vs exploratory/qualitative",
        "poles": ("benchmark_driven", "exploratory_qualitative"),
        "icon": "🧪", "label": "Reproducibility Stance",
    },
    "formalization_level": {
        "question": "What is the formalization level of this paper?",
        "options": ["mathematical", "semi_formal", "conceptual_narrative"],
        "description": "Heavily mathematical/formal vs conceptual/narrative",
        "poles": ("mathematical", "conceptual_narrative"),
        "icon": "📐", "label": "Formalization Level",
    },
    "iteration_speed": {
        "question": "Does this paper represent a one-shot contribution or part of an incremental program?",
        "options": ["one_shot", "incremental_program"],
        "description": "Standalone one-shot contribution vs part of incremental research program",
        "poles": ("one_shot", "incremental_program"),
        "icon": "🔄", "label": "Iteration Speed",
    },
    # Creativity research
    "novelty_source": {
        "question": "What is the source of novelty in this paper?",
        "options": ["combinatorial_bridging", "deepening_within"],
        "description": "Novelty from combining/bridging fields vs deepening within a field",
        "poles": ("combinatorial_bridging", "deepening_within"),
        "icon": "💡", "label": "Novelty Source",
    },
    "problem_orientation": {
        "question": "Is this paper more about finding new problems or solving existing ones?",
        "options": ["problem_finding", "problem_solving"],
        "description": "Asks new questions vs answers existing ones",
        "poles": ("problem_finding", "problem_solving"),
        "icon": "🎯", "label": "Problem Finding vs Solving",
    },
    "risk_appetite": {
        "question": "What is the risk appetite of this paper?",
        "options": ["safe_incremental", "moderate_risk", "wild_speculative"],
        "description": "Safe/incremental contribution vs wild/speculative ideas",
        "poles": ("safe_incremental", "wild_speculative"),
        "icon": "🌊", "label": "Risk Appetite",
    },
    "zeitgeist_alignment": {
        "question": "How does this paper relate to current trends?",
        "options": ["rides_trends", "independent", "contrarian_ahead"],
        "description": "Rides current trends vs contrarian/ahead-of-time",
        "poles": ("rides_trends", "contrarian_ahead"),
        "icon": "⏰", "label": "Zeitgeist Alignment",
    },
    # Bourdieu
    "capital_strategy": {
        "question": "What is the capital strategy of this paper?",
        "options": ["prestige_seeking", "field_disrupting"],
        "description": "Prestige-seeking (publishing in top venues, incremental) vs field-disrupting",
        "poles": ("prestige_seeking", "field_disrupting"),
        "icon": "🏆", "label": "Capital Strategy",
    },
    "position_taking": {
        "question": "What position does this paper take relative to the field orthodoxy?",
        "options": ["orthodox", "reformist", "heterodox"],
        "description": "Orthodox/mainstream vs heterodox/challenging the field",
        "poles": ("orthodox", "heterodox"),
        "icon": "📍", "label": "Position-Taking",
    },
    # Meta-level
    "audience_awareness": {
        "question": "Who is the intended audience of this paper?",
        "options": ["insiders", "mixed", "outsiders"],
        "description": "Written for domain insiders vs written for outsiders/broader audience",
        "poles": ("insiders", "outsiders"),
        "icon": "🎭", "label": "Audience Awareness",
    },
    "narrative_mode": {
        "question": "What is the narrative mode of this paper?",
        "options": ["argument_driven", "story_driven"],
        "description": "Argument-driven logical structure vs story-driven narrative",
        "poles": ("argument_driven", "story_driven"),
        "icon": "📖", "label": "Narrative Mode",
    },
    "future_orientation": {
        "question": "Is this paper oriented toward what IS or what COULD BE?",
        "options": ["what_is", "mixed", "what_could_be"],
        "description": "Describes current state vs envisions possibilities (speculative)",
        "poles": ("what_is", "what_could_be"),
        "icon": "🔮", "label": "Future Orientation",
    },
}

def annotate_paper(abstract, tokenizer, model, device):
    """Annotate a paper across all 17 new dimensions"""
    results = {}
    
    for dim_name, dim_info in NEW_DIMS.items():
        options_str = ", ".join(dim_info["options"])
        prompt = f"""Classify this research abstract on the following dimension.

Dimension: {dim_info["description"]}
Options: {options_str}

Abstract: {abstract}

Respond with ONLY one of the options listed above, nothing else.
Classification:"""
        
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=20,
                temperature=0.0,
                do_sample=False,
            )
        
        generated = tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip().lower()
        
        # Match to closest option
        best_match = None
        for opt in dim_info["options"]:
            if opt.lower() in generated.lower() or generated.lower() in opt.lower():
                best_match = opt
                break
        
        if best_match is None:
            # Fuzzy: take first word and try to match
            first_word = generated.split()[0] if generated.split() else ""
            for opt in dim_info["options"]:
                if first_word in opt or opt.startswith(first_word):
                    best_match = opt
                    break
        
        if best_match is None:
            best_match = dim_info["options"][0]  # default
        
        results[dim_name] = best_match
    
    return results

def main():
    # Load data
    print("Loading data...")
    with open("/workspace/research-taster/data/papers_meta_annotated.json") as f:
        all_data = json.load(f)
    rc = Counter(d["researcher"] for d in all_data)
    valid_r = {r for r, c in rc.items() if c >= 5}
    data = [d for d in all_data if d["researcher"] in valid_r]
    print(f"  {len(data)} papers from {len(valid_r)} researchers")
    
    # Load model
    print("Loading Qwen3.5-9B...")
    model_path = "/workspace/models/Qwen3.5-9B"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.bfloat16, device_map="auto")
    model.eval()
    device = model.device
    
    # Check for existing annotations
    output_file = "/workspace/research-taster/data/papers_extended_annotated.json"
    start_idx = 0
    if os.path.exists(output_file):
        with open(output_file) as f:
            existing = json.load(f)
        start_idx = len(existing)
        print(f"  Resuming from paper {start_idx}")
        data[:start_idx] = existing[:start_idx]
    
    # Annotate
    print(f"\nAnnotating {len(data) - start_idx} remaining papers with 17 new dimensions...")
    for i in range(start_idx, len(data)):
        paper = data[i]
        abstract = paper.get("abstract", "")
        if not abstract:
            continue
        
        new_taste = annotate_paper(abstract, tokenizer, model, device)
        
        # Merge with existing meta_taste
        if "extended_taste" not in paper:
            paper["extended_taste"] = {}
        paper["extended_taste"].update(new_taste)
        
        if (i + 1) % 10 == 0:
            print(f"  [{i+1}/{len(data)}] {paper.get('title', '?')[:50]}...")
            # Save incrementally
            with open(output_file, "w") as f:
                json.dump(data, f, indent=2)
    
    # Final save
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\nSaved to {output_file}")
    
    # Print distributions
    print("\n" + "="*60)
    print("ANNOTATION DISTRIBUTIONS")
    print("="*60)
    for dim_name in NEW_DIMS:
        vals = [d.get("extended_taste", {}).get(dim_name, "?") for d in data]
        dist = Counter(vals)
        print(f"\n  {dim_name}:")
        for v, c in dist.most_common():
            print(f"    {v}: {c} ({c/len(data)*100:.1f}%)")
    
    # Now train probes and compute steering directions
    print("\n" + "="*60)
    print("TRAINING PROBES FOR NEW DIMENSIONS")
    print("="*60)
    
    # Load reps
    reps = np.load("/workspace/research-taster/results/reps_Qwen3.5-9B.npz")["layer_12"]
    scaler = StandardScaler()
    pca = PCA(n_components=256)
    X_all = pca.fit_transform(scaler.fit_transform(reps))
    
    probe_results = {}
    for dim_name, dim_info in NEW_DIMS.items():
        labels = [d.get("extended_taste", {}).get(dim_name, "MISSING") for d in data]
        valid = {l for l, c in Counter(labels).items() if c >= 5 and l != "MISSING"}
        if len(valid) < 2:
            print(f"  {dim_name}: SKIPPED (not enough valid labels)")
            continue
        
        idx = [i for i, l in enumerate(labels) if l in valid]
        le = LabelEncoder()
        y = le.fit_transform([labels[i] for i in idx])
        clf = LogisticRegression(max_iter=2000)
        clf.fit(X_all[idx], y)
        acc = clf.score(X_all[idx], y)
        
        # Compute steering direction
        pos_label, neg_label = dim_info["poles"]
        pos_idx = [i for i, l in enumerate(labels) if l == pos_label]
        neg_idx = [i for i, l in enumerate(labels) if l == neg_label]
        
        if len(pos_idx) >= 3 and len(neg_idx) >= 3:
            direction = reps[pos_idx].mean(0) - reps[neg_idx].mean(0)
            norm = float(np.linalg.norm(direction))
            direction = direction / (norm + 1e-8)
            steerable = True
        else:
            direction = None
            norm = 0
            steerable = False
        
        probe_results[dim_name] = {
            "accuracy": float(acc),
            "n_classes": len(valid),
            "n_samples": len(idx),
            "steerable": steerable,
            "direction_norm": norm,
            "classes": list(le.classes_),
        }
        
        print(f"  {dim_name}: acc={acc:.3f}, {len(valid)} classes, {len(idx)} samples, steerable={steerable}, norm={norm:.3f}")
        
        # Save steering direction
        if steerable:
            np.save(f"/workspace/research-taster/results/steer_dir_{dim_name}.npy", direction)
    
    # Save probe results
    with open("/workspace/research-taster/results/extended_probe_results.json", "w") as f:
        json.dump(probe_results, f, indent=2)
    
    print("\n\nDONE — all 17 dimensions annotated, probed, and steering directions saved")

if __name__ == "__main__":
    main()
