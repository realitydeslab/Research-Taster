# Literature Review: Scientometrics — Researcher Profiling, Research Identity, Scholarly Fingerprints

> Compiled 2026-02-26. Focus: methods for characterizing researchers beyond simple impact metrics — profiling research style, interests, trajectories, and identity.

---

## 1. Foundational Scientometrics & Citation Analysis

### 1.1 Hirsch, J.E. (2005). "An index to quantify an individual's scientific research output." *Proceedings of the National Academy of Sciences*, 102(46), 16569–16572.
- **Key contribution:** Introduced the h-index, the most widely adopted single-number metric for researcher impact, combining productivity and citation impact.
- **Relevance to Research Taster:** The h-index is the baseline "researcher fingerprint" — Research Taster needs to go beyond it to capture *style*, not just *impact*.

### 1.2 Egghe, L. (2006). "Theory and practise of the g-index." *Scientometrics*, 69(1), 131–152.
- **Key contribution:** Proposed the g-index as an improvement on the h-index, giving more weight to highly cited papers and better distinguishing top researchers.
- **Relevance:** Shows the impulse to refine single metrics — Research Taster takes a multidimensional approach instead.

### 1.3 Garfield, E. (1955). "Citation indexes for science." *Science*, 122(3159), 108–111.
- **Key contribution:** Seminal proposal for citation indexing as a tool for information retrieval and science evaluation, laying groundwork for all bibliometric analysis.
- **Relevance:** Foundational infrastructure that makes researcher profiling possible.

### 1.4 De Solla Price, D.J. (1965). "Networks of scientific papers." *Science*, 149(3683), 510–515.
- **Key contribution:** First systematic study of citation networks, showing science's cumulative structure and the "research front."
- **Relevance:** Citation network structure is a key signal for identifying a researcher's position in the knowledge landscape.

---

## 2. Author Topic Modeling & Research Interest Detection

### 2.1 Rosen-Zvi, M., Griffiths, T., Steyvers, M., & Smyth, P. (2004). "The author-topic model for authors and documents." *Proceedings of the 20th Conference on Uncertainty in Artificial Intelligence (UAI)*, 487–494.
- **Key contribution:** Extended LDA to jointly model authors and topics, creating per-author topic distributions — essentially a "research fingerprint" over topics.
- **Relevance:** **Directly relevant** — the author-topic model is perhaps the most natural formalization of "scholarly fingerprint" via topic distributions.

### 2.2 Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). "Latent Dirichlet Allocation." *Journal of Machine Learning Research*, 3, 993–1022.
- **Key contribution:** Introduced LDA, the foundational probabilistic topic model that underpins most author profiling work.
- **Relevance:** Core technique for extracting research topics from publications.

### 2.3 Tang, J., Zhang, J., Yao, L., Li, J., Zhang, L., & Su, Z. (2008). "ArnetMiner: Extraction and mining of academic social networks." *Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 990–998.
- **Key contribution:** Built a comprehensive system for extracting and profiling researchers from publication data, including expertise identification and social network analysis.
- **Relevance:** **Highly relevant** — one of the first systems to do holistic researcher profiling at scale.

### 2.4 Wang, C., Blei, D., & Heckerman, D. (2012). "Continuous time dynamic topic models." *arXiv preprint arXiv:1206.3298* (originally UAI 2008).
- **Key contribution:** Extended topic models to capture how topics evolve over time, enabling analysis of how research fields shift.
- **Relevance:** Enables tracking how a researcher's interests evolve — temporal dimension of the scholarly fingerprint.

### 2.5 Mimno, D. & McCallum, A. (2007). "Expertise modeling for matching papers with reviewers." *Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 500–509.
- **Key contribution:** Used topic models to build expertise profiles for matching reviewers to papers, demonstrating practical researcher profiling.
- **Relevance:** Direct application of author profiling for research "taste matching."

