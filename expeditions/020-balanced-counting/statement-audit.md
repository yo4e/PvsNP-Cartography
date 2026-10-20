# Statement audit: accepted generic balanced affine obstruction

Final checkpoint2026-10-21 JST. This is the research author's semantic audit,
NOT independent human review. Actual production code dc58ea7d passed
run39510465687/job118929907745 with --wfail,589 namespace declarations and29
new explicit targets under the foundational allowlist. Completed output,
all four actual sources and matching commit/tree were re-fetched. See
ci-evidence.md/axiom-report.txt. The earlier pending audit is archived
byte-identically as statement-audit-pre-acceptance.md.

## Actual objects and quantifiers

The target is SmallSupportMod3.target: GF(2) value1 iff integer input Hamming
weight is divisible by3. Coefficients are not in the real probability field.
BinaryPolynomial is the existing actual MvPolynomial type and the hypothesis
is actual totalDegree<=1. no_degree_one_family allows any finite index type
and any nonnegative REAL probabilities summing to1. The family is fixed before
all inputs. No rational-only restriction, desired-score hypothesis, optimizer
premise, finite-n table or assumed quotient theorem is used.

## Counting and actual evaluation

Sample n is Fin n plus ordered triples. Mass is1/(2n) on each singleton,
1/(2n(n-1)(n-2)) on distinct triples and0 on repeated triples. sampleInput maps
to bits of the support set. Repeated triples do not necessarily map to weight3,
but their mass is zero and no positive-weight argument treats them as weight3.

Normalization is proved for n>=3 using the structural identity S^3-3QS+2R,
first proved by pointwise equality cases and then summed. The +2R correction
is essential. The all-ones count is valid even at n0/1/2; the normalizing
nonzero denominator conditions are not silently omitted.

singleton_correct and triple_correct rewrite original affineValue and target
on actual Boolean inputs. Their real-sign formulas are then proved by finite
GF(2) bit cases. With coefficient weightk and t=n-2k, sign sums and the generic
moment identity prove the actual sample score1/2+t(n^2-t^2)/(4n(n-1)(n-2))
for constant0. Constant1 is complementary. A sign is not used as a probability.

Pascal induction proves choose2/choose3 casts including small support sizes.
Actual singleton success count is n-k and ordered-triple success count is
6*(k*choose(n-k,2)+choose(k,3)). The binomial-to-cubic identity has n>=3,k<=n
and justified nonzero denominators. actual_score_binomial links that expression
to actual weighted correctness, rather than equating two free definitions.

## Input distribution and complete lower chain

Finite duality allows any finite input-index type, so sampleInput need not be
injective. The actual-cube inputMass also sums all sample fiber masses and has
proved positivity, normalization and expectation transport for every real
function. Duplicate masses are not dropped.

For each n>=7, a single B(n)=1/2+(2n^3/5)/(4n(n-1)(n-2)) bounds every affine row
and is strictly below2/3. Structural degree_one_eq_affine covers ALL actual
degree<=1 polynomial objects, not merely a search list. finite_dual_obstruction
excludes every finite REAL mixture. degree_one_impossible uses the unchanged
HasProbabilisticDegreeAtMost predicate with the explicit7<=n hypothesis.
No proof assumes feasibility, the desired score identity or the final bound.

## Explicit residual and attacks

A separately compiled closed formula for inputMass at each Hamming weight,
expressing half-uniform layer1/layer3 mass via fiber cardinalities, is NOT
present. #13 tracks that interface and general intersection counting. It is
not a premise of any accepted result here. Bounded half-uniformity checks are
not misrepresented as its generic formal proof.

The exact checker rejects missing diagonal correction, unordered denominator
on ordered triples and positive mass on repeated triples. The actual n6 affine
row reaching2/3 is also formally accepted. It refutes this distribution's strict
gap at n6, not earlier n6 degree equalities. Failed compiler recovery placeholders
were never accepted; warnings and deprecations were repaired instead of disabled.

The generic conclusion is degree-one exclusion, not a degree-two upper bound.
Exact degree2 equalities remain n5..11. Human review #8, a second kernel,
mathematical novelty, optimality, unrestricted circuit lower bounds and
P-vs-NP conclusions remain outside the evidence supplied.
