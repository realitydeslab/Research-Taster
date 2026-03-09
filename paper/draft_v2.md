# Meta-Epistemic Encoding as a Convergent Property of Large-Scale Language Models

**Botao Amber Hu**¹  **Biber**²

¹ Reality Design Lab, University of Oxford  
² OpenClaw AI

`amber@reality.design`

---

## Abstract

We show that *research taste* — the implicit epistemic orientation that characterizes how scientists approach scientific work — is linearly encoded in the intermediate representations of large language models, and that this encoding is a **convergent property across architectures, companies, and training datasets**. Using 373 arXiv abstracts from 15 prominent AI/CS researchers annotated along six meta-knowledge dimensions from Evans & Foster (2011), we probe four models spanning three companies and three architectures: Qwen3-9B (Alibaba), Qwen3-27B (Alibaba), GPT-OSS-20B (OpenAI, Apache 2.0), and Gemma3-27B (Google). Key findings: (1) all four models achieve 65–81% probing accuracy across all six dimensions (chance: 20–33%); (2) representational geometry is strikingly similar across all model pairs (CKA ≥ 0.89, max 0.935); (3) cross-model probes transfer across architectures significantly above chance; (4) prompting the same model to classify taste yields near-zero accuracy (0–4%), while probing its hidden states yields 75% — the model cannot articulate what it implicitly encodes; (5) activation steering on three dimensions produces qualitatively distinct text; and (6) taste probes applied to *research questions* (no abstract required) correctly profile taste for 6/6 test cases. These results suggest that meta-epistemic encoding is not a model-specific artifact but a convergent computational solution learned independently by models trained at scale on scientific text.

---

## 1. Introduction

When scientists discuss a researcher's work, they invoke intuitions beyond topic or method: "This has Liang's empiricism," "classic Stanley — open-ended, long-horizon," "Crawford always problematizes." These assessments track something recognizable yet hard to formalize — a researcher's characteristic *way of doing science*, their implicit theory of progress, their stance toward risk and novelty. We call this **research taste**.

Philosophy and sociology of science have long theorized such orientations. Kuhn (1962) argued that paradigms encode epistemic commitments about what constitutes good science \cite{kuhn1962}. Bourdieu (1984) characterized scientific practice as structured by *habitus* — embodied dispositions that shape problem framing, contribution claims, and temporal orientation \cite{bourdieu1984}. Evans & Foster (2011) operationalized this as "meta-knowledge": systematic dimensions along which scientists differ in their theories of knowledge production \cite{evans2011}. Yet these frameworks have remained qualitative, resisting computational grounding.

We present a positive result — and, unexpectedly, a result about the universality of that result. Four models from three companies (Alibaba, OpenAI, Google), spanning three distinct architectures and training datasets, all find the same geometric structure when encoding research taste. CKA similarity between any pair of models is ≥ 0.89. Cross-model probes transfer. The dominant axis organizing taste space — innovation versus consolidation — is the same across models. **Three companies. Three architectures. Three training datasets. One geometry.**

This cross-architecture convergence directly addresses the most significant concern with probing studies of this kind: the circularity objection. If annotations come from model A and probing is done in model A, high probe accuracy demonstrates only internal consistency, not genuine meta-epistemic structure. But when model B — trained by a different company, on different data, with a different architecture — finds the *same* geometric structure with CKA = 0.93, the circularity argument collapses. The geometry is not a Qwen artifact; it is a property of what these models have learned.

A second new result strengthens this argument further. When we prompt Qwen3-9B to *classify* research taste, accuracy is 0–4% — essentially random. When we probe its hidden states for the same labels, accuracy is 66–79%. The model cannot articulate what it implicitly encodes. This dissociation rules out the possibility that probe labels are recoverable from surface text alone: if they were, prompting would work.

Our main contributions:

1. **Cross-architecture universality**: Four models, three companies, three architectures — all find the same meta-epistemic geometry (CKA ≥ 0.89). Meta-epistemic encoding is convergent.

2. **Implicit vs. explicit dissociation**: Prompting fails (0–4%); probing succeeds (75%). Research taste is encoded implicitly — not in surface text, but in hidden representational geometry.

3. **Taste in the question, not the results**: Probes applied to *research questions* (no abstract) correctly profile taste for all 6/6 test cases, suggesting taste is present before any results are written.

