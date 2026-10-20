# Statement audit: generic balanced affine obstruction

Checkpoint2026-10-21 JST. This is the research author's semantic audit, NOT
independent human review. Formal production acceptance is recorded separately
and must not be inferred from this source audit. Current integration code:
6d91476aab2c11cb3c7d70223ac08ca5adca5aef; its run was pending when this audit
was written. Final conclusion/ci-evidence supersede this execution checkpoint.

## Actual objects and quantifiers

The target is SmallSupportMod3.target: GF(2) value1 iff integer input Hamming
weight is divisible by3. The field is NOT the real field used for probabilities.
BinaryPolynomial is the existing actual MvPolynomial type; totalDegree<=1 is
an actual polynomial-degree hypothesis. The final no_degree_one_family theorem
allows every finite index type and every nonnegative REAL weight vector summing
to1. The family and its weights are fixed before the universal input quantifier.
No rational-only search restriction, desired-score hypothesis, quotient
assumption, general-n numerical lookup table or optimizer premise is used.

## Why the ordered sample space is legitimate

Sample n is Fin n plus ordered triples of Fin n. Each singleton has mass1/(2n).
A pairwise-distinct triple has mass1/(2n(n-1)(n-2)); all repeated-index triples
have zero mass. sampleInput constructs a genuine Boolean input using bits of
the support set. Repeated indices can give another weight, but their score is
multiplied by zero. The proof does not silently treat them as weight3.

Normalization uses a structural identity on arbitrary finite real sequences:
S^3-3QS+2R is the sum over ordered distinct triples. The +2R correction is
proved pointwise by equality cases before summing. Taking all values1 gives
n(n-1)(n-2), including n0/1/2; normalization requires n>=3 explicitly.
The final impossibility theorem requires n>=7 explicitly.

Finite duality can use any finite input-index type, so sampleInput need not
be injective. The InputMeasure module additionally defines the actual-cube
pushforward by SUMMING all fiber masses and proves normalization, nonnegativity
and the expectation identity. Dropping duplicate masses is not used.
The separate closed point-mass formula 'exactly half uniform on weight1 and
half uniform on weight3' is not asserted to have its own fiber-cardinality
Lean theorem here. Its finite tests and elementary six-ordering interpretation
are distinguished from the implemented pushforward/expectation proof.

## Actual evaluation and counting, not a renamed surrogate

singleton_correct and triple_correct rewrite the original affineValue and
target on the actual bits input, then use checked two-/four-bit GF(2) identities.
Their real signs are1-2b; a sign is never substituted for a probability.
For coefficient weightk, the sign sum is n-2k, sum of squares is n and sum
of cubes is n-2k. This proves the actual sampleScore_formula structurally.
Constant0 agrees with the previously accepted algebraic score; constant1
agrees with its complement, equivalently score(n,n-k).

The binomial module proves casts of choose2 and choose3 by Pascal induction,
including small k, before clearing nonzero denominators for n>=3. The candidate
InputMeasure module proves actual singleton success count n-k and ordered
triple success count6*(k*choose(n-k,2)+choose(k,3)), with k bounded by n via
hammingWeight_le. actual_score_binomial connects the binomial expression to
actual weighted Boolean-cube correctness. It is not merely an identity between
two independently defined formulas.

## Common gap and full degree coverage

A single bound B(n)=1/2+(2n^3/5)/(4n(n-1)(n-2)) works for ALL coefficient rows
and both constants at a fixed n>=7. It is strictly below2/3. Proving a bound
for each row without a common threshold is not the argument used here.
Structural degree_one_eq_affine covers every actual degree<=1 polynomial.
The existing finite_dual_obstruction then excludes every finite REAL mixture.
The final degree_one_impossible uses the original HasProbabilisticDegreeAtMost
predicate; it does not introduce a weaker replacement definition.

## Attacks and exclusions

The independent exact checker explicitly rejects missing diagonal correction,
wrong ordered/unordered denominator and nonzero mass on repeated triples.
At n6,k1 the particular balanced dual reaches2/3, so strict-gap extension to6
is false. The original n5/n6 degree equalities are not contradicted.
Compiler-error recovery placeholders from failed builds are never accepted;
--wfail and the unchanged [propext,Classical.choice,Quot.sound] allowlist remain
mandatory. Only the final actual completed build can settle formal acceptance.

No degree-two upper bound for unbounded n, new complexity-class separation,
minimum support, optimum dual, proof-barrier escape or mathematical novelty
is claimed. Numerical exact-degree equalities remain n5..11. A generic affine
exclusion is a useful reusable explicit dual proof, not a new asymptotic landmark.
