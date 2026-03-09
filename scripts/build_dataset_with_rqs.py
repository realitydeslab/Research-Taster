"""
Build papers_meta_annotated.json and papers_with_rqs.json
Fetches arXiv papers for 15 researchers, annotates meta-knowledge dimensions,
extracts research questions.
"""
import json, time, re, requests
from pathlib import Path
from collections import Counter

DATA_DIR = Path("/home/biber/research/research-taster/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

S2_AUTHOR_IDS = {
    "ken_stanley": ("1736651", "Ken Stanley"),
    "joel_lehman": ("2791576", "Joel Lehman"),
    "jeff_clune": ("1753235", "Jeff Clune"),
    "percy_liang": ("1736815", "Percy Liang"),
    "michael_bernstein": ("2058421", "Michael Bernstein"),
    "iyad_rahwan": ("1700824", "Iyad Rahwan"),
    "sebastian_risi": ("2256527", "Sebastian Risi"),
    "jacob_steinhardt": ("2059699", "Jacob Steinhardt"),
    "takashi_ikegami": ("2109523", "Takashi Ikegami"),
    "michael_levin": ("145648308", "Michael Levin"),
    "kate_crawford": ("2792699", "Kate Crawford"),
    "david_ha": ("2592765", "David Ha"),
    "blaise_aguera": ("1745574", "Blaise Agüera y Arcas"),
    "joel_leibo": ("2069773", "Joel Z Leibo"),
    "joon_sung_park": ("2090659", "Joon Sung Park"),
}

def fetch_s2_papers(author_id, max_papers=35):
    url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    params = {"fields": "title,abstract,year,externalIds,venue,publicationDate,fieldsOfStudy", "limit": max_papers}
    headers = {"User-Agent": "ResearchTaster/1.0"}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=20)
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception as e:
        print(f"  Error: {e}")
        return []

def annotate_meta_taste(abstract, title):
    text = (title + " " + (abstract or "")).lower()
    
    def score_kws(text, kws):
        return sum(1 for k in kws if k in text)
    
    # strategic_orientation
    s = {
        "exploration": score_kws(text, ["novel", "new approach", "open-ended", "generative", "discover", "emergent", "creative", "imagination", "explore", "frontier", "curiosity"]),
        "consolidation": score_kws(text, ["survey", "benchmark", "review", "systematic", "comprehensive", "framework", "unified", "consolidat", "catalog", "taxonom"]),
        "translation": score_kws(text, ["apply", "application", "deploy", "real-world", "practical", "tool", "system", "pipeline", "implement"]),
    }
    strategic_orientation = max(s, key=s.get)
    
    # theory_of_progress
    s = {
        "novelty": score_kws(text, ["novel", "first", "new", "propose", "introduce", "advance", "improve", "state-of-the-art"]),
        "framework": score_kws(text, ["framework", "theory", "model", "formal", "principled", "foundation", "general"]),
        "understanding": score_kws(text, ["understand", "insight", "why", "how", "mechanism", "explain", "analyz", "investigat"]),
        "critique": score_kws(text, ["challeng", "problem", "limit", "fail", "critiq", "concern", "risk", "danger", "bias"]),
    }
    theory_of_progress = max(s, key=s.get)
    
    # contribution_claim
    s = {
        "advance": score_kws(text, ["we propose", "we present", "we introduce", "we develop", "we build", "outperform"]),
        "problematize": score_kws(text, ["we argue", "we challenge", "problematiz", "we question", "critiq", "misconception"]),
        "demonstrate": score_kws(text, ["we show", "we demonstrate", "we find", "we observe", "empirical", "experiment", "evaluat"]),
        "survey": score_kws(text, ["survey", "review", "overview", "taxonomy", "we review"]),
    }
    contribution_claim = max(s, key=s.get)
    
    # epistemic_posture
    s = {
        "embrace": score_kws(text, ["bold", "ambitious", "significant", "transformative", "fundamental", "general"]),
        "hedge": score_kws(text, ["suggest", "may", "might", "could", "potentially", "preliminary", "future work"]),
        "challenging": score_kws(text, ["challenge", "difficult", "hard", "open problem", "unsolved", "unknown"]),
        "empirical": score_kws(text, ["experiment", "dataset", "benchmark", "evaluat", "measur", "quantit"]),
    }
    epistemic_posture = max(s, key=s.get)
    
    # temporal_stance
    s = {
        "long": score_kws(text, ["long-term", "future", "decade", "open-ended", "agi", "artificial general", "evolution"]),
        "near": score_kws(text, ["near-term", "practical", "current", "today", "existing", "immediate", "deployment"]),
        "historical": score_kws(text, ["history", "historical", "retrospective", "origin", "past", "decades of"]),
        "speculative": score_kws(text, ["speculative", "might", "hypothes", "imagine", "envision", "what if"]),
    }
    temporal_stance = max(s, key=s.get)
    
    # field_positioning
    s = {
        "advancing": score_kws(text, ["extend", "build on", "improve", "advance", "beyond", "better than", "outperform"]),
        "bridging": score_kws(text, ["bridge", "connect", "interdisciplin", "across", "combine", "integrat"]),
        "founding": score_kws(text, ["first", "novel framework", "we introduce", "foundational", "foundation"]),
        "critiquing": score_kws(text, ["critiq", "challenge", "question", "problem with", "fail", "limit of"]),
    }
    field_positioning = max(s, key=s.get)
    
    return {
        "strategic_orientation": strategic_orientation,
        "theory_of_progress": theory_of_progress,
        "contribution_claim": contribution_claim,
        "epistemic_posture": epistemic_posture,
        "temporal_stance": temporal_stance,
        "field_positioning": field_positioning,
    }

