# Deep Literature Review: The AI Scientist — Autonomous & Semi-Autonomous Systems for Scientific Research

*Compiled for Research Taster project, March 2026*

---

## 1. End-to-End Autonomous Research Systems

### 1.1 The AI Scientist (v1)
**Lu, C., Lu, C., Lange, R.T., Foerster, J., Clune, J., & Ha, D. (2024).** The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. *arXiv preprint arXiv:2408.06292*.
- **URL:** https://arxiv.org/abs/2408.06292
- **Key contribution:** First comprehensive framework for fully automatic scientific discovery using LLMs. The system generates research ideas, writes code, runs experiments, visualizes results, writes full papers, and conducts automated peer review — all at ~$15 per paper. Demonstrated novel contributions in ML domains (language modeling, diffusion models, grokking).
- **Relevance to Research Taster:** The canonical reference for autonomous AI research. Directly demonstrates end-to-end automation of the research pipeline, though limited to ML subdomains. Raises key questions about quality, novelty assessment, and the role of human oversight.

### 1.2 The AI Scientist v2
**Yamada, Y., Lange, R.T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025).** The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. *Sakana AI Technical Report*.
- **URL:** https://pub.sakana.ai/ai-scientist-v2/paper/paper.pdf
- **Key contribution:** Extends v1 with agentic tree search for hypothesis exploration, achieving the first entirely AI-generated peer-review-accepted workshop paper (ICLR 2025 workshop). Iteratively formulates hypotheses, designs experiments, analyzes data, and writes manuscripts.
- **Relevance to Research Taster:** Shows rapid progress — from rejected papers to workshop acceptance in under a year. The tree search mechanism for navigating research spaces is a key architectural insight.

### 1.3 Google AI Co-Scientist
**Gottweis, J., Natarajan, V., et al. (2025).** Accelerating Scientific Breakthroughs with an AI Co-Scientist. *Google Research, February 19, 2025*.
- **URL:** https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- **Key contribution:** Multi-agent AI system built on Gemini 2.0 as a virtual scientific collaborator. Generates novel hypotheses and research proposals using debate and refinement among specialized agents. Focused on biomedical discovery with experimental validation.
- **Relevance to Research Taster:** Contrasts with the fully autonomous approach — Google explicitly frames this as augmentation (co-scientist) rather than replacement. The multi-agent debate architecture (generate, critique, refine) is a key design pattern.

### 1.4 AI-Researcher
**Tang, J., Xia, L., Li, Z., & Huang, C. (2025).** AI-Researcher: Autonomous Scientific Innovation. *arXiv preprint arXiv:2505.18705*.
- **URL:** https://arxiv.org/abs/2505.18705
- **Key contribution:** Fully autonomous research system from The University of Hong Kong that orchestrates the complete research lifecycle. Introduces evaluation framework for measuring quality of AI-generated research across novelty, significance, and correctness dimensions.
- **Relevance to Research Taster:** Another entry in the growing ecosystem of end-to-end research systems, demonstrating that the AI Scientist paradigm is being widely replicated and extended.

### 1.5 Microsoft R&D-Agent
**Yang, X., Yang, X., Fang, S., et al. (2025).** R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution. *Microsoft Research Asia*.
- **URL:** https://arxiv.org/abs/2505.14738
- **Key contribution:** Microsoft's approach to automating data-driven AI solution building through LLM-powered research and development. Focuses on the practical R&D workflow rather than academic paper writing.
- **Relevance to Research Taster:** Represents the industry perspective on AI research automation — focused on engineering utility rather than scientific novelty.

### 1.6 Kosmos: An AI Scientist for Autonomous Discovery
**Mitchener, L., Yiu, A., Chang, B., et al. (2025).** Kosmos: An AI Scientist for Autonomous Discovery. *arXiv preprint arXiv:2511.02824*.
- **URL:** https://arxiv.org/abs/2511.02824
- **Key contribution:** Large-scale autonomous research system with experimental validation capabilities. Demonstrates AI-driven discovery in materials science and biomedical domains with physical experiment integration.
- **Relevance to Research Taster:** Bridges computational and physical experimentation — an important step beyond ML-only AI scientists.