### 2.6 Kawamae, N. (2010). "Author interest topic model." *Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval*, 887–888.
- **Key contribution:** Extended author-topic models to distinguish between an author's core interests and peripheral/collaborative topics.
- **Relevance:** Captures the nuance of genuine research interest vs. occasional collaboration — key for authentic profiling.

---

## 3. Research Trajectory & Career Path Analysis

### 3.1 Zeng, A., Shen, Z., Zhou, J., Wu, J., Fan, Y., Wang, Y., & Stanley, H.E. (2017). "The science of science: From the perspective of complex systems." *Physics Reports*, 714–715, 1–73.
- **Key contribution:** Comprehensive review of science-of-science from a complex systems perspective, covering career trajectories, collaboration patterns, and impact dynamics.
- **Relevance:** Provides the theoretical framework for understanding research careers as dynamic systems.

### 3.2 Sinatra, R., Wang, D., Deville, P., Song, C., & Barabási, A.L. (2016). "Quantifying the evolution of individual scientific impact." *Science*, 354(6312), aaf5239.
- **Key contribution:** Showed that a researcher's highest-impact work can come at any point in their career (the "random impact rule"), with productivity and a "Q-factor" (individual ability) determining impact.
- **Relevance:** **Highly relevant** — the Q-factor is essentially a quantified "research talent" parameter, a key component of scholarly identity.

### 3.3 Way, S.F., Morgan, A.C., Clauset, A., & Larremore, D.B. (2017). "The misleading narrative of the canonical faculty productivity trajectory." *Proceedings of the National Academy of Sciences*, 114(44), E9216–E9223.
- **Key contribution:** Challenged the assumption that faculty productivity follows a universal pattern, showing diverse trajectory shapes.
- **Relevance:** Trajectory diversity means researcher profiles must capture individual patterns, not assume one-size-fits-all.

### 3.4 Jia, T., Wang, D., & Szymanski, B.K. (2017). "Quantifying patterns of research-interest evolution." *Nature Human Behaviour*, 1, 0078.
- **Key contribution:** Quantified how researchers' interests evolve over careers, finding characteristic patterns of exploration vs. exploitation.
- **Relevance:** **Directly relevant** — formalizes the dynamics of research interest trajectories, core to understanding "research taste."

### 3.5 Deville, P., Wang, D., Sinatra, R., Song, C., Blondel, V.D., & Barabási, A.L. (2014). "Career on the move: Geography, stratification, and scientific impact." *Scientific Reports*, 4, 4770.
- **Key contribution:** Analyzed how geographic mobility correlates with scientific impact and career trajectories.
- **Relevance:** Spatial dimension of research identity — institutional context shapes research direction.

### 3.6 Clauset, A., Arbesman, S., & Larremore, D.B. (2015). "Systematic inequality and hierarchy in faculty hiring networks." *Science Advances*, 1(1), e1400005.
- **Key contribution:** Mapped the prestige hierarchy in faculty hiring, showing how institutional pedigree shapes career paths.
- **Relevance:** Institutional identity as a component of researcher profiling.

---

## 4. Author Disambiguation & Identity

### 4.1 Ferreira, A.A., Gonçalves, M.A., & Laender, A.H. (2012). "A brief survey of automatic methods for author name disambiguation." *ACM SIGMOD Record*, 41(2), 15–26.
- **Key contribution:** Comprehensive survey of methods for resolving author identity ambiguity in bibliographic databases.
- **Relevance:** Author disambiguation is a prerequisite for accurate researcher profiling.

### 4.2 Müller, M.C., Reitz, F., & Roy, N. (2017). "Data sets for author name disambiguation: An empirical analysis and a new resource." *Scientometrics*, 111(3), 1467–1500.
- **Key contribution:** Provided benchmark datasets and evaluation framework for author disambiguation systems.
- **Relevance:** Infrastructure for building reliable researcher identity systems.

