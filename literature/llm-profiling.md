# Literature Review: LLM-Based Profiling and Preference Extraction

*Compiled 2026-02-26. Focus: Using language models to understand user preferences, taste, and style.*

---

## Surveys & Overviews

### 1. Tan & Jiang (2023). "User Modeling in the Era of Large Language Models: Current Research and Future Directions." arXiv:2312.11518.
- **Key contribution:** Comprehensive survey of LLM-based user modeling (LLM-UM), categorizing approaches for extracting user profiles, preferences, and behavioral patterns from user data using LLMs.
- **Relevance:** Foundational survey — maps the entire landscape of using LLMs to model users, directly applicable to Research Taster's goal of understanding researcher taste.

### 2. Zhang, Rossi, Kveton, Shao & Yang (2024). "Personalization of Large Language Models: A Survey." arXiv:2411.00027.
- **Key contribution:** Introduces a taxonomy of personalized LLM approaches, covering adaptation functions that integrate user-specific information. Categorizes datasets and methods (163 citations).
- **Relevance:** Core reference for how to personalize LLM outputs based on user profiles — directly informs Research Taster's architecture.

### 3. Liu, Qiu, Li, Dai, Yu, Zhu & Hu (2025). "A Survey of Personalized Large Language Models: Progress and Future Directions." arXiv:2502.11528.
- **Key contribution:** Surveys five categories of personalization data (historical content, dialogues, interactions, user profile, context) and methods including LoRA-based PEFT for injecting personalized information (62 citations).
- **Relevance:** Provides technical roadmap for personalization approaches Research Taster could adopt.

### 4. Chen, Liu, Huang, Wu, Liu, Jiang, Pu et al. (2024). "When Large Language Models Meet Personalization: Perspectives of Challenges and Opportunities." World Wide Web, Springer.
- **Key contribution:** Reviews LLM adaptation for recommendation and generative personalization, identifying key challenges (517 citations).
- **Relevance:** High-impact survey connecting LLM personalization to recommendation — the core loop of Research Taster.

### 5. Wang, Li, Wang, Xing, Niu & Kong (2024). "Towards Next-Generation LLM-Based Recommender Systems: A Survey and Beyond." arXiv:2410.19744.
- **Key contribution:** Surveys LLM-based recommender systems, highlighting how LLMs understand nuanced user preferences and enable context-sensitive recommendations (65 citations).
- **Relevance:** Maps how LLMs can power the recommendation engine behind Research Taster.

---

## Preference Extraction & User Profiling

### 6. Malik, Jagatap & Puranik (2024). "PEARL: Preference Extraction with Exemplar Augmentation and Retrieval with LLM Agents." EMNLP 2024 Industry Track.
- **Key contribution:** First published work on user preference extraction from multi-turn conversation logs using LLMs. The LLM identifies preferences from conversation history given a filter space.
- **Relevance:** Directly relevant — shows how to extract research preferences from natural interaction history, exactly what Research Taster needs.

### 7. Gao, Taymanov & Salinas (2024). "Aligning LLM Agents by Learning Latent Preference from User Edits." NeurIPS 2024.
- **Key contribution:** Learns latent user preferences from edits users make to LLM-generated output (e.g., writing assistants), extracting implicit preference signals (74 citations).
- **Relevance:** Demonstrates preference learning from implicit feedback — Research Taster could learn from how researchers modify or respond to recommendations.

### 8. Qiu, Zhao, Zhang, Bai & Wang (2025). "Measuring What Makes You Unique: Difference-Aware User Modeling for Enhancing LLM Personalization." ACL Findings 2025.
- **Key contribution:** Proposes inter-user comparison to extract distinguishing preferences — modeling what makes each user *different* rather than just their absolute preferences (30 citations).
- **Relevance:** Key insight for Research Taster: understanding what makes a researcher's taste *distinctive* compared to peers.

### 9. Bang & Song (2025). "LLM-Based User Profile Management for Recommender System." arXiv:2502.14541.
- **Key contribution:** Framework for building and maintaining evolving user profiles by systematically extracting preferences, modeling how they change over time (10 citations).
- **Relevance:** Addresses temporal evolution of taste — critical for Research Taster since research interests shift.

