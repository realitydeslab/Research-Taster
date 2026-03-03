# AI-Driven Scientific Discovery: Deep Literature Review

A comprehensive survey of computational approaches to discovering new knowledge, covering classical AI discovery systems, modern ML breakthroughs, knowledge-based discovery, open-endedness, and philosophy of science.

**Compiled for:** Research Taster project
**Date:** 2026-03-03

---

## 1. Scientific Discovery as Search (Classical AI)

### 1.1 Langley, P., Simon, H. A., Bradshaw, G. L., & Zytkow, J. M. (1987). *Scientific Discovery: Computational Explorations of the Creative Processes*. MIT Press.
- **URL:** http://www.isle.org/~langley/discovery.html
- **Key contribution:** Foundational work presenting BACON, DALTON, STAHL, and GLAUBER — AI systems that rediscovered empirical laws from the history of physics and chemistry. Demonstrated that scientific discovery could be modeled as heuristic search through a space of hypotheses.
- **Relevance:** Establishes the paradigm of discovery-as-search that Research Taster builds upon — the idea that computational agents can systematically explore knowledge spaces.

### 1.2 Langley, P. (2000). The Computational Support of Scientific Discovery. *International Journal of Human-Computer Studies*, 53(3), 393–410.
- **DOI:** 10.1006/ijhc.2000.0396
- **Key contribution:** Reviews progress in computational scientific discovery since the BACON era, identifying themes including data-driven discovery, theory revision, and experiment planning. Argues for tighter integration of discovery systems with working scientists.
- **Relevance:** Provides the intellectual lineage for AI-assisted research — the vision of computational tools that augment rather than replace human discovery.

### 1.3 Langley, P. (2016). Themes and Progress in Computational Scientific Discovery. *CCC Workshop*.
- **URL:** https://cra.org/ccc/wp-content/uploads/sites/2/2016/11/csd.11.16.pdf
- **Key contribution:** Updated overview of computational scientific discovery covering equation discovery, process model induction, and theory formation. Distinguishes between rediscovery (reproducing known results) and genuine novel discovery.
- **Relevance:** Frames the challenge that Research Taster addresses: moving beyond rediscovery to systems that find genuinely new knowledge.

### 1.4 Simon, H. A. (1973). Does Scientific Discovery Have a Logic? *Philosophy of Science*, 40(4), 471–480.
- **DOI:** 10.1086/288559
- **Key contribution:** Argues against Popper's claim that discovery is irrational, proposing that discovery follows normative patterns amenable to computational modeling. Laid groundwork for the BACON program.
- **Relevance:** Philosophical foundation for the entire enterprise of AI-driven discovery — if discovery has a logic, it can be automated or augmented.

### 1.5 Valdés-Pérez, R. E. (1999). Principles of Human-Computer Collaboration for Knowledge Discovery in Science. *Artificial Intelligence*, 107(2), 335–346.
- **DOI:** 10.1016/S0004-3702(98)00110-1
- **Key contribution:** Articulates principles for human-AI collaboration in scientific discovery, emphasizing that the most productive systems combine computational search with human judgment and domain knowledge.
- **Relevance:** Directly relevant to Research Taster's goal of augmenting researchers rather than replacing them.

---

## 2. Modern ML for Scientific Discovery

### 2.1 Jumper, J., Evans, R., Pritzel, A., et al. (2021). Highly Accurate Protein Structure Prediction with AlphaFold. *Nature*, 596, 583–589.
- **DOI:** 10.1038/s41586-021-03819-2
- **Key contribution:** Solved the 50-year protein structure prediction problem using deep learning, achieving atomic-level accuracy. Has been used by over 2 million researchers. Won Nobel Prize in Chemistry 2024.
- **Relevance:** The paradigmatic example of AI making a genuine scientific breakthrough — demonstrates that ML can solve problems humans could not at scale.

### 2.2 Merchant, A., Batzner, S., Schoenholz, S. S., et al. (2023). Scaling Deep Learning for Materials Discovery. *Nature*, 624, 80–85.
- **DOI:** 10.1038/s41586-023-06735-9
- **Key contribution:** GNoME discovered 2.2 million new crystal structures, including 380,000 stable materials — equivalent to ~800 years of conventional experimentation. Uses active learning with graph neural networks.
- **Relevance:** Shows AI can dramatically accelerate the discovery pipeline in materials science.

