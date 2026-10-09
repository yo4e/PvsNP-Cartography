# PvsNP-Cartography

> **An AI research notebook beyond the known proof barriers.**

PvsNP-Cartography is a long-horizon research notebook for exploring the **P vs NP problem** with AI-assisted mathematical research.

The objective is deliberately not:

> “Generate a proof of P ≠ NP.”

The objective is:

> **Map what is known, identify what known proof barriers actually rule out, explore the remaining terrain, attack every new claim adversarially, and preserve both discoveries and failures as durable research artifacts.**

A solved Millennium Prize Problem would be extraordinary.

A careful map of why our attempted routes fail is still useful.

## Research posture

This repository is governed by five rules.

1. **Known results come first.**  
   Before proposing a route, identify the theorems, lower bounds, and proof barriers that already constrain it.

2. **Every claim gets attacked.**  
   A proposed lemma is not progress until we have actively tried to falsify it, found edge cases, checked definitions, and searched for known counterexamples or prior art.

3. **Finite evidence is not an asymptotic proof.**  
   Computation can suggest structure and kill conjectures. It cannot silently become a theorem about all input sizes.

4. **Formalization is verification, not decoration.**  
   Lean/Coq or another proof assistant should be used where feasible for surviving lemmas and known-result reconstruction.

5. **Failure is data.**  
   Dead approaches go to the graveyard with a clear explanation of why they died, so the same seductive error is not rediscovered every week.

## Why cartography?

P vs NP has enormous prior literature and several famous proof barriers.

A useful AI research process therefore resembles exploration more than proclamation:

- chart known territory
- mark impassable walls
- identify poorly explored boundaries
- conduct small expeditions
- bring back only claims that survive hostile review

The repository is intended to preserve that map over time.

## Initial terrain

The first map should include at least:

- P, NP, NP-completeness, Cook–Levin
- circuit complexity and lower bounds
- proof complexity
- communication complexity
- SAT and restricted models
- relativization
- Natural Proofs
- algebrization
- known lower bounds for restricted circuit classes
- algorithmic lower-bound connections such as the Williams program
- formalization opportunities in Lean

The project should prefer small, sharply stated subproblems over vague attacks on the whole conjecture.

## Repository map

Planned structure:

```text
map/            known terrain, definitions, barriers, open directions
prior-art/      related human and AI research projects
expeditions/    bounded research attempts with explicit hypotheses
claims/         claims that currently survive internal attack
attacks/        adversarial reviews, counterexample searches, failure analysis
experiments/    finite computation and reproducible scripts
formal/         proof-assistant artifacts
graveyard/      dead approaches, false lemmas, seductive mistakes
logs/           chronological research sessions
```

## Claim states

A useful claim should carry an explicit state.

- **idea** — plausible direction, not checked
- **candidate** — precisely stated and under attack
- **finite-evidence** — supported only on bounded computation
- **literature-consistent** — checked against known references, not novel by default
- **formally-verified** — accepted by a proof assistant under explicit assumptions
- **refuted** — counterexample or invalid step found
- **novelty-unknown** — may be new, but prior-art search is incomplete
- **novelty-supported** — targeted prior-art search found no equivalent result; still not a publication claim

No file should casually jump from “interesting” to “proved.”

## AI research protocol

For each expedition:

1. state the exact target
2. record relevant known results/barriers
3. propose one or more approaches
4. derive the smallest testable lemma
5. search for counterexamples
6. run finite experiments where useful
7. conduct an adversarial self-review
8. compare with prior literature/projects
9. formalize surviving pieces where practical
10. either promote the claim or bury it with a post-mortem

The default loop is:

> **hypothesize → attack → repair → attack again → verify → record**

## Other AI attempts

This project is not the first attempt to use AI around P vs NP.

Early comparison targets include:

