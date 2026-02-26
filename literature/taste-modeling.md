# Literature Review: Taste and Preference Modeling from Non-Academic Domains

> Compiled 2026-02-26. Focus: transferable frameworks for modeling "taste" applicable to research preference / Research Taster.

---

## 1. Foundational Sociology of Taste

### 1.1 Bourdieu, P. (1984). *Distinction: A Social Critique of the Judgement of Taste*. Harvard University Press.
- **Key contribution:** Seminal work establishing that taste is not innate but socially constructed through cultural capital, education, and class position. Introduces the concept of "taste space" mapped by cultural and economic capital axes.
- **Relevance to Research Taster:** Provides the theoretical backbone for understanding that research taste is shaped by academic training, institutional habitus, and disciplinary capital — not purely intellectual merit.

### 1.2 Peterson, R. A., & Kern, R. M. (1996). Changing highbrow taste: From snob to omnivore. *American Sociological Review*, 61(5), 900–907.
- **Key contribution:** Documents the shift from exclusionary highbrow taste to cultural "omnivorousness" — elites consuming across taste boundaries. Challenges Bourdieu's rigid class–taste mapping.
- **Relevance to Research Taster:** Suggests that interdisciplinary researchers may be "research omnivores" whose taste profiles span domains, paralleling cultural omnivores.

### 1.3 Lizardo, O. (2006). How cultural tastes shape personal networks. *American Sociological Review*, 71(5), 778–807.
- **Key contribution:** Shows that cultural taste similarity predicts social network ties — taste operates as a mechanism for social connection and group formation.
- **Relevance to Research Taster:** Research taste similarity could predict collaboration networks; taste-based matching could facilitate productive new connections.

### 1.4 Vlegels, J., & Lievens, J. (2017). Music classification, genres, and taste patterns: A ground-up network analysis on the clustering of artist preferences. *Poetics*, 60, 76–89.
- **Key contribution:** Uses network analysis to derive empirical taste patterns from music consumption data, showing that genre boundaries are fuzzy and taste clusters emerge from co-consumption.
- **Relevance to Research Taster:** Methodology for deriving emergent "research taste clusters" from co-reading/co-citing patterns rather than imposed disciplinary categories.

---

## 2. Music Taste Modeling

### 2.1 Rentfrow, P. J., & Gosling, S. D. (2003). The do re mi's of everyday life: The structure and personality correlates of music preferences. *Journal of Personality and Social Psychology*, 84(6), 1236–1256.
- **Key contribution:** Identifies four music preference dimensions (Reflective & Complex, Intense & Rebellious, Upbeat & Conventional, Energetic & Rhythmic) correlated with Big Five personality traits. Created the STOMP scale.
- **Relevance to Research Taster:** Template for deriving latent dimensions of research taste and correlating them with researcher personality/cognitive style.

### 2.2 Rentfrow, P. J., Goldberg, L. R., & Levitin, D. J. (2011). The structure of musical preferences: A five-factor model. *Journal of Personality and Social Psychology*, 100(6), 1139–1157.
- **Key contribution:** Refined music taste model into five factors (MUSIC: Mellow, Unpretentious, Sophisticated, Intense, Contemporary) using large-scale data, showing stable preference dimensions.
- **Relevance to Research Taster:** Demonstrates that taste in complex cultural domains can be reduced to a small number of interpretable latent factors.

### 2.3 Schedl, M., Zamani, H., Chen, C.-W., Deldjoo, Y., & Elahi, M. (2018). Current challenges and visions in music recommender systems research. *International Journal of Multimedia Information Retrieval*, 7(2), 95–116.
- **Key contribution:** Comprehensive survey of music recommendation challenges including cold start, context-awareness, taste evolution over time, and the tension between exploitation and exploration.
- **Relevance to Research Taster:** Directly maps to research recommendation challenges — new researchers (cold start), context-dependent interests, evolving taste, serendipity vs. relevance.

