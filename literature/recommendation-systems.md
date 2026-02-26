# Literature Review: Academic Paper Recommendation Systems

*Compiled 2026-02-26. Focus: content-based, style-based, and beyond-keyword approaches to paper recommendation.*

---

## Surveys & Overviews

### 1. Pinedo, I., Larrañaga, M., & Arruarte, A. (2025). "Recent Advances and Trends in Research Paper Recommender Systems: A Comprehensive Survey." arXiv:2508.XXXXX.
- **Key contribution:** Comprehensive survey covering the exponential growth of scientific publications and the full landscape of research paper recommender systems (RPRS), including content-based, collaborative filtering, graph-based, and hybrid approaches.
- **Relevance:** Directly maps the field Research Taster operates in; essential baseline for positioning.

### 2. Beel, J., Gipp, B., Langer, S., & Breitinger, C. (2016). "Research-paper recommender systems: a literature survey." *International Journal on Digital Libraries*, 17(4), 305–338.
- **Key contribution:** The most-cited survey of paper recommender systems, covering content-based filtering, collaborative filtering, co-citation analysis, and hybrid methods. Identified key challenges: cold-start, data sparsity, evaluation difficulties.
- **Relevance:** Foundational reference; identifies the exact gaps (beyond-keyword, taste-based) that Research Taster aims to fill.

### 3. Bai, X., Wang, M., Lee, I., Yang, Z., Kong, X., & Xia, F. (2019). "Scientific paper recommendation: A survey." *IEEE Access*, 7, 9324–9339.
- **Key contribution:** Survey categorizing approaches into content-based, collaborative filtering, graph-based, and hybrid. Highlights the shift toward deep learning methods.
- **Relevance:** Provides taxonomy for classifying Research Taster's approach within existing work.

### 4. Raja, R., Vats, A., Vats, A., & Majumder, A. (2025). "A Comprehensive Review on Harnessing Large Language Models to Overcome Recommender System Challenges." arXiv, 2025.
- **Key contribution:** Reviews how LLMs can address cold-start, data sparsity, and cross-domain challenges in recommendation systems.
- **Relevance:** Directly relevant to Research Taster's LLM-based approach to paper understanding and matching.

---

## Content-Based & Semantic Approaches

### 5. Xi, H., Zhang, H., & Zhang, C. (2026). "Enhancing Academic Paper Recommendations Using Fine-Grained Knowledge Entities and Multifaceted Document Embeddings." arXiv:2501.XXXXX.
- **Key contribution:** Goes beyond keyword matching by extracting fine-grained knowledge entities and creating multifaceted document embeddings that capture different aspects of a paper's content.
- **Relevance:** Core technique for Research Taster — represents the shift from keyword to semantic understanding of papers.

### 6. Cohan, A., Feldman, S., Beltagy, I., Downey, D., & Weld, D. S. (2020). "SPECTER: Document-level Representation Learning using Citation-Informed Transformers." *ACL 2020*.
- **Key contribution:** Pre-trained transformer model that creates document embeddings using citation signals as training signal. Outperforms TF-IDF and other baselines on recommendation tasks.
- **Relevance:** Foundational embedding model for paper similarity; could serve as Research Taster's backbone representation.

### 7. Mysore, S., Cohan, A., & Hope, T. (2023). "SPECTER2: Adapting Scientific Document Embeddings for Multiple Tasks." *arXiv:2211.13308*.
- **Key contribution:** Multi-task extension of SPECTER with task-specific adapters for different downstream tasks including recommendation and search.
- **Relevance:** State-of-the-art document embeddings for academic papers; direct building block for Research Taster.

### 8. Liu, X., Yin, D., Zheng, J., Zhang, X., Zhang, P., Yang, H., Dong, Y., & Tang, J. (2021). "OAG-BERT: Towards A Unified Backbone Language Model For Academic Knowledge Services." arXiv:2103.02869 (corrected: KDD 2022).
- **Key contribution:** Pre-trained language model on the Open Academic Graph integrating paper text, author info, venue, and citation context for academic knowledge services.
- **Relevance:** Demonstrates how heterogeneous academic metadata can be unified in a single model — key architecture insight for Research Taster.

