#!/usr/bin/env python3
"""Collect CHI and EMNLP papers from DBLP and enrich with abstracts."""
import json, time, re, urllib.request, urllib.parse, sys
from pathlib import Path
from collections import Counter

DATA_DIR = Path("/home/biber/research/research-taster/data")
UA = "research-taster/1.0 (mailto:biber@openclaw.ai)"

def http_get(url, delay=1.0):
    time.sleep(delay)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return None

def fetch_dblp_venue(stream, year, batch=1000):
    papers = []
    offset = 0
    while True:
        q = urllib.parse.quote(f"stream:{stream}: year:{year}")
        url = f"https://dblp.org/search/publ/api?q={q}&h={batch}&f={offset}&format=json"
        raw = http_get(url, delay=1.2)
        if not raw: break
        data = json.loads(raw)
        hits_obj = data.get("result", {}).get("hits", {})
        total = int(hits_obj.get("@total", 0))
        sent  = int(hits_obj.get("@sent", 0))
        hits  = hits_obj.get("hit", [])
        if isinstance(hits, dict): hits = [hits]
        for h in hits:
            info = h.get("info", {})
            auth_obj = info.get("authors", {}).get("author", [])
            if isinstance(auth_obj, dict): auth_obj = [auth_obj]
            authors = [{"name": a.get("text", "")} for a in auth_obj]
            ee = info.get("ee", "")
            if isinstance(ee, list): ee_list, ee = ee, (ee[0] if ee else "")
            else: ee_list = [ee] if ee else []
            arxiv_id = None
            for e in ee_list:
                m = re.search(r'arxiv\.org/abs/(\d+\.\d+)', e, re.I)
                if m: arxiv_id = m.group(1); break
            doi = info.get("doi", "")
            if not doi:
                for e in ee_list:
                    m = re.search(r'doi\.org/(.+)', e, re.I)
                    if m: doi = m.group(1); break
            papers.append({
                "title": info.get("title", "").rstrip("."),
                "abstract": "",
                "authors": authors,
                "year": int(info.get("year", year)),
                "venue": "",
                "doi": doi,
                "dblp_key": info.get("key", ""),
                "arxiv_id": arxiv_id,
                "ee": ee,
            })
        print(f"    offset={offset} got={len(hits)} total={total}", flush=True)
        offset += sent
        if offset >= total or sent == 0 or offset >= 10000: break
    return papers

def fetch_openalex_abstract(doi):
    if not doi: return ""
    url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe='')}"
    raw = http_get(url, delay=0.5)
    if not raw: return ""
    try:
        d = json.loads(raw)
        inv = d.get("abstract_inverted_index", {})
        if not inv: return ""
        words = {}
        for word, positions in inv.items():
            for pos in positions: words[pos] = word
        return ' '.join(words[i] for i in sorted(words.keys()))
    except: return ""

def fetch_acl_abstract(doi):
    if not doi: return ""
    m = re.search(r'18653/v1/(.+)', doi, re.I)
    if not m: return ""
    acl_id = m.group(1)
    url = f"https://aclanthology.org/{acl_id}/"
    html = http_get(url, delay=0.8)
    if not html: return ""
    m = re.search(r'<div class="card-body acl-abstract"[^>]*>.*?<span[^>]*>(.*?)</span>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    return ""

def enrich_chi(papers):
    count, with_abstract = 0, 0
    for p in papers:
        if with_abstract >= 600: break
        count += 1
        if count % 100 == 0: print(f"  [CHI] {count}/{len(papers)}, abstracts={with_abstract}", flush=True)
        if p.get("abstract"): with_abstract += 1; continue
        abstract = fetch_openalex_abstract(p.get("doi",""))
        if abstract: p["abstract"] = abstract; with_abstract += 1
    print(f"  [CHI] Done: {len(papers)} papers, {with_abstract} with abstracts")

def enrich_emnlp(papers):
    count, with_abstract = 0, 0
    for p in papers:
        if with_abstract >= 600: break
        count += 1
        if count % 100 == 0: print(f"  [EMNLP] {count}/{len(papers)}, abstracts={with_abstract}", flush=True)
        if p.get("abstract"): with_abstract += 1; continue
        abstract = fetch_acl_abstract(p.get("doi",""))
        if abstract: p["abstract"] = abstract; with_abstract += 1
    print(f"  [EMNLP] Done: {len(papers)} papers, {with_abstract} with abstracts")

for venue_name, stream, years, enrich_fn in [
    ("CHI",   "conf/chi",   [2022,2023,2024], enrich_chi),
    ("EMNLP", "conf/emnlp", [2022,2023,2024], enrich_emnlp),
]:
    print(f"\n{'='*50}\n{venue_name}\n{'='*50}")
    venue_papers = []
    for year in years:
        print(f"\n  {venue_name} {year}...")
        papers = fetch_dblp_venue(stream, year)
        print(f"  -> {len(papers)} papers")
        venue_papers.extend(papers)
    print(f"\n  Total {venue_name}: {len(venue_papers)}")
    enrich_fn(venue_papers)
    clean = [{k:v for k,v in p.items()} for p in venue_papers]
    for c in clean: c["venue"] = venue_name
    path = DATA_DIR / f"papers_{venue_name.lower()}_dblp.json"
    with open(path, "w") as f:
        json.dump(clean, f, indent=2, ensure_ascii=False)
    print(f"  Saved to {path}")

print("\nDone with CHI and EMNLP")