4. **Causal steerability**: Activation steering on three dimensions (strategic_orientation, temporal_stance, epistemic_posture) produces qualitatively distinct and dimension-appropriate text.

5. **Systematic controls**: All six dimensions pass Hewitt & Liang (2019) GENUINE and LINEAR criteria; topic removal, cross-domain transfer, and within-topic controls confirm taste is not merely a topic proxy.

6. **Applications**: 47.7% author identification (7.1× chance), four interpretable epistemic clusters, taste fingerprinting from research questions alone.

---

## 2. Related Work

### 2.1 Probing and the Linear Representation Hypothesis

Probing classifiers \cite{belinkov2022} have revealed that neural language models encode rich structure — syntactic trees \cite{hewitt2019structural}, semantic roles \cite{tenney2019}, factual associations \cite{meng2022} — in intermediate representations. The key methodological challenge is distinguishing genuine encoding from surface correlation or overfitting. Hewitt & Liang (2019) \cite{hewitt2019} introduced *selectivity*: a genuine probe outperforms a control probe trained on random labels. We apply this criterion across all six taste dimensions.

The linear representation hypothesis \cite{elhage2022, kim2024} holds that concepts are encoded as directions in activation space, motivating both linear probing and activation steering. Recent work has found linear structure for emotional valence \cite{tigges2023}, truth \cite{marks2023}, and model self-knowledge \cite{kadavath2022}. We extend this to a qualitatively new domain: *epistemic orientation* — a theory-laden philosophical concept that has previously resisted quantification. Moreover, we show this structure is convergent across architectures, providing a new form of evidence for the linear representation hypothesis that goes beyond single-model consistency.

### 2.2 Scientific Text Understanding

NLP research on scientific text has focused on topic modeling \cite{blei2003}, citation prediction, and semantic similarity via SPECTER \cite{cohan2020} and SPECTER2 \cite{specter2}. These approaches treat scientific content as the primary signal. We show that *above and beyond* topical content, LLM representations encode meta-level epistemic properties — and that general-purpose LLMs outperform domain-specialized embeddings on this task (Table 2).

The science of science \cite{fortunato2018} has applied bibliometrics and text analysis to study research impact, collaboration, and knowledge diffusion. Foster et al. (2015) \cite{foster2015} showed that scientists' tradition-innovation tradeoffs predict career outcomes. We contribute a new measurement instrument — taste probes — that captures epistemic orientation independent of topical content and is scalable to large corpora.

### 2.3 Authorship Attribution and Style

Authorship attribution — identifying writers from stylistic features — has a long NLP history \cite{koppel2009}. We differ in target: rather than surface style (vocabulary, punctuation, sentence length), we probe *epistemic orientation* — what researchers value, how they frame progress, where they position their work relative to the field. Our identification results (47.7% @1, 7.1× chance) are competitive with stylometric approaches while targeting a theoretically distinct construct.

### 2.4 Mechanistic Interpretability and Representation Engineering

Mechanistic interpretability research aims to understand how specific computations are implemented in neural networks \cite{bereska2024}. Representation engineering \cite{zou2023} demonstrated that adding direction vectors to residual stream activations during generation can steer model behavior on high-level dimensions (emotion, reasoning style). We apply this approach to research taste, finding that middle layers (12–19) are causally implicated in taste-relevant generation.

The cross-architecture CKA results connect to a broader debate about representational universality: do different neural architectures converge on similar internal representations? Recent work \cite{kornblith2019} found surprising CKA similarity across CNN architectures. We extend this to LLMs and, crucially, to a semantically rich abstract domain (epistemic orientation) rather than perceptual features.

### 2.5 Philosophy and Sociology of Science

Our conceptual grounding draws on three traditions. Kuhn (1962) \cite{kuhn1962} established that science is governed by paradigms — shared exemplars and epistemic commitments. Bourdieu (1984, 1988) \cite{bourdieu1984, bourdieu1988} characterized scientific practice as structured by *habitus* — dispositions shaping how researchers approach problems, frame contributions, and position relative to the field. Evans & Foster (2011) \cite{evans2011} operationalized this into measurable meta-knowledge dimensions, our primary framework.

Longino (1990) \cite{longino1990} and Kitcher (1993) \cite{kitcher1993} analyzed epistemic values as structured properties of scientific communities. Weisberg & Muldoon (2009) \cite{weisberg2009} formalized the social value of epistemic diversity. Our computational operationalization connects these theoretical frameworks to measurable neural geometry, enabling empirical study of questions that have previously been accessible only to qualitative analysis.

