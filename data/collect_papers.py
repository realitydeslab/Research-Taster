#!/usr/bin/env python3
"""
Collect CHI, NeurIPS, EMNLP papers via DBLP, enrich abstracts via:
- NeurIPS: proceedings.neurips.cc scrape
- CHI: OpenAlex API
- EMNLP: ACL Anthology scrape
"""

import json, time, re, sys, urllib.request, urllib.parse
from pathlib import Path
from collections import Counter

DATA_DIR = Path("/home/biber/research/research-taster/data")

VENUES = {
    "NeurIPS": {"stream": "conf/nips",  "years": [2022, 2023, 2024]},
    "CHI":     {"stream": "conf/chi",   "years": [2022, 2023, 2024]},
    "EMNLP":   {"stream": "conf/emnlp", "years": [2022, 2023, 2024]},
}

UA = "research-taster/1.0 (mailto:biber@openclaw.ai)"

def http_get(url, delay=1.0, binary=False):
    time.sleep(delay)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            return data if binary else data.decode("utf-8", errors="replace")
    except Exception as e:
        return None

def fetch_dblp_venue(stream, year, batch=1000):
    papers = []
    offset = 0
    while True:
        q = urllib.parse.quote(f"stream:{stream}: year:{year}")
        url = f"https://dblp.org/search/publ/api?q={q}&h={batch}&f={offset}&format=json"
        raw = http_get(url, delay=1.2)
        if not raw:
            break
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
                "_ee": ee,
                "_ee_list": ee_list,
            })
        print(f"    offset={offset} got={len(hits)} total={total}")
        offset += sent
        if offset >= total or sent == 0 or offset >= 10000: break
    return papers

# --- Abstract fetchers ---

def fetch_neurips_abstract(ee_url):
    """Scrape abstract from proceedings.neurips.cc"""
    url = ee_url.replace("http://papers.nips.cc", "https://proceedings.neurips.cc")
    if not url.startswith("https://proceedings.neurips.cc"): return ""
    html = http_get(url, delay=0.5)
    if not html: return ""
    m = re.search(r'<p class="paper-abstract">\s*<p>(.*?)</p>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    m = re.search(r'<div[^>]*class="[^"]*abstract[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL|re.I)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    return ""

def fetch_openalex_abstract(doi):
    """Get abstract via OpenAlex inverted index."""
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
    """Scrape abstract from ACL Anthology."""
    if not doi: return ""
    # Extract ACL ID from DOI like 10.18653/v1/2024.findings-emnlp.595
    m = re.search(r'18653/v1/(.+)', doi, re.I)
    if not m: return ""
    acl_id = m.group(1)
    url = f"https://aclanthology.org/{acl_id}/"
    html = http_get(url, delay=0.8)
    if not html: return ""
    m = re.search(r'<div class="card-body acl-abstract"[^>]*>.*?<span[^>]*>(.*?)</span>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    return ""

def fetch_arxiv_abstract(arxiv_id):
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    html = http_get(url, delay=3.5)
    if not html: return ""
    m = re.search(r'<summary[^>]*>(.*?)</summary>', html, re.DOTALL)
    if m: return re.sub(r'\s+', ' ', m.group(1)).strip()
    return ""

# --- Enrichment ---

def enrich_neurips(papers):
    count, with_abstract = 0, 0
    for p in papers:
        if with_abstract >= 600: break
        count += 1
        if count % 100 == 0:
            print(f"  [NeurIPS] {count}/{len(papers)}, abstracts={with_abstract}")
        if p.get("abstract"): with_abstract += 1; continue
        ee = p.get("_ee", "")
        abstract = ""
        if "proceedings.neurips.cc" in ee or "papers.nips.cc" in ee:
            abstract = fetch_neurips_abstract(ee)
        if not abstract and p.get("arxiv_id"):
            abstract = fetch_arxiv_abstract(p["arxiv_id"])
        if abstract:
            p["abstract"] = abstract
            with_abstract += 1
    print(f"  [NeurIPS] Done: {len(papers)} papers, {with_abstract} with abstracts")

def enrich_chi(papers):
    count, with_abstract = 0, 0
    for p in papers:
        if with_abstract >= 600: break
        count += 1
        if count % 100 == 0:
            print(f"  [CHI] {count}/{len(papers)}, abstracts={with_abstract}")
        if p.get("abstract"): with_abstract += 1; continue
        abstract = ""
        if p.get("doi"):
            abstract = fetch_openalex_abstract(p["doi"])
        if not abstract and p.get("arxiv_id"):
            abstract = fetch_arxiv_abstract(p["arxiv_id"])
        if abstract:
            p["abstract"] = abstract
            with_abstract += 1
    print(f"  [CHI] Done: {len(papers)} papers, {with_abstract} with abstracts")

def enrich_emnlp(papers):
    count, with_abstract = 0, 0
    for p in papers:
        if with_abstract >= 600: break
        count += 1
        if count % 100 == 0:
            print(f"  [EMNLP] {count}/{len(papers)}, abstracts={with_abstract}")
        if p.get("abstract"): with_abstract += 1; continue
        abstract = ""
        if p.get("doi"):
            abstract = fetch_acl_abstract(p["doi"])
        if not abstract and p.get("arxiv_id"):
            abstract = fetch_arxiv_abstract(p["arxiv_id"])
        if abstract:
            p["abstract"] = abstract
            with_abstract += 1
    print(f"  [EMNLP] Done: {len(papers)} papers, {with_abstract} with abstracts")

ENRICHERS = {
    "NeurIPS": enrich_neurips,
    "CHI":     enrich_chi,
    "EMNLP":   enrich_emnlp,
}

def save(papers, filename, venue_name):
    clean = []
    for p in papers:
        cp = {k: v for k, v in p.items() if not k.startswith("_")}
        cp["venue"] = venue_name
        clean.append(cp)
    path = DATA_DIR / filename
    with open(path, "w") as f:
        json.dump(clean, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(clean)} to {path}")
    return clean

def main():
    all_papers = []
    for venue_name, cfg in VENUES.items():
        print(f"\n{'='*60}\nCollecting {venue_name}\n{'='*60}")
        venue_papers = []
        for year in cfg["years"]:
            print(f"\n  {venue_name} {year}...")
            papers = fetch_dblp_venue(cfg["stream"], year)
            print(f"  -> {len(papers)} papers")
            venue_papers.extend(papers)
        print(f"\n  Total raw {venue_name}: {len(venue_papers)}")
        ENRICHERS[venue_name](venue_papers)
        cleaned = save(venue_papers, f"papers_{venue_name.lower()}_dblp.json", venue_name)
        all_papers.extend(cleaned)
        time.sleep(2)
    
    print(f"\n{'='*60}\nCombined: {len(all_papers)} papers")
    with open(DATA_DIR / "papers_venues_combined.json", "w") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)
    
    by_v = Counter(p["venue"] for p in all_papers)
    by_a = Counter(p["venue"] for p in all_papers if p.get("abstract"))
    print("\nFinal Summary:")
    for v in ["NeurIPS", "CHI", "EMNLP"]:
        print(f"  {v}: {by_v.get(v,0)} total, {by_a.get(v,0)} with abstracts")

if __name__ == "__main__":
    main()