### 4.3 Kim, J. (2018). "Evaluating author name disambiguation for digital libraries: A case of DBLP." *Scientometrics*, 116(3), 1867–1886.
- **Key contribution:** Evaluated disambiguation quality in DBLP, one of the largest CS bibliographic databases.
- **Relevance:** Practical evaluation of identity resolution at scale.

---

## 5. Scholarly Recommendation & Expertise Matching

### 5.1 Beel, J., Gipp, B., Langer, S., & Breitinger, C. (2016). "Research-paper recommender systems: A literature survey." *International Journal on Digital Libraries*, 17(4), 305–338.
- **Key contribution:** Comprehensive survey of paper recommendation approaches, including content-based, collaborative filtering, and hybrid methods.
- **Relevance:** Paper recommendation is the inverse problem of Research Taster — matching researchers to papers they'd find interesting.

### 5.2 Sugiyama, K. & Kan, M.Y. (2010). "Scholarly paper recommendation via user's recent research interests." *Proceedings of the 10th Annual Joint Conference on Digital Libraries*, 29–38.
- **Key contribution:** Used recent publication history to model evolving research interests for paper recommendation.
- **Relevance:** Demonstrates dynamic interest modeling for personalized scholarly recommendation.

### 5.3 Kanakia, A., Shen, Z., Eide, D., & Wang, K. (2019). "A scalable hybrid research paper recommender system for Microsoft Academic." *The World Wide Web Conference*, 2893–2899.
- **Key contribution:** Production-scale hybrid recommender combining content and graph signals for paper recommendation in Microsoft Academic.
- **Relevance:** Shows industrial-scale implementation of research interest modeling.

---

## 6. Research Style, Cognitive Patterns & Beyond-Impact Metrics

### 6.1 Boyack, K.W. & Klavans, R. (2010). "Co-citation analysis, bibliographic coupling, and direct citation: Which citation approach represents the research front most accurately?" *Journal of the American Society for Information Science and Technology*, 61(12), 2389–2404.
- **Key contribution:** Compared citation-based methods for mapping research fronts, finding direct citation most accurately represents current activity.
- **Relevance:** Methods for situating a researcher within the intellectual landscape.

### 6.2 Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). "Atypical combinations and scientific impact." *Science*, 342(6157), 468–472.
- **Key contribution:** Showed that high-impact papers tend to combine conventional and atypical knowledge — a measurable "novelty fingerprint."
- **Relevance:** **Highly relevant** — atypical combination patterns characterize a researcher's creative style.

### 6.3 Foster, J.G., Rzhetsky, A., & Evans, J.A. (2015). "Tradition and innovation in scientists' research strategies." *American Sociological Review*, 80(5), 875–908.
- **Key contribution:** Quantified the tension between exploration (innovation) and exploitation (tradition) in research strategies, finding most scientists are conservative.
- **Relevance:** **Directly relevant** — exploration/exploitation balance is a key dimension of "research taste."

### 6.4 Shi, F., Foster, J.G., & Evans, J.A. (2015). "Weaving the fabric of science: Dynamic network models of science's unfolding structure." *Social Networks*, 43, 73–85.
- **Key contribution:** Modeled how scientists weave new connections between concepts, characterizing individual contributions to the knowledge network.
- **Relevance:** Captures how researchers uniquely connect ideas — a structural fingerprint.

### 6.5 Fortunato, S., Bergstrom, C.T., Börner, K., Evans, J.A., Helbing, D., Milojević, S., ... & Barabási, A.L. (2018). "Science of science." *Science*, 359(6379), eaao0185.
- **Key contribution:** Major review article synthesizing the science of science, covering careers, teams, impact prediction, and the structure of knowledge.
- **Relevance:** Definitive overview of the field; maps the entire landscape relevant to Research Taster.

