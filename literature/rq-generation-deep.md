# Deep Literature Review: Research Question Generation

**How AI systems generate, evaluate, and refine research questions**

*Literature review for the Research Taster project*
*Last updated: 2026-03-03*

---

## 1. LLM-Based Research Idea & Question Generation

### 1.1 Landmark Evaluations

**Si, C., Yang, D., & Hashimoto, T. (2024). Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers.** *ICLR 2025*. arXiv: https://arxiv.org/abs/2409.04109

Landmark blind study with 100+ NLP researchers comparing LLM-generated vs. human-generated research ideas. Found LLM ideas rated as significantly more novel but less feasible than human ideas. Highlights that LLMs excel at creative divergence but lack practical grounding.

**Relevance to Research Taster:** Validates that LLMs can generate novel research questions but need human "taste" for feasibility filtering—the core premise of Research Taster.

---

**IdeaBench: Benchmarking Large Language Models for Research Idea Generation.** (2024). arXiv: https://arxiv.org/abs/2411.02429

Proposes a benchmark for evaluating LLM-generated research ideas across multiple dimensions including novelty, feasibility, and significance. Provides standardized evaluation metrics for the idea generation task.

**Relevance to Research Taster:** Offers evaluation dimensions that Research Taster could adopt for scoring generated questions.

---

### 1.2 Agent-Based Research Idea Generation

**Baek, J., Jauhar, S.K., Cucerzan, S., & Hwang, S.J. (2024). ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models.** *NAACL 2025*. arXiv: https://arxiv.org/abs/2404.07738 | DOI: 10.18653/v1/2025.naacl-long.342

LLM-powered agent that takes a core paper, retrieves related work via entity-centric knowledge graphs, and iteratively generates/refines research ideas through multi-round LLM reviewer feedback. Demonstrates that iterative refinement significantly improves idea quality.

**Relevance to Research Taster:** The generate → review → refine loop is a key design pattern. Research Taster could adopt similar cycles but with human-in-the-loop taste judgments.

---

**Li, L., Xu, W., Guo, J., et al. (2024). Chain of Ideas: Revolutionizing Research in Idea Development with LLM Agents.** *Submitted to ICLR 2025*. OpenReview: https://openreview.net/forum?id=GHJzxPgFa6

Proposes Chain of Ideas (CoI) agent for automatic idea generation and experiment design. Models idea development as a progressive chain building on prior ideas, mimicking incremental researcher engagement with literature.

**Relevance to Research Taster:** The progressive chain metaphor aligns with Research Taster's guided question refinement—from broad interest to specific research questions.

---

**Schmidgall, S., et al. (2025). Agent Laboratory: Using LLM Agents as Research Assistants.** arXiv: https://arxiv.org/abs/2501.04227

End-to-end framework where LLM agents perform literature review, hypothesis generation, experiment design, and paper writing. Demonstrates full autonomous research capability.

**Relevance to Research Taster:** Represents the "full autonomy" pole. Research Taster occupies a different niche: augmenting human taste rather than replacing human judgment.

---

**Ghafarollahi, A. & Buehler, M.J. (2024). SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning.** *Advanced Materials*, 37(22), 2413523. DOI: 10.1002/adma.202413523 | PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12138853/

Multi-agent system using knowledge graphs for scientific hypothesis generation. Agents with different roles (ontologist, scientist, critic) collaborate through graph-based reasoning to generate novel cross-domain hypotheses.

**Relevance to Research Taster:** The multi-agent role differentiation (especially the "critic" agent) parallels the idea of taste-based evaluation. The graph reasoning approach could inform how Research Taster connects disparate research areas.

---

### 1.3 Scientific Ideation & Inspiration Systems

**Wang, Q., Downey, D., Ji, H., & Hope, T. (2024). SciMON: Scientific Inspiration Machines Optimized for Novelty.** *ACL 2024*. arXiv: https://arxiv.org/abs/2305.14259 | ACL Anthology: https://aclanthology.org/2024.acl-long.18/

Explores neural language models' ability to generate novel scientific ideas. Uses retrieval-augmented generation optimized specifically for novelty, with a novelty scoring mechanism that checks generated ideas against existing literature.

