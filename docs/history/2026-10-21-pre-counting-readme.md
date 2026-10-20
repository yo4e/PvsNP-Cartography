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

- **idea**: plausible direction, not checked
- **candidate**: precisely stated and under attack
- **finite-evidence**: supported only on bounded computation
- **literature-consistent**: checked against known references, not novel by default
- **formally-verified**: accepted by a proof assistant under explicit assumptions
- **refuted**: counterexample or invalid step found
- **novelty-unknown**: may be new, but prior-art search is incomplete
- **novelty-supported**: targeted prior-art search found no equivalent result; still not a publication claim

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

- [GISMO-1/p-vs-np-hunter](https://github.com/GISMO-1/p-vs-np-hunter): multi-agent circuit/lower-bound exploration with Lean-backed verification
- [LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai](https://github.com/LLMDeveloperAiPNP/LLM-Developer-AiPNPvs-NP---Autonomous-Solver-Ai): autonomous multi-agent solver architecture
- [MuchuCAT/p-vs-np-ai-quantum-research-notes](https://github.com/MuchuCAT/p-vs-np-ai-quantum-research-notes): conservative dossier on proof barriers and AI/quantum narratives
- [RenaudGL/Protocol_Cathedrale](https://github.com/RenaudGL/Protocol_Cathedrale): multi-model exploration of a thermodynamic route to P ≠ NP

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

- [AGENTS.md](AGENTS.md): research operating contract for AI collaborators
- [docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md): adversarial research loop and publication threshold
- [docs/PRIOR_ART.md](docs/PRIOR_ART.md): direct P vs NP AI projects and broader AI-mathematics systems
- [docs/BIBLIOGRAPHY.md](docs/BIBLIOGRAPHY.md): working primary-source bibliography
- [map/BARRIERS.md](map/BARRIERS.md): relativization, Natural Proofs, and algebrization map
- [Expedition 001](expeditions/001-audit-pvsnp-hunter/): audit of p-vs-np-hunter finite-degree findings
- [Expedition 002](expeditions/002-exact-probabilistic-degree-mod3/): finite MOD3 probabilistic-degree certificates, [reproducible checker](expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py), and CI
- [Expedition 003](expeditions/003-n8-sampled-dual/): historical exact sample-restricted n=8 dual and [adversarial counterexample](graveyard/002-n8-sampled-dual-extrapolation.md). Its sampled optimum did not decide the full n=8 problem.
- [Expedition 004](expeditions/004-exact-mod3-n8/): exact n=8 degree-two [certificate](expeditions/004-exact-mod3-n8/certificate.json), [checker](expeditions/004-exact-mod3-n8/verify.py), [finite argument](expeditions/004-exact-mod3-n8/conclusion.md), and [successful CI](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940070467).
- [Expedition 005](expeditions/005-formal-mod3-five/): concrete n=5 Lean lower/upper certificate components, [exact scope](expeditions/005-formal-mod3-five/conclusion.md), and [independent data audit](expeditions/005-formal-mod3-five/audit.py).
- [Expedition 006](expeditions/006-degree-interface/): complete n=5 degree-based [Lean equality](formal/PvsNPCartography/Mod3FiveDegree.lean), [statement audit](expeditions/006-degree-interface/statement-audit.md), [verified conclusion](expeditions/006-degree-interface/conclusion.md), and [quantifier countermodel](graveyard/005-input-dependent-polynomial.md).
- [Expedition 007](expeditions/007-small-support-mod3/): complete n=6/n=7 [Lean equalities](formal/PvsNPCartography/SmallSupportMod3.lean), compact [18-polynomial certificates](expeditions/007-small-support-mod3/certificate.json), [exact audit](expeditions/007-small-support-mod3/audit.py), [verified conclusion](expeditions/007-small-support-mod3/conclusion.md), and [failed cyclic compression](graveyard/006-single-cyclic-orbit.md).
- [Expedition 008](expeditions/008-full-symmetrization/): generic full [symmetrization](formal/PvsNPCartography/FiniteSymmetrization.lean), [MOD3 applications](formal/PvsNPCartography/SymmetryApplications.lean), [verified scope](expeditions/008-full-symmetrization/conclusion.md), [exact audit](expeditions/008-full-symmetrization/audit.py) and [seven invalid shortcuts](graveyard/007-symmetrization-hypotheses.md).
- [Expedition 009](expeditions/009-hamming-layer-bridge/): verified Hamming-layer counting and the complete [n=8 Lean degree equality](formal/PvsNPCartography/Mod3EightDegree.lean), with [completion evidence](expeditions/009-hamming-layer-bridge/conclusion.md).
- [Expedition 010](expeditions/010-n8-recovery/): [n=8 repair and compact-witness recovery](expeditions/010-n8-recovery/conclusion.md), [159-row certificate](expeditions/010-n8-recovery/certificate-159.json), exact validators and [failed probability rounding](graveyard/009-rounded-probabilities.md).
- [Expedition 011](expeditions/011-n9-one-orbit/): exact n=9 [one-orbit GF(2) MOD3 degree equality](formal/PvsNPCartography/Mod3NineDegree.lean), [strict 85/126 seed certificate](expeditions/011-n9-one-orbit/certificate.json), [reproducible validators](expeditions/011-n9-one-orbit/verify.py), [bounded 7432-pattern search](expeditions/011-n9-one-orbit/scan_blocks.py), and [formally verified conclusion](expeditions/011-n9-one-orbit/conclusion.md).
- [Expedition 012](expeditions/012-n10-three-blocks/): scoped failure of the restricted n10 single-orbit search; not a universal quadratic lower bound.
- [Expedition 013](expeditions/013-n10-mixture/): exact n10 eight-orbit certificate and universal affine-row dual.
- [Expedition 014](expeditions/014-n10-formal/): original n10 formal candidate, independent coefficient audit and historical interrupted execution; completed by Expedition016.
- [Expedition 015](expeditions/015-n11-mixture/): preserved n11 nine-orbit and three-orbit finite certificates, validators and original CI evidence.
- [Expedition 016](expeditions/016-n10-verification-repair/): completed n10 [formal repair](expeditions/016-n10-verification-repair/conclusion.md), [statement audit](expeditions/016-n10-verification-repair/statement-audit.md), isolated diagnostics and preserved failures.
- [Expedition 017](expeditions/017-n11-subset-compression/): exact n11 [496-row same-measure compression](expeditions/017-n11-subset-compression/conclusion.md), [verifier/generator](expeditions/017-n11-subset-compression/verify.py), [actual CI evidence](expeditions/017-n11-subset-compression/ci-evidence.md) and invalid-weighting counterexamples.
- [Expedition 018](expeditions/018-n11-formal/): complete n11 [degree equality](formal/PvsNPCartography/Mod3ElevenDegree.lean), [conclusion](expeditions/018-n11-formal/conclusion.md), [actual axiom output](expeditions/018-n11-formal/axiom-report.txt) and independent source-data audit.
- [Expedition 019](expeditions/019-balanced-affine-dual/): [verified pure real-algebra score bound](formal/PvsNPCartography/BalancedAffineDualAlgebra.lean), [exact scope](expeditions/019-balanced-affine-dual/conclusion.md), bounded computational checks and the still-open generic counting bridge.
- [formal/ASSUMPTIONS.md](formal/ASSUMPTIONS.md): current formal scope, actual axiom reports and preserved historical ledgers.
- [Finite dual scope](formal/FINITE_DUAL_SCOPE.md): generic real-mixture lemma and its concrete n=5 affine application.
- [Current status](docs/CURRENT_STATUS.md): the earliest unblocked task and exact evidence boundaries.

## Status

**2026-10-20 JST: formal numerical MOD3 degree equalities now cover n=5..11.** The n11 three-seed/full-permutation construction is accepted at [9733d800](https://github.com/yo4e/PvsNP-Cartography/commit/9733d800128ad6d92b1f1293e453a4c8d5188f34), [SUCCESS run39380310454](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39380310454), job118487684638: pinned Lean4.35.0-rc4/Mathlib9e6b3aac, --wfail9043 jobs,508 namespace declarations and18 explicit targets under the unchanged foundational allowlist. Actual full completed logs, source statements and matching commit/tree were re-fetched. [Issue #11](https://github.com/yo4e/PvsNP-Cartography/issues/11) is completed; earlier #10 remains completed.

The theorem preserves genuine GF(2) MvPolynomial.totalDegree, normalized nonnegative REAL probabilities, and one family before every input. The upper proof uses exact weights[1,4,2]/7 and all coordinate permutations; the lower proof excludes all actual degree<=1 polynomials and finite REAL mixtures via the strict69/110 affine dual and structural normal form. Separate [exact source-data CI39380579421](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39380579421) reproduces all2048 inputs,4096 affine scores,12 layer totals,201 coefficient mutations and5 source-data mutations under normal/-O Python. The496-row quotient with min158/231 remains separately finite evidence, not a new formal quotient transport theorem.

**A generic real-algebra bound is also verified, but its Boolean-cube counting bridge remains open.** Repaired code [dde6151a](https://github.com/yo4e/PvsNP-Cartography/commit/dde6151abd4a4a272a2bdcbbd277c7296487d2c5) passed [run39381768668](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39381768668), job118492254315: --wfail9044 jobs,518 allowlisted declarations, six algebra targets and all18 n11 reports. It proves a specified real score lies between1/3 and2/3 for n>=7 and0<=k<=n. The proof is algebraic, not extrapolated from tests. The generic input normalization, odd-intersection counts and actual polynomial-evaluation connection are the next task in [Issue #12](https://github.com/yo4e/PvsNP-Cartography/issues/12), not assumed completed.

The overbroad equal-half dual fails at n6,k1 with exactly2/3 and at n5,k1 with7/10; [graveyard018](graveyard/018-balanced-dual-low-arity-extension.md) preserves that specific failure. The auxiliary first build failed on computability and a warning; [graveyard019](graveyard/019-balanced-score-build-discipline.md) records its faithful repair without weakened statements or audits. The bounded33147-case exact check remains separate evidence.

[Issue #8](https://github.com/yo4e/PvsNP-Cartography/issues/8) remains open for independent human semantic review. A second proof kernel and mathematical novelty assessment are not supplied. These are new repository checkpoints, not asserted new mathematics. No n12 degree equality, minimum support/denominator, all-n degree2 upper bound, circuit lower bound, proof-barrier escape or P-vs-NP solution is claimed.

See the [session log](logs/2026-10-20-mod3-eleven-and-balanced-dual.md) and [assumption ledger](formal/ASSUMPTIONS.md). The previous README is preserved byte-identically in [the dated archive](docs/history/2026-10-20-pre-n11-readme.md); its older pending statements are historical.

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