### 9. Ostendorff, M., Rethmeier, N., Augenstein, I., Gipp, B., & Rehm, G. (2022). "Neighborhood Contrastive Learning for Scientific Document Representations with Citation Embeddings." *EMNLP 2022*.
- **Key contribution:** Uses citation neighborhoods as contrastive learning signal to create paper embeddings that capture topical and methodological similarity beyond surface-level text matching.
- **Relevance:** Captures "style" and methodology similarity — exactly the beyond-keyword signal Research Taster needs.

### 10. Bhagavatula, C., Feldman, S., Power, R., & Ammar, W. (2018). "Content-Based Citation Recommendation." *NAACL 2018*.
- **Key contribution:** Neural model for citation recommendation based on the textual content of the citing paper, moving beyond metadata-only approaches.
- **Relevance:** Demonstrates pure content-based recommendation can work; validates Research Taster's content-first philosophy.

---

## Citation-Based & Graph Approaches

### 11. Jeong, C., Jang, S., Shin, H., Park, E., & Choi, S. (2019). "A Context-Aware Citation Recommendation Model with BERT and Graph Convolutional Networks." arXiv:1903.06464.
- **Key contribution:** Combines BERT for text understanding with GCN for citation graph structure, achieving state-of-the-art context-aware citation recommendation. Introduces FullTextPeerRead dataset.
- **Relevance:** Shows how to combine textual understanding with citation structure — a key hybrid approach for Research Taster.

### 12. Jiang, Z., Yin, Y., Gao, L., Lu, Y., & Liu, X. (2018). "Cross-language Citation Recommendation via Hierarchical Representation Learning on Heterogeneous Graph." arXiv:1812.XXXXX.
- **Key contribution:** Addresses cross-language paper recommendation using hierarchical representation learning on heterogeneous citation graphs, enabling discovery across language barriers.
- **Relevance:** Expands Research Taster's potential scope to multilingual research discovery.

### 13. Wang, B., Weng, Z., & Wang, Y. (2021). "A Novel Paper Recommendation Method Empowered by Knowledge Graph: for Research Beginners." arXiv:2103.XXXXX.
- **Key contribution:** Leverages knowledge graphs to recommend papers specifically for research beginners, addressing the cold-start problem for new researchers entering a field.
- **Relevance:** Directly relevant to Research Taster's goal of helping researchers explore new areas they're unfamiliar with.

### 14. West, J. D., Wesley-Smith, I., & Bergstrom, C. T. (2016). "A Recommendation System Based on Hierarchical Clustering of an Article-Level Citation Network." *IEEE Transactions on Big Data*, 2(2), 113–123.
- **Key contribution:** Uses hierarchical clustering of citation networks to identify related papers, creating a recommendation system that captures field structure.
- **Relevance:** Citation-network approach to discovering related work that may use different terminology.

### 15. Cai, X., Han, J., & Yang, L. (2018). "Generative Adversarial Network Based Heterogeneous Bibliographic Network Representation for Personalized Citation Recommendation." *AAAI 2018*.
- **Key contribution:** GAN-based approach to learning representations in heterogeneous bibliographic networks (papers, authors, venues) for citation recommendation.
- **Relevance:** Demonstrates how heterogeneous network information enables more personalized recommendations.

---

## Serendipity, Diversity & Exploration

### 16. Kotkov, D., Wang, S., & Veijalainen, J. (2016). "A survey of serendipity in recommender systems." *Knowledge-Based Systems*, 111, 180–192.
- **Key contribution:** Comprehensive survey on serendipity in recommendation — the ability to surface unexpected but relevant items. Defines metrics and approaches for measuring serendipity.
- **Relevance:** Serendipitous discovery is a core goal of Research Taster; this paper defines the evaluation framework.

