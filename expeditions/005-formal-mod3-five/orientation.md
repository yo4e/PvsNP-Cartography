# Expedition 005: faithful n=5 formal certificate components

Date: 2026-10-10 (JST). Issue #8.
Initial status: concrete affine lower theorem passed CI; upper and field bridge
verification are being completed. Do not infer acceptance from file existence.
Novelty: not claimed; this reconstructs Expedition 002's finite certificate.

## Target

MOD3(x)=1 iff the Hamming weight of a five-bit input is divisible by three.
The target error is 1/3 at EVERY input. Coefficients are in GF(2).
Probabilities are real, not implicitly restricted to rational numbers.
The standard definition is Definition 1 of Srinivasan, Tripathi and Venkitesh,
FSTTCS 2019, https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28.

## Lower component

Use the full Cube = Fin 5 -> Fin 2 and Affine = Fin 2 x Cube types.
Integer mass by input weight is [0,12,3,7,2,10], divided by 180.
Kernel reduction checks the mass sum and all 64 affine weighted scores <=110.
The previously verified real-mixture finite_dual_obstruction lemma then
excludes all normalized real mixtures, with strict gap 2/3 - 11/18 = 1/18.
The field bridge relates the correctness bit to evaluation of actual
Mathlib multivariate affine polynomials, including arbitrary finite families
with repetitions in their coefficient choices.

## Upper component

The original (constant,linear,quadratic) masks (1,27,829) have 30 distinct
variable-permutation images, each occurring four times among 120 permutations.
Choose uniformly from the 30 displayed polynomials. The Lean checker verifies
all 32 inputs directly: at least 21 of 30 polynomials agree at each input.
Then it proves that the displayed formulas are genuine MvPolynomial objects
with totalDegree <=2 and converts counts to real pointwise probabilities.

This direct proof deliberately avoids relying on an unproved group-action
lemma. Orbit equivalence is an additional Python data audit, not a premise
of the formal upper guarantee.

## Boundary to keep visible

The lower theorem quantifies over the canonical affine coefficient type.
A general Mathlib normal-form theorem reducing an arbitrary polynomial
with totalDegree <=1 to that type has not yet been integrated. Nor has an
abstract probabilistic-degree definition been joined to these two components.
A generic symmetrization theorem, n=6/n=7 formal extension and external
human semantic review remain separate tasks. Do not close Issue #8.