---

## 2. Agent-Based Scientific Discovery

### 2.1 ChemCrow
**Bran, A.M., Cox, S., Schilter, O., Baldassari, C., White, A.D., & Schwaller, P. (2024).** Augmenting Large Language Models with Chemistry Tools. *Nature Machine Intelligence, 6*, 525–535.
- **DOI:** https://doi.org/10.1038/s42256-024-00832-8
- **URL:** https://arxiv.org/abs/2304.05376
- **Key contribution:** LLM chemistry agent integrating 18 expert-designed tools with GPT-4 for tasks across organic synthesis, drug discovery, and materials design. Demonstrated that tool-augmented LLMs can autonomously plan and execute chemistry workflows, including interfacing with robotic laboratories.
- **Relevance to Research Taster:** Pioneering example of domain-specific scientific agents. Shows the tool-augmentation paradigm — LLMs alone can't do science, but LLMs + specialized tools can.

### 2.2 Coscientist
**Boiko, D.A., MacKnight, R., Kline, B., & Gomes, G. (2023).** Autonomous Chemical Research with Large Language Models. *Nature, 624*, 570–578.
- **DOI:** https://doi.org/10.1038/s41586-023-06792-0
- **Key contribution:** First demonstration of an LLM-driven system performing real-world chemical synthesis autonomously, including palladium-catalyzed cross-coupling reactions. Integrates LLMs with robotic lab platforms at Carnegie Mellon.
- **Relevance to Research Taster:** Key example of AI going beyond computational experiments to physical-world research. Raises questions about safety and oversight in autonomous lab work.

### 2.3 FunSearch
**Romera-Paredes, B., Barekatain, M., Novikov, A., et al. (2024).** Mathematical Discoveries from Program Search with Large Language Models. *Nature, 625*, 468–475.
- **DOI:** https://doi.org/10.1038/s41586-023-06924-6
- **URL:** https://www.nature.com/articles/s41586-023-06924-6
- **Key contribution:** Evolutionary procedure pairing a pretrained LLM with a systematic evaluator to discover new mathematical constructions. Solved open problems in extremal combinatorics (cap set problem) and found new bin-packing heuristics. First LLM-driven discovery of verifiably new mathematical knowledge.
- **Relevance to Research Taster:** Demonstrates that AI can make genuine mathematical discoveries, not just reproduce known results. The evaluator-in-the-loop approach is key to avoiding hallucination.

### 2.4 AutoLabs
**Panapitiya, G., Saldanha, E., Job, H., & Hess, O. (2025).** AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation. *arXiv preprint arXiv:2509.25651*.
- **URL:** https://arxiv.org/abs/2509.25651
- **Key contribution:** Multi-agent system with self-correction capabilities for autonomous chemical experimentation. Introduces cognitive architectures that enable error detection and recovery in lab automation.
- **Relevance to Research Taster:** Addresses a critical gap — error handling and robustness in autonomous research systems.

---

## 3. Self-Driving Laboratories

### 3.1 Atlas: A Brain for Self-Driving Laboratories
**Hickman, R.J., Sim, M., Pablo-García, S., et al. (2025).** Atlas: A Brain for Self-Driving Laboratories. *Digital Discovery, 4*(4).
- **DOI:** https://doi.org/10.1039/D4DD00115J
- **URL:** https://pubs.rsc.org/en/content/articlelanding/2025/dd/d4dd00115j
- **Key contribution:** Decision-making framework for self-driving labs (SDLs) that goes beyond standard Bayesian optimization. Addresses diversity of hardware constraints and scientific questions with a unified SDL "brain" architecture.
- **Relevance to Research Taster:** SDLs represent the physical counterpart to computational AI scientists. Atlas shows how to build general-purpose decision-making for diverse experimental setups.

