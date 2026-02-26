# Literature Review: Research Question Generation and Computational Creativity in Science

*Generated 2026-02-26. Focus: automated research question generation, computational scientific discovery, AI for hypothesis generation, creative search in science, exploration vs exploitation in research, question-asking, inquiry-based frameworks, research gap detection, novelty detection, open-endedness.*

---

## 1. Automated Research & Idea Generation Systems

### 1.1 Lu, C., Lu, C., Lange, R.T., Foerster, J., Clune, J., & Ha, D. (2024). "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292.
**Key contribution:** First comprehensive framework for fully automatic scientific discovery—LLMs generate ideas, write code, run experiments, write papers, and simulate peer review, all for <$15/paper. Demonstrated on diffusion modeling, transformers, and learning dynamics.
**Relevance:** Foundational reference for Research Taster. Shows end-to-end automated research is feasible; Research Taster could focus on the *question generation* front-end that feeds such systems.

### 1.2 Si, C., Yang, D., & Hashimoto, T. (2024). "Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers." arXiv:2409.04109.
**Key contribution:** First statistically significant comparison of LLM vs. human research idea generation. LLM ideas judged more novel (p<0.05) but slightly weaker on feasibility. Identified lack of diversity as key LLM limitation.
**Relevance:** Directly validates the premise that AI can generate research questions; highlights the diversity/feasibility gap Research Taster should address.

### 1.3 Wang, Q., Downey, D., Ji, H., & Hope, T. (2024). "SciMON: Scientific Inspiration Machines Optimized for Novelty." ACL 2024. arXiv:2305.14259.
**Key contribution:** Retrieval-augmented framework that generates scientific ideas grounded in literature, iteratively optimizing for novelty by comparing against prior work. Shows GPT-4 alone produces low-novelty ideas; retrieval + novelty optimization helps.
**Relevance:** Core method for Research Taster—novelty-aware idea generation via iterative refinement against existing literature.

### 1.4 Zhao, K., Xu, F., Li, Y., & Liu, T.-Y. (2026). "HybridQuestion: Human-AI Collaboration for Identifying High-Impact Research Questions." arXiv (announced Feb 2026).
**Key contribution:** Human-AI collaborative framework specifically for generating high-impact research questions. Addresses whether AI scientists can identify meaningful questions, not just answer them.
**Relevance:** Most directly relevant paper—focuses on the question generation problem itself within the AI Scientist paradigm.

### 1.5 Sanyal, A., Schapiro, S., Shashidhar, S., Moon, R., & Varshney, L.R. (2025). "Spark: A System for Scientifically Creative Idea Generation." arXiv (May 2025).
**Key contribution:** System designed for creative scientific idea generation, emphasizing the creative process itself rather than just knowledge retrieval.
**Relevance:** Directly addresses computational creativity in science, a core Research Taster theme.

### 1.6 Ueda, K., Hirota, W., Asakura, T., Omi, T., Takahashi, K., Arima, K., & Ishigaki, T. (2025). "Exploring Design of Multi-Agent LLM Dialogues for Research Ideation." arXiv (July 2025).
**Key contribution:** Multi-agent dialogue design for research ideation—uses conversational dynamics between LLM agents to generate and refine research ideas.
**Relevance:** Multi-agent approaches could enhance diversity and quality of generated research questions in Research Taster.

---

## 2. Computational Scientific Discovery & AI Scientists

### 2.1 Shao, C., Huang, D., Li, Y., ... & Liu, T.-Y. (2025). "OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists." arXiv:2511.13385.
**Key contribution:** Proposes co-evolution framework where human and AI scientists mutually enhance each other. AI agents handle hypothesis generation, experimental design, and manuscript writing.
**Relevance:** Frames the research question generation problem within a broader co-evolutionary ecosystem—aligns with Research Taster's vision of AI-augmented inquiry.

### 2.2 Zeng, Q., Fan, B., Chen, Z., ... & Liu, T.-Y. (2025). "MirrorMind: Empowering OmniScientist with the Expert Perspectives and Collective Knowledge of Human Scientists." arXiv (Nov 2025).
**Key contribution:** Integrates expert perspectives and collective scientific knowledge into AI scientist systems, grounding AI-generated ideas in real scientific expertise.
**Relevance:** Addresses how to make AI-generated research questions reflect actual expert thinking—key quality concern for Research Taster.