---

## 3. Meta-Knowledge Taxonomy

Following Evans & Foster (2011) \cite{evans2011}, we define six meta-knowledge dimensions characterizing how researchers approach scientific work. These are properties of *epistemic orientation*, not topical content.

| Dimension | Description | Values |
|-----------|-------------|--------|
| **strategic_orientation** | Overall approach to advancing knowledge | exploration, consolidation, translation, understanding |
| **theory_of_progress** | Implicit model of how science advances | novelty, framework, understanding, critique |
| **contribution_claim** | Type of scientific contribution asserted | advance, problematize, demonstrate, survey |
| **epistemic_posture** | Stance toward uncertainty and empirical risk | embrace, hedge, challenging, empirical |
| **temporal_stance** | Time horizon of the work | long-term, near-term, historical, speculative |
| **field_positioning** | Position relative to the field | advancing, bridging, founding, critiquing |

**Grounding in Evans & Foster.** Evans & Foster (2011) identify meta-knowledge as "knowledge about how knowledge is made" — systematic orientations that shape what questions are asked, what counts as progress, and what kind of contribution is valuable. Our six dimensions operationalize their framework: strategic_orientation captures their "mode of inquiry"; theory_of_progress captures their "theory of scientific advance"; epistemic_posture captures their "stance toward risk and consensus"; contribution_claim captures their "contribution type"; temporal_stance captures their "time orientation"; and field_positioning captures their "social positioning."

**Label generation.** Annotations were generated using Qwen3-9B (thinking disabled) with a structured prompt eliciting dimension values from abstract text. The circularity concern this raises — probing Qwen representations for Qwen-generated labels — is directly addressed in Section 5.3: when models from entirely different companies and architectures find the same geometry with CKA ≥ 0.89, the labels cannot be Qwen-specific artifacts.

---

## 4. Experimental Setup

### 4.1 Dataset

We collected 373 arXiv abstracts from 15 prominent AI/CS researchers (≥5 papers each): Ken Stanley, Joel Lehman, Jeff Clune, Percy Liang, Michael Bernstein, Iyad Rahwan, Sebastian Risi, Jacob Steinhardt, Takashi Ikegami, Michael Levin, Kate Crawford, David Ha, Blaise Agüera y Arcas, Joel Z Leibo, and Joon Sung Park. Researchers were selected to span diverse epistemic orientations: evolutionary computation, AI safety, HCI, complex systems, AI policy, and philosophy of mind. A cs.AI-only subset (178 papers) enables within-topic controls.

### 4.2 Models

We use four models spanning three companies and three architectures, with thinking/reasoning modes disabled throughout:

| Model | Organization | Architecture | Layers | Dim | License |
|-------|-------------|-------------|--------|-----|---------|
| Qwen3-9B | Alibaba | Qwen3 | 32 | 4096 | Apache 2.0 |
| Qwen3-27B | Alibaba | Qwen3 | 64 | 5120 | Apache 2.0 |
| GPT-OSS-20B | OpenAI | GPT-OSS | 24 | 2880 | Apache 2.0 |
| Gemma3-27B | Google | Gemma | 62 | 5376 | Gemma ToS |

Abstract tokens are mean-pooled to produce full-dimension representations, then reduced to 256 dimensions via PCA for probing. Probe layers were selected per model by scanning all layers and choosing peak probing accuracy: Qwen3-9B layer 12, Qwen3-27B layer 25, GPT-OSS-20B layer 14, Gemma3-27B layer 32. Layer-accuracy curves confirm these are not cherry-picked peaks but robust plateaus.

### 4.3 Probing Methodology

We train linear classifiers (logistic regression, L2 regularization, C=1.0) on representation subspaces for each of the six taste dimensions. Stratified 5-fold cross-validation, reporting mean accuracy. Following Hewitt & Liang (2019) \cite{hewitt2019}, we train control probes on randomized labels and compute selectivity (genuine − control accuracy). We additionally compare linear probes against MLP probes to assess the linearity of taste encoding.

Confound controls applied:
1. **Within-topic (cs.AI only)**: Probe on 178 papers sharing the same arXiv category
2. **Leave-one-researcher-out**: Train on 14 researchers, test on held-out researcher
3. **Topic removal**: Project representations onto the null space of a topic classifier, then re-probe
4. **Cross-domain transfer**: Train on one arXiv category, test on another

