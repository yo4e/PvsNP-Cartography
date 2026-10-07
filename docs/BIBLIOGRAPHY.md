# Working Bibliography

This is a working source map, not yet a publication-ready bibliography.

Prefer primary papers and official project pages. Secondary summaries are useful for orientation but should not carry theorem-level claims when the original source is available.

## P vs NP: official problem statement

### Clay Mathematics Institute — P vs NP

https://www.claymath.org/millennium/p-vs-np/

Official Millennium Prize Problem page.

### Stephen Cook — The P versus NP Problem

Official Clay problem description:

https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf

Use this as a canonical source for the statement and historical framing of the problem.

## Core proof barriers

### Baker, Gill, Solovay — Relativizations of the P =? NP Question

The classical relativization barrier.

Key fact to track precisely:

There exist oracle worlds with different answers to the relativized P vs NP relation, so any proof method that relativizes cannot settle the unrelativized problem.

### Razborov, Rudich — Natural Proofs

Classical Natural Proofs barrier for broad circuit-lower-bound techniques under cryptographic assumptions.

Research rule:

Do not casually label an argument “non-natural.” Check constructivity, largeness, and usefulness against the actual framework.

### Aaronson, Wigderson — Algebrization: A New Barrier in Complexity Theory

Paper:

https://www.scottaaronson.com/papers/alg.pdf

Algebrization strengthens the lesson of relativization by showing that many arithmetization-based techniques still fall into a broader barrier class.

## Restricted lower bounds / positive landmarks

### Håstad — switching-lemma / AC0 lower-bound work

Relevant for understanding what successful restricted circuit lower bounds look like.

### Razborov — monotone circuit lower bounds

Relevant restricted-model success.

### Smolensky — algebraic lower bounds for bounded-depth circuits

Relevant for AC0[p] / polynomial-method discussions.

### Ryan Williams — NEXP vs ACC0

A major modern lower-bound landmark connecting algorithms and circuit lower bounds.

Before relying on any exact formulation, fetch and cite the primary paper.

## Formal mathematics and AI

### AlphaProof

Nature:

https://www.nature.com/articles/s41586-025-09833-y

DeepMind overview:

https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

### LeanDojo

https://arxiv.org/abs/2306.15626

### Gemini Deep Think / Aletheia

https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/

## AI-generated mathematical research

### OpenAI — Sharing AI progress in mathematics

https://openai.com/index/sharing-ai-progress-in-mathematics/

Important methodological details:

- broad portfolio of open research problems
- public manuscripts
- Lean formalization for many results
- reasoning summaries for selected results
- compute disclosure
- revision/citation protocol

### OpenAI — Unit-distance conjecture result

https://openai.com/index/model-disproves-discrete-geometry-conjecture/

Important methodological lesson:

Counterexample discovery can decisively resolve a conjectural direction without producing a giant proof.

### OpenAI — Navier–Stokes research announcement

OpenAI research listing:

https://openai.com/research/index/publication/

Treat any Millennium-level result as requiring independent expert verification beyond model-generated or formal artifacts.

### OpenAI — Advisory Group on Mathematics and AI

https://openai.com/index/advisory-group-on-mathematics-and-ai/

Relevant to publication ethics, disclosure, verification burden, and responsible release of machine-generated mathematics.

## Meta-rule

No citation should be included merely because an AI remembered it.

For theorem-level work:

1. retrieve the source
2. read the relevant statement
3. record the exact assumptions
4. distinguish the paper's theorem from our paraphrase
5. cite stable source information