### 3.2 Benchmarking Self-Driving Labs
**Adesiji, A.D., Wang, J., Kuo, C.-S., & Brown, K.A. (2025).** Benchmarking Self-Driving Labs. *Digital Discovery, 5*(1), 14–27.
- **DOI:** https://doi.org/10.1039/D5DD00337G
- **Key contribution:** Comprehensive review of how researchers benchmark optimization in SDLs. Provides heuristic simulations to contextualize common metrics (enhancement factor, acceleration factor).
- **Relevance to Research Taster:** Important for understanding how to evaluate autonomous research systems — what metrics matter and how to compare human vs. AI experimental efficiency.

### 3.3 Autonomous Self-Driving Laboratories: Technology and Policy Review
**Royal Society Open Science (2025).** Autonomous 'Self-Driving' Laboratories: A Review of Technology and Policy Implications. *Royal Society Open Science, 12*(7), 250646.
- **URL:** https://royalsocietypublishing.org/doi/10.1098/rsos.250646
- **Key contribution:** Comprehensive review of SDL technology landscape including policy implications, safety considerations, and governance frameworks for autonomous experimentation.
- **Relevance to Research Taster:** Addresses the governance dimension — what policies and safeguards are needed for autonomous labs? Directly relevant to responsible deployment of AI research systems.

### 3.4 Evolution-Guided Bayesian Optimization for SDLs
**npj Computational Materials (2024).** Evolution-Guided Bayesian Optimization for Constrained Multi-Objective Optimization in Self-Driving Labs.
- **DOI:** https://doi.org/10.1038/s41524-024-01274-x
- **Key contribution:** Combines evolutionary strategies with Bayesian optimization for multi-objective problems in SDLs. Addresses the challenge of constrained optimization in real experimental settings.
- **Relevance to Research Taster:** Technical advance in the decision-making algorithms that power autonomous experimentation.

### 3.5 Self-Driving Laboratories for Chemistry and Materials Science (Collection)
**Nature (2024).** Self-Driving Laboratories for Chemistry and Materials Science. *Nature Collection*.
- **URL:** https://www.nature.com/collections/eiiadfbbhb
- **Key contribution:** Curated Nature collection of papers on SDLs. Provides broad overview of the field including autonomous synthesis, characterization, and optimization platforms.
- **Relevance to Research Taster:** Useful entry point for understanding the breadth of SDL applications.

---

## 4. AI for Paper Writing, Reviewing, and Meta-Science

### 4.1 LLM Feedback in Peer Review (Large-Scale Randomized Study)
**Nature Machine Intelligence (2026).** A Large-Scale Randomized Study of Large Language Model Feedback in Peer Review.
- **DOI:** https://doi.org/10.1038/s42256-026-01188-x
- **URL:** https://www.nature.com/articles/s42256-026-01188-x
- **Key contribution:** First large-scale randomized controlled trial examining LLM-generated feedback in peer review. Provides empirical evidence on how AI review compares to human review quality.
- **Relevance to Research Taster:** Directly relevant to understanding AI's role in the quality assurance of research — can AI review be as good as human review?

### 4.2 DeepReview
**Zhu, M., Weng, Y., Yang, L., & Zhang, Y. (2025).** DeepReview: Improving LLM-based Paper Review with Human-like Deep Thinking Process. *Proceedings of ACL 2025*, 29330–29355.
- **URL:** https://aclanthology.org/2025.acl-long.1420.pdf
- **Key contribution:** Introduces deep thinking processes for LLM-based paper review, moving beyond surface-level assessment. Explicitly positions as assistance rather than replacement for human reviewers.
- **Relevance to Research Taster:** Shows the state of the art in automated reviewing — a critical component of the AI scientist pipeline.

