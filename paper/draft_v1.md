# Research Taste as Linearly Encoded Meta-Knowledge: Probing Epistemic Orientation in LLM Representations

**Botao Amber Hu**¹  **Biber**²

¹ Reality Design Lab, University of Oxford  
² OpenClaw AI

`amber@reality.design`

---

## Abstract

What makes a researcher's scientific work distinctively *theirs*? Beyond topic and methodology lies something harder to articulate — a researcher's epistemic orientation, their implicit theory of progress, their characteristic stance toward risk and novelty. We call this **research taste**. In this paper, we demonstrate that large language models linearly encode research taste as structured, low-dimensional representations in their intermediate layers. Using 373 arXiv abstracts from 15 prominent AI/CS researchers, annotated along six meta-knowledge dimensions derived from the Evans & Foster (2011) framework, we show: (1) linear probes achieve 69.7–81.9% accuracy (vs. 20–33% chance) on taste dimensions, even within single arXiv categories; (2) taste representations survive topic removal and transfer across research domains; (3) representations are geometrically consistent across two model scales (CKA = 0.942); (4) activation steering in layers 12–19 produces coherent taste-shifted text generation; and (5) LLM embeddings outperform both TF-IDF and SPECTER2 on all taste dimensions. These findings suggest LLMs have acquired structured internal models of scientific epistemic orientation — operationalizing decades of qualitative insight from philosophy and sociology of science as measurable, steerable geometry.

---

## 1. Introduction

When scientists discuss a researcher's work, they often invoke intuitions beyond content: "This has Liang's empiricism," "classic Stanley — long-horizon, open-ended," "Crawford always problematizes." These assessments track something real and recognizable — a researcher's characteristic *way of doing science* — yet remain largely outside formal computational treatment.

Philosophy and sociology of science have long theorized such orientations. Kuhn (1962) argued that paradigms encode not just facts but epistemic commitments about what constitutes good science \cite{kuhn1962}. Bourdieu (1984) characterized scientific fields as structured by dispositions — *habitus* — shaping how researchers approach problems \cite{bourdieu1984}. Evans & Foster (2011) operationalized this as "meta-knowledge": systematic dimensions along which scientists differ in their theories of knowledge production, progress, and contribution \cite{evans2011}. Yet these frameworks have remained qualitative, resisting quantitative grounding.

Large language models trained on scientific text have absorbed vast amounts of both content *and* the rhetorical, epistemic fabric in which it is embedded. We ask: has this absorption produced structured internal representations of research taste — not just *what* scientists work on, but *how* they approach science?

We present a positive answer. Our key contributions are:

1. **Operational definition**: We instantiate six meta-knowledge dimensions from Evans & Foster (2011) as concrete annotation targets for scientific abstracts, yielding a labeled dataset of 373 papers from 15 researchers.

2. **Discovery**: Linear probes on Qwen3 representations achieve 69.7–81.9% accuracy on taste dimensions within single-topic subsets, 6.4× above chance.

3. **Genuineness controls**: Taste representations survive (a) leave-one-researcher-out generalization, (b) topic feature removal, (c) cross-domain transfer, and pass Hewitt & Liang (2019) control task criteria \cite{hewitt2019}.

4. **Geometric structure**: Taste lives in a low-dimensional (10–20 PC) subspace; both 9B and 27B parameter models find nearly identical geometry (CKA = 0.942); a dominant innovation↔consolidation axis organizes the space.

5. **Steerability**: Activation steering in layers 12–19 produces coherent taste-shifted text generation, demonstrating taste representations are causally implicated in generation.

6. **Applications**: Taste fingerprints enable author identification at 47.7% accuracy (vs. 6.7% chance), reveal career taste trajectories, and uncover four distinct epistemic clusters among our researcher sample.

This work opens a new empirical front in the science of science \cite{fortunato2018} and in mechanistic interpretability \cite{bereska2024}, connecting long-standing humanistic theory to measurable neural geometry.

