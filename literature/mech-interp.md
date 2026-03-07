# Mechanistic Interpretability for Probing and Steering Language Model Representations

## Literature Review: Feasibility for Extracting "Research Taste" from Academic Text

*Compiled: 2026-03-07*

---

## 1. Foundational Probing Work

### 1.1. Belinkov & Glass (2019). Analysis Methods in Neural Language Processing: A Survey.
- **Citation:** Belinkov, Y. & Glass, J. (2019). Analysis Methods in Neural Language Processing: A Survey. *Transactions of the Association for Computational Linguistics*, 7, 49–72.
- **DOI:** 10.1162/tacl_a_00254
- **URL:** https://aclanthology.org/Q19-1004/
- **Key contribution:** Comprehensive survey of methods for analyzing neural NLP models, including probing classifiers, visualization, and challenge sets. Established taxonomy of analysis approaches.
- **Relevance to Research Taster:** Foundational reference — probing classifiers are the primary tool we'd use to detect "taste" features in model representations.
- **Feasibility:** HIGH. Probing is well-established for syntactic/semantic features; extending to stylistic/subjective features is a natural next step.

### 1.2. Belinkov (2022). Probing Classifiers: Promises, Shortcomings, and Advances.
- **Citation:** Belinkov, Y. (2022). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics*, 48(1), 207–219.
- **DOI:** 10.1162/coli_a_00422
- **URL:** https://arxiv.org/abs/2102.12452
- **Key contribution:** Critical review of probing methodology. Highlights that high probe accuracy doesn't necessarily mean the representation *encodes* that feature — the probe itself may learn the task. Discusses selectivity, control tasks, and information-theoretic approaches.
- **Relevance to Research Taster:** Critical warning — we must ensure probes for "research taste" genuinely detect features in representations, not just learn the classification task. Need control tasks.
- **Feasibility:** MEDIUM. Methodological rigor needed; naive probing may give false positives.

### 1.3. Hewitt & Manning (2019). A Structural Probe for Finding Syntax in Word Representations.
- **Citation:** Hewitt, J. & Manning, C. D. (2019). A Structural Probe for Finding Syntax in Word Representations. *Proc. NAACL-HLT 2019*, 4129–4138.
- **DOI:** 10.18653/v1/N19-1419
- **URL:** https://aclanthology.org/N19-1419/
- **Key contribution:** Proposed structural probes that find linear transformations under which L2 distance encodes parse tree distance. Showed entire syntax trees are embedded in BERT/ELMo geometry.
- **Relevance to Research Taster:** Demonstrates that complex structural properties can be linearly decoded from representations. Suggests "taste" features, if encoded, might also be linearly accessible.
- **Feasibility:** HIGH for structured features; UNCERTAIN for subjective/aesthetic features.

### 1.4. Hewitt & Liang (2019). Designing and Interpreting Probes with Control Tasks.
- **Citation:** Hewitt, J. & Liang, P. (2019). Designing and Interpreting Probes with Control Tasks. *Proc. EMNLP 2019*.
- **URL:** https://nlp.stanford.edu/pubs/hewitt2019control.pdf
- **Key contribution:** Introduced control tasks to evaluate whether probes reflect representations or just memorize. Proposed "selectivity" metric. Showed that probe complexity must be controlled.
- **Relevance to Research Taster:** Essential methodology — any probe for "speculative" vs. "rigorous" must be tested against control tasks to ensure validity.
- **Feasibility:** HIGH — provides concrete methodology we should adopt.

### 1.5. Tenney et al. (2019). BERT Rediscovers the Classical NLP Pipeline.
- **Citation:** Tenney, I., Das, D., & Pavlick, E. (2019). BERT Rediscovers the Classical NLP Pipeline. *Proc. ACL 2019*, 4593–4601.
- **DOI:** 10.18653/v1/P19-1452
- **URL:** https://aclanthology.org/P19-1452.pdf
- **Key contribution:** Used probing to show BERT's layers encode NLP pipeline stages in sequence: POS → parsing → NER → semantic roles → coreference. Model dynamically adjusts this pipeline.
- **Relevance to Research Taster:** Shows that higher-level semantic features emerge in later layers. "Research taste" likely resides in final layers where abstract semantic/pragmatic features are encoded.
- **Feasibility:** HIGH — suggests we should probe later layers for taste features.

---

## 2. Linear Representation Hypothesis

### 2.1. Park et al. (2024). The Geometry of Categorical and Hierarchical Concepts in Large Language Models.
- **Citation:** Park, K., Choe, Y. J., Jiang, Y., & Veitch, V. (2024). The Geometry of Categorical and Hierarchical Concepts in Large Language Models. *arXiv:2406.01506*. (ICLR 2025 Oral, Best Paper Award ICML 2024 Workshop on Mech Interp.)
- **DOI:** 10.48550/arXiv.2406.01506
- **Key contribution:** Formalized the linear representation hypothesis for features (not just binary contrasts). Showed categorical concepts are represented as polytopes and hierarchical concepts have geometric relationships. Validated on Gemma and LLaMA-3 with 900+ concepts from WordNet.
- **Relevance to Research Taster:** If concepts like "speculative," "rigorous," "interdisciplinary" are encoded as linear directions, we can extract them. The polytope formalization could capture categorical research styles.
- **Feasibility:** HIGH — if taste qualities are conceptual features, they should follow this geometry.