### 4.3 MetaWriter
**Sun, L., Tao, S., Hu, J., & Dow, S.P. (2024).** MetaWriter: Exploring the Potential and Perils of AI Writing Support in Scientific Peer Review. *Proceedings of the ACM on Human-Computer Interaction, 8*(CSCW1), 1–32.
- **DOI:** https://doi.org/10.1145/3637371
- **Key contribution:** Empirical study of AI writing support in peer review, examining both benefits and risks. Finds that AI can improve review quality but also introduces new biases.
- **Relevance to Research Taster:** Important for understanding the human factors dimension — how do scientists interact with AI writing support?

### 4.4 AI-Generated Literature Reviews Threaten Scientific Progress
**Zhang, L. (2025).** AI-Generated Literature Reviews Threaten Scientific Progress. *Nature, 631*, d41586-025-01603-0.
- **URL:** https://www.nature.com/articles/d41586-025-01603-0
- **Key contribution:** Commentary arguing that AI tools like OpenAI's "deep research" could undermine scientific progress by producing plausible but shallow literature reviews. Warns about erosion of deep reading and critical thinking.
- **Relevance to Research Taster:** Direct critique of the approach Research Taster might take — using AI for literature review. Highlights risks of superficial engagement with literature.

### 4.5 Automated Literature Research and Review Generation
**National Science Review (2025).** Automated Literature Research and Review-Generation Method Based on Large Language Models.
- **DOI:** https://doi.org/10.1093/nsr/nwaf169
- **URL:** https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwaf169/8120226
- **Key contribution:** Systematic method for automating literature search and review generation using LLMs. Provides pipeline from query to structured review.
- **Relevance to Research Taster:** Directly relevant methodology for Research Taster's literature review capabilities.

### 4.6 Is Your Paper Being Reviewed by an LLM?
**Yu, S., Luo, M., Madasu, A., Lal, V., & Howard, P. (2025).** Is Your Paper Being Reviewed by an LLM? Benchmarking AI Text Detection in Peer Review. *arXiv preprint arXiv:2502.19614*.
- **URL:** https://arxiv.org/abs/2502.19614
- **Key contribution:** Benchmarks AI text detection methods in the peer review context. Addresses growing concerns about LLM-generated reviews infiltrating conference review processes.
- **Relevance to Research Taster:** Raises important questions about the integrity of AI-generated scientific content and how to detect it.

### 4.7 Research Quality Evaluation by AI
**Scientometrics (2025).** Research Quality Evaluation by AI in the Era of Large Language Models: Advantages, Disadvantages, and Systemic Effects. *Scientometrics, 130*, 5309–5321.
- **DOI:** https://doi.org/10.1007/s11192-025-05361-8
- **Key contribution:** Opinion paper examining how AI threatens to displace bibliometrics as the primary method for research quality assessment. Discusses systemic effects on the research ecosystem.
- **Relevance to Research Taster:** Important for understanding how AI-driven quality evaluation could reshape academia.

---

## 5. Benchmarks for AI Research Agents

### 5.1 MLR-Bench
**Chen, H., Xiong, M., Lu, Y., Han, W., et al. (2025).** MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research. *NeurIPS 2025*.
- **DOI:** https://doi.org/10.48550/arXiv.2505.19955
- **URL:** https://arxiv.org/abs/2505.19955
- **Key contribution:** Comprehensive benchmark with 201 research tasks from NeurIPS, ICLR, and ICML workshops. Includes MLR-Judge (automated evaluation) and MLR-Agent (modular agent scaffold) covering idea generation, proposal formulation, experimentation, and paper writing.
- **Relevance to Research Taster:** The leading benchmark for evaluating AI research agents. Essential for positioning Research Taster's capabilities against existing systems.

### 5.2 ScienceAgentBench
**Chen, Z., Chen, S., Ning, Y., Zhang, Q., et al. (2024).** ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. *ICLR 2025*.
- **URL:** https://arxiv.org/abs/2410.05080
- **Key contribution:** Benchmark focused on individual tasks in the scientific workflow (data analysis, visualization, modeling) rather than end-to-end automation. Argues for rigorous per-task assessment before claiming end-to-end capability.
- **Relevance to Research Taster:** Provides a more granular evaluation framework — instead of asking "can AI do research?" it asks "can AI do each step well?"