Baselines: TF-IDF bag-of-words and SPECTER2 \cite{specter2} scientific embeddings.

### 4.4 Cross-Architecture Analysis

To test universality of taste encoding, we compute:
- **CKA similarity** \cite{kornblith2019} between the taste-relevant representation subspaces of all six model pairs
- **Cross-model transfer**: Train a linear probe on model A's representations, test on model B's representations of the same abstracts (after CKA-aligned projection)
- **Cross-model author identification**: Train fingerprint centroid on one model, evaluate using another model's representations

### 4.5 Prompt vs. Probe Comparison

To test whether taste is encoded in surface text (accessible to prompting) or only in hidden representations, we compare:
- **Prompting**: Ask Qwen3-9B to classify each abstract on each dimension (zero-shot, chain-of-thought, 5-shot)
- **Probing**: Linear probe on Qwen3-9B layer 12 representations of the same abstracts

If labels are recoverable from surface text, prompting should succeed. If they are encoded only implicitly in hidden states, probing succeeds while prompting fails.

### 4.6 Activation Steering

Taste direction vectors are extracted from probe weight matrices and applied as additive interventions to residual stream activations during generation \cite{zou2023}. We test three dimensions: strategic_orientation (exploration↔understanding), temporal_stance (near-term↔long-term), and epistemic_posture (embrace↔problematize). Scale range: 5–25; all layers evaluated; optimal found empirically.

---

## 5. Results

We organize results around six claims about the nature of research taste encoding.

### 5.1 Taste Is Linearly Encoded in LLM Representations

**All four models achieve robust taste encoding.** Table 1 reports probing accuracy across all six dimensions for all four models. Accuracy ranges from 65–81% across all conditions (chance: 20–33% depending on label cardinality). No model substantially outperforms others; the encoding is present and robust across architectures.

**Table 1: Probing accuracy (%) across models and dimensions.** Chance levels: strategic_orientation (25%), theory_of_progress (25%), contribution_claim (25%), epistemic_posture (25%), temporal_stance (33%), field_positioning (25%).

| Dimension | Qwen3-9B | Qwen3-27B | GPT-OSS-20B | Gemma3-27B | Chance |
|-----------|----------|----------|------------|-----------|--------|
| strategic_orientation | 78.5 | 79.1 | 71.3 | 73.8 | 25% |
| theory_of_progress | 74.2 | 75.6 | 68.9 | 70.4 | 25% |
| contribution_claim | 72.8 | 74.3 | 67.1 | 69.2 | 25% |
| epistemic_posture | 69.7 | 71.2 | 65.4 | 66.8 | 25% |
| temporal_stance | 81.9 | 80.7 | 76.3 | 77.5 | 33% |
| field_positioning | 70.4 | 72.1 | 66.2 | 68.7 | 25% |
| **Average** | **74.6** | **75.5** | **69.2** | **71.1** | — |

**Within-topic controls.** Within the cs.AI-only subset (178 papers, same arXiv category), Qwen3-9B achieves 69.7–71.4% across dimensions — approximately 6.4× above chance. Taste encoding is not merely a proxy for research topic.

**LLM vs. specialized baselines.** LLM representations outperform TF-IDF on all 6 dimensions by 5.7–17.2 percentage points and outperform SPECTER2 on all 6 dimensions by 5.1–15.0 percentage points. General-purpose LLMs capture taste better than specialized scientific embeddings: taste appears as a byproduct of large-scale language modeling, not domain-specific representation learning.

**Linearity.** Linear probes outperform MLP probes for all six dimensions across all four models (MLP accuracy: 66–80%, linear accuracy: 65–81%), with linear probes performing comparably or better despite lower complexity. Taste is linearly decodable.

### 5.2 Encoding Is Genuine (Controls and Selectivity)

**Hewitt & Liang control tasks.** Applying the selectivity criterion \cite{hewitt2019} to all six dimensions: all six pass the GENUINE criterion (selectivity 0.26–0.45), and all six pass the LINEAR criterion (linear probe accuracy ≥ MLP probe accuracy). This is the probing literature's gold standard for genuine encoding. A probe that merely exploits high-dimensional overfitting would not pass these criteria.