### 2.2. Marks & Tegmark (2023). The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets.
- **Citation:** Marks, S. & Tegmark, M. (2023). The Geometry of Truth. *arXiv:2310.06824*.
- **URL:** https://openreview.net/pdf/0ae055dff16c072ac024f0560d5484ddc2cb4aa8.pdf
- **Key contribution:** Showed that truth/falsehood is linearly represented in LLMs. Introduced "mass-mean probing" which generalizes across datasets. Causal interventions confirm the direction is functionally relevant.
- **Relevance to Research Taster:** Demonstrates that even abstract epistemic properties (truth) are linearly represented. "Research quality" or "novelty" may similarly have linear structure.
- **Feasibility:** HIGH — mass-mean probing could be adapted for taste dimensions.

### 2.3. Tigges et al. (2023). Linear Representations of Sentiment in Large Language Models.
- **Citation:** Tigges, C., Hollinsworth, O. J., Geiger, A., & Nanda, N. (2023). Linear Representations of Sentiment in Large Language Models. *arXiv:2310.15154*.
- **URL:** https://gwern.net/doc/www/arxiv.org/9b6ccd049db135859259c2b0b4bde6eabbf05a30.pdf
- **Key contribution:** Showed sentiment is represented as a single linear direction across multiple models and tasks. Causal interventions confirm this direction is causally relevant. Extended to positive/negative extremes.
- **Relevance to Research Taster:** DIRECTLY RELEVANT. Sentiment is subjective and stylistic — the fact that it's linearly represented strongly suggests that other subjective qualities (speculative tone, rigor, novelty) may also be linear.
- **Feasibility:** VERY HIGH — this is the closest analogue to what we want to do.

---

## 3. Steering Vectors & Activation Engineering

### 3.1. Turner et al. (2023). Activation Addition: Steering Language Models Without Optimization.
- **Citation:** Turner, A. M., Thiergart, L., Udell, D., Leech, G., Mini, U., & MacDiarmid, M. (2023). Activation Addition: Steering Language Models Without Optimization. *arXiv:2308.10248*.
- **URL:** https://turntrout.com/gpt2-steering-vectors
- **Key contribution:** Introduced "activation additions" (ActAdd) — adding steering vectors to residual stream activations to control model behavior without any training. Demonstrated on GPT-2-XL for wedding, anger, cheese, and other concepts.
- **Relevance to Research Taster:** Could steer a model to generate text in different "research taste" styles (speculative vs. formal, interdisciplinary vs. narrow). Zero training cost.
- **Feasibility:** HIGH — simple, no optimization needed. But effectiveness for subtle stylistic features is unproven.

### 3.2. Rimsky et al. (2024). Steering Llama 2 via Contrastive Activation Addition.
- **Citation:** Rimsky, N., Gabrieli, N., Schulz, J., Tong, M., Hubinger, E., & Turner, A. M. (2024). Steering Llama 2 via Contrastive Activation Addition. *Proc. ACL 2024*, 15504–15522.
- **DOI:** 10.18653/v1/2024.acl-long.828
- **URL:** https://aclanthology.org/2024.acl-long.828.pdf
- **Key contribution:** Introduced Contrastive Activation Addition (CAA) — computing steering vectors by averaging residual stream activation differences between positive/negative behavior pairs. Steered sycophancy, hallucination, corrigibility, power-seeking. Outperformed finetuning and few-shot prompting with zero inference cost.
- **Relevance to Research Taster:** DIRECTLY APPLICABLE. We could construct contrastive pairs (e.g., "speculative/exploratory" vs. "conservative/incremental" paper abstracts) and extract steering vectors. Could shift generation style.
- **Feasibility:** VERY HIGH — proven method, works on Llama 2, extensible to any contrastive behavior.

### 3.3. Li et al. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model.
- **Citation:** Li, K., Patel, O., Viégas, F., Pfister, H., & Wattenberg, M. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. *NeurIPS 2023* (Spotlight).
- **DOI:** 10.48550/arXiv.2306.03341
- **URL:** https://arxiv.org/abs/2306.03341
- **Key contribution:** ITI shifts model activations during inference using learned directions across specific attention heads. Improved LLaMA/Alpaca truthfulness from 32.5% to 65.1% on TruthfulQA. Minimally invasive, data-efficient.
- **Relevance to Research Taster:** ITI targets specific attention heads rather than full residual stream — could provide finer-grained control over "taste" features. Attention-head-level probing reveals WHERE taste is encoded.
- **Feasibility:** HIGH — light-weight, proven on LLaMA. Could probe for which heads encode "taste" dimensions.