---

## 6. Critiques and Limitations

### 6.1 Evaluating Sakana's AI Scientist (ARI Critique)
**Beel, J., Kan, M.-Y., & Baumgart, M. (2025).** Evaluating Sakana's AI Scientist for Autonomous Research: Wishful Thinking or an Emerging Reality Towards 'Artificial Research Intelligence' (ARI)? *University of Siegen / NUS*.
- **URL:** https://arxiv.org/abs/2502.14297
- **Key contribution:** Rigorous reproduction and evaluation of the AI Scientist system. Introduces the term "Artificial Research Intelligence" (ARI) as a milestone toward AGI. Finds mixed results — bold claims vs. actual capability gaps.
- **Relevance to Research Taster:** Essential critical perspective. Shows that current AI scientist systems have significant limitations in practice despite impressive demos.

### 6.2 The More You Automate, the Less You See
**Luo, Z., Kasirzadeh, A., & Shah, N.B. (2025).** The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems. *Carnegie Mellon University*.
- **URL:** https://arxiv.org/abs/2509.08713
- **Key contribution:** Examines the internal workflows of AI scientist systems and identifies hidden flaws — errors that compound through the pipeline, lack of genuine understanding, and risks to research integrity.
- **Relevance to Research Taster:** Critical for designing Research Taster — identifies specific failure modes to avoid and argues for human oversight at key decision points.

### 6.3 Risks of AI Scientists: Prioritizing Safeguarding over Autonomy
**Nature Communications (2025).** Risks of AI Scientists: Prioritizing Safeguarding over Autonomy.
- **DOI:** https://doi.org/10.1038/s41467-025-63913-1
- **URL:** https://www.nature.com/articles/s41467-025-63913-1
- **Key contribution:** Perspective examining vulnerabilities in AI scientists — misuse potential, safety concerns, and the need for safeguards. Argues for prioritizing safety mechanisms over increasing autonomy.
- **Relevance to Research Taster:** Essential safety reference. Directly informs how Research Taster should balance autonomy with safeguards.

### 6.4 AI Scientists Fail Without Strong Implementation Capability
**Zhu, M., Xie, Q., Weng, Y., et al. (2025).** AI Scientists Fail Without Strong Implementation Capability. *arXiv preprint arXiv:2506.01372*.
- **URL:** https://arxiv.org/abs/2506.01372
- **Key contribution:** Demonstrates that AI scientist systems are bottlenecked by implementation capability — the ability to write correct, executable code for experiments. Even with good ideas, poor implementation leads to failed research.
- **Relevance to Research Taster:** Identifies the key bottleneck in current systems. Research Taster should focus on robust implementation capabilities, not just idea generation.

### 6.5 The Rise of the Research Automaton
**Sætra, H.S. (2025).** The Rise of the Research Automaton: Science as Process or Product in the Era of Generative AI? *AI & Society*.
- **DOI:** https://doi.org/10.1007/s00146-025-02557-7
- **Key contribution:** Philosophical analysis distinguishing science-as-process from science-as-product. Argues that automating the product (papers) without the process (understanding) undermines the epistemic purpose of science.
- **Relevance to Research Taster:** Foundational philosophical challenge — does Research Taster produce knowledge or merely papers? Relevant to the "tasting" metaphor itself.

### 6.6 Artificial Intelligence in Peer Review (JAMA)
**JAMA (2025).** Artificial Intelligence in Peer Review.
- **URL:** https://jamanetwork.com/journals/jama/fullarticle/2838453
- **Key contribution:** Medical perspective on AI in peer review, examining implications for clinical research quality and patient safety.
- **Relevance to Research Taster:** Cross-domain perspective on AI review from a field where stakes (patient health) make quality especially critical.

---

