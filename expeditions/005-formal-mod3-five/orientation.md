# Expedition 005: faithful n=5 formal certificate components

Date: 2026-10-10 (JST). Issue #8.
Status: **concrete lower, upper and field bridge compiled and axiom-audited**.
The abstract degree-based interface remains unfinished; see conclusion.md.
Novelty: unknown for the underlying finite value; no new result claimed here.

## Target and definition

MOD3(x)=1 iff the Hamming weight of a five-bit input is divisible by three.
The error target is 1/3 at EVERY input. Coefficients are in GF(2).
Probabilities are real, not implicitly restricted to rational numbers.
The standard definition is Definition 1 of Srinivasan, Tripathi and Venkitesh,
FSTTCS 2019, https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28.
This session reconstructs Expedition 002's known-in-repository n=5 certificate.

## Lower component

Use the full Cube = Fin 5 -> Fin 2 and Affine = Fin 2 x Cube types.
Integer mass per input of weight w is [0,12,3,7,2,10][w], divided by 180.
Kernel reduction checks the total mass and all 64 affine weighted scores <=110.
The real-mixture finite_dual_obstruction lemma then excludes all normalized
real mixtures of those coefficients, with gap 2/3 - 11/18 = 1/18.
The field bridge proves that each correctness bit is the actual evaluation
agreement of a Mathlib multivariate affine polynomial over ZMod 2. It allows
arbitrary finite indexed families with repeated coefficient choices.

## Upper component

The original masks (constant,linear,quadratic)=(1,27,829) have 30 distinct
variable-permutation images, each occurring four times among 120 permutations.
Choose uniformly from the 30 displayed polynomials. Lean checks all 32
inputs directly: at least 21 of 30 polynomials agree at every input.
It also proves that the displayed formulas are genuine MvPolynomial objects
with totalDegree <=2 and converts the counts to real pointwise probabilities.

This direct proof does not depend on an unproved group-action lemma.
Orbit equivalence is an additional Python data audit, not a premise of the
formal upper guarantee. The support size is not claimed to be minimal.

## Verification and limits

[Lean run 38055370947](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370947)
and [semantic run 38055370864](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370864)
passed on code commit 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872.
The actual completed-job logs were read. Closed finite arithmetic uses
`decide +kernel`, not `native_decide`; the explicit target report contains
only propext, Classical.choice and Quot.sound. A different Python evaluator,
full orbit reconstruction and semantic negative controls passed too.

A general Mathlib normal-form proof reducing any polynomial of totalDegree
<=1 to the canonical affine type has not yet been integrated. Neither has
an abstract probabilistic-degree equality been assembled from these pieces.
Generic symmetrization, n=6/n=7 and independent human semantic review remain.
This is substantial concrete formal progress, not completion of Issue #8.
