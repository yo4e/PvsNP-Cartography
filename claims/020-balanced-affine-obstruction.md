---
id: balanced-affine-obstruction
status: formally-verified
statement: For every integer n>=7, GF(2) MOD3 has no pointwise error-at-most-1/3 finite REAL mixture of actual polynomials of totalDegree at most one.
dependencies: [formal/PvsNPCartography/BalancedAffineCounting.lean, formal/PvsNPCartography/BalancedAffineObstruction.lean, formal/PvsNPCartography/BalancedAffineBinomial.lean, formal/PvsNPCartography/BalancedAffineInputMeasure.lean, formal/PvsNPCartography/FiniteDual.lean, formal/PvsNPCartography/SmallSupportMod3.lean]
novelty: novelty-unknown
last_attacked: 2026-10-21
---

Accepted codedc58ea7dd4d3e2ed36ca5b7d8276de651d95aa08, SUCCESS formal
run39510465687/job118929907745: pinned --wfail9048 jobs,589 namespace
declarations and29 new explicit targets under [propext,Classical.choice,Quot.sound].
Actual completed logs, source statements and matching commit/tree re-fetched.
See Expedition020 conclusion, statement-audit, ci-evidence and axiom-report.

The generic proof uses structural ordered-triple inclusion-exclusion, normalized
REAL sample mass, actual GF(2) affine evaluation, a common strict score bound,
structural degree-one normal form and finite real duality. The polynomial
family and probabilities precede every input quantifier. No finite-n lookup
or assumed desired-score identity replaces the proof.

Additional accepted components include binomial score identification, actual
success counts, actual-cube pushforward and arbitrary-function expectation
transport. A separately named half-uniform closed point-mass/fiber theorem is
not implemented and is tracked in #13, not assumed here.

Finite tests have separate bounded scope:1093 moment vectors,3031040 actual
row/input checks n3..12 and33147 formula cases n3..256. The n6 boundary reaches
2/3 for this particular dual and is formally checked. Overcounting and failed
implementation attempts remain in graveyard021..024.

Independent human review (#8), a second kernel and novelty remain unfulfilled.
Exact degree2 equalities still cover n5..11; the new theorem is only a lower
obstruction for general n>=7. No new asymptotic lower-bound landmark, all-n
quadratic upper bound, optimal dual, support minimality or P-vs-NP result.
