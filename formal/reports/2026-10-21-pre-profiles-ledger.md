# Formal assumption ledger

## Current checkpoint: accepted fibers and Hamming intersections, 2026-10-21 JST

This ledger supplements, not replaces, the previously accepted generic
n>=7 degree-one obstruction and numerical n5..11 exact degree2 results.
The full previous ledger is archived byte-identically in
[reports/2026-10-21-pre-fibers-ledger.md](reports/2026-10-21-pre-fibers-ledger.md),
Git blob8e3dcf59ebf3df961e2bc6eeef6b13519eff0032. Its older pending #13 status
is historical. Earlier ledgers and all proof/failure artifacts remain retained.

## Actual production acceptance

Accepted code:598d54ed0940a331650b7e7eb733d62c9b6e40ab.
Tree:a9f26fbece775a5ad11e5cc8b84b5d31dac22341.
Completed SUCCESS [run39547776930](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39547776930),
job119049747106. Pinned Lean4.35.0-rc4 and Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8. --wfail root build9050 jobs;
639 namespace declarations within [propext,Classical.choice,Quot.sound].
All12 new explicit targets and all preceding target reports completed.

The full actual job log, two entire source files, final theorem statements
and matching Git commit/tree were retrieved and inspected. Actual timestamped
output is [Expedition021/axiom-report.txt](../expeditions/021-balanced-fibers/axiom-report.txt).
The saved report was also re-fetched, blob102ce578e960de6a858ae18964fac1f3cc48ff3b.
The record-only commit3e464878 does not change the accepted Lean sources.
Later documentation commits are not asserted to be separate proof executions.

Source correspondence:

| File in PvsNPCartography/ | Git blob | SHA256 |
|---|---|---|
| BalancedAffineFibers.lean | 25445a5d2bd6f38de932cf7b2d934ae7942adb38 | d72452628ac1ef133e4e69e61f79ce8bec30e1bd7298c1410b6e9f795e9b0374 |
| HammingIntersections.lean | 21065c45b75967971b19a0c852cf85a685c57c77 | e82185e0639a03e502cee7bb46d867e389027f7403441fda2ed0bfc9ca5a4500 |

## Statement fidelity and dependency direction

BalancedAffineFibers identifies the EXISTING inputMass, the pushforward of
tagged singleton/ordered-triple samples. Repeated coordinates have zero mass;
all samples with the same actual bits-support input contribute their masses.
Singleton fibers have cardinality1 at weight1, distinct-triple fibers6 at
weight3, zero otherwise. The generic indicator moment proves these counts,
not a finite enumerator or assumed uniformity hypothesis.

For n>=3, inputMass x is1/(2n) at weight1,1/(2 choose(n,3)) at weight3 and0
elsewhere. All necessary nonzero denominators are justified. For every real
function g, expectation equals half of each layer mean. There is no hidden
nonnegative or symmetric-function assumption. The fiber counts and decomposed
formula themselves are valid at all n. At n2, normalization fails; that does
not refute every bare mean identity with totalized empty-layer division.

HammingIntersections defines actual subset fibers and proves splitEquiv by
intersection/difference with inverse disjoint union. The guard r<=w is needed
because Nat subtraction truncates. The total cardinality is
choose(|A|,r)*choose(n-|A|,w-r) if r<=w,0 otherwise, with empty/impossible cases
included. The Boolean version uses the proved bits/ones bijection. The n1,w0,r1
zero-versus-one counterexample to the unguarded formula is also accepted.

No previous GF(2) coefficient field, actual totalDegree, normalized REAL
probability, family-before-input quantifier or foundational axiom was changed.
The prior generic lower obstruction does not depend on the new closed formula;
these new tools are an explicit representation and reusable counting interface.

## Complementary computation and rejected candidates

Exact code da8538d3 passed SUCCESS39546665458/job119046262844. Normal/-O actual
outputs agree bytewise and equal saved JSON. All8191 inputs for n0..12 and
1,398,101 subset pairs n0..10 are checked, including signed-score tests and
three invalid shortcuts. Bounded exact tests are not generic formal proofs.
See Expedition021/ci-finite-evidence.md for parameters and actual excerpts.

First code9abc8c23 failed conditional elaboration and warning checks; second
2404af3d failed one conditional rewrite plus warnings. Full failed logs were
inspected and graveyard026/027 preserve the repairs. The second run's partial
intersection build was not promoted before whole-root and audit completion.
No --wfail/axiom setting was relaxed and no desired conclusion was assumed.

## Prior accepted scope and remaining gates

Expedition020/code dc58ea7d, SUCCESS39510465687/job118929907745,589 declarations,
29 targets supplies the generic actual-degree-one obstruction for all n>=7.
Numerical exact degree2 coverage remains n5..11; earlier evidence is retained
in the archived ledger. The separately computed n11 quotient is not newly
formalized by the present generic intersection theorem.

#13 is completed. #14 is the next unimplemented weighted-layer-profile and
actual-polynomial connection. #8 remains independent human semantic review.
Another runner, author self-audit or model agreement is not that review.
A second proof kernel and mathematical novelty assessment are absent.

Reproduce from formal/: lake build --wfail; ./scripts/axiom_report.sh; the
production workflow additionally checks the compiled namespace allowlist.
Reported formal execution used Actions because local Lean was unavailable.
No optimality, n12 equality, arbitrary-n degree2 upper bound, new complexity
landmark, barrier escape or P-vs-NP result is asserted.