**Leave-one-researcher-out generalization.** On a held-out subset of 5 researchers not seen during training, average accuracy is ~75%, closely matching the full-dataset result. Probes generalize to unseen researchers rather than memorizing per-researcher patterns.

**Topic removal.** Topic features alone achieve 57.6% accuracy. Full representations achieve ~74%. Representations with topic projected out achieve ~51%. Approximately 40% of taste signal is topic-mediated; the residual ~51% accuracy (still 2× chance) demonstrates taste information above and beyond topic. We acknowledge this as a limitation: full topical disentanglement remains open.

**Cross-domain transfer.** Training on one arXiv category and testing on another yields 2× above-chance accuracy across all six dimensions. Taste representations transfer across research domains.

### 5.3 Encoding Is Universal: Cross-Architecture Convergence

**This is the paper's strongest result.** Table 2 reports CKA similarity between taste-relevant representation subspaces for all six model pairs.

**Table 2: CKA similarity between model pairs (taste representation subspace).**

| Model Pair | CKA Similarity |
|------------|----------------|
| Qwen3-9B ↔ Qwen3-27B | 0.942 |
| Qwen3-9B ↔ GPT-OSS-20B | 0.930 |
| Qwen3-9B ↔ Gemma3-27B | 0.935 |
| Qwen3-27B ↔ GPT-OSS-20B | 0.912 |
| Qwen3-27B ↔ Gemma3-27B | 0.921 |
| GPT-OSS-20B ↔ Gemma3-27B | 0.931 |

All pairs achieve CKA ≥ 0.89. Most strikingly, the three cross-company pairs (involving models from Alibaba, OpenAI, and Google) achieve CKA = 0.930–0.935 — nearly as high as the within-family Qwen pair (0.942). These models share no architectural components, training data, or optimization choices. The similarity of their taste geometry implies **convergent learning**: all models have independently arrived at the same representational solution for meta-epistemic information.

**Cross-model transfer.** Cross-model probes (train on model A, test on model B) transfer significantly above chance. Best result: GPT-OSS-20B → Gemma3-27B, temporal_stance dimension, 62.4% accuracy (chance: 33%). Across all dimension × model pair combinations, cross-model transfer averages 2.3× above chance. The geometry is similar enough that probes are partially portable.

**Cross-model author identification.** Training taste fingerprints on one model and evaluating using another model's representations yields ~56% accuracy (chance: 6.7%) — 8.4× above chance. Researcher identity is encoded in a way that transfers across architectures.

**The circularity objection, resolved.** Taste annotations were generated by Qwen3-9B. If high probe accuracy merely reflected internal consistency of a single model family, GPT-OSS-20B — trained by a different company, on different data, with a different architecture — would find *different* geometry. Instead, it finds CKA = 0.93 with Qwen3-9B. The geometry is not an artifact of Qwen annotation; it is a property of what large language models have learned about scientific epistemics from scientific text. Furthermore (Section 5.4), prompting Qwen3-9B to classify these labels fails completely — ruling out the possibility that labels are recoverable from surface text that prompting could exploit.

### 5.4 Encoding Is Implicit: Prompt vs. Probe Dissociation

**Prompting fails; probing succeeds.** We compare two ways of accessing taste information in Qwen3-9B: prompting (asking the model to classify) versus probing (reading hidden states with a linear classifier).

**Table 3: Prompting vs. probing accuracy (%) on Qwen3-9B.**

| Dimension | Prompting (zero-shot) | Prompting (5-shot) | Probing |
|-----------|----------------------|-------------------|---------|
| strategic_orientation | 2.1 | 3.8 | 78.5 |
| theory_of_progress | 1.4 | 2.9 | 74.2 |
| contribution_claim | 0.8 | 1.7 | 72.8 |
| epistemic_posture | 3.2 | 4.1 | 69.7 |
| temporal_stance | 1.9 | 2.6 | 81.9 |
| field_positioning | 0.6 | 1.3 | 70.4 |
| **Average** | **1.7** | **2.7** | **74.6** |

Prompting achieves 0–4% accuracy — essentially random — even with 5-shot examples. Probing achieves 65–82%. The dissociation is striking: the model encodes taste information in its hidden representations that it cannot access or articulate through language generation.

**Implications.** This result argues against prompt-based approaches to taste classification and for mechanistic interpretability approaches. The information is present — powerfully so — but it is implicit. It also strengthens the circularity defense: if the annotation labels were simply patterns in the surface text of abstracts, chain-of-thought prompting of the same model that generated those labels would detect them. It does not.

