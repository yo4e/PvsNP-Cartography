# Attack: n=5 statement fidelity and proof dependencies

Date: 2026-10-10. Role: Skeptic.

## Full inputs versus layers

Cube is Fin 5 -> Fin 2. It has 32 inhabitants. The upper_integer_bound
statement quantifies over all of them, not merely six Hamming weights.
Thus 21/30 is a per-input guarantee. The stronger profile is independently
checked in Python but is not needed for the formal inequality.

## Full coefficients versus a sample

Affine is Fin 2 x (Fin 5 -> Fin 2). All 64 binary constant/linear coefficient
choices are included. The deterministic q-average upper bound is proved in
Lean, not passed as a premise of the concrete obstruction theorem.
Arbitrary finite families with repeated coefficient rows are also covered.

Residual mapping: the repository still lacks a checked normal-form theorem
turning any Mathlib MvPolynomial of totalDegree <=1 into this coefficient
type. The ordinary argument is that only constant and unit-vector monomials
can occur. That general interface is not yet formalized here. Do not call
the current artifact a completed abstract pdeg equality theorem.

## Actual field, degree and target

The finite evaluator is checked against ZMod 2 arithmetic, including the
correctness/equality bit rather than only output values modulo two.
The upper formulas are genuine MvPolynomial (Fin 5) (ZMod 2) expressions.
Their degree <=2 follows from library degree bounds for constants, variables,
sums and products, not from an assumed label. MOD3 is 1 at weights zero
and three, including the zero input.

## Probabilities and quantifiers

The 30 upper polynomials are chosen uniformly before seeing x. The weights
do not vary with x. The lower mixture allows arbitrary real weights,
nonnegative and summing to one. Input-measure normalization and positivity
are proved. A zero-mass input measure would invalidate the obstruction if
normalization were removed; that deliberate mutation is archived.

## Trust boundary and controls

Closed finite arithmetic uses decide +kernel, not native_decide. Formal
acceptance comes from the successful pinned build and actual dependency
audit, not source-text absence of a placeholder. The final run audited
64 declarations with only propext, Classical.choice and Quot.sound.
The Python algorithms were authored by the same agent, so their agreement
is algorithmic replication, not independent human semantic review.

Controls: flipping all constants gives worst count 0/30; retaining only
(1,27,829) fails at x=(0,0,1,0,0); removing q-normalization is refuted by
I=X={0}, payoff=mu=1, q=b=0, t=2/3. The actual theorem retains normalization.

No counterexample to the retained components was found. No global success
optimum, minimum support, novelty or asymptotic conclusion is inferred.