### 2.3 Romera-Paredes, B., Barekatain, M., Novikov, A., et al. (2024). Mathematical Discoveries from Program Search with Large Language Models. *Nature*, 625, 468–475.
- **DOI:** 10.1038/s41586-023-06924-6
- **Key contribution:** FunSearch uses LLMs to search for novel mathematical functions, making the first LLM-driven discoveries in open problems (cap set problem, bin packing). Key insight: evolving programs rather than raw solutions enables verifiability.
- **Relevance:** Directly demonstrates that LLMs can make genuine new discoveries when paired with evolutionary search.

### 2.4 Abramson, J., Adler, J., Dunger, J., et al. (2024). Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3. *Nature*, 630, 493–500.
- **DOI:** 10.1038/s41586-024-07487-w
- **Key contribution:** AlphaFold 3 extends structure prediction beyond proteins to all biomolecular interactions including DNA, RNA, ligands, and post-translational modifications using a diffusion-based architecture.
- **Relevance:** Represents the expanding frontier of AI-driven discovery in structural biology.

---

## 3. Knowledge Graph Discovery & Literature-Based Discovery

*(Searching next...)*

---

## 3. Knowledge Graph Discovery & Literature-Based Discovery

### 3.1 Swanson, D. R. (1986). Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge. *Perspectives in Biology and Medicine*, 30(1), 7–18.
- **DOI:** 10.1353/pbm.1986.0087
- **Key contribution:** Pioneered literature-based discovery (LBD) by identifying a previously unknown connection between fish oil and Raynaud's syndrome through linking disjoint literatures. Introduced the ABC model: if A relates to B in one literature, and B relates to C in another, then A–C is a candidate discovery.
- **Relevance:** Foundational for Research Taster's approach to finding novel connections across disparate knowledge domains — the core of computational serendipity.

### 3.2 Swanson, D. R. (1990). Medical Literature as a Potential Source of New Knowledge. *Bulletin of the Medical Library Association*, 78(1), 29–37.
- **URL:** https://ncbi.nlm.nih.gov/pmc/articles/PMC225324/
- **Key contribution:** Extended the ABC model, demonstrating that the medical literature contains "undiscovered public knowledge" — implicit connections that no individual researcher has made because they span disciplinary boundaries.
- **Relevance:** Motivates the idea that AI systems can discover what humans miss due to cognitive and disciplinary limitations.

### 3.3 Swanson, D. R. & Smalheiser, N. R. (1997). An Interactive System for Finding Complementary Literatures: A Stimulus to Scientific Discovery. *Artificial Intelligence*, 91(2), 183–203.
- **DOI:** 10.1016/S0004-3702(97)00008-8
- **Key contribution:** Developed Arrowsmith, a tool implementing the ABC model for systematic literature-based discovery. Demonstrated practical utility in generating testable hypotheses from published literature.
- **Relevance:** Early computational tool for augmenting human discovery — a direct precursor to AI-assisted research tools like Research Taster.

### 3.4 Thilakaratne, M., Falkner, K., & Atapattu, T. (2019). A Systematic Review on Literature-Based Discovery. *Journal of Biomedical Informatics*, 93, 103141.
- **DOI:** 10.1016/j.jbi.2019.103141
- **Key contribution:** Comprehensive survey of LBD approaches in the biomedical domain, covering open vs. closed discovery, NLP techniques, knowledge representation, and evaluation methodologies.
- **Relevance:** Maps the state of the art in computational discovery from literature — directly informs Research Taster's methodology.

### 3.5 Spangler, S., Myers, A. D., Stanoi, I., et al. (2014). Automated Hypothesis Generation Based on Mining Scientific Literature. *KDD '14*, 1877–1886.
- **DOI:** 10.1145/2623330.2623667
- **Key contribution:** IBM's system for mining scientific literature to generate novel hypotheses about kinase targets, validated experimentally. Used NLP and knowledge graphs to identify promising but unexplored connections.
- **Relevance:** Demonstrates end-to-end pipeline from literature mining to experimentally validated discovery.

---

## 4. Novelty Search & Open-Endedness

### 4.1 Lehman, J. & Stanley, K. O. (2011). Abandoning Objectives: Evolution Through the Search for Novelty Alone. *Evolutionary Computation*, 19(2), 189–223.
- **DOI:** 10.1162/EVCO_a_00025
- **Key contribution:** Demonstrated that searching for novelty rather than optimizing toward objectives can outperform objective-driven search in deceptive domains. Novelty search rewards behavioral diversity, avoiding deceptive local optima.
- **Relevance:** Core theoretical foundation for Research Taster — suggests that scientific discovery benefits from pursuing interestingness rather than optimizing for predefined goals.