**Relevance to Research Taster:** The novelty optimization and checking mechanism is directly relevant—Research Taster needs to ensure generated questions are genuinely novel, not rehashes of existing work.

---

**Keya, F., Rabby, G., Mitra, P., Vahdati, S., Auer, S., & Jaradeh, Y. (2025). SCI-IDEA: Context-Aware Scientific Ideation Using Token and Sentence Embeddings.** arXiv: https://arxiv.org/abs/2503.19257

Context-aware scientific ideation using embedding-based retrieval. Generates research ideas grounded in specific paper contexts using token and sentence embeddings to bridge related concepts.

**Relevance to Research Taster:** The context-aware approach—generating ideas grounded in what the user is currently reading—maps to Research Taster's use case of generating questions from a specific paper or topic.

---

**Anonymous. (2024). Iterative Research Idea Development Through Evolving and Composing Idea Facets with Literature-Grounded Feedback.** arXiv: https://arxiv.org/abs/2410.04025

Proposes decomposing research ideas into "facets" (problem, method, evaluation) and iteratively evolving each facet with literature-grounded feedback. Enables modular refinement of different aspects of a research idea.

**Relevance to Research Taster:** The facet decomposition is elegant—Research Taster could help users refine different dimensions of their research question independently (scope, methodology, novelty claim).

---

**Xiong, G., Xie, E., Shariatmadari, A.H., Guo, S., Bekiranov, S., & Zhang, A. (2024). Improving Scientific Hypothesis Generation with Knowledge Grounded Large Language Models.** arXiv: https://arxiv.org/abs/2411.02382

Enhances hypothesis generation by grounding LLMs in structured knowledge bases. Shows that knowledge-grounded approaches significantly outperform naive LLM generation in producing scientifically valid hypotheses.

**Relevance to Research Taster:** Knowledge grounding is essential for Research Taster to avoid generating superficial or hallucinated research questions.

---

**Anonymous. (2024). Can LLMs Reason Like Scientists? A Survey on Hypothesis Generation.** Submitted to ACL. OpenReview: https://openreview.net/pdf?id=xXQdGIZp07

Survey of 37+ works on LLM-driven hypothesis generation. Presents a structured taxonomy of approaches, analyzes domain-specific datasets and evaluation strategies, and discusses open challenges.

**Relevance to Research Taster:** Comprehensive taxonomy of the field. Maps the landscape Research Taster operates in and identifies evaluation gaps.

---

### 1.4 Surveys & Landscape Papers

**Zhou, Z., Feng, X., Huang, L., et al. (2024). From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems.** GitHub: https://github.com/zkzhou126/AI-for-Research

Maps the full AI-for-research pipeline from hypothesis to publication. Identifies question/hypothesis generation as the least-covered early phase.

**Relevance to Research Taster:** Positions Research Taster in the broader ecosystem; validates focus on the under-explored early phase.

---

**Paureel. (2024). LLM-SCI-GEN: Papers about scientific hypothesis generation with large language models.** GitHub: https://github.com/Paureel/LLM-SCI-GEN

Curated repository of papers on LLM-based scientific hypothesis generation. Useful reference list.

**Relevance to Research Taster:** Living bibliography for tracking the rapidly growing field.

---

## 2. Question Taxonomies & Question Generation

### 2.1 Graesser's Question Taxonomy

**Graesser, A.C. & Wisher, R.A. (2001). Question Generation as a Learning Multiplier in Distributed Learning Environments.** *U.S. Army Research Institute Technical Report 1121*. URL: https://apps.dtic.mil/sti/tr/pdf/ADA399456.pdf

Foundational work on question generation as a learning tool. Develops Graesser's question taxonomy (16 categories including causal antecedent, causal consequence, enablement, comparison, definition, etc.). Shows that deeper questions (why, how, what-if) correlate with deeper learning.

**Relevance to Research Taster:** Graesser's taxonomy provides a structured framework for classifying generated research questions by cognitive depth. Research Taster could use this to ensure it generates questions across multiple depth levels.

---

**Sullins, J., Acuff, S., Neely, D., & Hu, X. (2015). Can Question Generation Training Improve Question Quality?** (Harding University / University of Memphis).