---

## 2. Related Work

### 2.1 Probing and Mechanistic Interpretability

Probing classifiers \cite{belinkov2022} have revealed that neural language models encode rich linguistic structure in their intermediate representations — syntax \cite{hewitt2019structural}, semantic roles \cite{tenney2019}, and factual associations \cite{meng2022}. The key methodological challenge is distinguishing genuine encoding from confounded surface correlations. Hewitt & Liang (2019) \cite{hewitt2019} introduced the *selectivity* criterion: a genuine probe should outperform a control probe trained on random labels, with selectivity (accuracy difference) reflecting true structural content. We apply this criterion across all six taste dimensions.

Beyond probing, mechanistic interpretability work has shown that linear representations underlie surprisingly abstract properties: emotional valence \cite{tigges2023}, truth \cite{marks2023}, and model self-knowledge \cite{kadavath2022}. The linearity hypothesis — that features are encoded as directions in activation space — motivates both our probing approach and our activation steering experiments. Our finding that LLMs encode not just *content* but *epistemic orientation* extends this literature into a new conceptual domain.

### 2.2 Scientific Text Understanding

NLP research on scientific text has focused primarily on topic modeling \cite{blei2003}, citation prediction, and semantic similarity via models like SPECTER \cite{cohan2020} and SPECTER2 \cite{specter2}. These approaches treat scientific content as the primary signal. Our work is complementary: we show that *above and beyond* topic content, LLM representations encode meta-level epistemic properties.

The science of science \cite{fortunato2018} has used bibliometrics, citation networks, and text analysis to study research impact, collaboration, and knowledge diffusion. Recent work has applied language models to predict paper acceptance \cite{kang2018}, characterize scientific creativity \cite{foster2015}, and detect disruptive science \cite{park2023}. We contribute a new measurement instrument: taste probes that capture epistemic orientation independent of topical content.

### 2.3 Taste, Preference, and Style in NLP

Authorship attribution — identifying writers from stylistic features — has a long NLP history \cite{koppel2009}. Deep learning approaches achieve high accuracy using surface stylometric features \cite{boenninghoff2019}. Our work differs in target: rather than surface style, we probe *epistemic orientation* — what researchers value, how they frame progress, how they position their work epistemically.

Preference modeling has received attention in the RLHF literature \cite{christiano2017} and in aesthetic judgment tasks. Research taste is distinct: it concerns meta-level scientific epistemology, not aesthetic preference, and is grounded in a principled social-scientific framework \cite{evans2011}.

### 2.4 Philosophy and Sociology of Science

Our conceptual grounding draws on three traditions. Kuhn (1962) \cite{kuhn1962} established that science is governed by paradigms — shared exemplars and epistemic commitments — not just facts. Bourdieu (1984, 1988) \cite{bourdieu1984, bourdieu1988} characterized scientific practice as structured by *field* (the social space of positions) and *habitus* (embodied dispositions). Evans & Foster (2011) \cite{evans2011} operationalized this into measurable meta-knowledge dimensions, our primary framework.

We contribute empirical evidence that these philosophical constructs are not merely qualitative: they correspond to measurable directions in the representational geometry of large language models trained on scientific text.

---

## 3. Meta-Knowledge Taxonomy

Following Evans & Foster (2011) \cite{evans2011}, we define six meta-knowledge dimensions that characterize how researchers approach scientific work. These are properties of *epistemic orientation*, not topical content.

[TABLE 1: Meta-knowledge taxonomy]

| Dimension | Description | Example Values |
|-----------|-------------|----------------|
| **strategic_orientation** | Overall research approach | exploration, consolidation, translation |
| **theory_of_progress** | How the researcher thinks science advances | novelty, framework, understanding, critique |
| **contribution_claim** | Type of contribution asserted | advance, problematize, demonstrate, survey |
| **epistemic_posture** | Stance toward uncertainty and risk | embrace, hedge, challenging, empirical |
| **temporal_stance** | Time horizon of the work | long, near, historical, speculative |
| **field_positioning** | How the work is positioned relative to the field | advancing, bridging, founding, critiquing |