### 4.2 Stanley, K. O. & Lehman, J. (2015). *Why Greatness Cannot Be Planned: The Myth of the Objective*. Springer.
- **DOI:** 10.1007/978-3-319-15524-1
- **Key contribution:** Book-length argument that ambitious objectives are often best achieved by not pursuing them directly. Uses novelty search, historical examples, and evolutionary theory to argue for "stepping stones" and serendipitous discovery.
- **Relevance:** Philosophical backbone of Research Taster's design — the argument that transformative discoveries emerge from open-ended exploration, not goal-directed optimization.

### 4.3 Lehman, J. & Stanley, K. O. (2011). Novelty Search and the Problem with Objectives. In *Genetic Programming Theory and Practice IX*, 37–56. Springer.
- **DOI:** 10.1007/978-1-4614-1770-5_3
- **Key contribution:** Synthesizes evidence that objective-driven search fails for ambitious goals, proposing novelty search as an alternative paradigm for evolutionary computation.
- **Relevance:** Technical grounding for the claim that discovery systems should optimize for novelty/interestingness rather than convergence on specific targets.

### 4.4 Stanley, K. O., Lehman, J., & Soros, L. (2017). Open-Endedness: The Last Grand Challenge You've Never Heard Of. *O'Reilly Radar*.
- **URL:** https://www.oreilly.com/radar/open-endedness-the-last-grand-challenge-youve-never-heard-of/
- **Key contribution:** Argues that creating truly open-ended systems — ones that continuously produce novel artifacts of increasing complexity, like biological evolution — is one of the greatest unsolved challenges in AI.
- **Relevance:** Positions Research Taster within the grand challenge of open-ended discovery — can we build systems that continuously generate genuinely new scientific knowledge?

---

## 5. Serendipity in Scientific Discovery

### 5.1 André, P., schraefel, m.c., Teevan, J., & Dumais, S. T. (2009). Discovery Is Never by Chance: Designing for (Un)Serendipity. *C&C '09*, 305–314.
- **DOI:** 10.1145/1640233.1640279
- **Key contribution:** Argues that serendipity requires more than chance encounters — it needs synthesis into insight. Proposes design principles for systems that foster serendipity by combining exposure to unexpected information with support for making connections.
- **Relevance:** Directly informs how Research Taster should be designed to support serendipitous discovery.

### 5.2 Simonton, D. K. (2004). *Creativity in Science: Chance, Logic, Genius, and Zeitgeist*. Cambridge University Press.
- **DOI:** 10.1017/CBO9781139165358
- **Key contribution:** Comprehensive analysis of creativity in science through the lens of chance, logic, genius, and zeitgeist. Uses combinatorial analysis to model how novel ideas emerge from recombination of existing knowledge elements.
- **Relevance:** Provides theoretical grounding for computational creativity approaches to scientific discovery.

### 5.3 Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and Innovation in Scientists' Research Strategies. *American Sociological Review*, 80(5), 875–908.
- **DOI:** 10.1177/0003122415601618
- **Key contribution:** Large-scale analysis of how scientists navigate the exploration-exploitation tradeoff. Found that most research is conservative (exploitative), combining familiar chemicals, while innovative combinations are rarer but have higher impact when successful.
- **Relevance:** Empirical evidence for the value of exploration in science — directly motivates AI systems that push researchers toward more exploratory strategies.

---

## 6. Abductive Reasoning & Hypothesis Generation

### 6.1 Pietrantuono, R. et al. (2022). Automated Hypothesis Generation via Evolutionary Abduction. *ICLR 2022 Workshop*.
- **URL:** https://openreview.net/forum?id=PnraKzlFvp
- **Key contribution:** Presents Evolutionary Abduction (EVA), combining abductive inference with evolutionary computation for automated hypothesis generation. Given observed effects, generates plausible explanatory hypotheses.
- **Relevance:** Connects evolutionary search with abductive reasoning — a mechanism Research Taster could use for hypothesis generation.

### 6.2 Agarwal, D., Majumder, B. P., et al. (2025). AUTODISCOVERY: Open-Ended Scientific Discovery via Bayesian Surprise. *Allen Institute for AI*.
- **URL:** https://allenai.org/papers/autodiscovery
- **Key contribution:** Proposes using Bayesian surprise as a driving criterion for autonomous scientific discovery, allowing AI systems to identify which questions to ask rather than relying on human-specified goals. Uses LLMs with surprise-guided exploration.
- **Relevance:** Directly aligned with Research Taster's vision — AI that drives its own exploration based on interestingness/surprise rather than predefined objectives.

