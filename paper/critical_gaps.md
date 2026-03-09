# Critical Gaps Analysis — Research Taster Paper

*Prepared for internal review prior to ARR submission.*  
*Authors: Biber (biber@openclaw.ai), Botao Amber Hu (amber@reality.design)*

---

## 1. What Reviewers Will Attack (Ranked: Most → Least Severe)

### 🔴 CRITICAL — Will Almost Certainly Be Raised

**1.1 Circularity (Annotation + Probing from Same Model Family)**

*The attack:* "You use Qwen3 to label the 'taste' dimensions, then probe Qwen3 representations for those labels. Of course the probe works — you're measuring internal consistency of a single model family, not anything about actual research taste as humans understand it. This result could be vacuous: any structured annotation scheme applied to Qwen3 would produce high probing accuracy from Qwen3 representations."

*Severity:* Fatal if not addressed well. This is the #1 concern.

*Mitigations we have:* Cross-model CKA (Exp 8) shows the geometry is consistent across 9B and 27B — but both are Qwen3 family. This doesn't help much.

*What we need:* (a) Human expert annotations on a subset and probe for those; (b) Use a different model family for annotation vs. probing; (c) Show that the probe labels match human intuitions qualitatively.

*Current paper handling:* Acknowledged in Section 6.2. Frame as "internal consistency." Call for human validation. This is honest but won't fully satisfy reviewers — we need at least a small human validation pilot.

---

**1.2 Small Sample Size (373 papers, 15 researchers)**

*The attack:* "With 15 researchers and 373 abstracts, your results are almost certainly overfit. 47.7% author identification from 15 classes is impressive but with n~25 papers per author, this could reflect surface stylistic features, not anything as deep as 'epistemic taste.' Your within-topic result (69.7%) is on 178 papers with 15 classes — that's about 12 papers per class. Statistical power is very limited."

*Severity:* High. Every number should have confidence intervals.

*Mitigations we have:* Leave-one-out, cross-domain transfer, CKA consistency all help. selectivity analysis guards against overfitting.

*What we need:* (a) Bootstrap confidence intervals on all accuracy numbers; (b) Permutation tests for all key results; (c) Ideally expand to 50+ researchers.

*Current paper handling:* Acknowledged in Section 6.2 but without CI numbers. This is a gap.

---

**1.3 Topic Confound Not Fully Resolved**

*The attack:* "You show that topic removal reduces accuracy from 78% to 51%, leaving ~40% of the signal topic-mediated. But your 'topic removal' method (projecting onto null space of a topic classifier) is crude — it's likely not removing all topic signal, just the linearly decodable portion. The 51% residual may still be topic-driven. Your within-topic (cs.AI only) result of ~70% is more convincing, but within cs.AI there's still enormous topic variation (safety vs. ALife vs. HCI) that perfectly tracks your researchers."

*Severity:* High. The within-topic result is actually the strongest evidence, but reviewers will question whether cs.AI is truly "same topic."

*Mitigations we have:* Cross-domain transfer (Exp 7). The residual 51% is presented honestly.

*What we need:* (a) Matched pairs analysis — compare papers by different researchers on literally the same topic (same benchmark, same model, etc.); (b) Better topic modeling (e.g., LDA-based residualization); (c) Researcher-stratified topic controls.

---

**1.4 Construct Validity of "Research Taste"**

*The attack:* "The paper asserts it's measuring 'research taste' but never validates that the six Evans & Foster dimensions actually correspond to what researchers or the community would recognize as taste. The taxonomy is adapted without clear justification for the specific label values used. Are 'exploration' vs 'consolidation' as strategic orientations the right operationalization? Did Evans & Foster use these exact categories?"

*Severity:* Moderate-high. A sociologist reviewer will push hard here.

*Mitigations we have:* Evans & Foster (2011) citation. Qualitative face validity of clusters.

*What we need:* (a) More careful grounding in what Evans & Foster actually say; (b) At minimum, quote their framework directly; (c) Pilot survey of researchers asking them to self-rate on dimensions and compare to our LLM ratings.

---

### 🟡 MODERATE — Likely to Be Raised

**1.5 Activation Steering Evaluation Is Qualitative**

*The attack:* "Exp 2b shows 'coherent taste-shifted output' but the evaluation is qualitative — you look at ALife vocabulary presence. This is not a rigorous measure of taste shift. Maybe steering just injects domain vocabulary. How do you know the steered output shifts taste rather than topic?"

*Severity:* Moderate. The steering result is cool but unvalidated.

