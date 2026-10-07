# Prior Art Map

This document maps earlier AI-assisted attempts relevant to P vs NP and the broader problem of AI-driven mathematical research.

The purpose is not to rank projects. It is to avoid duplicated work, inherit useful methods, and identify failure modes.

## A. Direct P vs NP / complexity projects

### GISMO-1/p-vs-np-hunter

https://github.com/GISMO-1/p-vs-np-hunter

Closest known public project to this repository's intended direction.

Observed structure:

- multi-agent architecture
- circuit exploration
- SAT instance generation
- lower-bound hunting
- conjecture synthesis
- Lean formalization
- meta-learning / barrier tagging
- CI and known-result validation

Strengths:

- distinguishes finite computational evidence from proof
- includes a falsification mindset
- uses Lean
- explicitly targets restricted circuit models rather than pretending to solve P vs NP in one leap
- maintains findings as bounded observations

Important caution:

Its current Lean lower-bound file still contains axiomatized landmarks and placeholder propositions such as statements reducing to `True`. These are useful scaffolding, not formalized proofs of the classical lower bounds.

Lesson for PvsNP-Cartography:

**Never count a theorem as formally verified merely because a Lean file compiles. Inspect assumptions, axioms, placeholders, and theorem content.**

### LLMDeveloperAiPNP autonomous solver

https://github.com/LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai

A 2025 multi-agent architecture built explicitly to attack P vs NP.

Roles include:

- complexity theorist
- algebraist
- formalist
- literature watcher
- skeptic
- intuitionist
- metacognitive architect

Interesting ideas:

- explicit skeptic role
- dynamic specialist agents
- stagnation detection
- strategy pivoting
- shared knowledge graph

Caution:

The repository appears more architecture-heavy than research-output-heavy. Its public history is small relative to the ambition of the README.

Lesson:

**Agent choreography is not itself mathematical progress. Evidence must live in claims, counterexamples, proofs, experiments, and literature comparisons.**

### MuchuCAT/p-vs-np-ai-quantum-research-notes

https://github.com/MuchuCAT/p-vs-np-ai-quantum-research-notes

A deliberately conservative dossier.

Scope includes:

- formal P/NP definitions
- relativization
- Natural Proofs
- algebrization
- restricted lower bounds
- AI/LLM limitations
- quantum complexity context

This project explicitly refuses to offer a P = NP or P ≠ NP proof sketch.

Lesson:

**Barrier literacy should precede speculative proof search.**

This repository is especially useful as a sanity-checking reference and bibliography seed.

### RenaudGL/Protocol_Cathedrale

https://github.com/RenaudGL/Protocol_Cathedrale

A multi-model research experiment using several AI systems to explore a thermodynamic route to P ≠ NP.

The project explicitly states that its derivation is conditional and not a proof.

Lesson:

Cross-domain hypotheses can be generative, but every bridge from physics to complexity classes must be formalized at the mathematical level. Physical evidence alone cannot settle the standard mathematical P vs NP question.

### chsahaka/llm-adversarial-theorem-prover

https://github.com/chsahaka/llm-adversarial-theorem-prover

A useful methodological precedent because it preserves multiple failed attempts instead of presenting only a polished final narrative.

Lesson:

**Attempt history is research data.**

PvsNP-Cartography will preserve dead approaches in `graveyard/` rather than deleting them after failure.

## B. AI mathematics systems and research programs

### OpenAI: Sharing AI progress in mathematics (2026)

https://openai.com/index/sharing-ai-progress-in-mathematics/

OpenAI reports a broad release of mathematical results from an internal frontier model, with:

- a public GitHub repository
- revision and citation protocols
- Lean formalizations for many proofs
- reasoning summaries for selected results
- compute estimates
- thousands of attempted problems

The reported average result used compute comparable to roughly three hours of ChatGPT Pro thinking with the internal model.

Relevance:

- open problems can be treated as a portfolio rather than one monolithic target
- formal verification should accompany natural-language mathematics where practical
- failed attempts and total problem count matter when interpreting success rates
- publication protocol matters once model output may contain genuinely novel mathematics

PvsNP-Cartography should copy the **transparency pattern**, not claim equivalent capability.

### OpenAI: Navier–Stokes Millennium Prize research (2026)

OpenAI reports an AI-generated proposed solution to the Navier–Stokes Millennium Prize Problem with a Lean formalization.

Reference:
https://openai.com/research/index/publication/

Relevance:

A Millennium problem can now be a serious AI research target, but extraordinary claims require extraordinary verification and community scrutiny.

### OpenAI: Unit-distance conjecture result (2026)

https://openai.com/index/model-disproves-discrete-geometry-conjecture/

OpenAI reports an AI-generated counterexample resolving a long-standing conjectural direction in the planar unit-distance problem.

Relevance:

**Counterexample search may be a better first AI research mode than proof generation.**

For P vs NP, this motivates aggressively trying to destroy candidate lemmas before attempting to strengthen them.

### Google DeepMind: AlphaProof

Nature:
https://www.nature.com/articles/s41586-025-09833-y

Background:
https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

AlphaProof combines:

- Lean
- reinforcement learning
- proof-state interaction
- search
- auto-formalization
- problem variants
- verifiable rewards

Relevance:

Formal theorem proving is not merely final-stage checking. A proof assistant can be the environment in which search itself occurs.

### Google DeepMind: Gemini Deep Think / Aletheia research agent

https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/

DeepMind describes research-level mathematical work using a system that iteratively generates, verifies, revises, and performs literature search.

Relevance:

The loop

> generate → verify → revise → search literature → regenerate

is close to the intended PvsNP-Cartography workflow.

### LeanDojo

https://arxiv.org/abs/2306.15626

LeanDojo provides an open framework for interacting programmatically with Lean and training/evaluating theorem-proving models with retrieval.

Relevance:

If this repository begins substantial Lean work, LeanDojo or equivalent tooling should be evaluated before inventing a custom prover interface.

## C. Research ethics / publication process

### OpenAI mathematics advisory process

https://openai.com/index/advisory-group-on-mathematics-and-ai/

The rapid production of AI-generated mathematical results creates a second problem beyond theorem proving:

**How should large volumes of machine-generated claims enter the mathematical community without overwhelming verification and attribution systems?**

PvsNP-Cartography should therefore treat publication discipline as part of research quality.

Before making any public novelty claim:

1. isolate the precise statement
2. verify correctness independently where possible
3. search prior literature deliberately
4. expose assumptions
5. distinguish model-generated conjecture from human/community validation
6. disclose finite evidence vs proof
7. preserve failed approaches and revisions

## D. Strategic gaps we can exploit

Several public projects already use multi-agent systems.

Therefore this repository should not compete on “number of agents.”

Distinctive focus:

1. **Barrier-first cartography**
2. **Explicit graveyard of failed reasoning**
3. **Claim-state discipline**
4. **Adversarial self-review**
5. **Formal assumption auditing**
6. **Reproducible finite experiments**
7. **Novelty checks before celebration**
8. **Longitudinal record of AI research behavior**

## E. Immediate takeaway

The first useful result is unlikely to be “P ≠ NP.”

A more realistic first result would be one of:

- a formally verified restricted lemma
- a counterexample to an AI-generated conjecture
- a rigorous reconstruction of a known lower-bound argument
- a new finite phenomenon with a clearly stated asymptotic question
- a map showing why an attractive proof family collides with a known barrier
- a methodology result about AI-assisted open mathematics