## 7. Surveys and Frameworks

### 7.1 From AI for Science to Agentic Science
**Wei, J., Yang, Y., Zhang, X., et al. (2025).** From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery. *Shanghai AI Laboratory et al.*
- **URL:** https://arxiv.org/abs/2508.14111
- **Key contribution:** Comprehensive survey tracing the evolution from "AI for Science" (AI as tool) to "Agentic Science" (AI as autonomous researcher). Maps the landscape of autonomous scientific discovery systems across domains.
- **Relevance to Research Taster:** The most comprehensive recent survey of the field. Essential for positioning Research Taster within the broader landscape.

### 7.2 Autonomous Agents for Scientific Discovery
**Zhou, L., Ling, H., Fu, C., et al. (2025).** Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics. *Texas A&M et al.*
- **URL:** https://arxiv.org/abs/2510.09901
- **Key contribution:** Framework for orchestrating multiple types of agents (scientist agents, code agents, physics simulators) for scientific discovery. Emphasizes the integration of domain knowledge with computational capabilities.
- **Relevance to Research Taster:** Architectural reference for how to design multi-agent scientific discovery systems.

### 7.3 Scientific Discoveries by LLM Agents
**So, R. (2025).** Scientific Discoveries by LLM Agents. *4open.science*.
- **URL:** https://project-rachel.4open.science/Rachel.So.Scientific.Discoveries.LLM.Agents.pdf
- **Key contribution:** Review of LLM agents in scientific discovery, covering the evolution from text generators to autonomous agents capable of the entire research pipeline. Surveys multi-agent systems with specialized roles (scientist, critic, evaluator).
- **Relevance to Research Taster:** Good overview of the multi-agent paradigm for scientific research, directly relevant to Research Taster's architecture.

### 7.4 Benefits and Risks of Using AI Agents in Research
**PMC/NIH (2025).** Benefits and Risks of Using AI Agents in Research.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12872602/
- **Key contribution:** Balanced assessment of AI agents in research from a biomedical perspective, covering benefits (speed, scale) and risks (bias, hallucination, deskilling).
- **Relevance to Research Taster:** Provides a measured perspective useful for framing Research Taster's value proposition.

### 7.5 Enhancing Agentic Scientific Discovery with VLMs
**Gandhi, K., Bolliet, B., & Zubeldia, I. (2025).** Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities. *arXiv preprint arXiv:2511.14631*.
- **URL:** https://arxiv.org/abs/2511.14631
- **Key contribution:** Shows that multi-agent systems guided by vision-language models (VLMs) improve end-to-end autonomous scientific discovery. Uses plots as verifiable checkpoints with VLM-as-a-judge evaluation.
- **Relevance to Research Taster:** Important extension — most AI scientist systems are text-only; this adds visual reasoning, which is critical for interpreting experimental results.

---

## 8. Historical Systems

### 8.1 DENDRAL
**Lindsay, R.K., Buchanan, B.G., Feigenbaum, E.A., & Lederberg, J. (1993).** DENDRAL: A Case Study of the First Expert System for Scientific Hypothesis Formation. *Artificial Intelligence, 61*, 209–261.
- **URL:** http://web.mit.edu/6.034/www/6.s966/dendral-history.pdf
- **Key contribution:** The first expert system for scientific hypothesis formation (started 1964). Automated identification of organic molecules from mass spectra using chemistry knowledge. Pioneered the idea that computers could generate and test scientific hypotheses.
- **Relevance to Research Taster:** The historical origin of AI-driven scientific discovery. Shows that the dream of automated science is 60+ years old, and traces the evolution from expert systems to LLM agents.

