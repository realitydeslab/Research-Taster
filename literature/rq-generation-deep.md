# Deep Literature Review: Research Question Generation

**How AI systems generate, evaluate, and refine research questions**

*Literature review for the Research Taster project*
*Last updated: 2026-03-03*

---

## 1. LLM-Based Research Idea & Question Generation

### 1.1 Core Systems

**Si, C., Yang, D., & Hashimoto, T. (2024). Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers.** *ICLR 2025*. arXiv: https://arxiv.org/abs/2409.04109 | DOI: 10.48550/arXiv.2409.04109

Landmark study evaluating whether LLMs can produce novel, expert-level research ideas. Conducted blind review with 100+ NLP researchers comparing LLM-generated vs. human-generated ideas. Found LLM ideas rated as more novel but less feasible than human ideas. Demonstrates that while LLMs can brainstorm creative directions, grounding in practical constraints remains a human strength.

**Relevance to Research Taster:** Directly validates the premise that LLMs can generate novel research questions, but highlights the need for feasibility filtering and human judgment—exactly what Research Taster aims to support.

---

**Baek, J., Jauhar, S.K., Cucerzan, S., & Hwang, S.J. (2024). ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models.** *NAACL 2025*. arXiv: https://arxiv.org/abs/2404.07738 | DOI: 10.18653/v1/2025.naacl-long.342

Proposes ResearchAgent, an LLM-powered agent that automatically defines problems, proposes methods, and designs experiments, iteratively refining them via LLM-powered reviewing agents. Uses a core paper as a seed, retrieves related literature, and generates research ideas through multi-round refinement with entity-centric knowledge graphs.

**Relevance to Research Taster:** The iterative refinement loop (generate → review → refine) is a key design pattern. Research Taster could adopt similar reviewing cycles but with human-in-the-loop "taste" judgments rather than purely automated review.

---

**Li, L., Xu, W., Guo, J., Zhao, R., Li, X., Yuan, Y., Zhang, B., Jiang, Y., Xin, Y., Dang, R., Rong, Y., Zhao, D., Feng, T., & Bing, L. (2024). Chain of Ideas: Revolutionizing Research in Idea Development with LLM Agents.** *Submitted to ICLR 2025*. OpenReview: https://openreview.net/forum?id=GHJzxPgFa6

Proposes Chain of Ideas (CoI), an agent framework for automatic idea generation and experiment design. Models the idea development process as a chain, where each step builds on prior ideas, mimicking how researchers incrementally develop concepts through literature engagement.

**Relevance to Research Taster:** The "chain" metaphor for progressive idea development aligns with Research Taster's goal of guided question refinement—helping users traverse from broad interest to specific, well-formed research questions.

---

**Zhou, Z., Feng, X., Huang, L., Feng, X., Song, Z., Chen, R., & Zhao, L. (2024). From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems.** GitHub: https://github.com/zkzhou126/AI-for-Research

Comprehensive survey mapping the entire AI-for-research pipeline from hypothesis generation through publication. Categorizes existing systems by research phase and identifies gaps in current tool coverage.

**Relevance to Research Taster:** Provides the landscape map for positioning Research Taster within the broader AI-for-research ecosystem. Research Taster focuses on the earliest phase (question generation) which this survey identifies as under-explored.

---

### 1.2 Agent Laboratory & Related Systems

**Schmidgall, S., et al. (2025). Agent Laboratory: Using LLM Agents as Research Assistants.** arXiv: https://arxiv.org/abs/2501.04227

Proposes a framework where LLM agents serve as full research assistants—literature review, hypothesis generation, experiment design, and paper writing. Demonstrates end-to-end autonomous research capabilities.

**Relevance to Research Taster:** Represents the "full autonomy" end of the spectrum. Research Taster deliberately occupies a different niche: augmenting human taste rather than replacing it.

---

## 2. Question Taxonomies & Generation in Education

### 2.1 Bloom's Taxonomy-Based Question Generation

**Budiharto, W., & Toba, H. (2020). Question generation model based on key-phrase, context-free grammar, and Bloom's taxonomy.** *Education and Information Technologies*, 26, 2207–2223. DOI: 10.1007/s10639-020-10356-4

Develops an automated question generation model using Bloom's taxonomy levels (remember, understand, apply, analyze, evaluate, create) combined with key-phrase extraction and context-free grammars. Demonstrates that taxonomic structure can guide question complexity.

**Relevance to Research Taster:** Bloom's taxonomy provides a ready-made framework for classifying research question depth. Research Taster could use similar taxonomic scaffolding to help users move from descriptive ("what") to evaluative ("why/how") questions.

---

## 3. Research Question Quality & Formulation

**Ratan, S.K., Anand, T., & Ratan, J. (2019). Formulation of Research Question – Stepwise Approach.** *Indian Journal of Anaesthesia*, 63(8), 611–616. DOI: 10.4103/ija.IJA_198_19 | PMC: https://ncbi.nlm.nih.gov/pmc/articles/PMC6322175/

Provides a stepwise methodology for formulating research questions using FINER criteria (Feasible, Interesting, Novel, Ethical, Relevant) and PICO framework. Widely cited in medical research methodology.

**Relevance to Research Taster:** FINER criteria could be operationalized as evaluation rubrics within Research Taster for scoring generated questions.

---

**Aslam, S., & Emmanuel, P. (2023). Formulating research questions for evidence-based studies.** *Journal of Medicine, Surgery, and Public Health*, 2. DOI: 10.1016/j.glmedi.2023.100047

Reviews frameworks for formulating research questions including PICO, SPIDER, and PEO. Emphasizes alignment between question type and methodology as a quality criterion.

**Relevance to Research Taster:** Multiple framework options (PICO, SPIDER, PEO) could inform domain-specific question templates in Research Taster.

---

*[Sections 4-8 being added incrementally...]*
