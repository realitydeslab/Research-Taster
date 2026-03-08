# Research Taster — Self-Proof Critical Review

## 🔴 FATAL FLAW: Style = Researcher (Confound)

**The current experiment does NOT prove taste is encoded. It likely proves TOPIC is encoded.**

Evidence:
- 8 out of 13 style categories have EXACTLY 1 researcher
- `ml_benchmark` = Percy Liang only, `ml_safety` = Jacob Steinhardt only, `alife` = Takashi Ikegami only, etc.
- Only `ml_creative` (5 researchers) and `social_ai` (2 researchers) have multiple researchers per style
- Therefore: classifying "style" is mathematically equivalent to classifying "researcher" for 8/13 categories
- And classifying "researcher" is likely just classifying TOPIC (Percy Liang writes about benchmarks, Ikegami writes about artificial life — different topics, not different "tastes")

**A probe achieving 75% on "style" could be achieving 75% on "who wrote this abstract about their specific topic."**

## 🔴 CRITICAL QUESTION: What Would Actually Prove Taste Exists?

Taste ≠ topic. Taste = HOW you produce knowledge regardless of WHAT you study.

To demonstrate taste, we need:
1. **Cross-domain transfer**: Train probe on researcher X's papers in domain A, test on domain B → if it still works, it's not topic
2. **Within-style diversity**: Multiple researchers with SAME style label who work on DIFFERENT topics → probe should group them by style, not topic
3. **Cross-style within-topic**: Different researchers working on the SAME topic but with different styles → probe should separate them by style

## 🟡 What We Can Salvage

The representations are valid (extraction was correct). The probes work mechanically. But the INTERPRETATION is wrong — we can't claim "taste" when the signal might entirely be "topic."

## 🟢 Redesigned Experiment Plan

### Experiment 1b: Topic vs Taste Separation
- Extract TOPIC vectors (from arXiv categories or keyword clusters)
- Extract STYLE vectors (from our labels)
- Test: Is style accuracy ABOVE what topic alone predicts?
- Method: Residual probing — regress out topic, probe remaining representation for style

### Experiment 1c: Cross-Researcher Validation
- For ml_creative (5 researchers): Leave-one-researcher-out cross-validation
- Train on 4 researchers' papers, test on held-out researcher
- If accuracy holds → style is generalizable, not researcher-specific
- This ONLY works for ml_creative and maybe social_ai (only multi-researcher styles)

### Experiment 1d: Richer Style Labels
- Re-label papers along ACTUAL taste dimensions (not researcher-assigned categories):
  - Problem selection: incremental vs revolutionary
  - Method: formal/mathematical vs empirical/experimental vs design-based
  - Epistemic values: prediction vs understanding vs creation
  - Scope: narrow/deep vs broad/connecting
- Use LLM to annotate these dimensions per paper (meta-analysis of abstracts)
- Then probe for these dimensions instead of researcher-assigned style labels

### Experiment 1e: Topic-Controlled Comparison
- Find researchers who work on OVERLAPPING topics but different styles
- E.g., Jeff Clune (creative ML) and Percy Liang (benchmark ML) both work on LLMs
- Can we distinguish their "taste" on papers about the SAME topic?