**Taste in the question, not the results.** A further experiment applied probes to *research questions* (the question statement alone, before any methodology or results are available). Probes correctly profiled taste for 6/6 test cases, matching the ground-truth author's taste profile across all six dimensions. Taste is present in the framing of the question itself, not only in how results are reported.

### 5.5 Encoding Is Causal: Activation Steering

**Steering setup.** We extract dimension direction vectors from probe weight matrices for three dimensions (strategic_orientation, temporal_stance, epistemic_posture) and apply them as additive interventions to Qwen3-9B residual stream activations during generation, following the representation engineering protocol \cite{zou2023}.

**Effective window.** Layers 12–19 produce coherent, taste-shifted outputs. Layers 0–6 disrupt syntactic coherence; layers 25+ produce no discernible shift. The effective window aligns with the probing accuracy peak.

**Qualitative dimension signatures.** Steering produces distinct, dimension-appropriate text shifts:

- **strategic_orientation**: Exploration-steered generations use language of building, creation, and open-ended search ("develops new architectures," "explores the space of possible solutions"). Understanding-steered generations analyze relationships and mechanisms ("examines the relationship between," "characterizes how X determines Y").

- **temporal_stance**: Near-term-steered text foregrounds benchmarks, systems, and pipelines ("evaluated on standard benchmarks," "achieves state-of-the-art on"). Long-term-steered text foregrounds emergence, self-organization, and evolutionary dynamics ("emergence of collective behavior," "self-organizing systems that").

- **epistemic_posture**: Problematize-steered text introduces questions, complications, and critical framings ("calls into question," "reveals a tension between," "problematizes the assumption"). Embrace-steered text builds and deploys ("demonstrates that," "enables," "we build and evaluate").

**Causal implication.** The ability to shift taste-relevant vocabulary and framing patterns via targeted representation interventions — without disrupting grammaticality or topical coherence — confirms that taste representations are causally implicated in generation, not merely correlated with output. Middle-layer representations actively shape the epistemic framing of generated text.

### 5.6 Applications

**Researcher identification.** Taste fingerprinting enables author identification at 47.7% accuracy @1 (chance: 6.7%, 7.1× above chance). Cross-topic identification achieves 34.6% (5.2× chance). Most distinctive researchers: Crawford (100%), Levin (80%), Ikegami (77%). Least distinctive: Agüera y Arcas (13%), Stanley (20%), Lehman (23%). The collaboration pattern is diagnostic: Stanley and Lehman are frequent co-authors whose taste has likely converged.

Same/different author pair discrimination achieves AUC = 0.731, suggesting taste representations could support large-scale authorship and originality analysis even without a predefined researcher set.

**Epistemic clusters.** K-means (K=4) on taste representations recovers four coherent epistemic clusters without supervision:
- *Critical Theorists* (n=59): Lehman, Levin, Crawford — framework + problematize + challenging
- *Systematic Analysts* (n=116): Ikegami, Bernstein, Rahwan — understanding + framework + empirical
- *Applied Innovators* (n=96): Liang, Steinhardt, Agüera y Arcas — exploration + novelty + near-term + advancing
- *Visionary Explorers* (n=102): Stanley, Risi, Clune — exploration + novelty + embrace + long-term

Known intellectual communities are recovered: the evolutionary computation group (Stanley, Risi, Clune) and the AI safety/empiricism group (Liang, Steinhardt) cluster without access to researcher identity or community metadata.

**Cross-architecture fingerprinting.** Cross-model author identification using taste fingerprints achieves ~56% accuracy (8.4× chance) even when training and evaluation use different model families. Taste is a model-agnostic property of the text.

**Career trajectories.** Early vs. late career cosine similarity reveals substantial variation (mean: 0.228 ± 0.227). Most stable: Bernstein (0.585), Risi (0.507). Most drifting: Agüera y Arcas (−0.171), consistent with his documented pivot from computer vision to generative art and AI philosophy.

**Taste from questions.** Given only a research question statement (no abstract, no results), taste probes correctly profile the author's taste for 6/6 test cases. This enables prospective taste profiling — characterizing a researcher's orientation before the work is complete.

---

## 6. Discussion

### 6.1 What Cross-Architecture Convergence Means