### 10. Bao, Wang, Lin, Zhu, Sun & Feng (2025). "Heterogeneous User Modeling for LLM-Based Recommendation." ACM 2025.
- **Key contribution:** Extracts user representations by compressing diverse user preferences into a single LLM for joint learning of user and item representations.
- **Relevance:** Technical approach to multi-faceted user modeling applicable to modeling researcher interests across topics.

### 11. Jiang, Hao, Cho, Li, Yuan & Chen (2025). "Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale." arXiv:2504.14225.
- **Key contribution:** Benchmark for evaluating LLMs' ability to dynamically build user profiles from conversations and generate personalized responses (56 citations).
- **Relevance:** Evaluation framework Research Taster could adopt to measure profiling quality.

---

## Personality & Persona Inference

### 12. Peters, Cerf & Matz (2024). "Large Language Models Can Infer Personality from Free-Form User Interactions." arXiv:2405.13052.
- **Key contribution:** Demonstrates that LLM chatbots can accurately infer Big Five personality traits from natural conversations (23 citations).
- **Relevance:** Shows LLMs can extract deep personal characteristics from interaction — supports the feasibility of inferring research "personality" from reading behavior.

### 13. Jiang, Zhang, Cao & Breazeal (2024). "PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits." NAACL Findings 2024.
- **Key contribution:** Creates LLM personas with distinct personality traits; demonstrates humans can infer these traits from generated text (299 citations).
- **Relevance:** Validates that personality/style is legible in LLM-generated text — bidirectional insight for profiling.

### 14. Maharjan, Jin, Zhu & Kenne (2025). "Psychometric Evaluation of Large Language Model Embeddings for Personality Trait Prediction." Journal of Medical Internet Research.
- **Key contribution:** Evaluates LLM embeddings vs. zero-shot inference (GPT-4o) for predicting personality traits from text (14 citations).
- **Relevance:** Compares embedding-based vs. prompt-based approaches to user profiling — technical choice Research Taster must make.

### 15. Bai, Huang, Sun & Chen (2025). "Scaling Law in LLM Simulated Personality: More Detailed and Realistic Persona Profile Is All You Need." arXiv:2510.11734.
- **Key contribution:** Shows that more detailed persona profiles lead to more realistic personality simulation in LLMs.
- **Relevance:** Implies Research Taster should build rich, detailed researcher profiles for better taste modeling.

### 16. Bhandari, Fay, Wise & Datta (2025). "Can LLM Agents Maintain a Persona in Discourse?" EMNLP 2025.
- **Key contribution:** Tests whether LLM agents can consistently maintain assigned personality personas across extended discourse (8 citations).
- **Relevance:** Relevant to maintaining consistent researcher taste profiles over time.

### 17. Lei, Wang, Lian, Hu, Lian & Xie (2026). "HumanLLM: Towards Personalized Understanding and Simulation of Human Nature." arXiv, January 2026.
- **Key contribution:** Uses LLMs to simulate human behavior with personalized understanding — implications for social science and customer insights.
- **Relevance:** Cutting-edge work on LLM-based human modeling; directly applicable to simulating researcher preferences.

---

## Personalized RLHF & Preference Learning

### 18. Poddar, Wan, Ivison & Gupta (2024). "Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning." NeurIPS 2024.
- **Key contribution:** Trains multiple LLM reward models that learn separable embedding spaces distinguishing users with divergent preferences (125 citations).
- **Relevance:** Technical approach to modeling diverse preferences — could distinguish between different research taste profiles.

### 19. Li, Zhou, Lipton & Leqi (2024). "Personalized Language Modeling from Personalized Human Feedback." arXiv:2402.05133.
- **Key contribution:** Develops personalized Direct Preference Optimization (P-DPO) incorporating user models, eliminating need for per-user training (100 citations).
- **Relevance:** Efficient personalization method — Research Taster could use similar approach to adapt to individual researchers.