### 3.4. Hoscilowicz et al. (2024). Non-Linear Inference Time Intervention: Improving LLM Truthfulness.
- **Citation:** Hoscilowicz, J., Wiacek, A., Chojnacki, J., Cieslak, A., Michon, L., & Janicki, A. (2024). Non-Linear Inference Time Intervention. *Interspeech 2024*.
- **DOI:** 10.48550/arXiv.2403.18680
- **URL:** https://arxiv.org/html/2403.18680v2
- **Key contribution:** Extended ITI with non-linear multi-token probing. Shows that some features benefit from non-linear probes, suggesting not everything is linearly represented.
- **Relevance to Research Taster:** Important warning — "research taste" may require non-linear probes if it's a complex, multi-faceted concept. Linear probes might miss it.
- **Feasibility:** MEDIUM — adds complexity but may be necessary.

---

## 4. Representation Engineering

### 4.1. Zou et al. (2023). Representation Engineering: A Top-Down Approach to AI Transparency.
- **Citation:** Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., Goel, S., Li, N., Byun, M. J., Wang, Z., Mallen, A., Basart, S., Koyejo, S., Song, D., Fredrikson, M., Kolter, J. Z., & Hendrycks, D. (2023). Representation Engineering: A Top-Down Approach to AI Transparency. *arXiv:2310.01405*.
- **URL:** https://arxiv.org/html/2310.01405
- **Key contribution:** Proposed RepE — reading and controlling high-level cognitive phenomena (honesty, fairness, harmlessness) via representation-level techniques. Uses "reading vectors" from contrastive stimuli and "control vectors" for steering. Unified framework for monitoring and control.
- **Relevance to Research Taster:** CORE FRAMEWORK. RepE is exactly the paradigm we'd use — define contrastive stimuli for taste dimensions (e.g., speculative vs. conservative papers), extract reading/control vectors.
- **Feasibility:** VERY HIGH — the paper explicitly demonstrates this for abstract, high-level concepts. "Research taste" is another such concept.

### 4.2. Bartoszcze et al. (2025). Representation Engineering for Large-Language Models: Survey and Research Challenges.
- **Citation:** Bartoszcze, L., Munshi, S., Sukidi, B., Yen, J., Yang, Z., Williams-King, D., Le, L., Asuzu, K., & Maple, C. (2025). Representation Engineering for LLMs: Survey and Research Challenges. *arXiv:2502.17601*.
- **DOI:** 10.48550/arXiv.2502.17601
- **Key contribution:** Comprehensive survey of RepE methods, challenges, and open problems. Covers reading, writing, and controlling representations.
- **Relevance to Research Taster:** Up-to-date survey for understanding the state of the art and limitations.
- **Feasibility:** Reference paper — provides landscape view.

---

## 5. Sparse Autoencoders for Feature Discovery

### 5.1. Bricken, Templeton, et al. (2023). Towards Monosemanticity: Decomposing Language Models With Dictionary Learning.
- **Citation:** Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., Conerly, T., Turner, N. L., Anil, C., Denison, C., Askell, A., Lasenby, R., Wu, Y., Kravec, S., Schiefer, N., Maxwell, T., Joseph, N., Tamkin, A., Nguyen, K., McLean, B., Burke, J. E., Hume, T., Carter, S., Henighan, T., & Olah, C. (2023). Towards Monosemanticity. *Transformer Circuits Thread*, Anthropic.
- **URL:** https://transformer-circuits.pub/2023/monosemantic-features
- **Key contribution:** Used sparse autoencoders (SAEs) to extract interpretable, monosemantic features from a one-layer transformer. Found features for specific topics, languages, and patterns. Demonstrated that SAEs can resolve polysemanticity.
- **Relevance to Research Taster:** SAEs could discover "research taste" features *without supervision*. If taste is a feature the model uses, SAEs might find it automatically among the decomposed features.
- **Feasibility:** MEDIUM-HIGH. SAEs are unsupervised and might find taste features, but searching through thousands of features for the relevant ones is labor-intensive. May need to scale to larger models.

### 5.2. Cunningham et al. (2023). Sparse Autoencoders Find Highly Interpretable Features in Language Models.
- **Citation:** Cunningham, H., Ewart, A., Riggs, L., Huben, R., & Sharkey, L. (2023). Sparse Autoencoders Find Highly Interpretable Features in Language Models. *arXiv:2309.08600*.
- **URL:** https://arxiv.org/abs/2309.08600
- **Key contribution:** Showed SAEs learn more interpretable and monosemantic features than alternatives. Features are causally responsible for model behavior (validated on IOI task). Scalable unsupervised method for resolving superposition.
- **Relevance to Research Taster:** Confirms SAEs as a viable tool for finding features. If "taste" is encoded as a direction in superposition, SAEs might extract it.
- **Feasibility:** MEDIUM-HIGH — same as above. Need to search for relevant features.

### 5.3. Templeton et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet.
- **Citation:** Templeton, A. et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. *Transformer Circuits Thread*, Anthropic.
- **URL:** https://transformer-circuits.pub/2024/scaling-monosemanticity/
- **Key contribution:** Scaled SAEs to Claude 3 Sonnet (a production model). Found features for abstract concepts like "sycophantic praise," "code errors," "deception." Demonstrated that features can be used for steering.
- **Relevance to Research Taster:** HIGHLY RELEVANT. Finding abstract features like "sycophantic praise" shows that subjective/stylistic features ARE discoverable by SAEs. "Research taste" features (novelty, rigor, speculation) are at a similar level of abstraction.
- **Feasibility:** HIGH — but requires significant compute for SAE training on large models. Open-weight models make this feasible.