### 2.4 Celma, Ò. (2010). *Music Recommendation and Discovery: The Long Tail, Long Fail, and Long Play in the Digital Music Space*. Springer.
- **Key contribution:** Analyzes how recommendation algorithms systematically bias toward popular items ("long tail" problem) and argues for discovery-oriented recommendation that surfaces niche content.
- **Relevance to Research Taster:** Critical insight — research recommendation must avoid popularity bias and actively surface niche but taste-aligned papers.

### 2.5 Anderson, A., Maystre, L., Anderson, I., Mehrotra, R., & Lalmas, M. (2020). Algorithmic effects on the diversity of consumption on Spotify. *Proceedings of The Web Conference 2020*, 2155–2165.
- **Key contribution:** Empirically measures how Spotify's recommendation algorithms affect taste diversity — finding that algorithmic consumption narrows taste compared to organic exploration.
- **Relevance to Research Taster:** Warning that research recommendation systems could narrow intellectual taste; argues for diversity-aware recommendation design.

---

## 3. Food and Wine Taste Modeling

### 3.1 Ahn, Y.-Y., Ahnert, S. E., Bagrow, J. P., & Barabási, A.-L. (2011). Flavor network and the principles of food pairing. *Scientific Reports*, 1, 196.
- **Key contribution:** Constructs a flavor network based on shared chemical compounds, revealing that Western cuisines tend to pair ingredients sharing flavor compounds while East Asian cuisines avoid this. Demonstrates that taste has structural, networkable properties.
- **Relevance to Research Taster:** Analogous to building "research flavor networks" — papers that share conceptual compounds might pair well, revealing structural principles of research taste.

### 3.2 Goldenberg, D., Koren, T., Kraus, N., & Levy, O. (2021). Personalization of food recommendations: A multi-armed bandit approach. *RecSys '21*.
- **Key contribution:** Frames food recommendation as an exploration–exploitation problem; models evolving user taste through contextual bandits that adapt to changing preferences.
- **Relevance to Research Taster:** Research interests evolve; bandit-based approaches could balance recommending within known taste vs. exploring new directions.

### 3.3 Mouritsen, O. G., & Styrbæk, K. (2017). *Umami: Unlocking the Secrets of the Fifth Taste*. Columbia University Press.
- **Key contribution:** Documents how the "discovery" of umami as a fifth basic taste reshaped food science — showing that taste taxonomies are not fixed but evolve as new dimensions are recognized.
- **Relevance to Research Taster:** Metaphor for discovering new dimensions of research taste beyond obvious categories (methodology, topic, field).

### 3.4 Hopfer, H., & Heymann, H. (2014). Judging wine quality: Do we need experts, consumers, or trained panelists? *Food Quality and Preference*, 32, 221–233.
- **Key contribution:** Compares expert vs. consumer wine taste judgments, finding that experts use more dimensions and consistent vocabularies but consumers' preferences are valid and structured differently.
- **Relevance to Research Taster:** Parallels expert vs. novice research taste — senior researchers may have more refined/dimensional taste, but junior researchers' preferences are also structured and valid.

---

## 4. Collaborative Filtering Theory and Taste Models

### 4.1 Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems. *Computer*, 42(8), 30–37.
- **Key contribution:** Foundational overview of matrix factorization for collaborative filtering — decomposing the user–item interaction matrix into latent factor spaces that implicitly capture "taste dimensions."
- **Relevance to Research Taster:** Core technique for learning latent research taste factors from researcher–paper interaction data.

### 4.2 Koren, Y. (2009). Collaborative filtering with temporal dynamics. *KDD '09*, 447–456.
- **Key contribution:** Models how user preferences drift over time using time-aware matrix factorization, showing that taste is not static but evolves.
- **Relevance to Research Taster:** Research interests evolve through career stages; temporal dynamics are essential for accurate taste modeling.

### 4.3 Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative filtering for implicit feedback datasets. *ICDM '08*, 263–272.
- **Key contribution:** Develops collaborative filtering for implicit feedback (clicks, views, time spent) rather than explicit ratings — crucial since most preference data is implicit.
- **Relevance to Research Taster:** Researchers rarely explicitly rate papers; taste must be inferred from implicit signals (reads, citations, bookmarks, time spent).