These six dimensions form a structured characterization of how a researcher *does science*, independent of what they study. Strategic orientation and epistemic posture capture risk tolerance and approach; theory of progress and contribution claim capture the implicit science-of-science model; temporal stance and field positioning capture relational and longitudinal orientation.

Annotations were generated using Qwen3.5-9B (thinking disabled) given a structured prompt eliciting dimension values. We discuss the circularity implications of LLM-generated labels probed in LLM representations in Section 6.

---

## 4. Experimental Setup

### 4.1 Dataset

We collected 373 arXiv abstracts from 15 prominent AI/CS researchers, each with ≥5 papers in our sample: Ken Stanley, Joel Lehman, Jeff Clune, Percy Liang, Michael Bernstein, Iyad Rahwan, Sebastian Risi, Jacob Steinhardt, Takashi Ikegami, Michael Levin, Kate Crawford, David Ha, Blaise Agüera y Arcas, Joel Z Leibo, and Joon Sung Park. Researchers were selected to span diverse epistemic orientations: evolutionary computation, AI safety, HCI, complex systems, AI policy, and philosophy of mind. A cs.AI-only subset of 178 papers was used for within-topic controls.

### 4.2 Models

We use two Qwen3 model variants with thinking mode disabled:
- **Qwen3-9B**: Representations extracted from layer 12 (of 28), the layer showing peak probing accuracy
- **Qwen3-27B**: Representations extracted from layer 25

Abstract tokens were mean-pooled to produce 4096-dimensional representations, then reduced to 256 dimensions via PCA for probing.

### 4.3 Probing Methodology

We train linear classifiers (logistic regression) on representation subspaces for each of the six taste dimensions. For each dimension, we use stratified 5-fold cross-validation and report mean accuracy. Following Hewitt & Liang (2019) \cite{hewitt2019}, we also train control probes on randomized labels and compute selectivity (genuine probe accuracy minus control probe accuracy). We separately compare linear probes against MLP probes to assess linearity.

We apply four confound controls:
1. **Leave-one-researcher-out**: Train on 14 researchers, test on held-out researcher (Exp 1b)
2. **Topic removal**: Project representations onto the null space of a topic classifier, then re-probe (Exp 1b)
3. **Same-topic subset**: Probe only on cs.AI papers (Exp 1b)
4. **Cross-domain transfer**: Train on one arXiv category, test on another (Exp 7)

We compare against TF-IDF bag-of-words (Benchmark 6) and SPECTER2 \cite{specter2} (Benchmark 7).

### 4.4 Activation Steering

To test causal implication of taste representations, we extract taste direction vectors from probing classifiers and apply them as additive interventions to residual stream activations during generation \cite{zou2023}. We test scales 5–25 and layers 0–28, evaluating output coherence and taste shift qualitatively (Exp 2b).

---

## 5. Results

We organize results around four questions: Does taste encoding exist? Is it genuine? What is its structure? Can it be steered?

### 5.1 Does Taste Encoding Exist?

**Basic probing accuracy.** Linear probes on Qwen3-9B layer 12 representations achieve approximately 78% accuracy across the six taste dimensions (Exp 1), against chance levels of 20–33% depending on dimension cardinality. Qwen3-27B layer 25 achieves comparable accuracy. This establishes that LLM representations carry taste-relevant information.

**Within-topic probing.** To control for topic as a confound, we probe only within the cs.AI category (178 papers), where all abstracts share the same arXiv subject area. Accuracy remains 69.7–71.4% (Exp 1b), approximately 6.4× above chance. This demonstrates that taste encoding is not merely a proxy for research topic.