### 6.3 Holmes, W. R. et al. (2024). Automating the Practice of Science: Opportunities, Challenges, and Implications. *PNAS*, 121(43), e2401238121.
- **DOI:** 10.1073/pnas.2401238121
- **Key contribution:** Comprehensive assessment of automation in scientific practice, discussing where the greatest opportunities lie, current bottlenecks, and ethical implications of automating science.
- **Relevance:** Maps the landscape of automated science — provides context for where Research Taster fits in the broader automation picture.

### 6.4 Ke, Y., et al. (2025). BioDisco: Multi-Agent Hypothesis Generation with Dual-Mode Evidence, Iterative Feedback and Temporal Evaluation. *arXiv:2508.01285*.
- **URL:** https://arxiv.org/html/2508.01285v1
- **Key contribution:** Multi-agent system for generating novel scientific hypotheses using LLMs with dual evidence modes and iterative refinement. Includes temporal evaluation to assess whether generated hypotheses predict future findings.
- **Relevance:** State-of-the-art in LLM-based hypothesis generation — represents the frontier Research Taster operates in.

### 6.5 Mitchener, L., et al. (2024). Kosmos: An AI Scientist for Autonomous Discovery. *arXiv:2511.02824*.
- **URL:** https://arxiv.org/pdf/2511.02824
- **Key contribution:** End-to-end AI scientist system capable of autonomous experimental design, execution, and analysis. Demonstrated in biological discovery contexts.
- **Relevance:** Represents the most ambitious vision of AI-driven discovery — fully autonomous scientific agents.

---

## 7. Discovery in Specific Fields

### Drug Discovery

### 7.1 Vamathevan, J., Clark, D., Czodrowski, P., et al. (2019). Applications of Machine Learning in Drug Discovery and Development. *Nature Reviews Drug Discovery*, 18, 463–477.
- **DOI:** 10.1038/s41573-019-0024-5
- **Key contribution:** Comprehensive review of ML applications across the drug discovery pipeline: target identification, hit discovery, lead optimization, and clinical trial design. Maps where AI adds most value.
- **Relevance:** Exemplar of domain-specific AI discovery — shows how the discovery pipeline can be decomposed and accelerated by AI.

### 7.2 Wang, E., Schmidgall, S., et al. (2025). TxGemma: Efficient and Agentic LLMs for Therapeutics. *Google DeepMind/Google Research*.
- **URL:** https://arxiv.org/pdf/2504.06196
- **Key contribution:** Suite of LLMs (2B–27B parameters) fine-tuned for therapeutic property prediction across small molecules, proteins, nucleic acids, and diseases. Achieves generalist performance across 66 therapeutic development tasks.
- **Relevance:** Represents the frontier of LLM-based drug discovery — general-purpose AI for the therapeutic pipeline.

### Materials Discovery

### 7.3 Merchant, A. et al. (2023). [See entry 2.2 — GNoME]

### Mathematical Discovery

### 7.4 Davies, A., Veličković, P., Buesing, L., et al. (2021). Advancing Mathematics by Guiding Human Intuition with AI. *Nature*, 600, 70–74.
- **DOI:** 10.1038/s41586-021-04086-x
- **Key contribution:** Used ML to discover previously unknown connections in pure mathematics — specifically new results in knot theory and representation theory. Crucially, AI guided human mathematicians' intuition rather than proving theorems autonomously.
- **Relevance:** Model for human-AI collaboration in discovery — AI identifies patterns, humans provide interpretation and proof.

### 7.5 Raayoni, G., Gottlieb, S., Manor, Y., et al. (2021). Generating Conjectures on Fundamental Constants with the Ramanujan Machine. *Nature*, 590, 67–73.
- **DOI:** 10.1038/s41586-021-03229-4
- **Key contribution:** Automated system that generates mathematical conjectures about fundamental constants (π, e, ζ). Uses MITM and gradient descent algorithms to discover new continued fraction representations. Named after Ramanujan's intuitive approach to mathematics.
- **Relevance:** Demonstrates AI can generate novel mathematical conjectures — extends discovery beyond pattern recognition to conjecture generation.

### 7.6 Beit-Halachmi, I. & Kaminer, I. (2024). The Ramanujan Library — Automated Discovery on the Hypergraph of Integer Relations. *arXiv:2412.12361*.
- **URL:** https://arxiv.org/pdf/2412.12361
- **Key contribution:** Creates the first library dedicated to mathematical constants and their interrelations, enabling systematic discovery of connections between constants across different fields. Collaborative platform for algorithm development.
- **Relevance:** Infrastructure for automated mathematical discovery — shows how knowledge organization enables further discovery.

---

## 8. Philosophy of Discovery