Studies whether explicit training in question generation improves question quality. Finds that even 25 minutes of question generation training significantly improves question depth and quality.

**Relevance to Research Taster:** Suggests that scaffolded question generation (what Research Taster provides) can genuinely improve research question quality, even with brief interaction.

---

### 2.2 Bloom's Taxonomy-Based Generation

**Budiharto, W. & Toba, H. (2020). Question generation model based on key-phrase, context-free grammar, and Bloom's taxonomy.** *Education and Information Technologies*, 26, 2207–2223. DOI: 10.1007/s10639-020-10356-4

Automated question generation using Bloom's taxonomy levels (remember → create). Combines key-phrase extraction with context-free grammars to generate questions at specified cognitive levels.

**Relevance to Research Taster:** Bloom's levels could scaffold question generation—helping users move from descriptive to evaluative to creative research questions.

---

### 2.3 Neural Question Generation

**Du, X., Shao, J., & Cardie, C. (2017). Learning to Ask: Neural Question Generation for Reading Comprehension.** *ACL 2017*. DOI: 10.48550/arXiv.1705.00106

Pioneering work on neural question generation from text passages. Trains sequence-to-sequence models to generate natural-language questions from paragraphs, establishing the NQG paradigm.

**Relevance to Research Taster:** Foundational NQG work; Research Taster's question generation from papers builds on this paradigm.

---

**Pan, L., Xie, Y., Feng, Y., Chua, T.-S., & Kan, M.-Y. (2020). Semantic Graphs for Generating Deep Questions.** *ACL 2020*. URL: https://aclanthology.org/2020.acl-main.135.pdf

Uses semantic graphs to generate "deep" questions requiring multi-hop reasoning. Moves beyond surface-level factoid questions to questions requiring causal and relational understanding.

**Relevance to Research Taster:** Deep question generation is exactly what Research Taster needs—questions that probe gaps, causes, and connections rather than surface facts.

---

**Guo, S., Liao, L., et al. (2024). A Survey on Neural Question Generation: Methods, Applications, and Prospects.** arXiv: https://arxiv.org/abs/2402.18267

Comprehensive 2024 survey of neural question generation methods, applications, and evaluation. Covers educational QG, conversational QG, and knowledge-grounded QG.

**Relevance to Research Taster:** Maps the full NQG landscape; identifies knowledge-grounded and deep question generation as key frontiers.

---

**Mulla, N. & Gharpure, P. (2023). Automatic question generation: a review of methodologies, datasets, evaluation metrics, and applications.** *Progress in Artificial Intelligence*, 12, 1–32. DOI: 10.1007/s13748-023-00295-9

Comprehensive review covering rule-based, template-based, and neural approaches to automatic question generation. Catalogs evaluation metrics including BLEU, ROUGE, METEOR, and human judgment.

**Relevance to Research Taster:** Evaluation metrics catalog is useful for benchmarking Research Taster's question generation quality.

---

### 2.4 Domain-Specific Question Generation

**Bedi, S., Fleming, S.L., Chiang, C.-C., et al. (2024). QUEST-AI: A System for Question Generation, Verification, and Refinement using AI for USMLE-Style Exams.** medRxiv. URL: https://www.medrxiv.org/content/10.1101/2023.04.25.23288588v2

AI system for generating, verifying, and refining medical exam questions (USMLE-style). Includes automated verification and iterative refinement pipeline.

**Relevance to Research Taster:** The generate-verify-refine pipeline is transferable. Domain-specific verification (checking against known literature) is essential for research question quality.

---

**MedQG: USMLE Style Question Generation Conditional on Clinical Notes.** GitHub: https://github.com/bio-nlp/MedQG

Medical question generation conditioned on clinical notes. Demonstrates domain-specific QG requiring specialized knowledge.

**Relevance to Research Taster:** Shows that effective QG requires domain grounding—Research Taster needs similar domain awareness.

---

## 3. Research Question Quality & Formulation Frameworks

**Ratan, S.K., Anand, T., & Ratan, J. (2019). Formulation of Research Question – Stepwise Approach.** *Indian Journal of Anaesthesia*, 63(8), 611–616. DOI: 10.4103/ija.IJA_198_19 | PMC: https://ncbi.nlm.nih.gov/pmc/articles/PMC6322175/