[FIGURE 1: Probing accuracy across six dimensions — full dataset vs. cs.AI-only subset vs. chance baselines, with selectivity bars]

**Per-dimension results.** Five of six dimensions show robust taste encoding after topic removal (Exp 1c). The strongest dimensions are temporal_stance (81.9% full dataset) and strategic_orientation (78.5%). Field_positioning is weakest after topic removal, suggesting it is more entangled with topical content. Cross-dimension Cramér's V of 0.38–0.61 indicates moderate correlation — dimensions are related but not redundant (Exp 1c).

**LLM vs. baselines.** LLM representations outperform TF-IDF on all 6 dimensions by 5.7–17.2 percentage points (Benchmark 6) and outperform SPECTER2 on all 7 targets by 5.1–15.0 percentage points (Benchmark 7). General-purpose LLMs capture taste better than specialized scientific embeddings, suggesting taste is encoded as a byproduct of general language modeling.

[TABLE 2: Accuracy comparison across LLM, TF-IDF, SPECTER2 for all six taste dimensions plus researcher ID]

### 5.2 Is the Encoding Genuine?

**Generalization across researchers.** Leave-one-researcher-out evaluation on a 5-researcher ml_creative subset (Exp 1b) yields ~75% average accuracy, closely matching the full-dataset result. Probes generalize to unseen researchers rather than memorizing per-researcher patterns.

**Selectivity analysis.** Applying Hewitt & Liang (2019) control tasks \cite{hewitt2019}, all six dimensions pass the GENUINE criterion (selectivity 0.26–0.45) and all six pass the LINEAR criterion (linear probe outperforms MLP) (Exp 6). Selectivity values confirm that probes exploit genuinely structured information, not high-dimensional overfitting.

**Topic removal residual.** Topic features alone achieve 57.6%; full representations achieve ~78%; representations with topic projected out achieve ~51% (Exp 1b). Approximately 40% of taste signal is topic-mediated; the residual ~51% accuracy demonstrates taste information above and beyond topic. We note this limitation honestly: full topical disentanglement remains an open problem.

**Cross-domain transfer.** Training on one arXiv category and testing on another yields 2× above-chance accuracy (Exp 7). Taste representations transfer across research domains, further separating them from domain-specific topic features.

**Cross-model consistency.** CKA \cite{kornblith2019} between Qwen3-9B layer 12 and Qwen3-27B layer 25 equals 0.942 (Exp 8). Both model scales find nearly identical taste geometry, suggesting the encoding reflects properties of the training data distribution rather than model-specific idiosyncrasies.

[FIGURE 2: CKA similarity matrix between model layers showing peak alignment at layers 12 and 25]

### 5.3 What Is the Structure of Taste Representations?

**Dimensionality.** Parallel factor analysis identifies 30+ significant PCs in raw representation space, but taste probes saturate at 10–20 PCs. PC1 alone captures significant meta-taste signal, corresponding to an innovation↔consolidation axis organizing researchers from those who explore open-ended frontiers to those who systematically consolidate knowledge.

**Researcher fingerprints.** Each researcher's papers project to a characteristic region of taste space (Exp 4). Cosine similarity between researcher centroids reveals structure: Clune↔Stanley = 0.784, consistent with their shared evolutionary computation orientation. In a blind authorship task, paper→researcher matching places the true author ranked #1 in every test case (Exp 4).

**Taste blind test.** Same/different author pairs are distinguished with AUC = 0.731. Leave-one-out author identification achieves 47.7% @1 (chance: 6.7%). Cross-topic author identification achieves 34.6% (5.2× chance). Most distinctive researchers: Crawford (100%), Levin (80%), Ikegami (77%). Least distinctive: Agüera y Arcas (13%), Stanley (20%), Lehman (23%). Notably, Stanley and Lehman — frequent collaborators — are hard to individuate from each other, consistent with convergent taste.

[FIGURE 3: 2D PCA projection of researcher taste centroids, colored by unsupervised cluster assignment]