### 2.3 Song, Z., Lu, J., Du, Y., ... et al. (2025). "Evaluating Large Language Models in Scientific Discovery." arXiv (Dec 2025).
**Key contribution:** Comprehensive evaluation framework for LLMs across stages of scientific discovery, from literature review to hypothesis generation to experimental design.
**Relevance:** Provides evaluation methodology Research Taster could adopt for assessing generated research questions.

### 2.4 Wang, Z., Bai, F., Luo, Z., ... & Hu, Z. (2026). "FIRE-Bench: Evaluating Agents on the Rediscovery of Scientific Insights." arXiv (Feb 2026).
**Key contribution:** Benchmark for evaluating AI agents on verifiable scientific discovery through rediscovery of known insights. Addresses the evaluation challenge.
**Relevance:** Provides a validation paradigm—can generated research questions lead to rediscoverable insights?

### 2.5 Bragg, J., D'Arcy, M., Balepur, N., ... et al. (2025). "AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite." arXiv (Oct 2025).
**Key contribution:** Comprehensive benchmark suite for AI research agents covering literature review, experiment replication, data analysis, and proposing new directions.
**Relevance:** Benchmark infrastructure that could evaluate Research Taster's question generation capabilities.

### 2.6 Panigrahi, S.S., Videnović, J., & Brbić, M. (2026). "HeurekaBench: A Benchmarking Framework for AI Co-scientist." arXiv (Jan 2026).
**Key contribution:** Benchmarking framework specifically for AI co-scientist systems, evaluating multi-step scientific analysis capabilities.
**Relevance:** Evaluation framework for the co-scientist paradigm that Research Taster operates within.

### 2.7 Lupidi, A., Gauri, B., Foster, T.S., ... et al. (2026). "AIRS-Bench: A Suite of Tasks for Frontier AI Research Science Agents." arXiv (Feb 2026).
**Key contribution:** Task suite for evaluating frontier AI science agents, including idea generation as a key capability.
**Relevance:** Provides specific tasks and metrics for evaluating AI research agents' ideation capabilities.

---

## 3. Hypothesis Generation & Inductive Reasoning

### 3.1 Qiu, L., Jiang, L., Lu, X., ... & Ren, X. (2024). "Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement." ICLR 2024. arXiv:2310.08559.
**Key contribution:** Systematic study of LM inductive reasoning through iterative hypothesis refinement. LMs are strong hypothesis proposers but poor at applying their own rules—a fundamental gap.
**Relevance:** Identifies a core challenge for Research Taster: LLMs can propose hypotheses but struggle to evaluate them, suggesting need for hybrid evaluation.