### 20. Sun, Feng, Liu & You (2025). "PREMIUM: LLM Personalization with Individual-Level Preference Feedback." OpenReview.
- **Key contribution:** Uses individual-level preference ranking feedback to personalize LLM outputs.
- **Relevance:** Shows how to use sparse individual feedback for personalization — applicable to limited researcher interaction data.

### 21. Zollo, Siah, Ye & Li (2024). "PersonalLLM: Tailoring LLMs to Individual Preferences." arXiv:2409.20296.
- **Key contribution:** Explores pairwise preference feedback for personalizing LLM output to individual tastes (50 citations).
- **Relevance:** Direct approach to taste-based personalization using preference pairs.

### 22. Nam, Wan, Liu, Lian & Ahnn (2025). "Learning to Summarize User Information for Personalized Reinforcement Learning from Human Feedback." arXiv:2507.13579.
- **Key contribution:** PLUS framework combines LLM-based user information summarization with personalized RLHF for zero-shot personalization.
- **Relevance:** Shows how to distill user information into actionable summaries — directly applicable to researcher taste profiles.

### 23. Iyer, Gheini, Federmann, Tan & Birch (2025). "Personalized Reward Modelling from Implicit User Preferences." OpenReview.
- **Key contribution:** Addresses personalized LLM evaluation conditioned on implicit user preferences, learning from user edits.
- **Relevance:** Implicit preference extraction is key for Research Taster — researchers rarely state preferences explicitly.

---

## Writing Style & Authorship Analysis

### 24. Weerasinghe, Seepersaud, Smothers & Jose (2025). "Be Sure to Use the Same Writing Style: Applying Authorship Verification on LLM-Generated Texts." Applied Sciences 15(5).
- **Key contribution:** Applies stylometry and authorship profiling techniques to distinguish human from LLM-generated text based on writing style analysis.
- **Relevance:** Stylometric methods could help Research Taster analyze researcher writing style as a taste signal.

### 25. Dubey (2024). "Capturing Style Through Large Language Models — An Authorship Perspective." Purdue University Thesis.
- **Key contribution:** Investigates using LLMs to extract defining stylistic features of authors, creating nuanced author profiles irrespective of content.
- **Relevance:** Directly applicable — extracting a researcher's stylistic signature could inform preference modeling.

### 26. Bevendorff, Casals, Chulvi et al. (2024). "Overview of PAN 2024: Multi-Author Writing Style Analysis, Multilingual Text Detoxification, and Generative AI Authorship Verification." ECIR 2024, Springer.
- **Key contribution:** Shared task on writing style analysis including authorship profiling and LLM-generated text attribution (49 citations).
- **Relevance:** Establishes benchmarks for style analysis that Research Taster could build upon.

### 27. Mikros (2025). "Beyond the Surface: Stylometric Analysis of GPT-4o's Capacity for Literary Style Imitation." Digital Scholarship in the Humanities.
- **Key contribution:** Analyzes GPT-4o's ability to imitate specific writing styles using stylometric methods (12 citations).
- **Relevance:** Shows LLMs can capture and reproduce style — suggests they can also *detect* and *characterize* research writing styles.

---

## LLM-Based Research Quality Assessment & Scientific Review

### 28. Schmidgall, Su, Wang, Sun & Wu (2025). "Agent Laboratory: Using LLM Agents as Research Assistants." EMNLP Findings 2025.
- **Key contribution:** Framework for LLM agents to conduct research autonomously, evaluated on experimental and report quality (246 citations).
- **Relevance:** Shows LLMs as research assistants — Research Taster could incorporate similar quality assessment capabilities.

### 29. Wu, Zhang & Zhao (2025). "Automated Novelty Evaluation of Academic Paper: A Collaborative Approach Integrating Human and Large Language Model Knowledge." JASIST.
- **Key contribution:** Leverages both human knowledge and LLMs to assess novelty in academic papers from peer-review reports (7 citations).
- **Relevance:** Novelty assessment is a key component of research taste — researchers value novelty differently.

### 30. Afzal, Nakov, Hope & Gurevych (2025). "Beyond 'Not Novel Enough': Enriching Scholarly Critique with LLM-Assisted Feedback." arXiv:2508.10795.
- **Key contribution:** End-to-end LLM novelty assessment pipeline for peer review, modeling expert reviewer reasoning.
- **Relevance:** Could be integrated into Research Taster to assess paper quality aligned with researcher preferences.