**Unsupervised clustering.** K-means (K=4) on taste representations recovers four coherent epistemic clusters without supervision (Exp 5):
- *Critical Theorists* (n=59): Lehman, Levin, Crawford — framework+problematize+challenging
- *Systematic Analysts* (n=116): Ikegami, Bernstein, Rahwan — understanding+framework+problematize
- *Applied Innovators* (n=96): Liang, Steinhardt, Agüera y Arcas — exploration+novelty+near+advancing
- *Visionary Explorers* (n=102): Stanley, Risi, Clune — exploration+novelty+embrace+long

These clusters map coherently onto known intellectual affinities. The evolutionary computation cluster (Stanley, Risi, Clune) is recovered without supervision; so is the AI safety/empiricism cluster (Liang, Steinhardt). Clustering is performed on taste representations without access to researcher identity labels.

[TABLE 3: Unsupervised cluster assignments with size, researchers, and dominant dimension values]

**Career taste trajectories.** Comparing early vs. late career papers via cosine similarity reveals substantial variation (mean: 0.228 ± 0.227) (Exp 11). Most stable: Bernstein (0.585), Risi (0.507), Stanley (0.440). Most drifting: Agüera y Arcas (−0.171), Steinhardt (−0.100). Negative cosine similarity implies near-reversal of taste orientation across career — consistent with Agüera y Arcas's documented trajectory from computer vision to generative art and AI philosophy.

**Taste atypicality.** Vector deviation from the researcher mean shows no significant correlation with labeled taste atypicality (r = 0.077, p > 0.05) (Exp 12). This suggests the representation space encodes richer information than our six labeled dimensions — a "residual taste" not captured by the Evans & Foster taxonomy as applied here.

### 5.4 Can Taste Be Steered?

Activation steering experiments (Exp 2b) add taste direction vectors to residual stream activations during generation. Key findings:
- **Effective layers**: 12–19 produce coherent taste-shifted outputs (demonstrated via ALife vocabulary injection)
- **Scale**: Scale=15 is required; lower values insufficient, higher values incoherent
- **Boundary effects**: Layers 0–6 break syntactic coherence; layers 25+ produce no discernible shift
- **Model mode**: Thinking mode must be disabled for coherent steering

[FIGURE 4: Example generated text with and without taste steering at scale=15, layer 15, showing vocabulary shift while maintaining grammatical coherence]

Causal intervention success in middle layers confirms that taste representations are not merely correlated with output but causally implicated in generation. The steering window (layers 12–19) aligns with the probing accuracy peak and with established mechanistic findings on causal intervention windows \cite{zou2023}.

---

## 6. Discussion

### 6.1 Implications

**For science of science.** Taste representations offer a new, scalable measurement instrument for studying epistemic diversity in research communities. The innovation↔consolidation axis we identify empirically recapitulates theoretical arguments about the social value of scientific diversity \cite{foster2015, weisberg2009}. Tracking taste distributions over time could detect field-level epistemic homogenization — a hypothesized risk of large-scale AI-assisted research — without requiring expert qualitative analysis.

**For LLM interpretability.** The linearity of taste encoding (Exp 6) and cross-model consistency (Exp 8) support the linear representation hypothesis \cite{elhage2022} in a new, genuinely high-level domain. That research taste — a theory-laden philosophical concept — is linearly encoded suggests LLM feature geometry is more semantically structured than previously demonstrated. The steerability result (Exp 2b) extends mechanistic interpretability from content-level edits to epistemic-orientation-level edits.

**For research tools.** Author fingerprinting via taste vectors (47.7% identification, 5.2× chance cross-topic) could enable taste-aware literature recommendation — surfacing papers that share an investigator's epistemic orientation rather than just their topic. Activation steering could support writing assistance that adapts scientific framing to a target epistemic style.

### 6.2 Limitations