### 5.4. Rajamanoharan et al. (2024). Improving Dictionary Learning with Gated Sparse Autoencoders.
- **Citation:** Rajamanoharan, S., Conmy, A., Smith, L., Lieberum, T., Varma, V., Kramár, J., Shah, R., & Nanda, N. (2024). Improving Dictionary Learning with Gated Sparse Autoencoders. *arXiv:2404.16014*.
- **DOI:** 10.48550/arXiv.2404.16014
- **Key contribution:** Gated SAEs solve shrinkage bias from L1 penalty, are more interpretable, and need half as many features for comparable reconstruction. Trained on models up to 7B parameters.
- **Relevance to Research Taster:** Better SAE architecture for feature extraction. If we use SAEs, Gated SAEs are the current best practice.
- **Feasibility:** HIGH — practical improvement over standard SAEs.

---

## 6. Superposition & Feature Theory

### 6.1. Elhage et al. (2022). Toy Models of Superposition.
- **Citation:** Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). Toy Models of Superposition. *Transformer Circuits Thread*, Anthropic.
- **URL:** https://transformer-circuits.pub/2022/toy_model/index.html
- **Key contribution:** Formalized superposition — neural networks represent more features than they have neurons by using overcomplete bases. Explored phase transitions, geometry of feature representations, and implications for interpretability.
- **Relevance to Research Taster:** Key theoretical challenge. "Research taste" might be encoded in superposition — entangled with many other features. SAEs or other decomposition needed to isolate it.
- **Feasibility:** Theoretical foundation — explains WHY simple neuron-level analysis fails and WHY we need SAEs or probing.

### 6.2. Olah et al. (2020). Zoom In: An Introduction to Circuits.
- **Citation:** Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). Zoom In: An Introduction to Circuits. *Distill*, 5(3).
- **DOI:** 10.23915/distill.00024.001
- **URL:** https://distill.pub/2020/circuits/zoom-in/
- **Key contribution:** Introduced the circuits framework — three claims: (1) features are the fundamental units, (2) features are connected by circuits, (3) analogous features/circuits appear across models (universality). Demonstrated in vision models.
- **Relevance to Research Taster:** Universality hypothesis suggests that if "research taste" features exist in one model, they likely exist in others. Circuits connecting taste features to outputs could be identified.
- **Feasibility:** MEDIUM — vision-focused but principles extend to language models.

### 6.3. Olah (2023). Distributed Representations: Composition & Superposition.
- **Citation:** Olah, C. (2023). Distributed Representations: Composition & Superposition. *Transformer Circuits Thread*.
- **URL:** https://transformer-circuits.pub/2023/superposition-composition/index.html
- **Key contribution:** Clarified relationship between classical distributed representations and superposition. Features can be composed and superposed, creating complex representational structures.
- **Relevance to Research Taster:** "Research taste" is likely a composed feature — combining multiple lower-level features (vocabulary choices, citation patterns, argumentation style).
- **Feasibility:** Theoretical insight — taste may need to be understood as a composition of simpler features.

---

## 7. Latent Knowledge Discovery

### 7.1. Burns et al. (2022). Discovering Latent Knowledge in Language Models Without Supervision.
- **Citation:** Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2022). Discovering Latent Knowledge in Language Models Without Supervision. *arXiv:2212.03827*. (ICLR 2023).
- **URL:** https://arxiv.org/abs/2212.03827
- **Key contribution:** Introduced Contrast-Consistent Search (CCS) — finds directions in activation space satisfying logical consistency (a statement and its negation have opposite truth values) *without labels*. Recovers latent knowledge across 6 models and 10 datasets.
- **Relevance to Research Taster:** Unsupervised approach — could discover "taste" dimensions by finding directions that consistently distinguish different paper qualities. No labeled data needed.
- **Feasibility:** MEDIUM — CCS works for binary truth/falsehood. "Taste" is multi-dimensional, so would need extension.

### 7.2. Farquhar et al. (2023). Challenges with Unsupervised LLM Knowledge Discovery.
- **Citation:** Farquhar, S., Varma, V., Kenton, Z., Gasteiger, J., Mikulik, V., & Shah, R. (2023). Challenges with Unsupervised LLM Knowledge Discovery.
- **URL:** https://sebastianfarquhar.com/assets/papers/farquharChallenges2023.pdf
- **Key contribution:** Showed CCS doesn't reliably discover knowledge — it discovers whatever feature is most prominent in activations. Proved theoretically that arbitrary features satisfy CCS consistency structure.
- **Relevance to Research Taster:** Critical warning — unsupervised methods may find "prominent but irrelevant" features rather than the taste features we want. Supervised probing with labeled examples may be more reliable.
- **Feasibility:** Lowers confidence in purely unsupervised approaches. Supervised probing preferred.

---

## 8. Style, Tone & Subjective Feature Detection

