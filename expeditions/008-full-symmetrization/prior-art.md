# Primary-source and novelty audit

Read on 2026-10-13 JST by the author. This is a targeted definition/library
check, not an exhaustive novelty search or independent mathematical review.

## Definition fidelity

Srikanth Srinivasan, Utkarsh Tripathi and S. Venkitesh,
*On the Probabilistic Degrees of Symmetric Boolean functions*,
arXiv:1910.02465v1, 6 October 2019, Definition 1.
Source inspected: https://arxiv.org/html/1910.02465v1

The definition uses a finite-support distribution over polynomials in a
specified coefficient field, an error bound separately at every Boolean
input, and a degree bound on the support. Our GF(2) predicate is this
specialization, with real probability weights and success at least 1-epsilon.
The formal transport theorem permits any real epsilon algebraically; its
probabilistic-degree interpretation uses an admissible error parameter.
This source supports the definition, not novelty of the present artifacts.

## Existing library identities

Pinned Mathlib revision: 9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
The following source files and declarations were read:

- Mathlib/Algebra/MvPolynomial/Rename.lean: eval_rename.
- Mathlib/Algebra/MvPolynomial/Degrees.lean: totalDegree_renameEquiv.
- Equiv.sum_comp supplies finite reindexing; specifying Equiv explicitly
  avoids selecting a different Perm-specific finset lemma by dot notation.

Stable source tree:
https://github.com/leanprover-community/mathlib4/tree/9e6b3aac99b624d10c84653ab9c5357283b9b3b8

The rename identities and uniform finite-group averaging are existing
mathematical tools. The contribution recorded here is their explicit,
assumption-audited integration with this repository's degree predicate,
applications, executable attacks and reproducible verification. We do not
claim to have discovered group averaging or any new MOD3 degree value.
Novelty of this particular presentation has not been established.