### 17. Kaminskas, M., & Bridge, D. (2016). "Diversity, serendipity, novelty, and coverage: a survey and empirical analysis of beyond-accuracy objectives in recommender systems." *ACM TIST*, 7(1), 1–42.
- **Key contribution:** Comprehensive analysis of beyond-accuracy metrics in recommender systems including diversity, novelty, serendipity, and coverage.
- **Relevance:** Provides the evaluation framework Research Taster needs — recommendations should optimize for more than just relevance.

### 18. Wang, J., Liu, Y., Sun, Y., Ma, X., Wang, Y., Ma, H., Su, Z., Chen, M., Gao, M., Dalal, O., Chi, E.H., Hong, L., Han, N., & Lu, H. (2025). "User Feedback Alignment for LLM-powered Exploration in Large-scale Recommendation Systems." arXiv, 2025.
- **Key contribution:** Uses LLMs to explore beyond established user preferences in large-scale recommendation, with user feedback alignment to maintain quality.
- **Relevance:** Directly models the exploration vs exploitation tradeoff that Research Taster must navigate.

### 19. "Beyond Relevance: An Adaptive Exploration-Based Framework for Personalized Recommendations." arXiv, 2025.
- **Key contribution:** Framework that adaptively balances personalization with exploration, ensuring recommendations go beyond what's merely relevant.
- **Relevance:** Core architectural pattern for Research Taster's recommendation engine.

### 20. Ziegler, C. N., McNee, S. M., Konstan, J. A., & Lausen, G. (2005). "Improving Recommendation Lists Through Topic Diversification." *WWW 2005*.
- **Key contribution:** Introduced topic diversification as an explicit optimization objective in recommendation lists, showing users prefer diverse recommendations.
- **Relevance:** Research Taster should actively diversify recommendations to encourage cross-disciplinary discovery.

---

## Personalized & Social Approaches

### 21. Greenwood, S. & Garg, N. (2026). "Paper Skygest: Personalized Academic Recommendations on Bluesky." arXiv:2501.XXXXX.
- **Key contribution:** Deployed system providing personalized scientific paper recommendations via social feeds on Bluesky/AT Protocol. Leverages decentralized social media for custom scholarly feeds.
- **Relevance:** Closest existing system to Research Taster's vision — personalized paper discovery through social/community signals. Key comparison point.

### 22. Ju, L., Zhao, J., Chai, M., et al. (2025). "WisPaper: Your AI Scholar Search Engine." arXiv, 2025.
- **Key contribution:** AI-powered academic search engine that goes beyond keyword matching to understand research intent and provide semantically relevant results.
- **Relevance:** Demonstrates the shift from search to discovery in academic tools; validates Research Taster's approach.

### 23. Lee, F. & Ma, T. (2025). "The Budget AI Researcher and the Power of RAG Chains." arXiv:2506.12317.
- **Key contribution:** Uses RAG chains with LLMs to help aspiring researchers navigate scientific literature, generating research ideas from personalized literature discovery.
- **Relevance:** Shows how LLM+RAG can democratize research exploration — aligns with Research Taster's mission.

### 24. Sugiyama, K. & Kan, M.-Y. (2010). "Scholarly Paper Recommendation via User's Recent Research Interests." *JCDL 2010*.
- **Key contribution:** Models user's research interests based on their recent publications and uses this profile to recommend papers, showing that recent interests outperform historical profiles.
- **Relevance:** Temporal dynamics of research taste — Research Taster should weight recent reading/interests more heavily.

### 25. Nascimento, C., Laender, A. H. F., da Silva, A. S., & Gonçalves, M. A. (2011). "A source independent framework for research paper recommendation." *JCDL 2011*.
- **Key contribution:** Framework for paper recommendation that works across different digital libraries by abstracting source-specific features.
- **Relevance:** Research Taster should be source-agnostic, pulling from arXiv, Semantic Scholar, etc.

---

## Embedding & Representation Learning

