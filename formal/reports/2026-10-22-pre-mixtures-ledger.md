# Formal assumption ledger

## Current checkpoint: certified clique layer profiles, 2026-10-21 JST night

Accepted numerical exact degree2 equalities remain n5..11, GF(2), pointwise
error1/3. The generic degree<=1 exclusion for every integer n>=7, balanced
input fibers and guarded intersection counts remain accepted and unchanged.
NEW: arbitrary-real weighted Hamming-layer profiles are connected to genuine
elementary symmetric and clique-quadratic MvPolynomial evaluation and degree.
This is an evaluator theorem, not arbitrary-n quadratic approximation success.

## Actual accepted execution

Code9785a2705cc88efd372ab3de29a61007387bd91d,
tree290f6b6e8196d2898d8612b0e1bbd0d2820462c7.
Completed SUCCESS run39615053307/job119273743612:
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39615053307
Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Whole-root --wfail9052 jobs;695 namespace declarations;26 new explicit target
reports plus all earlier targets within [propext,Classical.choice,Quot.sound].

The complete actual log, entire source files and matching Git commit/tree were
re-fetched. Evidence commit571b66370eda2be3ff9a00c7431870305b03e4f4 saves actual
attributed output in Expedition022/axiom-report.txt and ci-formal-evidence.md.
No source-generated report, partial build or finite checker was used as proof
acceptance. No warning or axiom policy was weakened.

Re-fetched source blobs:
HammingProfiles.lean:bd1be55aa6605d53cbee78313af662dab5e10f60
CliqueProfiles.lean:22634fba45b6bf3089354a261fd9515ed33bc232

## Faithful statement chain

HammingProfiles partitions an ACTUAL Layer n w by overlap with an actual
coordinate subset A. Previously proved Boolean intersection cardinalities
supply choose(|A|,r)*choose(n-|A|,w-r), with r in0..w. Every real score h is
allowed, including negative values. The sum theorem assumes neither symmetry
of h nor the desired identity. The totalized mean divides by choose(n,w).
Positive denominator and probability normalization require w<=n; empty layers
have totalized value0, explicitly not a normalized probability measure.

CliqueProfiles defines subsetMonomial using a Finset product, and elementary
A d using d-element subsets. It proves actual MvPolynomial.totalDegree<=d and
actual GF(2) evaluation equal to a natural binomial count cast into the field.
No ordered-edge double counting or division by2 in characteristic2 is used.
The formulas for q_A=1+sum_all X_i+clique(A) and
r_A=1+sum_outside_A X_i+clique(A) have proved degree<=2 and actual evaluation.
Their correctness is compared against the ORIGINAL MOD3 target before applying
the generic weighted sums/means. Full symmetrization is still needed to turn
suitable layer bounds into a fixed pointwise polynomial mixture.

The original target, family-before-input predicate, totalDegree and normalized
nonnegative REAL probabilities are unchanged. Generic parameterized evaluation
does not imply success>=2/3 at every arity or for every parameter choice.

## Exact finite corroboration and separately scoped obstruction

Exact run39614264276/job119270959043 at d65bfec7 reproduces174762 q/r evaluations,
1022 Mobius checks,4608 signed layer cases,41870 elementary integer counts,
4096 n11 canonical-row comparisons and134 coefficient mutations. Normal/-O and
actual/saved output agree. This independent implementation is by the same author,
not a second reviewer or a proof for all n. Source/result/commit were re-fetched.
The old n11 masks match the intended q8/r7 values on all inputs, but no new Lean
polynomial-equality bridge to those literal coefficient encodings was compiled.

A fixed n11-to-n12 clique lift fails at weight10 with19/33. More strongly, a
finite dual bounds ALL716 zero/q9/r8 n12 polynomials by9/14<2/3, so reweighting
within THIS family cannot repair it. Completed run39616486615/job119278821696
at9673b206 reproduces both attacks, with708840 restricted-family/input checks,
independent formulas, normal/-O and saved/actual equality. Re-fetched scripts,
results and commit match local source/canonical-output Git blobs. See
Expedition022/ci-attack-evidence.md and graveyard031/032.

This restricted-family dual is exact finite evidence plus a weak-duality
argument, NOT a separately compiled Lean corollary. Issue16 requests that
formal integration and a reusable mixture interface without dropping the
support restriction. It neither excludes all quadratics nor determines n12
degree. The 496-row old n11 quotient also retains its separately bounded scope.

## Failures and review status

Inspected formal failures: e6fd5ff3 extra closed-goal tactic, d65bfec7 addition
order mismatch; graveyard028/030. fd41fdf7 inherited the failed prefix, but its
own run was not inspected. Graveyard029 preserves ordered-edge, normalization
and constant-term shortcuts. No mathematical target was weakened to pass.

Gemini's independent AI semantic audit and corrected addendum in Issue15 cover
only checkpoint0e30b5b7. The new modules were NOT covered by that review. See
reviews/2026-10-21-gemini-review-scope.md for provenance and limits. Independent
AI review is legitimate evidence, not merely agreement; it is also not a local
Lean rerun or a second kernel. External human academic review #8 is separate
and nonblocking. New-code independent review, second-kernel validation and
novelty assessment are absent. No new reviewer is requested at this milestone.

Reproduce from formal/: lake build --wfail; ./scripts/axiom_report.sh, plus
production namespace audit. Local Lean is absent; actual accepted execution
used Actions. No write-permission blocker or unapplied patch remains.

## Preserved history

The preceding assumption ledger is archived BYTE-IDENTICALLY in
reports/2026-10-21-pre-profiles-ledger.md, blob
2cd0d59b36d6285c3f2641e9cf1ecd3aee3cb1a4. It retains the complete older evidence,
archives and failure links. Historical pending statements are not live blockers.

Issue14 is complete; Issue16 is the earliest unblocked implementation frontier.
No novelty, support/denominator optimality, n12 degree determination, all-n
degree2 upper bound, circuit lower bound, proof-barrier escape or P-vs-NP result.