### 8.2 Meta-DENDRAL
**Feigenbaum, E.A., & Buchanan, B.G. (1993).** DENDRAL and Meta-DENDRAL: Roots of Knowledge Systems and Expert System Applications. *Artificial Intelligence, 59*, 233–240.
- **URL:** https://stacks.stanford.edu/file/druid:pj337tr4694/pj337tr4694.pdf
- **Key contribution:** Meta-DENDRAL extended DENDRAL by learning new rules for mass spectrometry interpretation — one of the first machine learning systems applied to scientific discovery.
- **Relevance to Research Taster:** Early example of learning-to-discover rather than just applying fixed rules. Relevant to Research Taster's meta-learning aspirations.

### 8.3 BACON
**Langley, P. (1977).** BACON: A Production System That Discovers Empirical Laws. *Proceedings of IJCAI-77*.
- **URL:** https://www.ijcai.org/Proceedings/77-1/Papers/057.pdf
- **Key contribution:** Production system capable of rediscovering simple empirical laws (e.g., Kepler's third law, Ohm's law) from numerical data. Demonstrated that scientific discovery could be modeled as heuristic search.
- **Relevance to Research Taster:** Foundational work on computational scientific discovery. BACON's approach of finding patterns in data foreshadows modern data-driven AI science.

### 8.4 EURISKO
**Lenat, D.B. (1983).** EURISKO: A Program That Learns New Heuristics and Domain Concepts. *Artificial Intelligence, 21*, 61–98.
- **URL:** https://users.cs.northwestern.edu/~mek802/papers/not-mine/Lenat_EURISKO.pdf
- **Key contribution:** Extended Lenat's earlier AM program to learn not just concepts but new heuristics for discovery itself. Demonstrated cross-domain discovery but ultimately failed due to inability to learn powerful domain-specific heuristics.
- **Relevance to Research Taster:** EURISKO's failure mode — inability to develop deep domain expertise — foreshadows challenges facing current AI scientists. The lesson: broad search without deep understanding has limits.

### 8.5 AM (Automated Mathematician)
**Lenat, D.B. (1983).** Theory Formation by Heuristic Search: The Nature of Heuristics II. *Artificial Intelligence, 21*, 31–59.
- **URL:** https://users.cs.northwestern.edu/~mek802/papers/not-mine/Lenat_1983_theory_formation_by_heuristic_search.pdf
- **Key contribution:** AM explored mathematical concepts guided by heuristics, discovering concepts like prime numbers and Goldbach's conjecture from basic set theory. Pioneered learning by discovery in mathematics.
- **Relevance to Research Taster:** Shows that AI mathematical discovery has a long history. AM's creative exploration approach (guided by "interestingness" heuristics) is echoed in modern AI scientist systems.

---

## 9. Human-AI Collaboration in Science

### 9.1 Autonomous Multi-Agent Research (361-Project Case Study)
**OpenReview (2025).** Autonomous Multi-Agent Scientific Research: A 361-Project Case Study in Thermoelectric Materials Discovery.
- **URL:** https://openreview.net/pdf?id=6jqcouwCay
- **Key contribution:** Largest-scale autonomous research study — 361 thermoelectric materials projects without human intervention. Hierarchical architecture spanning experimental validation, physics checks, ML modeling, and documentation. Achieved 100% physical constraint compliance.
- **Relevance to Research Taster:** Demonstrates autonomous research at unprecedented scale, but also reveals limitations in systematic metric capture and the importance of knowledge accumulation (7,500 RAG entries).

### 9.2 Open Source Planning & Control for Autonomous Discovery
**Xu, L., Sarkar, M., Lonappan, A.I., et al. (2025).** Open Source Planning & Control System with Language Agents for Autonomous Scientific Discovery. *arXiv preprint arXiv:2507.07257*.
- **URL:** https://arxiv.org/abs/2507.07257
- **Key contribution:** Open-source framework for planning and control in autonomous scientific discovery. Provides modular architecture that can be adapted to different scientific domains.
- **Relevance to Research Taster:** Practical open-source resource for building autonomous research systems. Directly applicable to Research Taster's implementation.

