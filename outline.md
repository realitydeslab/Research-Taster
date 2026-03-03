# Research Taster: Profiling and Testing Research Taste with Large Language Models

## 1. Introduction
- Research taste exists but remains tacit — researchers "know it when they see it" but can't articulate it
- Current discovery systems rely on keywords, citations, topics — miss the *how* of inquiry
- Problem: no formal framework for what research taste is, no tools to extract or test it
- Contribution: (1) a formal taxonomy of research taste dimensions, (2) an LLM-based system to extract taste profiles, (3) retrospective and proactive evaluation methods, (4) taste-based paper discovery

## 2. What Is Research Taste?

### 2.1 Philosophy of Science
- Kuhn's values, aesthetic judgment in theory choice (McAllister), epistemic virtues

### 2.2 Sociology of Knowledge
- Bourdieu's scientific habitus, Knorr-Cetina's epistemic cultures, tacit knowledge (Polanyi, Collins)

### 2.3 Taste in Other Domains
- Bourdieu's *Distinction*, music/food/art preference modeling — what transfers?

### 2.4 Cultural Dimensions
- East-West research styles, disciplinary cultures (Becher & Trowler)

### 2.5 Proposed Taxonomy of Research Taste Dimensions
- **Problem selection style** — safe → risky, incremental → paradigmatic
- **Question framing** — how / why / what-if; scale; abstraction level
- **Methodological preference** — formal / empirical / design / speculative
- **Epistemic values** — simplicity, novelty, elegance, impact, rigor
- **Aesthetic sensibility** — minimalist → baroque, theoretical beauty → practical utility
- **Interdisciplinarity appetite** — deep specialist → boundary-crossing
- **Community orientation** — field-building → field-disrupting, solo → collaborative
- **Temporal orientation** — historical grounding → future speculation

## 3. System Design: The Research Taster

### 3.1 Architecture Overview
- Input: researcher's papers (abstracts, full text, or curated selections)
- Processing: LLM-based extraction pipeline
- Output: structured taste table + natural language taste narrative

### 3.2 Taste Extraction Pipeline
- Paper-level analysis: extract taste signals from individual works
- Aggregation: synthesize across papers into a coherent taste profile
- Confidence scoring: which dimensions are strongly evidenced vs inferred

### 3.3 Taste Table Representation
- Structured format (dimensions × values, with evidence)
- Embedding representation (for similarity computation)
- Natural language "taste card" (human-readable summary)

### 3.4 Taste-Based Discovery
- Matching papers by taste alignment rather than topic
- "Researchers who taste like you also read..."
- Cross-taste exploration: deliberately surfacing work from different taste profiles

## 4. Evaluation

### 4.1 Retrospective Test
- Given a researcher's taste profile (from N papers), predict which papers from a held-out set they authored/cited/endorsed

### 4.2 Proactive Test
- Generate research questions from a taste profile → have the researcher rate alignment ("sounds like me" vs "doesn't")

### 4.3 Discrimination Test
- Can the system distinguish between researchers with known stylistic differences? (e.g., two researchers in the same field with different approaches)

### 4.4 Cross-Cultural Test
- Do taste profiles capture meaningful cultural/disciplinary differences? Compare profiles across traditions

### 4.5 User Study
- Researchers explore their own taste profiles — do they find them accurate? Surprising? Useful for self-reflection?

## 5. Case Studies

### 5.1 Distinctive Taste Profiles
- Profiling known researchers with distinctive tastes (e.g., contrasting a formalist vs a speculative designer in HCI)

### 5.2 Taste Archaeology
- Retrospective analysis of a research career's taste evolution

### 5.3 Taste-Based Paper Discovery
- Finding unexpected papers that match taste but not topic

### 5.4 Cultural Taste Mapping
- Comparing taste profiles across research traditions

## 6. Discussion

### 6.1 What Taste Reveals
- What taste captures that keywords and citations don't

### 6.2 Applications
- Taste as a tool for self-reflection and mentorship

### 6.3 Risks
- Reification of taste, filter bubbles, cultural bias in taste modeling

### 6.4 Taste as Cultural Artifact
- Whose taste does the LLM privilege?

### 6.5 Open-Endedness
- Can taste profiles generate genuinely novel research directions?

### 6.6 Limitations
- LLM biases, English-language bias, coverage gaps

## 7. Related Work
- Academic recommendation systems (Beel, Sugiyama)
- Researcher profiling & scientometrics (author-topic models, SPECTER)
- LLM-based preference extraction (PEARL, personalization)
- Computational creativity & question generation (AI Scientist, SciMON)

## 8. Conclusion & Future Work
- Research taste is formalizable, extractable, and testable
- Future: taste-aware peer review matching, taste evolution tracking, collective taste of research communities, taste-based conference design