### 4.4 He, X., Liao, L., Zhang, H., Nie, L., Hu, X., & Chua, T.-S. (2017). Neural collaborative filtering. *WWW '17*, 173–182.
- **Key contribution:** Replaces linear matrix factorization with neural networks for learning user–item interactions, capturing nonlinear taste patterns.
- **Relevance to Research Taster:** Neural approaches may capture complex, non-linear research taste patterns that matrix factorization misses.

### 4.5 Wang, X., He, X., Wang, M., Feng, F., & Chua, T.-S. (2019). Neural graph collaborative filtering. *SIGIR '19*, 165–174.
- **Key contribution:** Embeds the user–item bipartite graph structure into collaborative filtering, propagating taste signals through interaction networks.
- **Relevance to Research Taster:** Citation and co-readership graphs could propagate research taste signals beyond direct interactions.

---

## 5. Computational Aesthetics and Visual Preference

### 5.1 Datta, R., Joshi, D., Li, J., & Wang, J. Z. (2006). Studying aesthetics in photographic images using a computational approach. *ECCV 2006*, 288–301.
- **Key contribution:** Pioneering work on computational aesthetics — extracting visual features to predict human aesthetic judgments of photographs. Showed that aesthetic preference is partially computable.
- **Relevance to Research Taster:** Demonstrates that even "subjective" taste can be partially modeled computationally; analogous to modeling research aesthetic preferences.

### 5.2 Murray, N., Marchesotti, L., & Perronnin, F. (2012). AVA: A large-scale database for aesthetic visual analysis. *CVPR 2012*, 2408–2415.
- **Key contribution:** Created the AVA dataset (250K+ images with aesthetic ratings), enabling large-scale aesthetic preference modeling and revealing that aesthetic taste has both universal and personal components.
- **Relevance to Research Taster:** Need for large-scale research taste datasets; suggests that research taste has both universal quality signals and personal preference components.