### 9.3 The AI Scientist's First Peer-Reviewed Publication
**Sakana AI (2025).** The AI Scientist Generates its First Peer-Reviewed Scientific Publication. *Sakana AI Blog, April 2025*.
- **URL:** https://sakana.ai/ai-scientist-first-publication/
- **Key contribution:** Milestone announcement — first fully AI-generated paper accepted through standard peer review at an ICLR 2025 workshop. Conducted with full cooperation of ICLR leadership and workshop organizers.
- **Relevance to Research Taster:** Watershed moment for AI science — demonstrates that AI-generated research can pass human peer review. Raises important questions about transparency and ethical conduct.

---

## 10. Additional Key References

### 10.1 AlphaFold / AlphaFold2
**Jumper, J., Evans, R., Pritzel, A., et al. (2021).** Highly Accurate Protein Structure Prediction with AlphaFold. *Nature, 596*, 583–589.
- **DOI:** https://doi.org/10.1038/s41586-021-03819-2
- **Key contribution:** Solved the 50-year-old protein folding problem using deep learning. While not an "AI scientist" per se, AlphaFold represents the most impactful AI contribution to science to date.
- **Relevance to Research Taster:** The gold standard for AI impact on science. Shows what's possible when AI is applied to well-defined scientific problems with clear evaluation criteria.

### 10.2 GNoME (Graph Networks for Materials Exploration)
**Merchant, A., Batzner, S., Schoenholz, S.S., et al. (2023).** Scaling Deep Learning for Materials Discovery. *Nature, 624*, 80–85.
- **DOI:** https://doi.org/10.1038/s41586-023-06735-9
- **Key contribution:** Used GNNs to discover 2.2 million new stable crystal structures — 800 years' worth of conventional discovery. Demonstrates AI-driven materials discovery at massive scale.
- **Relevance to Research Taster:** Shows the potential of AI for large-scale automated discovery in materials science, a domain where Research Taster could have significant impact.

### 10.3 SWE-bench (Software Engineering Benchmark)
**Jimenez, C.E., Yang, J., Wettig, A., et al. (2024).** SWE-bench: Can Language Models Resolve Real-World GitHub Issues? *ICLR 2024*.
- **URL:** https://arxiv.org/abs/2310.06770
- **Key contribution:** Benchmark for evaluating LLM agents on real-world software engineering tasks. While not science-specific, it established the paradigm for evaluating agentic coding capabilities that AI scientists rely on.
- **Relevance to Research Taster:** SWE-bench's methodology (real-world tasks, automated evaluation) directly influenced ScienceAgentBench and MLR-Bench.

---

## Summary Statistics

- **Total papers reviewed:** 43
- **Categories:** End-to-end systems (6), Agent-based discovery (4), Self-driving labs (5), AI for meta-science (7), Benchmarks (2), Critiques (6), Surveys (5), Historical (5), Human-AI collaboration (3), Additional (3)
- **Key themes:**
  1. Rapid progression from tool-assisted to fully autonomous research
  2. Tension between autonomy and oversight/safety
  3. Gap between ML-domain demos and real-world scientific discovery
  4. Critical need for evaluation frameworks and benchmarks
  5. Historical continuity — 60+ years of computational scientific discovery
  6. The "process vs. product" question — does AI understand or merely generate?

## Key Gaps and Opportunities for Research Taster

1. **No system addresses the "tasting" metaphor** — sampling diverse research directions quickly to identify promising areas. Current systems go deep on narrow topics.
2. **Limited cross-domain capability** — most systems are domain-specific (ML, chemistry, materials). A genuine "research taster" would need to span domains.
3. **Human-AI interface underexplored** — most systems are either fully autonomous or minimally interactive. The middle ground of deep human-AI collaboration in research direction-setting is underdeveloped.
4. **Quality assessment remains unsolved** — even with benchmarks, we lack reliable ways to assess whether AI-generated research is genuinely novel vs. incremental.
5. **Historical lessons underutilized** — EURISKO's failure modes (shallow heuristics, lack of deep domain knowledge) are being repeated in current systems.