### 26. Ammar, W., Groeneveld, D., Bhagavatula, C., Beltagy, I., Crawford, M., Downey, D., Dunber, J., Elgohary, A., Feldman, S., Ha, V., Kinney, R., Kohlmeier, S., Lo, K., Murray, T., Ooi, H., Peters, M., Power, J., Skjonsberg, S., Wang, L., ... Etzioni, O. (2018). "Construction of the Literature Graph in Semantic Scholar." *NAACL 2018*.
- **Key contribution:** Describes the construction of Semantic Scholar's literature graph — papers, authors, citations, topics, and entities — enabling graph-based paper discovery.
- **Relevance:** The infrastructure layer that Research Taster could build upon; Semantic Scholar API as a key data source.

### 27. Beltagy, I., Lo, K., & Cohan, A. (2019). "SciBERT: A Pretrained Language Model for Scientific Text." *EMNLP 2019*.
- **Key contribution:** Domain-specific BERT model pre-trained on scientific text (Semantic Scholar corpus), achieving state-of-the-art on scientific NLP tasks.
- **Relevance:** Foundation model for understanding scientific text; key component for Research Taster's paper analysis pipeline.

### 28. Singh, A., D'Arcy, M., Cohan, A., Downey, D., & Feldman, S. (2023). "SciRepEval: A Multi-Format Benchmark for Scientific Document Representations." *ACL 2023*.
- **Key contribution:** Benchmark for evaluating scientific document representations across multiple tasks (classification, recommendation, search), enabling fair comparison of embedding approaches.
- **Relevance:** Evaluation benchmark for Research Taster's paper representation quality.

### 29. Wahle, J. P., Ruas, T., Gipp, B., & Meuschke, N. (2022). "D3: A Massive Dataset of Scholarly Metadata for Analyzing the State of Computer Science Research." *LREC 2022*.
- **Key contribution:** Large-scale dataset of scholarly metadata enabling analysis of research trends, topics, and collaboration patterns.
- **Relevance:** Training data source for Research Taster's understanding of research landscape dynamics.

---

## Cold-Start & New Researcher Support

### 30. Zhang, W., Bei, Y., Yang, L., et al. (2025). "Cold-Start Recommendation towards the Era of Large Language Models (LLMs): A Comprehensive Survey and Roadmap." arXiv:2501.01945.
- **Key contribution:** Comprehensive survey on cold-start recommendation in the LLM era, covering how LLMs can leverage world knowledge to bootstrap recommendations for new users/items.
- **Relevance:** Core challenge for Research Taster — recommending papers to researchers entering entirely new fields where they have no history.

### 31. Porcel, C., Tejeda-Lorente, Á., Martínez, M. A., & Herrera-Viedma, E. (2012). "A hybrid recommender system for the selective dissemination of research resources in a technology transfer office." *Information Sciences*, 184(1), 1–19.
- **Key contribution:** Hybrid recommender combining content-based and collaborative approaches for selective dissemination of research resources, addressing information overload in academic settings.
- **Relevance:** Technology transfer context shows recommendation beyond pure academia — Research Taster could bridge research communities.

---

## Tools & Systems

### 32. Färber, M. & Jatowt, A. (2020). "Citation Recommendation: Approaches and Datasets." *International Journal on Digital Libraries*, 21, 375–405.
- **Key contribution:** Comprehensive overview of citation recommendation approaches and available datasets, providing practical guidance for building recommendation systems.
- **Relevance:** Practical reference for Research Taster's implementation — which datasets and evaluation methods to use.

### 33. McNee, S. M., Albert, I., Cosley, D., Gopalkrishnan, P., Lam, S. K., Rashid, A. M., Konstan, J. A., & Riedl, J. (2002). "On the recommending of citations for research papers." *CSCW 2002*.
- **Key contribution:** One of the earliest systems for automatic citation recommendation using collaborative filtering on citation data. Introduced the idea that "papers that cite the same papers are related."
- **Relevance:** Foundational work establishing that citation patterns encode research taste and relevance.

