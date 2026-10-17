# Statement audit: n=10 interface

Evidence status at this checkpoint: exact independent Python verification;
Lean source committed, CI execution pending. Do not promote before completed
run logs and axiom reports are inspected.

## Exact mathematical object
The function is one iff the integer Hamming weight is divisible by three.
The coefficient field is GF(2), not real polynomial approximation. Polynomial
degree means MvPolynomial.totalDegree. Real nonnegative mixture probabilities
sum to one, and the family is selected before every input quantifier.

The eight block codes in Expedition013 were converted independently by querying
the block evaluator at weights zero, one and two, recovering all ANF coefficients.
All 1024 inputs then match explicit monomial evaluation and a full Mobius
transform; lexicographic 45-edge rows and the actual Lean literals agree.
Stored weights [10,2,39,22,15,6,4,2]/100 become triple tickets divided by300.
The eleven exact layer ticket totals are saved in finite-result.json.

## Upper chain
polynomial_degree / polynomial_eval -> seed_correct -> seed_success ->
layer_tickets_exact -> seed_layer_bound -> feasible_of_layer_bounds ->
degree_two_feasible. The existing Hamming-layer theorem supplies one product
distribution over ALL permutations, not an input-conditioned choice.

## Lower chain
mass_sum -> canonical_affine_bound -> proved coefficient-permutation and score
invariance -> affine_bound -> structural degree_one_normal_form through
no_degree_one_family -> degree_one_impossible. The twenty-two canonical checks
cover all2048 affine coefficient rows. The final obstruction applies to ALL
finite real mixtures of degree-at-most-one polynomial objects. It does not
merely exclude a searched list. The strict gap is 152/240=19/30<2/3.

## Interface and attack
feasible_degree_iff, least_feasible_degree and pdeg_eq_two use actual upper/lower
proofs, not desired-result assumptions. The original finite-family definition
and layer adapter were read directly. Quantifier reversal is already refuted in
ProbabilisticDegree.input_dependent_constant. At input mask832 the raw eight
seeds without permutations succeed only6/300=1/50. All448 single-coefficient
mutations are detected. Normal and optimized Python outputs agree.

Residual gates: actual Lean completion/axiom audit, independent human semantic
review, and novelty. Computational agreement is not independent human review.