### 31. Zhang, Tan, Huang et al. (2026). "OpenNovelty: An LLM-Powered Agentic System for Verifiable Scholarly Novelty Assessment." arXiv:2601.01576.
- **Key contribution:** Agentic LLM system for verifiable novelty assessment of scholarly work using retrieval-augmented evaluation.
- **Relevance:** Automated novelty scoring is a key building block for personalized paper recommendation.

### 32. Lin, Peng & Fang (2025). "Evaluating and Enhancing Large Language Models for Novelty Assessment in Scholarly Publications." AISD Workshop 2025.
- **Key contribution:** Mirrors human peer review by grounding novelty assessment in literature, showing LLMs can assess novelty using paper content (22 citations).
- **Relevance:** Validates LLM-based quality signals Research Taster could use.

### 33. Shahid, Radensky & Fok (2025). "Literature-Grounded Novelty Assessment of Scientific Ideas." SDP Workshop 2025.
- **Key contribution:** Retrieval-augmented LLM approach (Idea Novelty Checker) for grounded novelty evaluation of scientific ideas (5 citations).
- **Relevance:** RAG-based novelty checking applicable to Research Taster's paper assessment pipeline.

### 34. Thakkar, Yuksekgonul, Silberg & Garg (2025). "Can LLM Feedback Enhance Review Quality? A Randomized Study of 20k Reviews at ICLR 2025." arXiv:2504.09737.
- **Key contribution:** Large-scale randomized experiment showing LLM-generated feedback enhances peer review quality (42 citations).
- **Relevance:** Validates LLMs as quality assessors in academic contexts.

### 35. Wang, Duong-Trung & Bhoyar (2025). "LLM-Based Literature Recommender System in Higher Education." CEUR-WS Vol. 3994.
- **Key contribution:** LLM-based literature recommendation for supervising student term papers, combining traditional recommendation with LLM approaches.
- **Relevance:** Closest existing system to Research Taster — LLM-powered paper recommendation in academic context.

---

## Conversational Recommendation & Personalized Agents

### 36. Zhang (2023). "User-Centric Conversational Recommendation: Adapting the Need of User with Large Language Models." RecSys 2023.
- **Key contribution:** Conditions recommendations on user profile and conversation history using LLMs (48 citations).
- **Relevance:** Conversational preference elicitation — Research Taster could use dialogue to refine taste models.

### 37. Otsuka, Matsuo, Ishii & Nomoto (2024). "User-Specific Dialogue Generation with User Profile-Aware Pre-Training Model and Parameter-Efficient Fine-Tuning." arXiv:2409.00887.
- **Key contribution:** Pre-trains LLMs with user profile awareness for personalized dialogue generation (7 citations).
- **Relevance:** Profile-aware generation could help Research Taster explain *why* a paper matches a researcher's taste.

### 38. Liang, Zhang & Guo (2025). "PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM." arXiv, November 2025.
- **Key contribution:** Combines persona-based LLM agents with graph-based knowledge retrieval for personalized AI that adapts to individual users.
- **Relevance:** Graph-based persona modeling could capture complex research interest networks.

---

## Summary of Key Themes

| Theme | Papers | Key Insight for Research Taster |
|-------|--------|-------------------------------|
| LLM User Modeling Surveys | #1, #2, #3, #4, #5 | Rich existing framework; LLMs are effective at user modeling |
| Preference Extraction | #6, #7, #8, #9, #10, #11 | Preferences extractable from conversations, edits, interactions |
| Personality/Persona Inference | #12–#17 | LLMs can infer deep traits from natural interaction |
| Personalized RLHF | #18–#23 | Individual preferences learnable from sparse feedback |
| Writing Style Analysis | #24–#27 | Stylometric signals complement content-based profiling |
| Research Quality Assessment | #28–#35 | LLMs can assess novelty, quality — key taste dimensions |
| Conversational Recommendation | #36–#38 | Dialogue-based preference elicitation is effective |