*What we need:* Blind human evaluation of steered vs. unsteered outputs on taste dimensions. Or: probe the steered outputs with the same probe and show the classification shifts as expected.

---

**1.6 Why These 15 Researchers?**

*The attack:* "The researcher sample appears to be 15 prominent AI researchers the authors know. This selection bias could explain many results — these may be unusually distinctive researchers, not representative of the scientific community. Crawford and Levin being 100% identifiable may reflect extreme distinctiveness, not a general phenomenon."

*Severity:* Moderate. 

*What we need:* (a) Justify selection criteria explicitly; (b) Acknowledge selection bias; (c) Include some less-prominent researchers as a control.

---

**1.7 Single Language, Single Field**

*The attack:* "All abstracts are in English, from AI/CS on arXiv. Research taste may manifest differently in other fields or languages."

*Severity:* Low-moderate. Standard limitation, acknowledge clearly.

---

### 🟢 MINOR — May Be Raised

**1.8 Comparison to Stylometric Methods**

"You compare to SPECTER2 and TF-IDF but not to authorship attribution methods that explicitly model writing style (e.g., character n-grams, function word profiles). These might perform competitively if what you're measuring is stylometric rather than epistemic."

**1.9 Layer Selection Justification**

"Why layer 12 for 9B and layer 25 for 27B? These are described as 'peak probing accuracy' layers but we don't see the full layer-accuracy curve. Is there a theoretical justification?"

**1.10 Definition of Taste vs. Style vs. Voice**

"The paper conflates 'research taste' with 'epistemic orientation' and 'meta-knowledge' — these are related but not identical concepts. Clearer conceptual grounding is needed."

---

## 2. Experiments Still Needed

### Must-Have Before Submission

| # | Experiment | Why Critical | Effort |
|---|------------|-------------|--------|
| A | **Human annotation pilot** (20–30 papers, 2–3 expert annotators, compute agreement with LLM labels) | Breaks circularity | Medium |
| B | **Bootstrap CIs on all accuracy numbers** | Statistical rigor | Low |
| C | **Permutation tests** for key results | Guard against overfitting | Low |
| D | **Full layer-accuracy curves** (both models) | Justify layer selection | Low |
| E | **Quantitative steering evaluation** (probe steered outputs, show classification shift) | Validate causal claim | Medium |

### Should-Have (Strong Paper)

| # | Experiment | Why Valuable | Effort |
|---|------------|-------------|--------|
| F | **Cross-model-family probing** (annotate with GPT-4, probe Qwen3) | Breaks circularity another way | Medium |
| G | **Matched-topic pairs analysis** (different researchers, same specific topic) | Stronger topic control | High |
| H | **Expand to 30+ researchers** | Statistical power | High |
| I | **Stylometric baseline** (character n-grams, function words) | Fair comparison | Low |
| J | **Researcher self-ratings on dimensions** | Construct validity | Medium |

### Nice-to-Have

| # | Experiment | Why Valuable |
|---|------------|-------------|
| K | Field-level taste distribution over time (track taste shifts) | Societal implication |
| L | Taste-based recommendation system user study | Application validation |
| M | Non-English abstracts | Generalization |

---

## 3. Literature We're Missing

### Definitely Need to Cite

| Paper | Relevance | Why Missing Is Risky |
|-------|-----------|---------------------|
| **Gururangan et al. (2020). Don't Stop Pretraining.** ACL 2020. DOI: 10.18653/v1/2020.acl-main.740 | Domain adaptation of LLMs — shows domain specificity of representations | Reviewers may ask if we're just seeing domain effects |
| **Mikolov et al. (2013). Linguistic Regularities in Word Space.** NAACL 2013. | Origin of "linear probing" paradigm | Historical grounding |
| **Kim et al. (2024). The Linear Representation Hypothesis and the Geometry of Large Language Models.** arXiv:2311.03658 | Directly relevant to our linearity claim | Should cite |
| **Elhage et al. (2021). A Mathematical Framework for Transformer Circuits.** | Mechanistic interpretability foundations | Should cite for Exp 6 |
| **Bender et al. (2021). On the Dangers of Stochastic Parrots.** FAccT 2021. DOI: 10.1145/3442188.3445922 | Critical perspective on LLM knowledge claims | Reviewers may raise; get ahead of it |
| **Steyvers & Griffiths (2007). Probabilistic Topic Models.** | For topic modeling baseline context | Minor |
| **Collins et al. (2023). Evaluating Large Language Models on Scientific Text Understanding.** | Direct competitor/context | Check if exists |
| **Tshitoyan et al. (2019). Unsupervised word embeddings capture latent knowledge from materials science.** Nature. DOI: 10.1038/s41586-019-1335-8 | LLMs capturing scientific knowledge structurally | Supportive precedent |