def extract_research_question(abstract, title):
    if not abstract:
        return f"What are the key contributions and findings of: {title}?"
    text = abstract
    
    # Direct questions
    m = re.search(r'([A-Z][^.!?]{10,}\?)', text)
    if m:
        return m.group(1).strip()
    
    # Investigate/ask/study patterns
    patterns = [
        r'[Ww]e (investigate|ask|study|examine|explore|analyze|address|seek to) (whether|how|what|why|when|if)[^.]{10,}\.',
        r'[Tt]his paper (addresses|investigates|studies|asks|examines|explores) [^.]{10,}\.',
        r'[Ww]e (are interested in|focus on) (whether|how|what|why) [^.]{10,}\.',
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group(0).strip().rstrip('.')

    # Problem statement synthesis
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.strip()) > 20]
    
    # Propose X to Y -> How can we Y?
    if sentences:
        propose_m = re.search(r'[Ww]e (propose|present|introduce|develop) ([^,]{5,}),? (to|for) ([^.]{10,})\.', text)
        if propose_m:
            goal = propose_m.group(4).strip()
            return f"How can we {goal}?"
    
    # Synthesize from title
    if sentences:
        first = sentences[0].strip()
        if len(first) > 30:
            # Check if it describes a problem
            if any(kw in first.lower() for kw in ["remains", "lack", "challenge", "difficult", "problem", "unknown", "despite", "although", "however"]):
                return f"How can we address: {first}"
    
    return f"What does this work contribute to: {title}?"

def categorize_rq_type(abstract, title, rq):
    text = ((abstract or "") + " " + title + " " + rq).lower()
    
    def score(kws):
        return sum(1 for k in kws if k in text)
    
    scores = {
        "constructive": score(["we propose", "we present", "we introduce", "we develop", "we design", "we build", "we create", "we train", "a new", "a novel", "our system", "our method", "our approach", "we release"]),
        "confirmatory": score(["we hypothesize", "we test whether", "we evaluate whether", "we verify", "we confirm", "hypothesis", "consistent with", "we show that"]),
        "exploratory": score(["we investigate", "we explore", "we examine", "we study", "we analyze", "we ask", "what are", "how does", "what is the effect", "to understand"]),
        "critical": score(["we challenge", "we question", "we argue against", "problematize", "misconception", "we critique", "contrary to", "despite claims"]),
        "bridging": score(["we apply", "we adapt", "we connect", "we bridge", "we transfer", "interdisciplinary", "we combine", "inspired by", "drawing on"]),
    }
    
    max_score = max(scores.values())
    if max_score == 0:
        # Default heuristic
        if any(k in text for k in ["we propose", "we present", "we introduce", "a new", "a novel"]):
            return "constructive"
        elif "?" in (abstract or ""):
            return "exploratory"
        return "constructive"
    
    return max(scores, key=scores.get)

