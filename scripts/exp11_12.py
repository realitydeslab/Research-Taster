"""Experiments 11 & 12: Career Taste Consistency + Atypical Combinations

Exp 11: Foster, Rzhetsky & Evans (2015) — taste stability across career phases
Exp 12: Uzzi et al. (2013) — taste-atypicality and impact
"""
import json, numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from collections import Counter, defaultdict
from scipy.stats import spearmanr, pearsonr

RESULTS_DIR = Path("/workspace/research-taster/results")

with open("/workspace/research-taster/data/papers_meta_annotated.json") as f:
    all_data = json.load(f)
rc = Counter(d["researcher"] for d in all_data)
valid_r = {r for r, c in rc.items() if c >= 5}
data = [d for d in all_data if d["researcher"] in valid_r]

DIMS = ["strategic_orientation", "theory_of_progress", "contribution_claim",
        "epistemic_posture", "temporal_stance", "field_positioning"]

model_name = "Qwen3.5-9B"
reps_data = np.load(str(RESULTS_DIR / f"reps_{model_name}.npz"))
reps = reps_data["layer_12"]

scaler = StandardScaler()
reps_pca = PCA(n_components=256).fit_transform(scaler.fit_transform(reps))

# =========================================================
# EXPERIMENT 11: CAREER TASTE CONSISTENCY
# =========================================================
print("="*60)
print("EXPERIMENT 11: CAREER TASTE CONSISTENCY")
print("="*60)
print("Ref: Foster, Rzhetsky & Evans (2015). DOI: 10.1177/0003122415601618")
print("Question: Is research taste a stable trait or does it drift?")

researchers = sorted(set(d["researcher"] for d in data))