### 8.1. Hicke & Mimno (2025). Looking for the Inner Music: Probing LLMs' Understanding of Literary Style.
- **Citation:** Hicke, R. M. M. & Mimno, D. (2025). Looking for the Inner Music: Probing LLMs' Understanding of Literary Style. *arXiv:2502.03647*.
- **URL:** https://www.arxiv.org/pdf/2502.03647
- **Key contribution:** Probed LLMs for authorship and genre classification of literary passages. Found LLMs distinguish authorship and genre but via different mechanisms. Authorial style is defined by minor syntactic decisions and contextual word usage; genre is harder.
- **Relevance to Research Taster:** DIRECTLY RELEVANT. This is probing for *style* — the closest analogue to "research taste." Shows LLMs do encode stylistic features. Genre detection (like "speculative" vs. "empirical" research styles) is feasible but harder than authorship.
- **Feasibility:** HIGH — demonstrates that style probing works in LLMs. Our task is similar.

### 8.2. Conneau et al. (2018). What You Can Cram into a Single Vector: Probing Sentence Embeddings for Linguistic Properties.
- **Citation:** Conneau, A., Kruszewski, G., Lample, G., Barrault, L., & Baroni, M. (2018). What You Can Cram into a Single Vector. *Proc. ACL 2018*, 2126–2136.
- **DOI:** 10.18653/v1/P18-1198
- **URL:** https://aclanthology.org/P18-1198/
- **Key contribution:** Introduced SentEval probing tasks: 10 probing tasks for sentence embeddings including sentence length, word content, tree depth, tense, etc. Established probing as standard methodology.
- **Relevance to Research Taster:** Foundational probing methodology for sentence-level features. We'd extend this to document-level "taste" features.
- **Feasibility:** HIGH — well-established framework to build on.

### 8.3. Alain & Bengio (2017). Understanding Intermediate Layers Using Linear Classifier Probes.
- **Citation:** Alain, G. & Bengio, Y. (2017). Understanding Intermediate Layers Using Linear Classifier Probes. *ICLR 2017 Workshop*.
- **URL:** https://arxiv.org/abs/1610.01644
- **Key contribution:** Pioneered linear probing — training linear classifiers on intermediate representations to understand what layers encode. Showed progressive feature development across layers.
- **Relevance to Research Taster:** Foundation for all probing work. Linear probes are computationally cheap and interpretable.
- **Feasibility:** HIGH — baseline method.

---

## 9. Concept Bottleneck Models

### 9.1. Sun et al. (2025). Concept Bottleneck Large Language Models.
- **Citation:** Sun, C.-E., Oikarinen, T., Ustun, B., & Weng, T.-W. (2025). Concept Bottleneck Large Language Models (CB-LLMs). *ICLR 2025*.
- **URL:** https://arxiv.org/abs/2412.07992
- **Key contribution:** Integrated concept bottleneck models into LLMs for text classification and generation. Models predict explicit concepts before making predictions, enabling interpretability. Competitive with black-box models.
- **Relevance to Research Taster:** Could define "taste concepts" (novelty, rigor, interdisciplinarity, speculation) as the bottleneck layer. Model explicitly reasons through these before classifying papers.
- **Feasibility:** HIGH — directly applicable architecture. Would need curated taste concepts.

### 9.2. Ludan et al. (2023). Interpretable-by-Design Text Classification with Iteratively Generated Concept Bottleneck.
- **Citation:** Ludan, J. M., Lyu, Q., Yang, Y., Dugan, L., Yatskar, M., & Callison-Burch, C. (2023). Text Bottleneck Models. *arXiv:2310.19660*.
- **URL:** https://liamdugan.com/files/interpretable-by-design.pdf
- **Key contribution:** Proposed Text Bottleneck Models (TBMs) — LLM-generated concepts as interpretable intermediate layer. Concepts auto-discovered by prompting an LLM, then measured and used for classification.
- **Relevance to Research Taster:** Could auto-discover "taste" concepts by prompting an LLM about what makes research "speculative" vs. "rigorous" etc. Then use these as bottleneck layer.
- **Feasibility:** HIGH — practical, off-the-shelf approach.

### 9.3. Bhan et al. (2025). Towards Achieving Concept Completeness for Textual Concept Bottleneck Models.
- **Citation:** Bhan, M., Choho, Y., Moreau, P., Vittaut, J.-N., Chesneau, N., & Lesot, M.-J. (2025). Complete Textual Concept Bottleneck Model (CT-CBM). *Findings of EMNLP 2025*.
- **URL:** https://aclanthology.org/anthology-files/pdf/findings/2025.findings-emnlp.106.pdf
- **Key contribution:** Addressed concept completeness — ensuring the concept set covers all relevant features for accurate prediction. Critical for bottleneck models.
- **Relevance to Research Taster:** "Research taste" has many dimensions; ensuring our concept set is complete is essential.
- **Feasibility:** HIGH — provides methodology for ensuring concept coverage.