### 8.1 Popper, K. (1934/1959). *The Logic of Scientific Discovery*. Routledge.
- **DOI:** 10.4324/9780203994627
- **Key contribution:** Foundational work arguing that scientific knowledge advances through conjecture and refutation (falsificationism). Claimed the "context of discovery" was irrational and only the "context of justification" could be analyzed logically — a claim that computational discovery research directly challenges.
- **Relevance:** The philosophical opponent — Research Taster argues that discovery CAN be systematized, contra Popper's skepticism about the logic of discovery.

### 8.2 Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.
- **DOI:** 10.7208/chicago/9780226458144.001.0001
- **Key contribution:** Introduced "paradigm shifts" and "normal science" — the idea that science alternates between cumulative puzzle-solving within a paradigm and revolutionary shifts that overthrow it. Distinguishes between incremental and revolutionary discovery.
- **Relevance:** Raises the question: can AI systems produce paradigm shifts, or are they limited to "normal science" within existing paradigms?

### 8.3 Lakatos, I. (1970). Falsification and the Methodology of Scientific Research Programmes. In *Criticism and the Growth of Knowledge*, 91–196. Cambridge University Press.
- **DOI:** 10.1017/CBO9781139171434.009
- **Key contribution:** Proposed "research programmes" as the unit of scientific appraisal, with a "hard core" of assumptions protected by a "protective belt" of auxiliary hypotheses. Distinguished progressive from degenerative programmes.
- **Relevance:** Framework for evaluating whether AI-driven discovery is progressive (generating novel predictions) or degenerative (only accommodating known results).

### 8.4 Kuhn, T. S. (1970). Logic of Discovery or Psychology of Research? In Lakatos, I. & Musgrave, A. (Eds.), *Criticism and the Growth of Knowledge*, 1–23. Cambridge University Press.
- **URL:** https://www.cambridge.org/core/books/criticism-and-the-growth-of-knowledge/logic-of-discovery-or-psychology-of-research/AEEDF747C8822D4F5A053BBD4B4890BC
- **Key contribution:** Kuhn's response to Popper, arguing that the logic of discovery is inseparable from the psychology and sociology of scientific communities. Discovery is a social, not purely logical, process.
- **Relevance:** Suggests AI discovery systems must account for social dimensions of science — not just logical search.

---

## 9. Exploration-Exploitation in Research

### 9.1 Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and Innovation in Scientists' Research Strategies. *American Sociological Review*, 80(5), 875–908.
- **DOI:** 10.1177/0003122415601618
- **Key contribution:** Analyzed millions of biomedical papers showing scientists overwhelmingly pursue conservative strategies. Innovative combinations are rare but higher-impact. Demonstrates the exploration-exploitation tradeoff in real scientific practice.
- **Relevance:** Key empirical motivation for Research Taster — AI can push researchers toward more exploratory strategies.

### 9.2 Rzhetsky, A., Foster, J. G., Foster, I. T., & Evans, J. A. (2015). Choosing Experiments to Accelerate Collective Discovery. *PNAS*, 112(47), 14569–14574.
- **DOI:** 10.1073/pnas.1509757112
- **Key contribution:** Models scientific knowledge as a network and analyzes how experiment choices affect discovery pace. Found that conservative strategies slow science, especially in mature fields. More risk and less redundancy would accelerate discovery.
- **Relevance:** Provides the quantitative argument for why AI should guide researchers toward exploration.

---

## 10. AI Scientists & Autonomous Research Systems

### 10.1 Lu, C., Lu, C., Lange, R. T., et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. *arXiv:2408.06292*.
- **URL:** https://arxiv.org/abs/2408.06292
- **Key contribution:** First comprehensive framework for fully automated scientific discovery using LLMs: idea generation, experiment design, execution, paper writing, and peer review — all without human intervention. Demonstrated on ML research tasks.
- **Relevance:** The most ambitious instantiation of the Research Taster vision — end-to-end autonomous research.

### 10.2 Tang, J., Xia, L., Li, Z., & Huang, C. (2025). AI-Researcher: Autonomous Scientific Innovation. *arXiv:2505.18705*.
- **URL:** https://arxiv.org/html/2505.18705v1
- **Key contribution:** Fully autonomous research system using LLMs with agentic frameworks for scientific innovation. Builds on the AI Scientist paradigm with improved reasoning and automation capabilities.
- **Relevance:** Represents the state of the art in autonomous AI research systems.

### 10.3 Mitchener, L. et al. (2024). Kosmos: An AI Scientist for Autonomous Discovery. [See entry 6.5]

---