Introduces FINER criteria (Feasible, Interesting, Novel, Ethical, Relevant) for evaluating research questions. Provides a stepwise methodology for formulation.

**Relevance to Research Taster:** FINER criteria are directly operationalizable as evaluation rubrics for scoring generated research questions.

---

**Aslam, S. & Emmanuel, P. (2023). Formulating research questions for evidence-based studies.** *Journal of Medicine, Surgery, and Public Health*, 2. DOI: 10.1016/j.glmedi.2023.100047

Reviews multiple frameworks: PICO, SPIDER, PEO for research question formulation. Emphasizes alignment between question type and methodology.

**Relevance to Research Taster:** Multiple frameworks could inform domain-specific question templates.

---

**Peters, M.A.K. (2025). How to develop good research questions.** *Nature Human Behaviour*. URL: https://www.nature.com/articles/s41562-025-02292-5

Recent Nature perspective on developing good research questions. Provides practical guidance on what makes questions generative, tractable, and impactful.

**Relevance to Research Taster:** Contemporary framing of research question quality from a high-impact venue; defines the quality standard Research Taster should target.

---

**Ratan, S.K. et al. (2022). How to Build and Assess the Quality of Healthcare-Related Research Questions.** PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10229003/

Operationalizes quality assessment of research questions in healthcare with specific scoring criteria.

**Relevance to Research Taster:** Scoring rubric transferable to automated evaluation.

---

## 4. Gap Detection → Question Generation

**Anonymous. (2024). GAPMAP: Mapping Scientific Knowledge Gaps in Biomedical Literature Using Large Language Models.** OpenReview: https://openreview.net/pdf/2734d2963a0cefc1ed5599ab95d8d163de6c8f69.pdf

Defines two categories of knowledge gaps: explicit (clear declarations of missing knowledge) and implicit (context-inferred). Uses LLMs to detect both types across ~1500 biomedical documents. Novel task of inferring implicit gaps.

**Relevance to Research Taster:** Directly relevant—Research Taster's question generation could be driven by detected knowledge gaps. The explicit/implicit gap distinction is a key design consideration.

---

## 5. Interactive Question Refinement

**QueryExplorer: An Interactive Query Generation Assistant for Search and Exploration.** (2024). arXiv: https://arxiv.org/abs/2403.15667

Interactive system for generating and refining search queries through conversational interaction. Helps users explore information spaces by iteratively refining their questions.

**Relevance to Research Taster:** The interactive refinement paradigm directly maps to Research Taster's design—conversational guidance from broad interest to specific research question.

---

**Nested Knowledge. (2025). Research Question Refinement.** URL: https://about.nested-knowledge.com/docs/research-question-refinement

Commercial tool for research question refinement in systematic review workflows. Demonstrates market demand for question refinement tooling.

**Relevance to Research Taster:** Validates commercial viability; shows that even focused question refinement (not just generation) is valued.

---

## 6. The Role of "Taste" in Choosing Research Questions

**Alon, U. (2009). How To Choose a Good Scientific Problem.** *Molecular Cell*, 35(6), 726–728. DOI: 10.1016/j.molcel.2009.09.013 | URL: https://www.weizmann.ac.il/mcb/UriAlon/sites/mcb.UriAlon/files/uploads/nurturing/howtochoosegoodproblem.pdf

Seminal essay on the subjective, emotional dimensions of choosing scientific problems. Argues that good problem choice requires self-knowledge ("What do I find fascinating?"), not just strategic calculation. Frames lab leadership as nurturing, not optimizing for publications.

**Relevance to Research Taster:** Core philosophical foundation. Research Taster aims to help develop this "taste"—the subjective capacity to recognize which questions are worth pursuing. Alon's framing of fascination and self-expression as criteria is exactly the kind of tacit knowledge Research Taster should help cultivate.

---

**Wilke, C.O. (2014). How to develop a research question, Part II.** Blog post. URL: https://clauswilke.com/blog/2014/06/18/how-to-develop-a-research-question-part-ii/

