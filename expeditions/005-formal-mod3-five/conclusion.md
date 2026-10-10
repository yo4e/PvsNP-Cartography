# Conclusion: concrete n=5 certificate components are Lean-checked

Date: 2026-10-10 (JST). Issue #8 remains open.
Evidence class: formally verified components under the audited foundational
axioms; independent executable data audit; no independent human review.

## What is proved in Lean

1. The complete five-bit input type has 32 values, and the canonical affine
   coefficient type has 64 choices. The input integer masses sum to 180.
   Every affine weighted correctness sum is <=110. After dividing by 180,
   the deterministic bound 11/18 is strictly below the target 2/3.
2. The generic finite-duality lemma is applied with that bound discharged,
   not assumed. `no_affine_approximation` excludes all normalized real
   mixtures on the coefficient type. `no_affine_polynomial_family` expresses
   the same obstruction for arbitrary finite indexed families, with genuine
   GF(2) polynomial evaluations and repeated rows allowed.
3. `upper_integer_bound` checks each of the 32 inputs against 30 explicitly
   listed quadratic formulas. At least 21 agree at each input.
   `upper_degree` proves their Mathlib totalDegree <=2; evaluation lemmas
   connect the integer checker to actual MvPolynomial (Fin 5) (ZMod 2).
   `exists_quadratic_approximation` supplies a normalized nonnegative
   finite-support real distribution with pointwise success at least 2/3.
   A stronger intermediate bound is 7/10.
4. A concrete singleton countermodel explains why removing normalization
   from the input distribution would invalidate the weak-duality claim.

The upper proof does not assume symmetry or a layer-to-pointwise transfer.
It directly checks every input. A separate Python audit reconstructs all
120 permutations of the original (1,27,829) representative, finds 30 distinct
polynomials of equal multiplicity four, and verifies the stronger pointwise
profile [1,4/5,7/10,7/10,1,1].

## What is not yet proved in the formal interface

The lower theorem uses the explicit canonical affine representation.
The general normal-form theorem mapping ANY Mathlib polynomial with
`totalDegree <=1` into that representation is not yet integrated.
An abstract probabilistic-degree definition and equality theorem have not
been assembled. Thus do not describe this commit as a completed abstract
Lean theorem `pdeg(MOD3^5)=2`, or as formal completion of n=6,7,8.

The ordinary mathematical n=5 result was already established by Expedition
002. This session improves its formal verification, not its numerical value
or novelty status. No general-n, circuit lower-bound or P-versus-NP claim.

## Actual verification evidence

Code commit: 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872.

- Lean CI: [run 38055370947](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370947),
  job 114222616643, success. Pinned Lean 4.35.0-rc4 / Mathlib
  9e6b3aac99b624d10c84653ab9c5357283b9b3b8, build with --wfail.
  All 64 namespace declarations passed the compiled axiom audit.
  All new printed targets depend only on propext, Classical.choice,
  Quot.sound. See ../../formal/reports/2026-10-10-mod3-five-axioms.txt.
- Semantic CI: [run 38055370864](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370864),
  job 114222616310, success, normal Python and python -O. Exact counts,
  orbit coverage, two evaluators, and three negative controls agree.
  See audit-output.txt for attributed stdout.
- The source files, blob hashes and code commit were re-fetched after
  verification. Local files had matching Git blob hashes.

The Python algorithms were written by the same research lead as the Lean
code. Different algorithms and a separate runner reduce some errors; they
are not an independent human semantic review or a second proof kernel.

## Next frontier

Prove and audit the degree-one normal-form bridge; package the components
under a faithful degree-based definition; then extend to n=6 and n=7.
A generic symmetry theorem may improve scaling, but is not needed to
justify the present direct pointwise upper witness.