### 9.4. Koh et al. (2020). Concept Bottleneck Models.
- **Citation:** Koh, P. W., Nguyen, T., Tang, Y. S., Mussmann, S., Pierson, E., Kim, B., & Liang, P. (2020). Concept Bottleneck Models. *ICML 2020*.
- **DOI:** 10.48550/arXiv.2007.04612
- **URL:** https://arxiv.org/abs/2007.04612
- **Key contribution:** Original concept bottleneck model paper. Predictions must pass through a layer of human-interpretable concepts. Enables intervention at concept level.
- **Relevance to Research Taster:** Foundation for CB-LLMs. The bottleneck architecture is directly applicable to taste decomposition.
- **Feasibility:** HIGH — proven architecture.

---

## 10. Neel Nanda's Work

### 10.1. Nanda (n.d.). A Comprehensive Mechanistic Interpretability Explainer & Glossary.
- **Citation:** Nanda, N. (n.d.). A Comprehensive Mechanistic Interpretability Explainer & Glossary.
- **URL:** https://www.neelnanda.io/mechanistic-interpretability/glossary
- **Key contribution:** Definitive glossary and explainer for mech interp concepts: residual streams, attention patterns, induction heads, superposition, features, circuits.
- **Relevance to Research Taster:** Essential reference for understanding the machinery we'd use.
- **Feasibility:** Reference resource.

### 10.2. Nanda et al. (2023). Progress Measures for Grokking via Mechanistic Interpretability.
- **Citation:** Nanda, N., Chan, L., Liberum, T., Smith, J., & Steinhardt, J. (2023). Progress Measures for Grokking via Mechanistic Interpretability. *ICLR 2023*.
- **DOI:** 10.48550/arXiv.2301.05217
- **URL:** https://arxiv.org/abs/2301.05217
- **Key contribution:** Used mech interp to fully reverse-engineer a small transformer trained on modular addition. Identified discrete Fourier transform algorithm learned by the network.
- **Relevance to Research Taster:** Demonstrates full mechanistic understanding is possible. For taste probing, we don't need full reverse-engineering — just feature identification.
- **Feasibility:** N/A — different scope but validates approach.

---

## 11. Document-Level Features & Aggregation

### 11.1. Li et al. (2025). ChuLo: Chunk-Level Key Information Representation for Long Document Understanding.
- **Citation:** Li, Y., Han, S. C., Dai, Y., & Cao, F. (2025). ChuLo. *Findings of ACL 2025*, 14756–14773.
- **URL:** https://aclanthology.org/2025.findings-acl.762.pdf
- **Key contribution:** Groups tokens into semantically meaningful chunks for long document understanding. Preserves core content while reducing input length.
- **Relevance to Research Taster:** Key challenge — academic papers are long documents. Chunk-level approaches could help aggregate token-level taste features.
- **Feasibility:** MEDIUM — document-level aggregation remains an open challenge.

---

## 12. Additional Relevant Work

### 12.1. Kim et al. (2018). Interpretability Beyond Feature Attribution: TCAV.
- **Citation:** Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., Viegas, F., & Sayres, R. (2018). TCAV. *ICML 2018*.
- **DOI:** 10.48550/arXiv.1711.11279
- **URL:** https://arxiv.org/abs/1711.11279
- **Key contribution:** Testing with Concept Activation Vectors — quantifies influence of user-defined concepts on model predictions via directional derivatives.
- **Relevance to Research Taster:** Could define taste concepts and measure their influence on predictions. Quantitative, concept-level explanations.
- **Feasibility:** HIGH — extensible to text.

### 12.2. Vig et al. (2020). Investigating Gender Bias in Language Models Using Causal Mediation Analysis.
- **Citation:** Vig, J., Gehrmann, S., Belinkov, Y., et al. (2020). *NeurIPS 2020*.
- **DOI:** 10.48550/arXiv.2004.12265
- **URL:** https://arxiv.org/abs/2004.12265
- **Key contribution:** Applied causal mediation analysis to identify model components mediating gender bias. Used interchange interventions.
- **Relevance to Research Taster:** Methodological template for identifying components mediating taste features.
- **Feasibility:** HIGH.

### 12.3. Meng et al. (2022). Locating and Editing Factual Associations in GPT.
- **Citation:** Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). ROME. *NeurIPS 2022*.
- **DOI:** 10.48550/arXiv.2202.05262
- **URL:** https://arxiv.org/abs/2202.05262
- **Key contribution:** Located factual associations in MLP layers using causal tracing, edited them surgically. Showed factual knowledge is localized.
- **Relevance to Research Taster:** If taste preferences are localized, they could be identified via causal tracing.
- **Feasibility:** MEDIUM — taste is less localized than individual facts.

### 12.4. Geva et al. (2021). Transformer Feed-Forward Layers Are Key-Value Memories.
- **Citation:** Geva, M., Schuster, R., Berant, J., & Levy, O. (2021). *EMNLP 2021*.
- **DOI:** 10.18653/v1/2021.emnlp-main.446
- **URL:** https://arxiv.org/abs/2012.14913
- **Key contribution:** MLP layers act as key-value memories — keys detect input patterns, values store associated outputs.
- **Relevance to Research Taster:** MLP layers might store taste-associated patterns.
- **Feasibility:** MEDIUM.