def main():
    all_papers = []
    
    for researcher_key, (author_id, researcher_name) in S2_AUTHOR_IDS.items():
        print(f"\n{'='*50}")
        print(f"Fetching: {researcher_name} (S2: {author_id})")
        
        papers = fetch_s2_papers(author_id)
        valid = [p for p in papers if p.get("abstract") and len(p.get("abstract","")) > 50]
        valid = valid[:30]
        print(f"  {len(papers)} fetched, {len(valid)} with abstracts")
        
        for paper in valid:
            title = paper.get("title", "")
            abstract = paper.get("abstract", "")
            year = paper.get("year")
            arxiv_id = (paper.get("externalIds") or {}).get("ArXiv")
            categories = paper.get("fieldsOfStudy") or []
            
            meta_taste = annotate_meta_taste(abstract, title)
            research_question = extract_research_question(abstract, title)
            rq_type = categorize_rq_type(abstract, title, research_question)
            
            all_papers.append({
                "title": title,
                "abstract": abstract,
                "year": int(year) if year else None,
                "arxiv_id": arxiv_id,
                "researcher": researcher_key,
                "researcher_name": researcher_name,
                "venue": paper.get("venue", ""),
                "categories": categories,
                "meta_taste": meta_taste,
                "research_question": research_question,
                "rq_type": rq_type,
                "introduction": None,
                "intro_research_questions": [],
            })
        
        time.sleep(1.0)
    
    print(f"\n\nTotal papers: {len(all_papers)}")
    
    # Researcher distribution
    rc = Counter(p["researcher"] for p in all_papers)
    print("Per researcher:", dict(sorted(rc.items(), key=lambda x:-x[1])))
    
    # Save papers_meta_annotated.json (without RQ fields)
    meta_fields = ["title","abstract","year","arxiv_id","researcher","researcher_name","venue","categories","meta_taste"]
    papers_meta = [{k: p[k] for k in meta_fields} for p in all_papers]
    with open(DATA_DIR / "papers_meta_annotated.json", "w") as f:
        json.dump(papers_meta, f, indent=2, ensure_ascii=False)
    print(f"Saved papers_meta_annotated.json ({len(papers_meta)} papers)")
    
    # Save papers_with_rqs.json
    with open(DATA_DIR / "papers_with_rqs.json", "w") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)
    print(f"Saved papers_with_rqs.json ({len(all_papers)} papers)")
    
    # Summary stats
    print(f"\n{'='*60}")
    print("SUMMARY STATISTICS")
    print(f"{'='*60}")
    
    rq_types = Counter(p["rq_type"] for p in all_papers)
    print("\nRQ Type Distribution:")
    for t, c in sorted(rq_types.items(), key=lambda x:-x[1]):
        print(f"  {t}: {c} ({100*c/len(all_papers):.1f}%)")
    
    arxiv_count = sum(1 for p in all_papers if p.get("arxiv_id"))
    print(f"\nPapers with arXiv IDs: {arxiv_count}")
    print(f"Intros fetched: 0 (focused on Task 1 and 3 from abstracts)")
    
    print("\nExamples by RQ type:")
    shown = set()
    for p in all_papers:
        rt = p["rq_type"]
        if rt not in shown:
            print(f"\n  [{rt.upper()}]")
            print(f"  Researcher: {p['researcher_name']}")
            print(f"  Title: {p['title'][:80]}")
            print(f"  RQ: {p['research_question'][:200]}")
            shown.add(rt)
        if len(shown) == 5:
            break

if __name__ == "__main__":
    main()
