# ATL ECHO — Public Evidence Demo

**Gizem Akıncı İşten** · Independent Researcher  
**Scope:** A small, non-proprietary demonstration of research evaluation, not an ATL ECHO implementation.

## The shared research question

**Can temporal structure and phase-dependent information provide distinguishable evidence of internal state changes, beyond what is explained by conventional baselines or randomized controls?**

This question connects three related research directions:

1. **Signal-domain studies:** testing whether recorded phase/temporal structure is distinguishable from randomized controls in IQ measurements.
2. **Multi-agent AI safety:** investigating whether internal activation trajectories can help attribute controlled changes to a particular agent in Qwen-based experiments.
3. **Auditable computational research:** investigating how evidence, uncertainty, and computational provenance can be retained across analytical stages.

These are connected by a **methodological question**, not by a demonstrated transfer of performance across domains. Signal-domain findings do not validate model-activation source attribution, and neither establishes a finished safety product.

## What this demo does

`demo.py` reads a **small table of selected aggregate results** from the prior IQ evaluation and prints simple, independently understandable comparisons. It does **not** reconstruct a signal, compute an ATL ECHO transformation, load a language model, or run the original experiment.

Run with Python 3.9+ (standard library only):

```bash
python demo.py
```

### Recorded evaluation snapshot

| Quantity | Reported value |
|---|---:|
| Observed ATL_Delay structural score | 0.707506 |
| Random-delay ensemble mean | 0.702490 |
| Random-delay 99th percentile | 0.703180 |
| Shuffled-phase ensemble mean | 0.580282 |
| Shuffled-phase 95th percentile | 0.995939 |
| Shuffled-phase empirical p-value | 0.425 |

In this evaluation, the observed score exceeds the random-delay 99th percentile. **It does not exceed the shuffled-phase 95th percentile**, and the reported shuffled-phase empirical p-value is **0.425**. The latter control therefore does not support a strong claim of phase-order-specific separation.

The source experiment calls its score *Loschmidt*. Here it is described as a **computational structural-similarity score**, not a measurement of physical quantum reversibility. The original dataset, preprocessing, transformation and scoring implementations are **not distributed**. Re-running this script verifies only the arithmetic comparisons above, **not** the experimental findings.

## Relationship to the Qwen research

The separate ATL ECHO AI Safety research uses internal model activations in controlled multi-agent scenarios. A pilot with Qwen2.5-1.5B-Instruct reported **34/40** correct source attributions in two validation sets, compared with a five-agent random-choice baseline of 20%. That result comes from **a different experiment** and is not reproduced by this demo. Generalization and independent replication remain open.

## Public/private boundary

**Included:** a small read-only aggregate-results table, transparent comparison code, scope statements and limitations.  
**Not included:** proprietary ATL ECHO equations/operators, source implementations, activation-extraction routines, calibration logic, original experiment scripts, original IQ recordings, evaluation pipelines or deployment architecture.

No public performance or safety guarantee is implied. This repository is intended for research communication and methodological transparency only.

## Research origin

Akıncı Bertan, G. (2025). *The Origin of Dark Energy: The Role of Interactions Between Imaginary and Anti Time Dimensions.* **Cumhuriyet Science Journal, 46**(3), 621–643. https://doi.org/10.17776/csj.1574774

The publication's *Future Work* section introduces ATL ECHO as a candidate protocol. The computational and AI-safety research described here is subsequent work; the paper does not validate these experiments.

**ORCID:** https://orcid.org/0009-0009-8555-9690  
**Researcher:** Gizem Akıncı İşten (published as Gizem Akıncı Bertan)

© 2026 Gizem Akıncı İşten. All rights reserved in the original documentation and demo materials. No license to proprietary research implementations is granted.