### 12.5. Bolukbasi et al. (2016). Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings.
- **Citation:** Bolukbasi, T., Chang, K.-W., Zou, J., Saligrama, V., & Kalai, A. (2016). *NeurIPS 2016*.
- **URL:** https://arxiv.org/abs/1607.06520
- **Key contribution:** Gender bias encoded as linear direction in word embeddings. Removed bias by projecting out this direction. Early demonstration of linear concept geometry.
- **Relevance to Research Taster:** Pioneering linear direction finding for abstract concepts. Same principle applies.
- **Feasibility:** HIGH — foundational analogy.

### 12.6. Todd et al. (2024). Function Vectors in Large Language Models.
- **Citation:** Todd, E., Li, M. L., Sharma, A. S., Mueller, A., Wallace, B. C., & Bau, D. (2024). *ICLR 2024*.
- **DOI:** 10.48550/arXiv.2310.15213
- **URL:** https://arxiv.org/abs/2310.15213
- **Key contribution:** Identified "function vectors" encoding in-context-learned I/O functions. Transfer across inputs, extractable from attention heads.
- **Relevance to Research Taster:** Taste evaluation is a function; if encoded as a vector, extractable.
- **Feasibility:** MEDIUM-HIGH.

### 12.7. Hernandez et al. (2024). Linearity of Relation Decoding in Transformer Language Models.
- **Citation:** Hernandez, E., Li, A. S., & Bau, D. (2024). *ICLR 2024*.
- **DOI:** 10.48550/arXiv.2308.09124
- **URL:** https://arxiv.org/abs/2308.09124
- **Key contribution:** Subject-relation-object decoding is approximately linear. Relation vectors extractable.
- **Relevance to Research Taster:** More evidence for linear representation of abstract relationships.
- **Feasibility:** HIGH — theoretical support.

### 12.8. Conmy et al. (2023). Towards Automated Circuit Discovery for Mechanistic Interpretability.
- **Citation:** Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimersheim, S., & Garriga-Alonso, A. (2023). *NeurIPS 2023*.
- **DOI:** 10.48550/arXiv.2304.14997
- **URL:** https://arxiv.org/abs/2304.14997
- **Key contribution:** ACDC — automated method for finding circuits responsible for specific behaviors.
- **Relevance to Research Taster:** Could identify circuits for taste judgments. Ambitious.
- **Feasibility:** MEDIUM — computationally expensive.

### 12.9. Bills et al. (2023). Language Models Can Explain Neurons in Language Models.
- **Citation:** Bills, S., Cammarata, N., et al. (2023). *OpenAI Technical Report*.
- **URL:** https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html
- **Key contribution:** Used GPT-4 to auto-explain GPT-2 neurons in natural language. Automated interpretability.
- **Relevance to Research Taster:** Could auto-explain SAE features to identify taste-relevant ones.
- **Feasibility:** HIGH — practical automation.

### 12.10. Templeton et al. (2024). Mapping the Mind of a Large Language Model (Anthropic Blog).
- **URL:** https://www.anthropic.com/research/mapping-mind-language-model
- **Key contribution:** Found millions of interpretable features in Claude 3 Sonnet including abstract/subjective concepts. Demonstrates features for sycophancy, deception, bias at production scale.
- **Relevance to Research Taster:** Validates that abstract features ARE discoverable. "Taste" is comparable in abstraction level.
- **Feasibility:** HIGH.

### 12.11. Palumbo et al. (2025). Validating Mechanistic Interpretations: An Axiomatic Approach.
- **Citation:** Palumbo, N., et al. (2025). *arXiv:2407.13594*.
- **URL:** https://arxiv.org/pdf/2407.13594
- **Key contribution:** Formalized validation of mechanistic interpretations using axioms from abstract interpretation.
- **Relevance to Research Taster:** Validation framework for claimed taste features.
- **Feasibility:** Reference.

### 12.12. Subramanian et al. (2018). SPINE: SParse Interpretable Neural Embeddings.
- **Citation:** Subramanian, A., et al. (2018). *AAAI 2018*.
- **DOI:** 10.1609/aaai.v32i1.11935
- **URL:** https://arxiv.org/abs/1711.08792
- **Key contribution:** Created sparse, interpretable embeddings with denoising k-sparse autoencoders.
- **Relevance to Research Taster:** Precursor to SAE-based feature extraction.
- **Feasibility:** MEDIUM.

### 12.13. Adler & Shavit (2024). On the Complexity of Neural Computation in Superposition.
- **URL:** https://dspace.mit.edu/bitstream/handle/1721.1/157073/Superposition.pdf
- **Key contribution:** First lower bounds on computation in superposition.
- **Relevance to Research Taster:** Theoretical context for feature extraction from superposed representations.
- **Feasibility:** Theoretical reference.

---

## SUMMARY

### Overall Feasibility Verdict: **HIGH — Strongly Feasible**

The evidence overwhelmingly suggests that mechanistic interpretability techniques can extract "research taste" from academic text. Key reasons:

1. **Subjective features ARE linearly represented.** Sentiment (Tigges et al.), truth (Marks & Tegmark), and literary style (Hicke & Mimno) are all linearly represented in LLMs. "Research taste" — which is essentially a complex stylistic/epistemic quality — is a natural extension.