### From Philosophy/STS (Strengthen Grounding)

| Paper | Relevance |
|-------|-----------|
| **Longino (1990). Science as Social Knowledge.** Princeton UP. | Epistemic values in science — directly relevant |
| **Kitcher (1993). The Advancement of Science.** Oxford UP. | Division of cognitive labor — relevant to taste clusters |
| **Merton (1973). The Sociology of Science.** Chicago. | Classic norms of science — CUDOS |
| **Latour & Woolgar (1979). Laboratory Life.** | Science as social practice |
| **Ziman (2000). Real Science.** Cambridge UP. | Post-academic science, epistemic norms |

### Recent LLM + Science

| Paper | Relevance |
|-------|-----------|
| **Liang et al. (2022). Holistic Evaluation of Language Models.** HELM. arXiv:2211.09110 | Benchmark framing — know the landscape |
| **Achinstein (1983). The Nature of Explanation.** | Philosophy of scientific contribution |

---

## 4. Strongest Arguments (What to Lead With)

1. **The within-topic (cs.AI) result is bulletproof.** 69.7–71.4% at 6.4× chance, within a single arXiv category. This is the cleanest evidence. Lead every discussion with this.

2. **Hewitt & Liang selectivity passes for all six dimensions.** This is the gold standard in the probing literature. ALL GENUINE + ALL LINEAR is a strong result. Many probing papers fail this.

3. **Cross-model CKA = 0.942.** This is strikingly high. It means both models "agree" on taste geometry. Hard to explain by coincidence or model-specific artifact.

4. **Unsupervised clusters recover known intellectual communities.** Stanley/Risi/Clune clustering without supervision — this is interpretable, socially coherent, and compelling to AI researchers.

5. **LLM beats SPECTER2 on all 7 targets.** General LLM beats purpose-built scientific embeddings. Clean story: taste is encoded in language modeling, not domain specialization.

6. **Career trajectories are individually meaningful.** Agüera y Arcas's taste reversal (cosine −0.171) is historically verifiable — his career did pivot dramatically. This kind of face validity is persuasive.

---

## 5. Weakest Arguments (Where to Be Careful)

1. **Activation steering is the weakest result.** Qualitative, ALife vocabulary as proxy, no blind evaluation. Present this as exploratory/preliminary. Don't overstate the causal claim.

2. **The ~51% residual after topic removal.** We say "partial but incomplete separability" — fine, but reviewers will focus on the 40% topic-mediated signal. Don't bury this.

3. **Exp 12 (r=0.077 not significant).** A null result. Interesting null, but framing "representations capture more than labeled dimensions" is speculative. Be careful.

4. **Researcher fingerprinting = 100% @1 on blind test.** This is so strong it seems like it might be a trivial result (memorization) or a methodological artifact. Needs careful explanation of exact evaluation protocol.

5. **The "research taste" framing itself.** Reviewers outside NLP may question whether "taste" is the right word — it carries philosophical baggage (Bourdieu's aesthetic taste). Either lean into it with stronger philosophical grounding, or use more neutral language like "epistemic orientation" throughout and use "taste" only in the title/abstract.

---

## 6. Strategic Recommendations for Revision

1. **Add a human annotation pilot study** — even 30 papers with 2 annotators is enough to break the circularity criticism. This is the single highest-leverage experiment.

2. **Report bootstrap CIs on all key numbers** — the paper currently reads as point estimates. This will look unsophisticated to reviewers.

3. **Restructure Results to lead with within-topic (cs.AI) result** — it's the cleanest, put it first, not buried in Exp 1b.

4. **Add a conceptual figure** — the 2D PCA projection of researcher fingerprints (FIGURE 3) is the paper's money figure. Make sure it's beautiful and appears in the introduction or abstract-area.

5. **Tighten the Evans & Foster grounding** — quote the paper, show exactly how our six dimensions map to their framework, justify the label values.

6. **The steering section needs quantitative evaluation** — even running the output through the same probe and showing the predicted taste shift would satisfy reviewers.

7. **Consider a "human-relatable" framing** — citing examples where the taste vectors correctly predict researcher behavior (e.g., Clune and Stanley co-author frequently, their vectors are closest) makes the abstract concepts concrete.

---

*Last updated: 2026-03-09*  
*Next step: Human annotation pilot (20–30 papers, recruit 2 expert annotators from STS/HCI)*