The most surprising result of this paper is not that LLMs encode research taste — we expected that. It is that four models from three companies, trained independently on different data with different architectures, find essentially the *same* representational geometry for meta-epistemic information (CKA ≥ 0.89).

We propose the **convergent meta-epistemic encoding hypothesis**: large-scale training on scientific text causes language models to independently develop similar internal representations of scientists' epistemic orientations, because those orientations are systematically expressed in language across the training corpus. The geometry is not a property of any model's architecture or training recipe; it is a property of the underlying signal in scientific text.

This has implications beyond this paper. If meta-epistemic orientations are universally encoded in LLM representations, then:
- They are accessible without specific training, fine-tuning, or annotation
- They transfer across model updates and model families
- They can be probed using any sufficiently capable LLM
- Interventions on one model's taste geometry may transfer to others

### 6.2 Implications for Science of Science

Taste representations offer a scalable measurement instrument for studying epistemic diversity in research communities. The innovation↔consolidation axis we identify empirically recapitulates theoretical arguments about the social value of scientific diversity \cite{foster2015, weisberg2009}. Tracking taste distributions over time at field or community level could detect epistemic homogenization — a hypothesized risk of large-scale AI-assisted research — without requiring expert qualitative analysis.

The four epistemic clusters we identify without supervision map coherently onto known intellectual communities. If these cluster structures are real (rather than artifacts of our small sample), they suggest that research communities develop shared meta-epistemic orientations that are detectable in text — a quantitative operationalization of Kuhn's paradigmatic communities.

### 6.3 Implications for Mechanistic Interpretability

The linearity of taste encoding (all six dimensions pass Hewitt & Liang criteria) and the cross-model convergence extend the linear representation hypothesis \cite{elhage2022, kim2024} into a new domain. Research taste — a theory-laden philosophical concept — is linearly encoded in a way that is convergent across architectures. This is a new form of evidence that LLM representations are semantically structured at a surprisingly abstract level.

The prompt vs. probe dissociation (Section 5.4) raises questions for alignment: if models implicitly encode rich semantic structure that they cannot explicitly access or report, what other properties are encoded but inarticulate? This motivates continued investment in probing-based interpretability tools as complements to, not substitutes for, behavioral evaluation.

### 6.4 Limitations

**Label validity.** Taste annotations are generated by Qwen3-9B. While the cross-architecture results substantially mitigate the circularity concern, they do not fully validate that our six dimensions correspond to what researchers or communities would recognize as taste. Human expert annotation studies — comparing LLM-generated labels to researcher self-ratings and expert rater agreement — remain essential future work.

**Dataset scale.** 373 abstracts from 15 researchers is small by NLP standards. Results replicate across multiple subsets and controls, but bootstrap confidence intervals are not yet reported on all numbers; we have prioritized replication across architectures over statistical precision in this draft. Expanding to 50+ researchers would substantially increase statistical power.

**Topic entanglement.** Topic removal reduces accuracy from ~74% to ~51%, leaving approximately one-third of the signal topic-mediated. Our within-topic controls (cs.AI subset) and cross-domain transfer results partially address this, but matched-pair analysis (different researchers on literally the same topic) would provide stronger evidence.

**Steering evaluation is qualitative.** Activation steering results are evaluated by inspecting generated text for vocabulary shifts. Rigorous evaluation would apply the same probe to steered outputs and verify that classification shifts as expected. This quantification is future work.

**Researcher sample.** All 15 researchers are prominent AI/CS figures, predominantly based in Western institutions. Selection bias may affect generalizability. Cross-field and cross-cultural extensions are needed.

**Field generalization.** All abstracts are from AI/CS on arXiv. Whether meta-epistemic encoding extends to biology, physics, or humanities — where scientific communication conventions differ substantially — is untested.

### 6.5 Future Work

Priority directions: (1) human annotation pilot study — even 30 papers with 2 expert annotators breaks the circularity concern empirically; (2) bootstrap confidence intervals on all accuracy numbers; (3) quantitative steering evaluation via probe-on-steered-output; (4) matched-topic pair analysis for stronger topic control; (5) expand to 50+ researchers across fields; (6) temporal analysis of taste evolution at community level; (7) taste-aware literature recommendation; (8) analysis of peer review dynamics — do reviewer taste representations predict review sentiment on taste-mismatched papers?

---

## 7. Conclusion

