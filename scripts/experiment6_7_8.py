"""Experiments 6, 7, 8: Control Tasks + Cross-Domain Transfer + CKA

Exp 6: Control tasks (Hewitt & Liang 2019) — probe selectivity
Exp 7: Cross-domain transfer (Belinkov 2022) — train on one arXiv cat, test on others
Exp 8: CKA (Kornblith et al. 2019) — cross-model representation similarity
"""
import json, numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

RESULTS_DIR = Path("/workspace/research-taster/results")

with open("/workspace/research-taster/data/papers_meta_annotated.json") as f:
    all_data = json.load(f)
rc = Counter(d["researcher"] for d in all_data)
valid_r = {r for r, c in rc.items() if c >= 5}
data = [d for d in all_data if d["researcher"] in valid_r]

DIMS = ["strategic_orientation", "theory_of_progress", "contribution_claim",
        "epistemic_posture", "temporal_stance", "field_positioning"]

# Prepare arXiv categories
for d in data:
    cats = d.get("categories", "")
    if isinstance(cats, list):
        d["primary_cat"] = cats[0] if cats else "unknown"
    elif isinstance(cats, str):
        d["primary_cat"] = cats.split()[0] if cats else "unknown"

for model_name in ["Qwen3.5-9B", "Qwen3.5-27B"]:
    print(f"\n{'#'*70}")
    print(f"# MODEL: {model_name}")
    print(f"{'#'*70}")
    
    reps_data = np.load(str(RESULTS_DIR / f"reps_{model_name}.npz"))
    layers = sorted([int(k.split("_")[1]) for k in reps_data.files])
    best_layer = 12 if "9B" in model_name else 25
    reps = reps_data[f"layer_{best_layer}"]
    
    scaler = StandardScaler()
    reps_scaled = scaler.fit_transform(reps)
    pca = PCA(n_components=256)
    reps_pca = pca.fit_transform(reps_scaled)

    # =========================================================
    # EXPERIMENT 6: CONTROL TASKS (Hewitt & Liang 2019)
    # =========================================================
    print(f"\n{'='*60}")
    print("EXPERIMENT 6: CONTROL TASKS — Probe Selectivity")
    print(f"{'='*60}")
    print("Ref: Hewitt & Liang (2019). DOI: 10.18653/v1/D19-1275")
    print("Selectivity = real_accuracy - control_accuracy")
    print("High selectivity → model genuinely encodes the feature")
    
    np.random.seed(42)
    n_control_runs = 5
    
    for dim in DIMS:
        labels = [d["meta_taste"].get(dim, "MISSING") for d in data]
        valid_labels = {l for l, c in Counter(labels).items() if c >= 10 and l != "MISSING"}
        if len(valid_labels) < 2:
            continue
        
        indices = [i for i, l in enumerate(labels) if l in valid_labels]
        y_labels = [labels[i] for i in indices]
        le = LabelEncoder()
        y_real = le.fit_transform(y_labels)
        X = reps_pca[indices]
        chance = 1 / len(le.classes_)
        
        # Real accuracy (linear probe)
        pipe_linear = Pipeline([("c", LogisticRegression(max_iter=2000))])
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        real_acc = cross_val_score(pipe_linear, X, y_real, cv=cv, scoring='accuracy').mean()
        
        # Real accuracy (MLP probe — to test linearity)
        pipe_mlp = Pipeline([("c", MLPClassifier(hidden_layer_sizes=(128,), max_iter=500, random_state=42))])
        mlp_acc = cross_val_score(pipe_mlp, X, y_real, cv=cv, scoring='accuracy').mean()
        
        # Control: random labels (same distribution)
        control_accs = []
        for run in range(n_control_runs):
            y_control = np.random.permutation(y_real)
            ctrl_acc = cross_val_score(pipe_linear, X, y_control, cv=cv, scoring='accuracy').mean()
            control_accs.append(ctrl_acc)
        control_acc = np.mean(control_accs)
        
        selectivity = real_acc - control_acc
        linearity = real_acc / mlp_acc if mlp_acc > 0 else 0
        
        verdict = "GENUINE" if selectivity > 0.1 else "MARGINAL" if selectivity > 0.05 else "SUSPECT"
        linear_verdict = "LINEAR" if linearity > 0.9 else "MOSTLY LINEAR" if linearity > 0.8 else "NONLINEAR"
        
        print(f"\n  {dim}:")
        print(f"    Real accuracy (linear):  {real_acc:.4f}")
        print(f"    Real accuracy (MLP):     {mlp_acc:.4f}")
        print(f"    Control accuracy:        {control_acc:.4f} ± {np.std(control_accs):.4f}")
        print(f"    Selectivity:             {selectivity:.4f} → {verdict}")
        print(f"    Linearity ratio:         {linearity:.3f} → {linear_verdict}")
        print(f"    Chance:                  {chance:.4f}")

    # =========================================================
    # EXPERIMENT 7: CROSS-DOMAIN TRANSFER
    # =========================================================
    print(f"\n{'='*60}")
    print("EXPERIMENT 7: CROSS-DOMAIN TRANSFER")
    print(f"{'='*60}")
    print("Ref: Belinkov (2022). DOI: 10.1162/coli_a_00422")
    print("Train on one arXiv category, test on others")
    print("If taste transfers across domains → genuinely meta")
    
    for dim in ["strategic_orientation", "theory_of_progress", "contribution_claim"]:
        labels = [d["meta_taste"].get(dim, "MISSING") for d in data]
        valid_labels = {l for l, c in Counter(labels).items() if c >= 10 and l != "MISSING"}
        if len(valid_labels) < 2:
            continue
        
        print(f"\n  {dim}:")
        
        # Get papers with valid labels
        valid_indices = [i for i, l in enumerate(labels) if l in valid_labels]
        valid_data = [data[i] for i in valid_indices]
        valid_labels_list = [labels[i] for i in valid_indices]
        le = LabelEncoder()
        y = le.fit_transform(valid_labels_list)
        X = reps_pca[valid_indices]
        chance = 1 / len(le.classes_)
        
        # Find categories with enough papers
        cat_counts = Counter(d["primary_cat"] for d in valid_data)
        big_cats = [c for c, n in cat_counts.items() if n >= 20]
        
        print(f"    Categories with >=20 papers: {big_cats}")
        
        for train_cat in big_cats:
            train_mask = np.array([d["primary_cat"] == train_cat for d in valid_data])
            test_mask = ~train_mask
            
            if train_mask.sum() < 10 or test_mask.sum() < 10:
                continue
            
            # Check class balance in train
            train_classes = Counter(y[train_mask])
            if min(train_classes.values()) < 3:
                continue
            
            clf = LogisticRegression(max_iter=2000, C=1.0)
            clf.fit(X[train_mask], y[train_mask])
            
            test_acc = accuracy_score(y[test_mask], clf.predict(X[test_mask]))
            train_acc = accuracy_score(y[train_mask], clf.predict(X[train_mask]))
            
            transfer = "TRANSFERS" if test_acc > chance + 0.1 else "WEAK" if test_acc > chance + 0.05 else "FAILS"
            print(f"    Train: {train_cat} ({train_mask.sum()}) → Test: rest ({test_mask.sum()})")
            print(f"      Train acc: {train_acc:.3f}, Test acc: {test_acc:.3f} (chance: {chance:.3f}) → {transfer}")

    # =========================================================
    # EXPERIMENT 8: CKA CROSS-MODEL COMPARISON
    # =========================================================
    if model_name == "Qwen3.5-27B":  # Only run on second model
        print(f"\n{'='*60}")
        print("EXPERIMENT 8: CKA — Cross-Model Taste Geometry")
        print(f"{'='*60}")
        print("Ref: Kornblith et al. (2019). DOI: 10.48550/arXiv.1905.00414")
        print("Do 9B and 27B encode taste in the same way?")
        
        reps_9b = np.load(str(RESULTS_DIR / "reps_Qwen3.5-9B.npz"))
        
        def linear_CKA(X, Y):
            """Compute linear CKA between two representation matrices."""
            X = X - X.mean(0)
            Y = Y - Y.mean(0)
            
            hsic_xy = np.linalg.norm(X.T @ Y, 'fro') ** 2
            hsic_xx = np.linalg.norm(X.T @ X, 'fro') ** 2
            hsic_yy = np.linalg.norm(Y.T @ Y, 'fro') ** 2
            
            return hsic_xy / np.sqrt(hsic_xx * hsic_yy)
        
        layers_9b = sorted([int(k.split("_")[1]) for k in reps_9b.files])
        layers_27b = layers
        
        print("\n  CKA between 9B and 27B layers:")
        print(f"  {'':10s}", end="")
        for l2 in layers_27b:
            print(f"  27B-L{l2:02d}", end="")
        print()
        
        for l1 in layers_9b:
            X1 = reps_9b[f"layer_{l1}"]
            print(f"  9B-L{l1:02d}  ", end="")
            for l2 in layers_27b:
                X2 = np.load(str(RESULTS_DIR / "reps_Qwen3.5-27B.npz"))[f"layer_{l2}"]
                cka = linear_CKA(X1, X2)
                m = "█" if cka > 0.5 else "▓" if cka > 0.3 else "░" if cka > 0.1 else " "
                print(f"  {cka:.3f}{m}", end="")
            print()
        
        # CKA specifically for taste-relevant subspace
        print("\n  CKA on taste-relevant subspace (PCA of taste-labeled papers only):")
        for dim in ["strategic_orientation", "theory_of_progress"]:
            labels = [d["meta_taste"].get(dim, "MISSING") for d in data]
            valid_labels = {l for l, c in Counter(labels).items() if c >= 10 and l != "MISSING"}
            indices = [i for i, l in enumerate(labels) if l in valid_labels]
            
            X1 = reps_9b["layer_12"][indices]
            X2 = np.load(str(RESULTS_DIR / "reps_Qwen3.5-27B.npz"))["layer_25"][indices]
            
            cka = linear_CKA(X1, X2)
            print(f"    {dim}: CKA(9B-L12, 27B-L25) = {cka:.4f}")

print("\n\nALL EXPERIMENTS COMPLETE")
