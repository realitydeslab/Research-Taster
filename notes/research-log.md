# Research Log

## 2025-06-01 — Initial Ideas
- **Core thesis:** Research taste is an implicit, aesthetic-epistemic sensibility that can be formalized and tested via LLMs
- **Key angles:**
  - Literature review on "research taste" as a concept
  - Summarizing/profiling individual research tastes into structured tables
  - Building a "Research Taster" system that can taste-test research
  - Taste-based paper discovery (structural question-framing match vs keywords)
  - Cultural dimensions of research taste
  - Retrospective tests (does the profile predict past choices?) and proactive tests (what questions would this taste generate?)
- **Intended contributions:** Framework + system + evaluation
- **Open questions:** What dimensions constitute a taste profile? How to validate taste accuracy?

## 2026-03-07 — Core Framing Decision
- **Research Taster is a metaknowledge tool** (Evans & Foster 2011)
- Not a recommendation system, not a profiling tool — a metaknowledge instrument
- Makes tacit knowledge-production preferences visible, testable, and comparable
- Connects to Amber's broader research agenda: agent ethology = metaknowledge about AI behavior; machine death = metaknowledge about AI mortality
- Key reference: Evans & Foster (2011) "Metaknowledge" Science. DOI: 10.1126/science.1201765

## 2026-03-07 — Methodological Decision: Mech Interp First
- **Core method:** Mechanistic interpretability, not prompt engineering
- Research Taster applies mech interp to discover whether research taste exists as interpretable structure in LLM representations
- Key RQ: Do LLMs encode research taste as interpretable features?
- Approach: probing classifiers, steering vectors, SAEs on academic text embeddings
- This is NOT a tool paper — it's a mech interp paper with taste profiling as application
- The "complex system" nature of taste is acknowledged but the method contribution is mech interp
- Connects to latest work: representation engineering (Zou 2023), steering vectors (Turner/Rimsky), SAEs (Anthropic/Cunningham)