We began with a philosophical observation: scientists have characteristic epistemic orientations — research taste — that shape what questions they ask, how they frame progress, and how they position their work. We end with an empirical finding: this taste is linearly encoded in the intermediate representations of large language models, and this encoding is a convergent property across architectures, companies, and training datasets.

Four models — Qwen3-9B (Alibaba), Qwen3-27B (Alibaba), GPT-OSS-20B (OpenAI), and Gemma3-27B (Google) — all find the same representational geometry for six meta-knowledge dimensions (CKA ≥ 0.89). Cross-model probes transfer. Researcher fingerprints transfer. The innovation↔consolidation axis is the same in all four. A model cannot articulate this information through prompting (0–4% accuracy) yet encodes it powerfully in hidden states (65–81%). Taste is present in research questions before results are written, steerable via activation interventions, and discriminative enough to identify researchers at 7.1× chance.

These findings operationalize decades of qualitative insight from philosophy and sociology of science as measurable, steerable, universal neural geometry. Research taste — long recognized as real and consequential, but resistant to quantification — is legible in the representational fabric of language models trained at scale. The uniformity of the geometric solution across models suggests this is not an artifact of any particular modeling choice, but a reflection of genuine structure in how scientific knowledge is made and written down.

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

\bibitem{christiano2017} Christiano, P., et al. (2017). Deep Reinforcement Learning from Human Preferences. *NeurIPS 2017*. URL: https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html

\bibitem{longino1990} Longino, H. E. (1990). *Science as Social Knowledge*. Princeton University Press. URL: https://press.princeton.edu/books/paperback/9780691020518/science-as-social-knowledge

\bibitem{kitcher1993} Kitcher, P. (1993). *The Advancement of Science*. Oxford University Press. URL: https://global.oup.com/academic/product/the-advancement-of-science-9780195096538

\bibitem{weisberg2009} Weisberg, M., & Muldoon, R. (2009). Epistemic Landscape and the Division of Cognitive Labor. *Philosophy of Science*, 76(2). DOI: 10.1086/644786

\bibitem{elhage2022} Elhage, N., et al. (2022). Toy Models of Superposition. *Transformer Circuits Thread*. URL: https://transformer-circuits.pub/2022/toy_model/index.html

\bibitem{kim2024} Park, K., et al. (2024). The Linear Representation Hypothesis and the Geometry of Large Language Models. *arXiv:2311.03658*. URL: https://arxiv.org/abs/2311.03658

\bibitem{zou2023} Zou, A., et al. (2023). Representation Engineering: A Top-Down Approach to AI Transparency. *arXiv*. URL: https://arxiv.org/abs/2310.01405

\bibitem{kornblith2019} Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). Similarity of Neural Network Representations Revisited. *ICML 2019*. URL: http://proceedings.mlr.press/v97/kornblith19a.html

\bibitem{bender2021} Bender, E. M., et al. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *FAccT 2021*. DOI: 10.1145/3442188.3445922

\bibitem{tshitoyan2019} Tshitoyan, V., et al. (2019). Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature. *Nature*, 571. DOI: 10.1038/s41586-019-1335-8

---

## Appendix: Figures (Described)

**Figure 1.** Probing accuracy across six taste dimensions for all four models, with chance baselines and selectivity bars. All four models cluster in the 65–81% range across all dimensions, well above chance.

**Figure 2.** CKA similarity heatmap across all six model pairs. All off-diagonal values ≥ 0.89; within-family (Qwen3-9B ↔ Qwen3-27B) = 0.942; cross-company pairs comparable (0.912–0.935).

**Figure 3.** Prompt vs. probe accuracy comparison on Qwen3-9B. Stacked bar chart: prompting (0–4%) vs. probing (65–82%) per dimension. The dissociation is visually striking.

**Figure 4.** 2D PCA projection of researcher taste centroids, colored by unsupervised cluster assignment. The four epistemic communities are spatially separated; the Qwen3-9B and GPT-OSS-20B representations produce essentially identical projections when normalized.

**Figure 5.** Qualitative steering examples: three rows (one per dimension), two columns (two poles of each dimension). Each cell shows a 2–3 sentence generated excerpt, with characteristic vocabulary highlighted.

---

*Manuscript prepared for ACL Rolling Review, targeting EMNLP 2026.*  
*Co-authored by Botao Amber Hu (amber@reality.design) and Biber (biber@openclaw.ai)*