### 34. Ekstrand, M. D., Riedl, J. T., & Konstan, J. A. (2011). "Collaborative filtering recommender systems." *Foundations and Trends in Human-Computer Interaction*, 4(2), 81–173.
- **Key contribution:** Comprehensive textbook-style treatment of collaborative filtering, covering user-based, item-based, and matrix factorization approaches.
- **Relevance:** Theoretical foundation for the collaborative component of Research Taster — "researchers who read X also read Y."

### 35. Semantic Scholar Research Team (2015–present). "Semantic Scholar: AI-Powered Research Tool." semanticscholar.org.
- **Key contribution:** Large-scale academic search and recommendation platform using AI to analyze papers, extract key information, and surface relevant research through the Semantic Scholar Recommendation API.
- **Relevance:** Primary comparison system and potential data source for Research Taster. Their "Research Feeds" feature is the closest mainstream equivalent.

---

## Style & Methodology Matching

### 36. Hope, T., Portenoy, J., Vasan, K., Bras, R. L., Chan, S., Feldman, S., & Weld, D. (2023). "A Computational Inflection for Scientific Discovery." *Communications of the ACM*.
- **Key contribution:** Argues for AI-driven tools that go beyond search to actively support scientific discovery through computational analysis of research literature — understanding methods, findings, and connections.
- **Relevance:** Philosophical foundation for Research Taster — the goal is discovery, not just retrieval.

### 37. Lops, P., de Gemmis, M., & Semeraro, G. (2011). "Content-based recommender systems: State of the art and trends." In *Recommender Systems Handbook*, Springer.
- **Key contribution:** Comprehensive treatment of content-based recommendation, including representation learning, user modeling, and evaluation beyond keyword matching.
- **Relevance:** Foundational reference for Research Taster's content-based approach.

### 38. Kang, W.-C., Wan, M., & McAuley, J. (2018). "Recommendation Through Mixtures of Heterogeneous Item Relationships." arXiv:1808.XXXXX.
- **Key contribution:** Models multiple types of item relationships simultaneously (visual, textual, behavioral) for recommendations, showing that heterogeneous signals improve over any single signal.
- **Relevance:** Research Taster should combine multiple signals: content, methodology, writing style, citation patterns, author networks.

---

## Emerging Directions

### 39. Fu, J., Ge, X., Karatzoglou, A., Arapakis, I., Verberne, S., Jose, J. M., & Ren, Z. (2026). "Differentiable Semantic ID for Generative Recommendation." arXiv, 2026.
- **Key contribution:** Represents items as learnable discrete semantic IDs for generative recommendation, bridging the gap between retrieval and generation paradigms.
- **Relevance:** Future direction for Research Taster — generative recommendation could synthesize "the paper you need" from literature understanding.

### 40. Lu, M., Wu, M., Xu, J., Li, W., Liu, F., Ding, Y., Sun, Y., Lu, J., & Zhang, Y. (2025). "From Newborn to Impact: Bias-Aware Citation Prediction." arXiv, 2025.
- **Key contribution:** Addresses bias in citation prediction, ensuring new papers aren't disadvantaged by lack of citation history.
- **Relevance:** Research Taster should avoid citation-count bias and surface quality new work alongside established papers.

---

## Summary & Gaps

**Key themes in the literature:**
1. **Shift from keywords to semantics:** SPECTER, SciBERT, OAG-BERT show embeddings beat keywords
2. **Hybrid approaches dominate:** Best systems combine content + citations + metadata
3. **Cold-start remains hard:** LLMs offer new hope (Zhang et al. 2025)
4. **Serendipity is valued but under-served:** Most systems optimize for relevance, not discovery
5. **Social signals emerging:** Paper Skygest shows community-driven recommendation works

**Gaps Research Taster can fill:**
- **Taste-based recommendation:** No system explicitly models "research taste" (methodology preferences, writing style affinity, intellectual aesthetics)
- **Cross-field exploration:** Most systems keep researchers in their bubble; Research Taster should actively bridge fields
- **Reading experience quality:** No system considers how enjoyable/accessible a paper is to read, only topical relevance
- **Adaptive difficulty:** No system adjusts recommendation complexity based on reader's expertise in a new field