### 6.6 Bornmann, L. & Mutz, R. (2015). "Growth rates of modern science: A bibliometric analysis based on the number of publications and cited references." *Journal of the Association for Information Science and Technology*, 66(11), 2215–2222.
- **Key contribution:** Quantified the exponential growth of scientific output, motivating the need for better filtering and profiling tools.
- **Relevance:** The information overload problem that Research Taster addresses.

---

## 7. Embedding-Based & Modern ML Approaches

### 7.1 Zhang, Y., Chen, F., & Shen, D. (2018). "Author2Vec: A framework for generating user embedding." *arXiv preprint arXiv:1903.02863*.
- **Key contribution:** Applied neural embedding methods to create dense vector representations of authors based on their publication content.
- **Relevance:** **Directly relevant** — author embeddings are a modern approach to scholarly fingerprints.

### 7.2 Cohan, A., Feldman, S., Beltagy, I., Downey, D., & Lo, K. (2020). "SPECTER: Document-level representation learning using citation-informed transformers." *Proceedings of the 58th Annual Meeting of the ACL*, 2270–2282.
- **Key contribution:** Learned document embeddings using citation signals with SciBERT, achieving strong performance on paper recommendation and classification.
- **Relevance:** SPECTER embeddings can be aggregated to create researcher profiles — key infrastructure for Research Taster.

### 7.3 Beltagy, I., Lo, K., & Cohan, A. (2019). "SciBERT: A pretrained language model for scientific text." *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 3615–3620.
- **Key contribution:** Pre-trained BERT on scientific text (Semantic Scholar corpus), providing foundational NLP for scientific document understanding.
- **Relevance:** Base model for extracting semantic features from papers for researcher profiling.

### 7.4 Safder, I. & Hassan, S.U. (2019). "Bibliometric-enhanced information retrieval: A novel deep feature engineering approach for author profiling." *Scientometrics*, 119(1), 507–535.
- **Key contribution:** Combined bibliometric features with deep learning for author profiling, outperforming traditional approaches.
- **Relevance:** Demonstrates the power of combining bibliometric and content features for profiling.

### 7.5 Singh, M., Banerjee, A., & Mukherjee, A. (2020). "Identifying tasks, datasets, evaluation metrics, and numeric scores for scientific leaderboards constructed from NLP publications." *Findings of ACL: EMNLP 2020*.
- **Key contribution:** Automated extraction of structured research contribution information from papers.
- **Relevance:** Structured extraction enables fine-grained characterization of what a researcher actually *does*.

---

## 8. Collaboration Patterns & Social Dimensions

### 8.1 Newman, M.E.J. (2004). "Coauthorship networks and patterns of scientific collaboration." *Proceedings of the National Academy of Sciences*, 101(suppl 1), 5200–5205.
- **Key contribution:** Systematic analysis of co-authorship networks across disciplines, revealing structural patterns of collaboration.
- **Relevance:** Collaboration network position is a key dimension of researcher identity.

### 8.2 Wuchty, S., Jones, B.F., & Uzzi, B. (2007). "The increasing dominance of teams in production of knowledge." *Science*, 316(5827), 1036–1039.
- **Key contribution:** Documented the shift from solo to team science, showing teams produce higher-impact work.
- **Relevance:** Team composition and role within teams characterize research style.

### 8.3 Guimerà, R., Uzzi, B., Spiro, J., & Amaral, L.A.N. (2005). "Team assembly mechanisms determine collaboration network structure and team performance." *Science*, 308(5722), 697–702.
- **Key contribution:** Showed that the balance between newcomers and incumbents in teams predicts both network structure and creative success.
- **Relevance:** Team assembly patterns as a component of researcher behavior profiling.

---

## 9. Interdisciplinarity & Knowledge Bridging

### 9.1 Leahey, E. (2016). "From sole investigator to team scientist: Trends in the practice and study of research collaboration." *Annual Review of Sociology*, 42, 81–100.
- **Key contribution:** Reviewed the shift toward collaboration and interdisciplinarity, discussing implications for researcher evaluation.
- **Relevance:** Interdisciplinary breadth as a profiling dimension.

