"""Experiment 1b: Is the probe detecting TASTE or just TOPIC?

Three critical tests:
1. Leave-one-researcher-out within ml_creative (the only style with 5 researchers)
2. Residual probing: regress out arXiv categories, probe residual for style
3. Same-topic different-style separation
"""
import json, numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression, Ridge, RidgeCV
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from collections import Counter

RESULTS_DIR = Path("/workspace/research-taster/results")

with open("/workspace/research-taster/data/arxiv_papers.json") as f:
    all_data = json.load(f)

rc = Counter(d["researcher"] for d in all_data)
valid_r = {r for r, c in rc.items() if c >= 5}
data = [d for d in all_data if d["researcher"] in valid_r]
print(f"Using {len(data)} papers (filtered from {len(all_data)})")

sc = Counter(d["researcher_style"] for d in data)
valid_s = {s for s, c in sc.items() if c >= 10}

for model_name in ["Qwen3.5-9B", "Qwen3.5-27B"]:
    print(f"\n{'='*70}")
    print(f"MODEL: {model_name}")
    print(f"{'='*70}")

    reps_data = np.load(str(RESULTS_DIR / f"reps_{model_name}.npz"))
    layers = sorted([int(k.split("_")[1]) for k in reps_data.files])
    representations = {l: reps_data[f"layer_{l}"] for l in layers}

    # =========================================================
    # TEST 1: Leave-One-Researcher-Out for ml_creative
    # =========================================================
    print("\n" + "="*60)
    print("TEST 1: Leave-One-Researcher-Out (ml_creative vs rest)")
    print("="*60)
    print("If taste is real, training on 4 creative researchers should classify the 5th.")

    creative_set = set(d["researcher"] for d in data if d["researcher_style"] == "ml_creative")
    y_binary = np.array([1 if d["researcher_style"] == "ml_creative" else 0 for d in data])
    groups = np.array([d["researcher"] for d in data])

    for l in layers:
        X = representations[l]
        scaler = StandardScaler()
        pca = PCA(n_components=min(256, X.shape[1]))

        creative_accs = []
        for researcher in sorted(creative_set):
            train_mask = groups != researcher
            test_mask = groups == researcher

            X_train = pca.fit_transform(scaler.fit_transform(X[train_mask]))
            X_test = pca.transform(scaler.transform(X[test_mask]))
            y_train = y_binary[train_mask]
            y_test = y_binary[test_mask]

            clf = LogisticRegression(max_iter=2000, C=1.0)
            clf.fit(X_train, y_train)
            acc = accuracy_score(y_test, clf.predict(X_test))
            creative_accs.append((researcher, acc, sum(test_mask)))

        avg = np.mean([a for _, a, _ in creative_accs])
        print(f"\n  Layer {l}: avg={avg:.3f}")
        for r, a, n in creative_accs:
            tag = "PASS" if a > 0.7 else "FAIL"
            print(f"    {r}: {a:.3f} ({n} papers) {tag}")

    # =========================================================
    # TEST 2: Topic features vs Style + Residual probing
    # =========================================================
    print("\n" + "="*60)
    print("TEST 2: Topic vs Style (arXiv category features)")
    print("="*60)

    all_cats = set()
    for d in data:
        cats = d.get("categories", "")
        if isinstance(cats, str):
            for c in cats.split():
                all_cats.add(c)
        elif isinstance(cats, list):
            for c in cats:
                all_cats.add(c)
    all_cats = sorted(all_cats)
    cat_to_idx = {c: i for i, c in enumerate(all_cats)}

    topic_features = np.zeros((len(data), len(all_cats)))
    for i, d in enumerate(data):
        cats = d.get("categories", "")
        if isinstance(cats, str):
            for c in cats.split():
                if c in cat_to_idx:
                    topic_features[i, cat_to_idx[c]] = 1
        elif isinstance(cats, list):
            for c in cats:
                if c in cat_to_idx:
                    topic_features[i, cat_to_idx[c]] = 1

    print(f"  Topic features: {topic_features.shape[1]} arXiv categories")

    si = [i for i, d in enumerate(data) if d["researcher_style"] in valid_s]
    sl = [data[i]["researcher_style"] for i in si]
    le = LabelEncoder()
    y = le.fit_transform(sl)

    # (a) Topic features alone
    X_topic = topic_features[si]
    clf_topic = LogisticRegression(max_iter=2000, C=1.0)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    topic_scores = cross_val_score(clf_topic, X_topic, y, cv=cv, scoring='accuracy')
    print(f"  Topic features alone → Style: {topic_scores.mean():.4f} +/- {topic_scores.std():.4f}")

    # (b) Full representations → Style (baseline)
    print(f"\n  Full representations → Style:")
    for l in layers:
        X = representations[l][si]
        pipe = Pipeline([("s", StandardScaler()), ("p", PCA(n_components=256)), ("c", LogisticRegression(max_iter=2000))])
        scores = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
        print(f"    Layer {l}: {scores.mean():.4f}")

    # (c) Residual probing
    print(f"\n  Residual (topic removed) → Style:")
    for l in layers:
        X_full = representations[l][si]
        X_t = topic_features[si]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        ridge = RidgeCV(alphas=[0.1, 1.0, 10.0])
        X_residual = np.zeros_like(X_scaled)
        chunk = 512
        for start in range(0, X_scaled.shape[1], chunk):
            end = min(start + chunk, X_scaled.shape[1])
            ridge.fit(X_t, X_scaled[:, start:end])
            pred = ridge.predict(X_t)
            X_residual[:, start:end] = X_scaled[:, start:end] - pred

        pca = PCA(n_components=256)
        X_pca = pca.fit_transform(X_residual)
        clf = LogisticRegression(max_iter=2000, C=1.0)
        scores = cross_val_score(clf, X_pca, y, cv=cv, scoring='accuracy')
        print(f"    Layer {l}: {scores.mean():.4f} (topic-removed)")

    # =========================================================
    # TEST 3: Same-topic different-style separation
    # =========================================================
    print("\n" + "="*60)
    print("TEST 3: Same-Topic Different-Style Papers")
    print("="*60)

    cat_style_map = {}
    for d in data:
        if d["researcher_style"] not in valid_s:
            continue
        cats = d.get("categories", "")
        if isinstance(cats, str):
            cats = cats.split()
        elif not isinstance(cats, list):
            cats = []
        for c in cats:
            if c not in cat_style_map:
                cat_style_map[c] = Counter()
            cat_style_map[c][d["researcher_style"]] += 1

    multi_style_cats = {c: styles for c, styles in cat_style_map.items()
                       if len(styles) >= 3 and sum(styles.values()) >= 20}

    print(f"  Categories spanning 3+ styles (>=20 papers):")
    for cat, styles in sorted(multi_style_cats.items(), key=lambda x: -sum(x[1].values())):
        print(f"    {cat}: {dict(styles)}")

    if multi_style_cats:
        best_cat = max(multi_style_cats, key=lambda c: sum(multi_style_cats[c].values()))
        cat_indices = []
        for i, d in enumerate(data):
            cats = d.get("categories", "")
            if isinstance(cats, str):
                cats = cats.split()
            elif not isinstance(cats, list):
                cats = []
            if best_cat in cats and d["researcher_style"] in valid_s:
                cat_indices.append(i)

        cat_styles = [data[i]["researcher_style"] for i in cat_indices]
        le_cat = LabelEncoder()
        y_cat = le_cat.fit_transform(cat_styles)
        cat_chance = 1/len(le_cat.classes_)

        print(f"\n  Within '{best_cat}' ({len(cat_indices)} papers, {len(le_cat.classes_)} styles, chance={cat_chance:.3f}):")
        print(f"  Styles: {dict(Counter(cat_styles))}")
        for l in layers:
            X = representations[l][cat_indices]
            n_comp = min(128, X.shape[1], len(cat_indices)-1)
            pipe = Pipeline([("s", StandardScaler()), ("p", PCA(n_components=n_comp)), ("c", LogisticRegression(max_iter=2000))])
            mc = min(Counter(y_cat).values())
            ns = min(5, mc)
            if ns < 2:
                print(f"    Layer {l}: skipped (min class too small)")
                continue
            cv2 = StratifiedKFold(n_splits=ns, shuffle=True, random_state=42)
            scores = cross_val_score(pipe, X, y_cat, cv=cv2, scoring='accuracy')
            print(f"    Layer {l}: {scores.mean():.4f} +/- {scores.std():.4f} (above chance: {scores.mean()-cat_chance:+.4f})")

print("\n\nDONE — ALL TESTS COMPLETE")