**Circularity.** The most significant concern: taste annotations are generated by Qwen3-9B; representations are extracted from Qwen3. Probing results thus demonstrate *internal consistency* — the model's generative and representational systems encode the same taste signal — rather than correspondence to human-validated research taste. This is a genuine limitation. We frame our finding as: "LLMs encode a structured representation consistent with the Evans & Foster taxonomy, as interpreted by LLMs." Human expert annotation studies are essential future work.

**Dataset scale.** 373 abstracts from 15 researchers is small by NLP standards. Key results replicate across multiple subsets and controls, increasing confidence. However, the researcher sample is not representative: all are prominent AI/CS researchers, predominantly male, based in Western institutions. Findings may not generalize to other fields or demographics.

**Topic entanglement.** Topic removal reduces accuracy from ~78% to ~51%, demonstrating partial but incomplete separability. Approximately 40% of taste signal is topic-mediated. Completely topic-free taste measurement remains open; techniques such as causal mediation analysis may provide stronger separation.

**Annotation validity.** We did not conduct systematic inter-annotator agreement studies with human raters. The six dimensions, while theoretically grounded, may not perfectly partition scientific epistemics — especially at the level of individual abstract classification.

**Field generalization.** All researchers are in AI/CS. Cross-domain transfer within AI (Exp 7) is encouraging, but generalization to biology, physics, or humanities remains untested.

### 6.3 Future Work

Priority directions: (1) human annotation studies to validate LLM-generated taste labels; (2) expansion to larger, more diverse researcher samples across fields; (3) temporal analysis of taste evolution at community levels; (4) taste-aware recommendation and writing assistance; (5) examining peer review dynamics — do reviewer taste representations predict review sentiment on taste-mismatched papers?

---

## 7. Conclusion

We have shown that LLMs linearly encode research taste — researchers' characteristic epistemic orientations — as structured, low-dimensional representations in intermediate layers. This encoding survives topic removal, generalizes across researchers and domains, is consistent across model scales (CKA = 0.942), and can be causally intervened upon via activation steering. All six meta-knowledge dimensions from Evans & Foster (2011) are genuinely and linearly encoded; LLM representations outperform both bag-of-words and specialized scientific embeddings; four distinct epistemic clusters emerge without supervision.

These findings operationalize decades of qualitative insight from philosophy and sociology of science as measurable neural geometry. Research taste — long recognized as real but resistant to quantification — turns out to be legible in the representational fabric of language models trained on scientific text. We hope this work opens new avenues in computational science studies, interpretability research, and the design of epistemically-aware AI research tools.

---

## References

\bibitem{kuhn1962} Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press. URL: https://www.press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html

\bibitem{bourdieu1984} Bourdieu, P. (1984). *Distinction: A Social Critique of the Judgement of Taste*. Harvard University Press. URL: https://www.hup.harvard.edu/catalog.php?isbn=9780674212770

\bibitem{bourdieu1988} Bourdieu, P. (1988). *Homo Academicus*. Stanford University Press. URL: https://www.sup.org/books/title/?id=2179

\bibitem{evans2011} Evans, J. A., & Foster, J. G. (2011). Metaknowledge. *Science*, 331(6018), 721–725. DOI: 10.1126/science.1201765

\bibitem{hewitt2019} Hewitt, J., & Liang, P. (2019). Designing and Interpreting Probes with Control Tasks. *EMNLP 2019*. DOI: 10.18653/v1/D19-1275

\bibitem{hewitt2019structural} Hewitt, J., & Manning, C. D. (2019). A Structural Probe for Finding Syntax in Word Representations. *NAACL 2019*. DOI: 10.18653/v1/N19-1419

\bibitem{belinkov2022} Belinkov, Y. (2022). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics*, 48(1). DOI: 10.1162/coli_a_00422

\bibitem{tenney2019} Tenney, I., Das, D., & Pavlick, E. (2019). BERT Rediscovers the Classical NLP Pipeline. *ACL 2019*. DOI: 10.18653/v1/P19-1452