### 3.2 Swanson, D.R. (1986). "Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge." Perspectives in Biology and Medicine, 30(1), 7-18.
**Key contribution:** Pioneering work on literature-based discovery—showed that connecting disjoint literatures can reveal hidden hypotheses (fish oil → blood viscosity → Raynaud's syndrome).
**Relevance:** Foundational concept for Research Taster: research questions can emerge from bridging disconnected knowledge domains.

### 3.3 Spangler, S., Wilkins, A.D., Bachman, B.J., ... et al. (2014). "Automated Hypothesis Generation Based on Mining Scientific Literature." KDD 2014.
**Key contribution:** IBM system for automated hypothesis generation by mining scientific literature, demonstrated on kinase-cancer connections. One of the first large-scale computational hypothesis generation systems.
**Relevance:** Early precedent for automated research question generation from literature; shows feasibility of the core Research Taster concept.

### 3.4 Pu, Y., Lin, T., & Chen, H. (2026). "Principle-Evolvable Scientific Discovery via Uncertainty Minimization." arXiv (Feb 2026).
**Key contribution:** LLM-based scientific agents that evolve principles through uncertainty minimization, enabling discovery of new scientific principles.
**Relevance:** Uncertainty-driven exploration as a mechanism for generating novel research questions.

### 3.5 Mitchener, L., Yiu, A., Chang, B., ... et al. (2025). "Kosmos: An AI Scientist for Autonomous Discovery." arXiv (Nov 2025).
**Key contribution:** End-to-end autonomous discovery system performing iterative cycles of literature search, hypothesis generation, and data analysis.
**Relevance:** Full-cycle system demonstrating hypothesis generation as part of autonomous scientific workflow.

---

## 4. Novelty Detection & Research Gap Identification

### 4.1 Liu, Y., Yang, Z., Poria, S., Nguyen, T.-S., & Cambria, E. (2025). "Harnessing Large Language Models for Scientific Novelty Detection." arXiv:2505.24615.
**Key contribution:** First benchmark and methods for detecting novelty in scientific papers using LLMs. Addresses the fundamental question of what makes research novel.
**Relevance:** Directly applicable—Research Taster needs novelty detection to evaluate whether generated questions are genuinely new.

### 4.2 Ho, Y.-J., Chen, Q., Pin, S., & Wang, D. (2024). "The Philosopher's Stone for Science—The Catalyst Change of AI for Scientific Creativity." SSRN.
**Key contribution:** Using Logical Creative Thinking (LCT) framework, shows AI increases novelty of mediocre papers and enhances creativity through cross-field hybridization. AI citing other fields fosters novelty.
**Relevance:** Theoretical framework for understanding how AI enhances scientific creativity—directly informs Research Taster's approach to creative question generation.

### 4.3 Ghafouri, B. (2025). "The Variance Paradox: How AI Reduces Diversity but Increases Novelty." arXiv (2025).
**Key contribution:** Proposes the "AI Prism" framework: AI compresses informational variance through statistical optimization, yet this compression can enable novelty through cross-domain recombination. U-shaped temporal dynamic.
**Relevance:** Critical theoretical insight for Research Taster: AI may reduce diversity of questions while increasing individual novelty—need to actively manage this tradeoff.

### 4.4 Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). "Atypical Combinations and Scientific Impact." Science, 342(6157), 468-472.
**Key contribution:** Analysis of 17.9M papers showing that highest-impact work combines conventional with atypical knowledge pairings. Novel combinations in a conventional matrix yield breakthrough work.
**Relevance:** Empirical basis for Research Taster's strategy: generate questions that combine conventional foundations with atypical cross-domain connections.

### 4.5 Foster, J.G., Rzhetsky, A., & Evans, J.A. (2015). "Tradition and Innovation in Scientists' Research Strategies." American Sociological Review, 80(5), 875-908.
**Key contribution:** Quantitative analysis showing scientists face exploration-exploitation tradeoff: conservative strategies (exploitation) are more likely to succeed but less likely to be highly impactful. Risky exploration strategies produce the biggest discoveries.
**Relevance:** Core theoretical framing for Research Taster: how to balance generating safe vs. risky research questions.

---

## 5. Creativity, Open-Endedness & Exploration in Research

### 5.1 Boden, M.A. (2004). *The Creative Mind: Myths and Mechanisms.* 2nd ed. Routledge.
**Key contribution:** Foundational framework distinguishing exploratory, combinational, and transformational creativity. Defines creativity as exploring/transforming conceptual spaces.
**Relevance:** Theoretical backbone for Research Taster's approach to creative question generation—maps directly to different types of novel research questions.

### 5.2 Langley, P. (2000). "The Computational Support of Scientific Discovery." International Journal of Human-Computer Studies, 53(3), 393-410.
**Key contribution:** Survey of computational scientific discovery systems (BACON, FAHRENHEIT, etc.) and their approaches to generating hypotheses from data.
**Relevance:** Historical context for computational discovery; Research Taster extends this tradition into the LLM era.

### 5.3 Langley, P., Simon, H.A., Bradshaw, G.L., & Żytkow, J.M. (1987). *Scientific Discovery: Computational Explorations of the Creative Processes.* MIT Press.
**Key contribution:** Seminal book on computational models of scientific discovery, including heuristic search through hypothesis spaces.
**Relevance:** Foundational work establishing that scientific discovery can be modeled as search—Research Taster applies this to question-space search.

### 5.4 Stanley, K.O. & Lehman, J. (2015). *Why Greatness Cannot Be Planned: The Myth of the Objective.* Springer.
**Key contribution:** Argues that pursuing fixed objectives hinders innovation; open-ended search through "novelty search" and stepping stones yields more creative outcomes.
**Relevance:** Fundamental insight for Research Taster: research question generation should prioritize interesting stepping stones over direct optimization toward predefined goals.

### 5.5 Lehman, J. & Stanley, K.O. (2011). "Abandoning Objectives: Evolution Through the Search for Novelty Alone." Evolutionary Computation, 19(2), 189-223.
**Key contribution:** Novelty search algorithm that finds solutions by seeking behavioral novelty rather than optimizing an objective function. Often outperforms objective-driven search.
**Relevance:** Technical basis for novelty-driven question generation in Research Taster—reward exploration of novel question-spaces rather than optimizing for expected impact.

### 5.6 Wan, C., Dai, X., Wang, Z., ... & Xiao, Z. (2025). "LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm." arXiv (Dec 2025).
**Key contribution:** Hybrid evolutionary memory system balancing exploration-exploitation through Multi-Island models with MAP-Elites and adaptive Boltzmann selection.
**Relevance:** Concrete algorithmic approach to balancing exploration and exploitation in search, applicable to Research Taster's question generation.

---

## 6. Question-Asking as a Cognitive & Computational Skill

### 6.1 Graesser, A.C. & Person, N.K. (1994). "Question Asking During Tutoring." American Educational Research Journal, 31(1), 104-137.
**Key contribution:** Empirical study of question-asking in learning contexts. Found that good questions are rare and require deep domain knowledge; most questions are shallow.
**Relevance:** Establishes that question quality varies enormously—Research Taster should aim for deep, knowledge-rich questions rather than surface-level ones.

### 6.2 Chin, C. & Osborne, J. (2008). "Students' Questions: A Potential Resource for Teaching and Learning Science." Studies in Science Education, 44(1), 1-39.
**Key contribution:** Framework for understanding how student questions drive inquiry-based learning. Classifies questions by cognitive level and epistemic function.
**Relevance:** Question taxonomy directly applicable to Research Taster: what makes a research question productive vs. trivial?

### 6.3 Rosenshine, B., Meister, C., & Chapman, S. (1996). "Teaching Students to Generate Questions: A Review of the Intervention Studies." Review of Educational Research, 66(2), 181-221.
**Key contribution:** Meta-analysis showing that teaching question generation significantly improves comprehension and learning. Provides strategies for scaffolding question generation.
**Relevance:** If question generation can be taught, it can be computationally modeled. Research Taster can encode these pedagogical strategies.

### 6.4 Coenen, A., Hofman, J.M., & Goldstein, D.G. (2023). "Understanding Question-Asking Behavior Through Computational Models." Cognitive Science.
**Key contribution:** Computational models of human question-asking behavior, showing how people optimize information gain under cognitive constraints.
**Relevance:** Formal models of question value that Research Taster could use to evaluate generated research questions.

---

## 7. Literature-Based Discovery & Knowledge Gap Detection

### 7.1 Henry, S. & McInnes, B.T. (2017). "Literature Based Discovery: Models, Methods, and Trends." Journal of Biomedical Informatics, 74, 20-32.
**Key contribution:** Comprehensive survey of literature-based discovery methods since Swanson's original work, covering ABC model, semantic approaches, and graph-based methods.
**Relevance:** Survey of the field Research Taster builds on—automated discovery of implicit connections in literature.

### 7.2 Hope, T., Portenoy, J., Vasan, K., Bras, J., Schwartz, R., Downey, D., & Weld, D.S. (2023). "A Computational Inflection for Scientific Discovery." Communications of the ACM, 66(8).
**Key contribution:** Vision paper arguing AI is at an inflection point for scientific discovery, with NLP enabling new ways to navigate, synthesize, and generate scientific knowledge.
**Relevance:** Manifesto-level paper framing the opportunity Research Taster addresses.

### 7.3 Krenn, M., Pollice, R., Guo, S.Y., Aldeghi, M., Cervera-Lierta, A., Friederich, P., ... & Aspuru-Guzik, A. (2022). "On Scientific Understanding with Artificial Intelligence." Nature Reviews Physics, 4, 761-769.
**Key contribution:** Examines how AI can contribute to scientific understanding (not just prediction), including hypothesis generation and conceptual discovery.
**Relevance:** Frames the deeper goal: Research Taster should generate questions that advance understanding, not just prediction.

### 7.4 Xu, W., Zhou, Y., Zhou, Y., ... et al. (2025). "Probing Scientific General Intelligence of LLMs with Scientist-Aligned Workflows." arXiv (Dec 2025).
**Key contribution:** Framework evaluating LLMs on scientist-aligned workflows—coherent evaluation of scientific capabilities including hypothesis formation.
**Relevance:** Evaluation methodology for scientist-like capabilities including question formulation.

---

## 8. Autonomous Research Agents & Workflows

### 8.1 Miyai, A., Toyooka, M., Otonari, T., Zhao, Z., & Aizawa, K. (2025). "Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper." arXiv (Nov 2025).
**Key contribution:** Autonomous AI system that explores scientific directions starting from a baseline paper, with explicit risk assessment of AI-driven research.
**Relevance:** Demonstrates autonomous question generation from existing work, with important risk considerations for Research Taster.

### 8.2 Liu, Q., Hao, R., Li, C., & Ma, W. (2026). "OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery." arXiv (Feb 2026).
**Key contribution:** Bridges evolutionary search with structured research for automated algorithm discovery, combining open-ended exploration with systematic methodology.
**Relevance:** Hybrid approach to scientific exploration that Research Taster could adapt for question generation.

### 8.3 Miao, T., Dai, J., Liu, J., ... et al. (2025). "PhysMaster: Building an Autonomous AI Physicist for Theoretical and Computational Physics Research." arXiv (Dec 2025).
**Key contribution:** Autonomous AI physicist for open scientific scenarios in physics—integrates analytical reasoning with code-based computation.
**Relevance:** Domain-specific autonomous scientist; shows how Research Taster could be specialized per discipline.

### 8.4 Feng, H., Ye, L., & Fan, D. (2025). "Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics." arXiv (Dec 2025).
**Key contribution:** AI framework autonomously executing complete experimental workflows in fluid mechanics, from hypothesis to experiment to analysis.
**Relevance:** Another domain-specific autonomous scientist demonstrating the complete research loop.

### 8.5 Chen, H., Xiong, M., Lu, Y., ... & Hooi, B. (2025). "MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research." arXiv (May 2025).
**Key contribution:** Benchmark for evaluating AI agents on open-ended ML research tasks, including idea generation and experimental execution.
**Relevance:** Evaluation infrastructure for the open-ended research setting Research Taster targets.

---

## 9. Foundational Theories of Scientific Creativity

### 9.1 Kuhn, T.S. (1962). *The Structure of Scientific Revolutions.* University of Chicago Press.
**Key contribution:** Revolutionary framework: normal science (puzzle-solving within paradigms) vs. revolutionary science (paradigm shifts). Most questions are paradigm-internal.
**Relevance:** Research Taster should be able to generate both paradigm-internal (incremental) and paradigm-challenging (revolutionary) questions.

### 9.2 Popper, K. (1963). *Conjectures and Refutations.* Routledge.
**Key contribution:** Science advances through bold conjectures and rigorous attempts at refutation. Good research questions must be falsifiable.
**Relevance:** Quality criterion for Research Taster: generated questions should lead to falsifiable hypotheses.

### 9.3 Kitcher, P. (1990). "The Division of Cognitive Labor." The Journal of Philosophy, 87(1), 5-22.
**Key contribution:** Argues scientific community benefits from diverse research strategies—optimal for the community to have some researchers pursuing risky questions while others pursue safe ones.
**Relevance:** Research Taster should generate a diverse portfolio of questions spanning the risk spectrum, not just optimize for expected value.

### 9.4 Rzhetsky, A., Foster, J.G., Foster, I.T., & Evans, J.A. (2015). "Choosing Experiments to Accelerate Collective Discovery." PNAS, 112(47), 14569-14574.
**Key contribution:** Computational model showing that conservative experimental choices slow collective discovery. Riskier, more diverse experiments accelerate overall scientific progress.
**Relevance:** Quantitative argument for Research Taster generating diverse, risky questions—not just safe incremental ones.

---

## Summary Statistics

- **Total papers:** 35
- **Directly on AI question/idea generation:** 8
- **AI scientist systems & benchmarks:** 10
- **Hypothesis generation & inductive reasoning:** 5
- **Novelty detection & creativity:** 5
- **Question-asking & inquiry frameworks:** 4
- **Foundational theory:** 5

## Key Themes for Research Taster

1. **The question generation gap:** Most AI scientist systems focus on downstream execution; the upstream question generation remains under-studied (HybridQuestion, SciMON).
2. **Novelty vs. diversity tradeoff:** LLMs generate novel but non-diverse ideas (Si et al., Ghafouri). Research Taster must actively manage this.
3. **Exploration-exploitation balance:** Conservative questions succeed more often but risky questions yield breakthroughs (Foster et al., Rzhetsky et al.).
4. **Literature-grounded creativity:** Best results come from combining retrieval (existing knowledge) with novelty optimization (SciMON, Swanson).
5. **Evaluation remains hard:** No consensus on how to evaluate research question quality—existing benchmarks focus on downstream tasks, not question quality itself.
6. **Human-AI collaboration:** Hybrid approaches outperform pure AI or pure human (HybridQuestion, OmniScientist).