- [GISMO-1/p-vs-np-hunter](https://github.com/GISMO-1/p-vs-np-hunter) — multi-agent circuit/lower-bound exploration with Lean-backed verification
- [LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai](https://github.com/LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai) — autonomous multi-agent solver architecture
- [MuchuCAT/p-vs-np-ai-quantum-research-notes](https://github.com/MuchuCAT/p-vs-np-ai-quantum-research-notes) — conservative dossier on proof barriers and AI/quantum narratives
- [RenaudGL/Protocol_Cathedrale](https://github.com/RenaudGL/Protocol_Cathedrale) — multi-model exploration of a thermodynamic route to P ≠ NP

These projects are prior expeditions, not targets to imitate blindly.

Their successes, omissions, failure modes, and methodological choices should be mapped before duplicating work.

See `prior-art/` as it develops.

## What would count as progress?

Progress can be much smaller than solving P vs NP.

Examples:

- a clean machine-checkable reconstruction of a relevant known result
- a new finite pattern that survives replication and has a plausible asymptotic interpretation
- a conjecture with a precise falsification path
- a useful reduction between narrowly defined subproblems
- a rigorously documented dead end that eliminates a tempting family of approaches
- a genuinely new lemma that survives literature search and formal verification
- a better research protocol for AI-assisted open mathematics

## What does *not* count?

- “The model feels confident.”
- A long proof-shaped text with an unchecked step.
- Numerical agreement for small n presented as asymptotic truth.
- Renaming a known theorem.
- Ignoring relativization / Natural Proofs / algebrization because they are inconvenient.
- A proof assistant file with unproved axioms hidden behind impressive names.
- A literature search that only asks an LLM from memory.
- Declaring novelty before searching.

## Safety against mathematical self-deception

P vs NP attracts false proofs for good reason: the gap between “this argument is compelling” and “this argument is valid” is enormous.

This repository therefore treats **self-criticism as part of the research object**.

The most valuable file in a research session may be the one explaining why the idea failed.

## Research documents

- [AGENTS.md](AGENTS.md) — research operating contract for AI collaborators
- [docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) — adversarial research loop and publication threshold
- [docs/PRIOR_ART.md](docs/PRIOR_ART.md) — direct P vs NP AI projects and broader AI-mathematics systems
- [docs/BIBLIOGRAPHY.md](docs/BIBLIOGRAPHY.md) — working primary-source bibliography
- [map/BARRIERS.md](map/BARRIERS.md) — relativization, Natural Proofs, and algebrization map
- [Expedition 001](expeditions/001-audit-pvsnp-hunter/) — audit of p-vs-np-hunter finite-degree findings
- [Expedition 002](expeditions/002-exact-probabilistic-degree-mod3/) — finite MOD3 probabilistic-degree certificates, [reproducible checker](expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py), and CI
- [Expedition 003](expeditions/003-n8-sampled-dual/): historical exact sample-restricted n=8 dual and [adversarial counterexample](graveyard/002-n8-sampled-dual-extrapolation.md). Its sampled optimum did not decide the full n=8 problem.
- [Expedition 004](expeditions/004-exact-mod3-n8/): exact n=8 degree-two [certificate](expeditions/004-exact-mod3-n8/certificate.json), [checker](expeditions/004-exact-mod3-n8/verify.py), [finite argument](expeditions/004-exact-mod3-n8/conclusion.md), and [successful CI](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940070467).
- [formal/ASSUMPTIONS.md](formal/ASSUMPTIONS.md) — verified scaffold axioms, CI evidence, and the formalization boundary
- [Finite dual scope](formal/FINITE_DUAL_SCOPE.md): Lean-checked generic real-mixture lemma, not yet a formal MOD3 instantiation.

## Status

**2026-10-09 checkpoint: exact finite MOD3 certificates through n=8 and a Lean-checked finite dual bridge.**

The standard pointwise probabilistic degree over GF(2), at error 1/3,
is exactly 2 for n=5,6,7,8 in the recorded finite certificates. The n=8
result and its verification are in Expedition 004. Novelty remains unknown.
The generic finite-duality lemma has passed pinned Lean CI and axiom audit;
the MOD3 certificates themselves are not yet Lean-verified. No general-n
or P-vs-NP conclusion follows. See [the latest session log](logs/2026-10-09-night-n8-and-duality.md).

The research environment must continue telling the difference between:

- known
- conjectured
- experimentally suggested
- formally verified
- refuted
- genuinely unresolved

---

Research lead / AI investigator: **月野テンプレクス**

Created with 山田佳江 as the human collaborator and repository steward.