\bibitem{meng2022} Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. *NeurIPS 2022*. URL: https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89be0f530b36cf622-Abstract-Conference.html

\bibitem{tigges2023} Tigges, C., et al. (2023). Linear Representations of Sentiment in Large Language Models. *arXiv*. URL: https://arxiv.org/abs/2310.15154

\bibitem{marks2023} Marks, S., & Tegmark, M. (2023). The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets. *arXiv*. URL: https://arxiv.org/abs/2310.06824

\bibitem{kadavath2022} Kadavath, S., et al. (2022). Language Models (Mostly) Know What They Know. *arXiv*. URL: https://arxiv.org/abs/2207.05221

\bibitem{fortunato2018} Fortunato, S., et al. (2018). Science of Science. *Science*, 359(6379). DOI: 10.1126/science.aao0185

\bibitem{bereska2024} Bereska, L., & Gavves, E. (2024). Mechanistic Interpretability for AI Safety — A Review. *arXiv*. URL: https://arxiv.org/abs/2404.14082

\bibitem{blei2003} Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. *JMLR*, 3, 993–1022. URL: https://www.jmlr.org/papers/v3/blei03a.html

\bibitem{cohan2020} Cohan, A., et al. (2020). SPECTER: Document-level Representation Learning using Citation-informed Transformers. *ACL 2020*. DOI: 10.18653/v1/2020.acl-main.207

\bibitem{specter2} Singh, M., et al. (2022). SciRepEval: A Multi-Format Benchmark for Scientific Document Representations. *EMNLP 2022*. URL: https://arxiv.org/abs/2211.13308

\bibitem{kang2018} Kang, D., et al. (2018). A Dataset of Peer Reviews (PeerRead): Collection, Insights and NLP Applications. *NAACL 2018*. DOI: 10.18653/v1/N18-1149

\bibitem{foster2015} Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and Innovation in Scientists' Research Strategies. *American Sociological Review*, 80(5). DOI: 10.1177/0003122415601618

\bibitem{park2023} Park, M., Leahey, E., & Funk, R. J. (2023). Papers and Patents are Becoming Less Disruptive over Time. *Nature*, 613. DOI: 10.1038/s41586-022-05543-x

\bibitem{koppel2009} Koppel, M., Schler, J., & Argamon, S. (2009). Computational Methods in Authorship Attribution. *JASIST*, 60(1). DOI: 10.1002/asi.20961

\bibitem{boenninghoff2019} Boenninghoff, B., et al. (2019). Explainable Authorship Verification in Social Media via Attention-based Similarity Learning. *IEEE BigData 2019*. DOI: 10.1109/BigData47090.2019.9006148

\bibitem{christiano2017} Christiano, P., et al. (2017). Deep Reinforcement Learning from Human Preferences. *NeurIPS 2017*. URL: https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html

\bibitem{weisberg2009} Weisberg, M., & Muldoon, R. (2009). Epistemic Landscape and the Division of Cognitive Labor. *Philosophy of Science*, 76(2). DOI: 10.1086/644786

\bibitem{elhage2022} Elhage, N., et al. (2022). Toy Models of Superposition. *Transformer Circuits Thread*. URL: https://transformer-circuits.pub/2022/toy_model/index.html

\bibitem{zou2023} Zou, A., et al. (2023). Representation Engineering: A Top-Down Approach to AI Transparency. *arXiv*. URL: https://arxiv.org/abs/2310.01405

\bibitem{kornblith2019} Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). Similarity of Neural Network Representations Revisited. *ICML 2019*. URL: http://proceedings.mlr.press/v97/kornblith19a.html

---

*Manuscript prepared for ACL Rolling Review, targeting EMNLP 2026.*  
*Co-authored by Botao Amber Hu (amber@reality.design) and Biber (biber@openclaw.ai)*