for r in researchers:
    r_papers = [(d, i) for i, d in enumerate(data) if d["researcher"] == r]
    r_papers.sort(key=lambda x: x[0].get("year", 2020))
    
    if len(r_papers) < 10:
        continue
    
    years = [p[0].get("year", 2020) for p in r_papers]
    vecs = np.array([reps_pca[idx] for _, idx in r_papers])
    
    # Split into thirds
    n = len(r_papers)
    t1, t2, t3 = n//3, 2*n//3, n
    
    early = vecs[:t1].mean(axis=0)
    mid = vecs[t1:t2].mean(axis=0)
    late = vecs[t2:].mean(axis=0)
    
    # Cosine similarities between phases
    def cos(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    em = cos(early, mid)
    ml = cos(mid, late)
    el = cos(early, late)
    
    # Per-paper drift: compute distance from centroid
    centroid = vecs.mean(axis=0)
    dists = [np.linalg.norm(v - centroid) for v in vecs]
    
    # Year-ordered taste stability (rolling cosine sim)
    rolling_sims = []
    window = max(3, n // 5)
    for i in range(n - window):
        w1 = vecs[i:i+window//2].mean(axis=0)
        w2 = vecs[i+window//2:i+window].mean(axis=0)
        rolling_sims.append(cos(w1, w2))
    
    stability = np.mean(rolling_sims) if rolling_sims else 0
    
    # Meta-taste drift per dimension
    early_tastes = {}
    late_tastes = {}
    for dim in ["strategic_orientation", "theory_of_progress", "contribution_claim"]:
        early_vals = Counter(r_papers[i][0]["meta_taste"].get(dim, "?") for i in range(t1))
        late_vals = Counter(r_papers[i][0]["meta_taste"].get(dim, "?") for i in range(t2, n))
        early_top = early_vals.most_common(1)[0][0] if early_vals else "?"
        late_top = late_vals.most_common(1)[0][0] if late_vals else "?"
        early_tastes[dim] = early_top
        late_tastes[dim] = late_top
    
    shifts = sum(1 for d in early_tastes if early_tastes[d] != late_tastes[d])
    
    print(f"\n  {r} ({min(years)}-{max(years)}, {n} papers):")
    print(f"    Phase similarity: early-mid={em:.3f}, mid-late={ml:.3f}, early-late={el:.3f}")
    print(f"    Rolling stability: {stability:.3f}")
    print(f"    Dimension shifts (early→late): {shifts}/3")
    for dim in ["strategic_orientation", "theory_of_progress", "contribution_claim"]:
        arrow = "→" if early_tastes[dim] != late_tastes[dim] else "="
        print(f"      {dim}: {early_tastes[dim]} {arrow} {late_tastes[dim]}")

# Overall statistics
print(f"\n  SUMMARY:")
all_stabilities = []
all_el_sims = []
for r in researchers:
    r_papers = [(d, i) for i, d in enumerate(data) if d["researcher"] == r]
    if len(r_papers) < 10:
        continue
    r_papers.sort(key=lambda x: x[0].get("year", 2020))
    vecs = np.array([reps_pca[idx] for _, idx in r_papers])
    n = len(r_papers)
    early = vecs[:n//3].mean(axis=0)
    late = vecs[2*n//3:].mean(axis=0)
    all_el_sims.append(cos(early, late))
print(f"    Mean early-late similarity: {np.mean(all_el_sims):.3f} ± {np.std(all_el_sims):.3f}")
print(f"    Range: {min(all_el_sims):.3f} to {max(all_el_sims):.3f}")

# =========================================================
# EXPERIMENT 12: ATYPICAL COMBINATIONS
# =========================================================
print(f"\n{'='*60}")
print("EXPERIMENT 12: TASTE ATYPICALITY AND IMPACT")
print("="*60)
print("Ref: Uzzi et al. (2013). DOI: 10.1126/science.1240474")
print("Question: Are papers that deviate from a researcher's usual taste more impactful?")

# For each paper, compute deviation from researcher's taste centroid
researcher_centroids = {}
for r in researchers:
    indices = [i for i, d in enumerate(data) if d["researcher"] == r]
    researcher_centroids[r] = reps_pca[indices].mean(axis=0)

deviations = []
for i, d in enumerate(data):
    centroid = researcher_centroids[d["researcher"]]
    dev = np.linalg.norm(reps_pca[i] - centroid)
    
    # Compute taste consistency score: how different is this paper from the researcher's typical taste?
    r_papers = [p for p in data if p["researcher"] == d["researcher"]]
    taste_consistency = 0
    for dim in DIMS:
        r_dominant = Counter(p["meta_taste"].get(dim, "?") for p in r_papers).most_common(1)[0][0]
        paper_taste = d["meta_taste"].get(dim, "?")
        if paper_taste == r_dominant:
            taste_consistency += 1
    
    deviations.append({
        "researcher": d["researcher"],
        "title": d["title"][:60],
        "year": d.get("year", 2020),
        "vector_deviation": float(dev),
        "taste_consistency": taste_consistency,  # out of 6
        "taste_atypicality": 6 - taste_consistency,  # out of 6
    })

# Analyze: do atypical papers cluster in specific career phases?
print("\n  Taste atypicality distribution:")
for atyp in range(7):
    count = sum(1 for d in deviations if d["taste_atypicality"] == atyp)
    bar = "█" * (count // 3)
    print(f"    Atypicality={atyp}: {count} papers {bar}")

# Most atypical papers per researcher
print("\n  Most ATYPICAL papers (highest deviation from researcher's taste centroid):")
deviations.sort(key=lambda x: -x["vector_deviation"])
for d in deviations[:15]:
    print(f"    {d['researcher']:25s} | dev={d['vector_deviation']:.2f} | atyp={d['taste_atypicality']}/6 | {d['title']}")

# Most typical papers
print("\n  Most TYPICAL papers (lowest deviation):")
deviations.sort(key=lambda x: x["vector_deviation"])
for d in deviations[:10]:
    print(f"    {d['researcher']:25s} | dev={d['vector_deviation']:.2f} | atyp={d['taste_atypicality']}/6 | {d['title']}")

# Correlation between vector deviation and taste dimension atypicality
vec_devs = [d["vector_deviation"] for d in deviations]
taste_atyps = [d["taste_atypicality"] for d in deviations]
r_corr, p_val = spearmanr(vec_devs, taste_atyps)
print(f"\n  Correlation (vector deviation ↔ taste atypicality):")
print(f"    Spearman r = {r_corr:.4f}, p = {p_val:.6f}")
print(f"    {'SIGNIFICANT' if p_val < 0.05 else 'NOT SIGNIFICANT'}")

# Career phase analysis
print("\n  Atypicality by career phase:")
for r in researchers:
    r_devs = [d for d in deviations if d["researcher"] == r]
    if len(r_devs) < 10:
        continue
    r_devs.sort(key=lambda x: x["year"])
    n = len(r_devs)
    early_atyp = np.mean([d["taste_atypicality"] for d in r_devs[:n//3]])
    late_atyp = np.mean([d["taste_atypicality"] for d in r_devs[2*n//3:]])
    trend = "↑ MORE ATYPICAL" if late_atyp > early_atyp + 0.3 else "↓ LESS ATYPICAL" if late_atyp < early_atyp - 0.3 else "= STABLE"
    print(f"    {r:25s}: early={early_atyp:.2f} → late={late_atyp:.2f} {trend}")

print("\nDONE")