Discusses the challenge of distinguishing rare good research ideas from many mediocre ones. Argues that "the real key to success is to formulate the question after you've found the answer"—i.e., taste involves recognizing interesting answers and reverse-engineering the question.

**Relevance to Research Taster:** Highlights that taste is partly retrospective—recognizing good results and framing the right question around them. Research Taster could include exercises where users evaluate existing findings and practice articulating what makes them interesting.

---

**Fischer, E. (2026). The pursuitworthiness of experiments.** *European Journal for Philosophy of Science*, 16, 5. DOI: 10.1007/s13194-025-00711-y | URL: https://link.springer.com/article/10.1007/s13194-025-00711-y

Philosophical analysis of what makes experiments "pursuitworthy"—worth doing even before results are known. Develops criteria beyond expected truth-value including fruitfulness, learning potential, and resource considerations.

**Relevance to Research Taster:** Provides philosophical grounding for the "taste" dimension. Pursuitworthiness criteria (fruitfulness, learning potential) complement FINER criteria as evaluation rubrics for research questions.

---

**Schickore, J. (2025). Scientific Discovery.** *Stanford Encyclopedia of Philosophy*. URL: https://plato.stanford.edu/entries/scientific-discovery/

Comprehensive philosophical treatment of scientific discovery, including the logic of discovery, the role of creativity, and whether discovery can be rational/systematic. Covers historical debates from Bacon through Popper to modern computational approaches.

**Relevance to Research Taster:** Provides the philosophical backbone for understanding whether and how research question generation can be systematized, and what role human judgment must retain.

---

**Cain, R. (2019). An Instinct for Truth: Curiosity and the Moral Character of Science.** MIT Press. URL: https://direct.mit.edu/books/monograph/4525/An-Instinct-for-TruthCuriosity-and-the-Moral

Examines curiosity as a moral virtue in scientific practice. Argues that scientific curiosity is not neutral but has ethical dimensions—what we choose to investigate reflects values.

**Relevance to Research Taster:** The ethical dimension of "taste"—choosing questions that matter, not just questions that are publishable—is relevant to Research Taster's goal of developing principled research sensibility.

---

## 7. Human-AI Collaboration for Creativity & Ideation

**Extending human creativity with AI.** (2024). *Journal of Creativity*, 34(2), 100080. DOI: 10.1016/j.yjoc.2024.100080

Models three modes of AI-creativity interaction: AI as tool, AI as collaborator, AI as autonomous creator. Reviews creativity support and co-creativity systems.

**Relevance to Research Taster:** Research Taster operates in the "AI as collaborator" mode—neither fully autonomous nor purely passive tool.

---

**Heyman, J., Rick, S., Giacomelli, G., et al. (2024). Supermind Ideator: How Scaffolding Human-AI Collaboration Can Increase Creativity.** MIT. URL: https://dspace.mit.edu/handle/1721.1/155927

Shows that scaffolded human-AI collaboration (structured prompts, guided interaction) increases creative output compared to unstructured AI interaction. Scaffolding matters more than model capability.

**Relevance to Research Taster:** Validates the scaffolding approach—Research Taster's structured question refinement process should outperform unstructured "ask ChatGPT for research questions."

---

**Maier, S., Schneider, M., & Feuerriegel, S. (2024). Partnering with Generative AI: Experimental Evaluation of Human-Led and Model-Led Interaction in Human-AI Co-Creation.** arXiv: https://arxiv.org/abs/2510.23324

Compares human-led vs. model-led interaction designs for AI co-creation. Finds that the locus of control (who leads) significantly affects creative outcomes.

**Relevance to Research Taster:** Design implication—should Research Taster lead the question refinement process, or should the human lead with AI support? Likely a human-led design is better for developing taste.

---

**Establishing the importance of co-creation and self-efficacy in creative collaboration with artificial intelligence.** (2024). *Scientific Reports*. DOI: 10.1038/s41598-024-69423-2

Finds that people were most creative writing alone, compared to AI collaboration—but co-creation increased self-efficacy. Challenges assumption that AI always boosts creativity.

**Relevance to Research Taster:** Important cautionary finding. Research Taster should enhance confidence in question-asking ability (self-efficacy) without necessarily replacing human creative generation.