2. **Steering vectors work for abstract behaviors.** CAA (Rimsky et al.) successfully steers sycophancy, corrigibility, and power-seeking. RepE (Zou et al.) controls honesty and fairness. Steering for "speculative" vs. "rigorous" writing style is directly analogous.

3. **SAEs find abstract features.** Anthropic's work on Claude 3 Sonnet discovered features for "sycophantic praise" and "deception" — subjective features at a similar abstraction level to "taste."

4. **Concept bottleneck models work for text.** CB-LLMs (Sun et al.) and TBMs (Ludan et al.) enable interpretable text classification through explicit concept layers — directly applicable to taste decomposition.

### Recommended Approach

**Phase 1: Linear Probing (Lowest Risk, Fastest)**
- Train linear probes on labeled examples of different "taste" dimensions (speculative, rigorous, interdisciplinary, novel, etc.)
- Use contrastive pairs of paper abstracts/introductions
- Probe at different layers to find where taste is encoded (likely layers 60-80% deep)
- Apply Hewitt & Liang control tasks for validation
- **Timeline:** Days to weeks with labeled data

**Phase 2: Steering Vectors via CAA (Medium Effort, High Impact)**
- Construct contrastive pairs for each taste dimension
- Extract steering vectors using CAA methodology (Rimsky et al.)
- Test steering: can we shift model generation from "speculative" to "rigorous" question generation?
- Validate with human evaluation
- **Timeline:** Weeks

**Phase 3: SAE Feature Discovery (Higher Effort, Deeper Understanding)**
- Train SAEs on a suitable model's activations while processing academic text
- Search for taste-relevant features among discovered features (using LLM-based explanation à la Bills et al.)
- Map discovered features to taste dimensions
- **Timeline:** Weeks to months, requires compute

**Phase 4: Concept Bottleneck (Production Path)**
- Define explicit taste concepts from Phase 1-3 discoveries
- Build CB-LLM for paper classification/evaluation
- Enable human intervention at concept level
- **Timeline:** Months

### Suggested Model Choices

1. **Llama 3 (8B, 70B)** — Best choice. Open-weight, extensively studied by mech interp community, good SAE support (Gated SAEs from Nanda et al.), CAA proven to work on Llama 2.
2. **Gemma 2 (9B, 27B)** — Good alternative. Google-supported, TransformerLens compatible, Park et al. validated linear representation hypothesis on Gemma.
3. **Mistral (7B)** — Viable but less mech interp tooling support.
4. **Pythia (various sizes)** — Useful for developmental experiments due to checkpoint availability, but smaller and less capable.

**Recommendation: Start with Llama 3 8B for probing experiments, scale to 70B for steering and SAE work.**

### Key Risks and Limitations

1. **Non-linearity.** "Research taste" may be a fundamentally non-linear feature, requiring more complex probes (Hoscilowicz et al.). Mitigate by trying both linear and non-linear probes.

2. **Polysemanticity / Superposition.** Taste features may be entangled with many other features in superposition (Elhage et al.). SAEs help but don't fully solve this.

3. **Document-level aggregation.** Most mech interp works at token level. Academic papers are long documents. Aggregating token-level features to document-level taste signals is an open challenge. Options: probe on abstract/introduction only, use chunking (Li et al.), or attention-weighted pooling.

4. **Subjectivity and label noise.** "Research taste" is inherently subjective. Probe performance is bounded by inter-annotator agreement. Need clear operational definitions (e.g., "speculative" = makes claims beyond available evidence with explicit uncertainty markers).

5. **Concept granularity.** "Taste" is multi-dimensional. Individual dimensions (novelty, rigor, speculation, interdisciplinarity) may each have their own direction/feature, or they may be entangled. Start with binary contrasts, then combine.

6. **Validation difficulty.** Unlike truth (testable) or sentiment (clear labels), "taste" has no ground truth. Need human expert panels for validation. Belinkov's warnings about probe overfitting are especially relevant.

7. **Model capability ceiling.** If the base model hasn't "seen" enough academic text to develop taste features, they won't exist to extract. Use models trained on diverse academic corpora.

### Feasibility by Research Question

| Question | Verdict | Confidence |
|----------|---------|------------|
| Can linear probes detect subjective qualities (speculative vs. rigorous)? | **YES** — sentiment and style are already linearly probeable | HIGH |
| Can steering vectors shift generation style? | **YES** — CAA demonstrably shifts behavioral style | HIGH |
| Has anyone applied mech interp to academic text? | **Not directly** — Hicke & Mimno on literary style is closest | LOW (gap = opportunity) |
| What are the limitations? | Non-linearity, doc-level aggregation, subjectivity of labels | — |
| Best open-weight models? | Llama 3 8B/70B (best tooling), Gemma 2 (validated theory) | HIGH |

### Total Papers Reviewed: 42+

---

*This literature review supports the Research Taster project's mechanistic interpretability component. The evidence strongly suggests that extracting "research taste" from LLM representations is feasible, with linear probing and steering vectors as the recommended starting approaches.*
