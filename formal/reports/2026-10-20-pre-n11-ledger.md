# Formal assumption ledger

## Current checkpoint: approved 2026-10-18 night, n10 verified

The production run completed on 2026-10-19 JST, within the same approved Oct18
session. Complete numerical GF(2), error1/3 MOD3 probabilistic-degree equalities
now cover **n=5..10**. The n11 three-orbit and496-row witnesses remain separately
validated finite data, not compiled n11 Lean degree theorems. No asymptotic
P-vs-NP or all-n MOD3 conclusion follows.

## Actual production acceptance

- Code: `1739ccfa2ebe5997e568135cdfacf06e9f6d1f87`.
- Tree: `693fff576290749ebbd023d861041e53ca0a9812`.
- n10 source blob: `cf6c6ec257f0a5c20e9b12f3c265864db57e58ca`.
- n10 source SHA256: `5d6aa5a2df006cee95a9d43b0707505298f431d38f0c984440fb5b0d1553b571`.
- [Completed SUCCESS formal run39139432083](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39139432083), job117710608870.
- Pinned Lean4.35.0-rc4 and Mathlib `9e6b3aac99b624d10c84653ab9c5357283b9b3b8`.
- Production **--wfail** root build:9042 jobs. Mod3TenDegree actually built in176s.
- Namespace audit: **420 declarations**, all within `[propext, Classical.choice, Quot.sound]`.
- All **15 explicit n10 target reports** use only that same foundational allowlist.

The full completed job log, matching source statements and Git commit/tree were
retrieved and inspected. [Attributed actual output](reports/2026-10-18-n10-axioms.txt)
records the toolchain, build, namespace count and all15 n10 targets. A queued
run, green diagnostic wrapper or source file alone was not used as acceptance.
No new project-specific axiom, sorryAx, native_decide or decide_cbv was accepted.

## Statement and dependency fidelity

The n10 target is one iff integer Hamming weight is divisible by3. Coefficients
are GF(2), not real-valued approximation polynomials. The degree bound is actual
MvPolynomial.totalDegree. Nonnegative REAL probabilities sum to1 and a single
finite family is selected before every input quantifier.

Upper: the unchanged eight seeds with weights[10,2,39,22,15,6,4,2]/100 are encoded
by triple tickets/300. Genuine quadratic polynomial evaluation and all11 exact
layer sums feed the already verified full-permutation/Hamming-layer adapter.
The resulting family includes ALL coordinate permutations, not input-dependent
polynomial choices. Exact finite minimum is2123/3000>2/3.

Lower: mass12 per weight-one input and1 per weight-three input, total240, yields
bound152/240=19/30<2/3. Proved coefficient-permutation coverage turns22 canonical
checks into coverage of all2048 affine rows. Structural degree-one normal form
then applies the dual to ALL actual degree<=1 polynomial objects and arbitrary
finite REAL mixtures. The final `feasible_degree_iff`, `least_feasible_degree`
and `pdeg_eq_two` use proved feasibility and infeasibility, not desired-result
hypotheses. The raw unsymmetrized mixture counterexample is also formally checked.

The original HasProbabilisticDegreeAtMost definition, real probabilities,
family-before-input quantifiers, layer adapter, code coefficients, success
thresholds and heartbeat settings were unchanged by the repair.

## Separate computational evidence

[Completed SUCCESS semantic run39139432110](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39139432110),
job117710608842, at the same production commit, reproduced the independently
derived n10 coefficients on1024 canonical inputs, all2048 affine rows, all11
layer sums and448 coefficient-mutation tests. Normal/-O output matches saved
JSON and the exact production-source hash. This is complementary evidence,
not a replacement for the completed Lean audits.

For n11, Expedition017 proves no new Lean theorem: its exact computational
quotient removes redundant partition labels from the same old probability
measure,1925 indexed entries to496 distinct rows, denominator27720 to1155,
unchanged minimum158/231 on all2048 inputs. The three-seed/full-permutation and
496-row implementations must not be conflated if either is later formalized.

## Failure history and repair boundary

The Oct17 n10 candidate run39037050907 was cancelled twice with shutdown/exit143;
its cause remains unknown. This session's isolated diagnostic found the original
kernel lower prefix passes. Default decide_cbv substitutions failed the step
budget, propagating sorryAx into failed dependent declarations. Those outputs
were rejected and preserved in graveyard017, not called proof success.

The successful repair changes only the layer proof to:

```lean
  intro w
  fin_cases w <;> decide +kernel
```

Diagnostic run39138440340 passed the layer-only and full candidate with15
allowlisted reports. The exact candidate was then applied and accepted by the
production run above. No increased CBV budget was adopted or tested after the
first strategy passed. Historical diagnostic scripts intentionally pin the old
candidate hash; reproduce them at their recorded commits instead of bypassing
those provenance guards.

## Reproduction and remaining gates

From `formal/` run `lake build --wfail` and `./scripts/axiom_report.sh`.
The production workflow additionally runs the compiled namespace axiom audit.
The local research container lacked Lean; the reported formal execution was in
Actions. **Independent human semantic review (#8) and a second proof kernel are
still absent.** Formal statement checking is not a mathematical novelty claim.
The next autonomous mathematical task is n11's faithful degree interface (#11),
not redoing completed n10 (#10).

## Preserved historical ledger

The full previous ledger is archived byte-identically as
[2026-10-18-pre-n10-ledger.md](reports/2026-10-18-pre-n10-ledger.md), Git blob
`1dd727cd960d10570dde0b307b287fb50113cec4`. It retains all n5..9 evidence,
earlier archived ledgers, failure history and original source hashes. Its old
pending statements are historical, not the current n10 status. No earlier
proof artifact, statement or failed direction was deleted.