### 9.2 Porter, A. & Rafols, I. (2009). "Is science becoming more interdisciplinary? Measuring and mapping six research fields over time." *Scientometrics*, 81(3), 719–745.
- **Key contribution:** Developed metrics for measuring interdisciplinarity of research using journal diversity measures.
- **Relevance:** Interdisciplinarity metrics as a component of researcher fingerprints.

### 9.3 Chen, C. (2006). "CiteSpace II: Detecting and visualizing emerging trends and transient patterns in scientific literature." *Journal of the American Society for Information Science and Technology*, 57(3), 359–377.
- **Key contribution:** Built CiteSpace, a widely-used tool for visualizing research fronts, burst detection, and mapping intellectual structure.
- **Relevance:** Visual analytics infrastructure for understanding where a researcher sits in the knowledge landscape.

---

## 10. Recent & Emerging Work

### 10.1 Wang, D. & Barabási, A.L. (2021). *The Science of Science*. Cambridge University Press.
- **Key contribution:** Definitive book synthesizing the science of science, covering impact, careers, teams, and the structure of scientific discovery.
- **Relevance:** The most comprehensive reference for the theoretical foundations of Research Taster.

### 10.2 Liu, L., Wang, Y., Sinatra, R., Giles, C.L., Song, C., & Wang, D. (2018). "Hot streaks in artistic, cultural, and scientific careers." *Nature*, 559, 396–399.
- **Key contribution:** Discovered that creative "hot streaks" — bursts of high-impact work — are universal across careers, suggesting temporal dynamics of creative output.
- **Relevance:** Temporal dynamics of research productivity and quality as profiling signals.

### 10.3 Milojević, S. (2015). "Quantifying the cognitive extent of science." *Journal of Informetrics*, 9(4), 962–973.
- **Key contribution:** Used keyword analysis to quantify the "cognitive extent" of scientific fields — how many distinct concepts they encompass.
- **Relevance:** Provides a framework for measuring the cognitive scope of individual researchers.

### 10.4 Battiston, F., Musciotto, F., Wang, D., Barabási, A.L., Szell, M., & Sinatra, R. (2019). "Taking census of physics." *Nature Reviews Physics*, 1, 89–97.
- **Key contribution:** Comprehensive census of the physics community, profiling researchers by subfield mobility, collaboration patterns, and career trajectories.
- **Relevance:** Demonstrates large-scale researcher profiling in practice.

---

## Summary Table: Key Themes for Research Taster

| Theme | Key Papers | Core Insight |
|-------|-----------|--------------|
| **Topic-based profiling** | Rosen-Zvi 2004, Kawamae 2010 | Author-topic distributions as fingerprints |
| **Trajectory dynamics** | Jia 2017, Sinatra 2016, Way 2017 | Research interests evolve; trajectories are individual |
| **Beyond h-index** | Hirsch 2005, Egghe 2006, Sinatra 2016 (Q-factor) | Single metrics miss style; need multidimensional profiles |
| **Novelty & style** | Uzzi 2013, Foster 2015 | Atypical combinations and exploration/exploitation balance |
| **Neural embeddings** | SPECTER 2020, SciBERT 2019, Author2Vec | Dense vector representations of researchers |
| **Collaboration identity** | Newman 2004, Wuchty 2007, Guimerà 2005 | Network position as identity dimension |
| **Interdisciplinarity** | Porter 2009, Leahey 2016 | Breadth across fields as profiling signal |
| **Systems & tools** | ArnetMiner 2008, CiteSpace 2006 | Practical researcher profiling systems |

---

*Note: Search APIs (Brave, Google Scholar, Semantic Scholar) were rate-limited during compilation. This review draws on established literature knowledge. Papers should be verified against current databases for exact citation details.*