---

**Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI Co-Design and Co-Creation: A Review of Emerging Approaches, Challenges, and Future Directions.** *AAAI Spring Symposium*. URL: https://ojs.aaai.org/index.php/AAAI-SS/article/download/36061/38216

Reviews emerging approaches to human-AI co-design. Identifies key challenges including maintaining human agency, avoiding over-reliance, and designing appropriate handoff points.

**Relevance to Research Taster:** Design principles for maintaining human agency during AI-assisted question generation.

---

## 8. Foundational & Complementary Works

### 8.1 Retrieval-Augmented & Knowledge-Grounded Generation

**Retrieval-augmented generation for educational application: A systematic survey.** (2025). *Computers and Education: Artificial Intelligence*. ScienceDirect: https://www.sciencedirect.com/science/article/pii/S2666920X25000578

Surveys RAG applications in education, including question generation. RAG significantly improves factual accuracy and relevance of generated educational content.

**Relevance to Research Taster:** RAG is likely the core architecture for Research Taster's question generation—retrieving relevant papers to ground generated questions.

---

### 8.2 Research Methodology & Question Frameworks

**PICO Framework.** (Various). Standard framework for clinical research questions: Population, Intervention, Comparison, Outcome.

**SPIDER Framework.** Sample, Phenomenon of Interest, Design, Evaluation, Research type. Alternative to PICO for qualitative research.

**PEO Framework.** Population, Exposure, Outcome. For observational/epidemiological studies.

**Relevance to Research Taster:** These structured frameworks could be adapted for HCI/CS research question generation (e.g., Users, System, Evaluation, Context).

---

### 8.3 Evaluation & Metrics

Standard automatic evaluation metrics for question generation:
- **BLEU** (Papineni et al., 2002) — n-gram precision
- **ROUGE** (Lin, 2004) — recall-oriented
- **METEOR** (Banerjee & Lavie, 2005) — semantic matching
- **BERTScore** (Zhang et al., 2020) — contextual embedding similarity
- **Human evaluation** — novelty, relevance, depth, feasibility

For research question evaluation specifically:
- **FINER** — Feasible, Interesting, Novel, Ethical, Relevant
- **Pursuitworthiness** — fruitfulness, learning potential, resource fit (Fischer, 2026)
- **Taste dimensions** — fascination, self-expression, personal resonance (Alon, 2009)

---

## Summary Statistics

- **Total papers/works reviewed:** 42
- **Core LLM idea generation systems:** 12
- **Question taxonomy & NQG:** 8
- **Research question quality frameworks:** 5
- **Gap detection:** 1
- **Interactive refinement:** 2
- **Taste & philosophy of science:** 5
- **Human-AI collaboration:** 6
- **Foundational/complementary:** 3

## Key Themes for Research Taster

1. **The Novelty-Feasibility Tradeoff:** LLMs generate novel but impractical questions (Si et al.). Research Taster must help bridge this gap through human taste.

2. **Iterative Refinement is Key:** Nearly all successful systems (ResearchAgent, CoI, QUEST-AI) use iterative generate-review-refine loops. Research Taster should embed this pattern.

3. **Taxonomic Scaffolding:** Question taxonomies (Bloom's, Graesser's) provide structured frameworks for guiding question depth and type. Research Taster should use similar scaffolding.

4. **Gap Detection Drives Question Generation:** GAPMAP shows that detecting knowledge gaps (explicit and implicit) can seed meaningful research questions. This is a natural input to Research Taster.

5. **Taste is Subjective and Emotional:** Alon (2009) and philosophical literature emphasize that choosing good problems involves self-knowledge, fascination, and values—not just strategic calculation. Research Taster must cultivate this sensibility, not replace it.

6. **Scaffolding > Raw AI:** Supermind Ideator shows structured human-AI interaction outperforms unstructured prompting. Research Taster's value is in the scaffolding, not just the model.

7. **Human Agency Matters:** Co-creation research suggests human-led interaction preserves creativity better. Research Taster should empower, not supplant.

8. **Knowledge Grounding is Essential:** SciMON, knowledge-grounded hypothesis generation work shows that grounding in literature prevents hallucination and improves quality.
