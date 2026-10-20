# Conclusion: generic balanced affine obstruction formally verified

Approved2026-10-21 JST session. The original GF(2), pointwise error1/3 predicate
now has an accepted proof that degree-at-most-one is impossible for EVERY
integer n>=7. This is a generic theorem with a structural counting proof,
not an extrapolation of finite computations. Exact degree-two equalities remain
n5..11; no unbounded-n upper bound is supplied.

## Mathematical chain completed

1. Inclusion-exclusion proves the arbitrary finite real ordered-triple moment
   S^3-3QS+2R. Taking all entries1 gives n(n-1)(n-2) distinct ordered triples.
2. A tagged singleton/ordered-triple sample measure is nonnegative and sums to1
   for n>=3. Repeated-coordinate triples carry zero mass. Its map produces
   actual Boolean inputs, not a free score surrogate.
3. Original affineValue/target evaluation on those inputs gives the exact
   single/triple sign identities. With k the coefficient Hamming weight and
   t=n-2k, the constant-zero score is
   1/2+t(n^2-t^2)/(4n(n-1)(n-2)); constant-one score is complementary.
4. Pascal induction proves choose2/choose3 cast identities. Actual singleton
   success count is n-k; actual ordered-triple success count is
   6*(k*choose(n-k,2)+choose(k,3)). The binomial score is connected to actual
   correctness, with small-support cases and nonzero denominators justified.
5. For every fixed n>=7, all affine rows share the bound
   B(n)=1/2+(2n^3/5)/(4n(n-1)(n-2))<2/3. Structural degree-one normal form and
   existing finite REAL duality exclude any finite nonnegative normalized
   mixture of actual totalDegree<=1 polynomials chosen before all inputs.
6. The actual-cube pushforward adds duplicate fiber masses and preserves the
   mean of every real function. Positivity, normalization and the polynomial
   input bound are proved. No injectivity or unproved fiber uniformity is used.

The accepted endpoint is BalancedAffineCounting.degree_one_impossible, with
its only size hypothesis7<=n and the unchanged HasProbabilisticDegreeAtMost
predicate. no_degree_one_family additionally states the arbitrary finite REAL
mixture version directly. six_balanced_dual_tight checks the actual n6 affine
row [1,0,0,0,0,0], whose score is exactly2/3.

## Actual verification and attacks

Accepted codedc58ea7d, completed SUCCESS formal run39510465687/job118929907745:
pinned Lean4.35.0-rc4/Mathlib9e6b3aac, --wfail9048 jobs,589 allowlisted namespace
declarations and29 explicit new targets. Full completed log, all four actual
source files and matching commit/tree were fetched. See ci-evidence.md and the
attributed axiom-report.txt. Five earlier failed candidate builds were not
promoted; exact defects and repairs remain in graveyard022..024.

Independent standard-library code31778484 passed actual exact run39507686566/
job118920623125, including normal/-O byte equality and saved/actual result equality.
It checks1093 moment vectors,3031040 actual affine/input evaluations for n3..12,
and33147 formula cases for n3..256. Those tests retain their bounded scope.

Overcounting shortcuts fail concretely: omitting the double-diagonal correction
gives0 instead of6; using an unordered denominator on ordered triples gives
mass7/2; allowing repeated triples gives11/4. graveyard021 preserves these.
Extending this particular strict-gap dual to n6 is false: its score can equal
2/3. This does not refute the earlier n6 degree equality or alternative duals.

## Completion boundary and next frontier

The core objective of #12 is implemented through the valid ordered-sample
representation and its actual-cube pushforward. The separately named point-mass
formula '1/(2n) on weight1,1/(2choose(n,3)) on weight3,0 otherwise' is NOT a new
compiled theorem in these files. Its explicit fiber proof, half-layer mean
interface and subsequent generic intersection counting are separated into #13.
They are not assumed in the accepted obstruction. Do not redo that completed
chain merely because this additional representation theorem remains open.

Independent human semantic review remains open in #8. No second proof kernel,
mathematical novelty, support or denominator optimality, n12 degree equality,
all-n degree2 upper bound, circuit lower bound, proof-barrier escape or P-vs-NP
resolution is claimed. This is a reusable explicit dual/counting reconstruction,
not a claimed new asymptotic complexity landmark. All research writes succeeded;
no unapplied patch or write-permission blocker remains. Future sessions still
require fresh approval.