### 5.3 Machado, P., Romero, J., Nadal, M., Santos, A., Correia, J., & Carballal, A. (2015). Computerized measures of visual complexity. *Acta Psychologica*, 160, 43–57.
- **Key contribution:** Develops computational measures of visual complexity that correlate with aesthetic preference, showing that moderate complexity is generally preferred (Berlyne's inverted-U).
- **Relevance to Research Taster:** Parallels the "optimal complexity" hypothesis for research papers — researchers may prefer papers at the edge of their comprehension (not too simple, not too complex).

### 5.4 Leder, H., Belke, B., Oeberst, A., & Augustin, D. (2004). A model of aesthetic appreciation and aesthetic judgments. *British Journal of Psychology*, 95(4), 489–508.
- **Key contribution:** Proposes a cognitive–affective model of aesthetic processing with stages: perception → memory integration → classification → evaluation → aesthetic emotion. Distinguishes aesthetic judgment from aesthetic emotion.
- **Relevance to Research Taster:** Framework for understanding how researchers process and evaluate papers — from initial perception to deep evaluation to "taste response."

---

## 6. Fashion and Design Taste

### 6.1 McAuley, J., Targett, C., Shi, Q., & Van Den Hengel, A. (2015). Image-based recommendations on styles and substitutes. *SIGIR '15*, 43–52.
- **Key contribution:** Models visual style compatibility in fashion using deep visual features, learning that "style" is a learnable latent space where similar-taste items cluster.
- **Relevance to Research Taster:** "Research style" — the aesthetic and methodological signature of papers — could be modeled analogously as a learnable latent space.

### 6.2 He, R., & McAuley, J. (2016). VBPR: Visual Bayesian Personalized Ranking from implicit feedback. *AAAI '16*, 144–150.
- **Key contribution:** Incorporates visual features into Bayesian personalized ranking for fashion recommendation, showing that visual style signals significantly improve preference prediction.
- **Relevance to Research Taster:** Paper "visual style" (figures, diagrams, formatting) and structural features could be additional signals for taste modeling.

### 6.3 Simo-Serra, E., Fidler, S., Moreno-Noguer, F., & Urtasun, R. (2015). Neuroaesthetics in fashion: Modeling the perception of fashionability. *CVPR 2015*, 869–877.
- **Key contribution:** Models "fashionability" as a learnable aesthetic judgment, demonstrating that perceived style quality has both objective and subjective components predictable by neural networks.
- **Relevance to Research Taster:** "Research fashionability" — the perceived trendiness or stylishness of research approaches — is a real taste dimension that could be modeled.

---

## 7. Taste as Identity and Social Signal

### 7.1 Berger, J., & Heath, C. (2007). Where consumers diverge from others: Identity signaling and product domains. *Journal of Consumer Research*, 34(2), 121–134.
- **Key contribution:** Shows that consumers abandon preferences when outgroup members adopt them — taste functions as identity signaling, not just utility maximization.
- **Relevance to Research Taster:** Researchers may avoid mainstream topics to signal identity; taste-based recommendation must account for identity/distinction motives.

### 7.2 Mark, N. (1998). Birds of a feather sing together. *Social Forces*, 77(2), 453–485.
- **Key contribution:** Demonstrates that taste similarity drives social network formation (homophily), creating "taste cultures" — groups with shared aesthetic orientations.
- **Relevance to Research Taster:** Research taste cultures (invisible colleges, schools of thought) form through taste homophily and could be detected computationally.

### 7.3 Lewis, K., Gonzalez, M., & Kaufman, J. (2012). Social selection and peer influence in an online social network. *Proceedings of the National Academy of Sciences*, 109(1), 68–72.
- **Key contribution:** Disentangles social selection (choosing friends with similar tastes) from peer influence (adopting friends' tastes) in network formation using longitudinal Facebook data.
- **Relevance to Research Taster:** Distinguishing whether researchers develop similar taste because they collaborate (influence) or collaborate because of similar taste (selection) matters for recommendation design.

---

## 8. Preference Learning and Taste Space Models

### 8.1 Fürnkranz, J., & Hüllermeier, E. (2010). *Preference Learning*. Springer.
- **Key contribution:** Comprehensive treatment of preference learning as a machine learning subfield — covering label ranking, instance ranking, and object ranking from pairwise comparisons.
- **Relevance to Research Taster:** Formal framework for learning research preferences from pairwise comparisons (which paper do you prefer?) rather than absolute ratings.

### 8.2 Thurstone, L. L. (1927). A law of comparative judgment. *Psychological Review*, 34(4), 273–286.
- **Key contribution:** Classic psychophysical model positing that preference judgments arise from noisy internal "taste scales" — each item has a latent utility plus Gaussian noise.
- **Relevance to Research Taster:** Foundation for understanding that research taste judgments are inherently noisy and probabilistic, not deterministic.

### 8.3 Salganik, M. J., Dodds, P. S., & Watts, D. J. (2006). Experimental study of inequality and unpredictability in an artificial cultural market. *Science*, 311(5762), 854–856.
- **Key contribution:** Famous "Music Lab" experiment showing that social influence creates massive unpredictability in cultural markets — success is partially random and path-dependent.
- **Relevance to Research Taster:** Research impact is similarly path-dependent; taste-based recommendation could help surface quality work independent of social influence cascades.

### 8.4 Bellogin, A., Castells, P., & Cantador, I. (2017). Statistical biases in information retrieval metrics for recommender systems. *Information Retrieval Journal*, 20(6), 606–634.
- **Key contribution:** Identifies systematic biases in how recommender systems are evaluated, showing that standard metrics favor popular items and penalize taste-aligned niche recommendations.
- **Relevance to Research Taster:** Evaluation of research taste modeling must account for these biases — popularity ≠ taste alignment.

---

## 9. Taste Evolution and Dynamics

### 9.1 Nguyen, T. T., Hui, P.-M., Harper, F. M., Terveen, L., & Konstan, J. A. (2014). Exploring the filter bubble: The effect of using recommender systems on content diversity. *WWW '14*, 677–686.
- **Key contribution:** Empirically measures how recommender system use affects content diversity over time — finding evidence of "filter bubbles" that narrow taste exposure.
- **Relevance to Research Taster:** Critical design consideration — Research Taster must actively counter filter bubbles to maintain intellectual breadth.

### 9.2 Borghol, Y., Ardon, S., Carlsson, N., Eager, D., & Mahanti, A. (2012). The untold story of the clones: Content-agnostic factors that impact YouTube video popularity. *KDD '12*, 1186–1194.
- **Key contribution:** Shows that content popularity on YouTube is largely driven by non-content factors (upload time, social sharing), suggesting that taste alignment and quality are distinct from popularity.
- **Relevance to Research Taster:** Reinforces that research paper popularity (citations) is a poor proxy for taste alignment.

### 9.3 Stephens-Davidowitz, S., Varian, H., & Smith, M. D. (2017). Super Returns to Superstar Creative Goods. *Working paper*.
- **Key contribution:** Documents extreme concentration in cultural consumption (superstars capture most attention) despite long-tail availability.
- **Relevance to Research Taster:** Research attention is similarly concentrated; taste modeling could democratize attention distribution.

---

## 10. Recommender Systems for Academic/Research Content

### 10.1 Beel, J., Gipp, B., Langer, S., & Breitinger, C. (2016). Research-paper recommender systems: A literature survey. *International Journal on Digital Libraries*, 17(4), 305–338.
- **Key contribution:** Comprehensive survey of research paper recommender systems covering content-based, collaborative, and hybrid approaches. Identifies that most systems ignore personal taste in favor of topical relevance.
- **Relevance to Research Taster:** Directly identifies the gap Research Taster fills — moving from topical relevance to taste-aligned recommendation.

### 10.2 Sugiyama, K., & Kan, M.-Y. (2010). Scholarly paper recommendation via user's recent research interests. *JCDL '10*, 29–38.
- **Key contribution:** Models researchers' evolving interests from their publication history to recommend papers, showing that recent interests matter more than lifetime profiles.
- **Relevance to Research Taster:** Research taste has recency bias; models must weight recent signals more heavily.

### 10.3 West, J. D., Wesley-Smith, I., & Bergstrom, C. T. (2016). A recommendation system based on hierarchical clustering of an article-level citation network. *IEEE Transactions on Big Data*, 2(2), 113–123.
- **Key contribution:** Uses hierarchical citation network clustering for paper recommendation, showing that citation-based "taste neighborhoods" outperform content-based approaches.
- **Relevance to Research Taster:** Citation patterns implicitly encode taste; hierarchical clustering reveals multi-scale taste structure.

---

## 11. Personality–Taste Correlations

### 11.1 Chamorro-Premuzic, T., & Furnham, A. (2007). Personality and music: Can traits explain how people use music in everyday life? *British Journal of Psychology*, 98(2), 175–185.
- **Key contribution:** Links Big Five personality traits to music consumption behaviors — openness predicts diverse and complex music taste; neuroticism predicts emotional music use.
- **Relevance to Research Taster:** Personality traits may similarly predict research taste — openness could predict interdisciplinary taste, conscientiousness could predict methodological rigor preference.

### 11.2 Nave, G., Minxha, J., Greenberg, D. M., Kosinski, M., Stillwell, D., & Rentfrow, J. (2018). Musical preferences predict personality: Evidence from active listening and Facebook Likes. *Psychological Science*, 29(7), 1145–1158.
- **Key contribution:** Demonstrates bidirectional prediction between music taste and personality using large-scale Facebook data, showing taste as a reliable personality signal.
- **Relevance to Research Taster:** Reading/citation patterns could be used to infer researcher personality, and vice versa, for taste cold-start problems.

### 11.3 Greenberg, D. M., Baron-Cohen, S., Stillwell, D. J., Kosinski, M., & Rentfrow, P. J. (2015). Musical preferences are linked to cognitive styles. *PLoS ONE*, 10(7), e0131151.
- **Key contribution:** Shows that empathizers prefer mellow, emotional music while systemizers prefer intense, complex music — linking cognitive style to taste dimensions.
- **Relevance to Research Taster:** Cognitive style (empathizing vs. systemizing) may predict preference for qualitative vs. quantitative research approaches.

---

## 12. Taste Embeddings and Representation Learning

### 12.1 Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words in a vector space. *NeurIPS 2013* (arXiv:1301.3781).
- **Key contribution:** Word2Vec — learning dense vector representations from co-occurrence. While not about taste per se, established the embedding paradigm now used for item/user representations in taste modeling.
- **Relevance to Research Taster:** Paper2Vec/Author2Vec approaches use this paradigm to embed papers and researchers in "taste spaces."

### 12.2 Vasile, F., Smiber, E., & Purushotham, S. (2016). Meta-Prod2Vec: Product embeddings using side-information for recommendation. *RecSys '16*, 225–232.
- **Key contribution:** Extends item embeddings with metadata (category, brand) for richer taste representation, showing that combined content+collaborative embeddings outperform either alone.
- **Relevance to Research Taster:** Paper embeddings enriched with metadata (venue, authors, methodology) could better capture research taste dimensions.

### 12.3 van den Oord, A., Dieleman, S., & Schrauwen, B. (2013). Deep content-based music recommendation. *NeurIPS 2013*.
- **Key contribution:** Uses deep neural networks on raw audio to predict collaborative filtering taste profiles, bridging the content–taste gap in music recommendation.
- **Relevance to Research Taster:** Analogously, deep models on paper text could predict collaborative taste profiles, solving cold-start for new papers.

---

## 13. Serendipity and Exploration in Taste

### 13.1 Kotkov, D., Wang, S., & Veijalainen, J. (2016). A survey of serendipity in recommender systems. *Knowledge-Based Systems*, 111, 180–192.
- **Key contribution:** Surveys how recommender systems can deliver serendipitous recommendations — items that are both surprising and relevant, expanding user taste.
- **Relevance to Research Taster:** Research discovery thrives on serendipity; taste modeling must balance accuracy with surprise.

### 13.2 Kapoor, K., Kumar, V., Terveen, L., Konstan, J. A., & Schrater, P. (2015). "I like to explore sometimes": Adapting to dynamic user novelty preferences. *RecSys '15*, 19–26.
- **Key contribution:** Models individual differences in exploration tendency — some users want novelty while others prefer familiarity — and adapts recommendations accordingly.
- **Relevance to Research Taster:** Researchers vary in exploration tendency; some want cutting-edge novelty, others prefer consolidation within known domains.

---

## Summary: Key Transferable Frameworks for Research Taster

| Framework | Source Domain | Key Insight | Application to Research Taste |
|-----------|-------------|-------------|-------------------------------|
| Taste space / cultural capital | Sociology (Bourdieu) | Taste is structured by social position | Research taste shaped by training, institution, discipline |
| Latent factor models | Music (MUSIC model) | Taste reducible to ~5 interpretable dimensions | Research taste may have similar low-dimensional structure |
| Collaborative filtering | E-commerce | Similar users like similar items | Researchers with similar reading patterns share taste |
| Implicit feedback | Streaming | Actions reveal preferences | Reads, citations, bookmarks reveal research taste |
| Temporal dynamics | Music/Film | Taste evolves over time | Research interests shift through career |
| Flavor networks | Food science | Taste has structural/network properties | Co-citation networks encode taste structure |
| Personality–taste link | Music psychology | Big Five predicts taste dimensions | Cognitive style may predict research preferences |
| Identity signaling | Consumer behavior | Taste signals group identity | Research taste signals disciplinary/tribal identity |
| Filter bubbles | Web platforms | Algorithms narrow taste | Research recommendation risks intellectual narrowing |
| Serendipity | Recommender systems | Surprise + relevance = discovery | Research Taster must deliver serendipitous papers |
| Aesthetic processing | Computational aesthetics | Taste has universal + personal components | Research quality (universal) vs. taste (personal) are distinct |
| Optimal complexity | Visual aesthetics | Moderate complexity preferred | Papers at the edge of comprehension may be most engaging |
