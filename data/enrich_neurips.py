#!/usr/bin/env python3
"""Enrich NeurIPS papers with abstracts from proceedings.neurips.cc"""
import json, time, re, urllib.request, urllib.parse, sys
from pathlib import Path

DATA_DIR = Path("/home/biber/research/research-taster/data")
UA = "research-taster/1.0 (mailto:biber@openclaw.ai)"

def http_get(url, delay=0.5):
    time.sleep(delay)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return None

def fetch_neurips_abstract(ee_url):
    url = ee_url.replace("http://papers.nips.cc", "https://proceedings.neurips.cc")
    if not url.startswith("https://proceedings.neurips.cc"): return ""
    html = http_get(url, delay=0.5)
    if not html: return ""
    m = re.search(r'class="paper-abstract">\s*<p>(.*?)</p>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    m = re.search(r'Abstract</h2>.*?<p[^>]*>(.*?)</p>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    return ""

with open(DATA_DIR / "papers_neurips_dblp.json") as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} NeurIPS papers")
print(f"With abstract: {sum(1 for p in papers if p.get('abstract'))}")

# Only process up to 700 papers to get 600 abstracts (some will fail)
with_abstract = 0
for i, p in enumerate(papers):
    if with_abstract >= 600: break
    if i % 100 == 0:
        print(f"Progress {i}/{len(papers)}, abstracts={with_abstract}", flush=True)
    if p.get("abstract"):
        with_abstract += 1
        continue
    ee = p.get("ee", "")
    if not ee: continue
    abstract = fetch_neurips_abstract(ee)
    if abstract:
        p["abstract"] = abstract
        with_abstract += 1

print(f"\nFinal: {len(papers)} papers, {with_abstract} with abstracts")
with open(DATA_DIR / "papers_neurips_dblp.json", "w") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)
print("Saved NeurIPS file")
