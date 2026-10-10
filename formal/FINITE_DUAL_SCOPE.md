# Finite dual obstruction: exact scope and assumption audit

Updated: 2026-10-10. Issue #8.
Status: **generic lemma and concrete n=5 affine application compiled and
audited; arbitrary degree-one normal-form interface pending**.

finite_dual_obstruction proves a finite weighted-sum statement over REAL
probabilities. Given payoff A(i,x), normalized nonnegative row weights mu
and input weights q, if every deterministic row has q-average at most b<t,
no mu-mixture can have pointwise payoff at least t for every input.

The proof exchanges two finite sums. It assumes neither existence of an
optimal strategy, minimax equality nor an asymptotic theorem. It contains
no sorry, admit, project-specific axiom, native_decide or external oracle.
Its foundational dependencies are propext, Classical.choice and Quot.sound.
The deterministic-row bound is an explicit certificate premise, not an
assumption that randomized polynomials are already impossible.

## Statement-fidelity attack

- `forall i` is over the supplied finite type I. A sampled type excludes
  only that sample. The lemma cannot repair graveyard/002 by itself.
- The negated conclusion quantifies over EVERY input x, not input-average
  deterministic error.
- mu and q are real, so irrational mixture probabilities are not excluded.
- Both normalization and nonnegativity are explicit. Omitting q-normalization
  is refuted by a singleton payoff-one, mu-one, q-zero countermodel.
- The generic theorem does not itself define fields, degrees or polynomials.

## Concrete application added on 2026-10-10

Mod3Five.lean uses all 64 binary constant/linear coefficient choices and all
32 inputs. It proves the input normalization and each deterministic bound
before applying the generic theorem. Mod3FiveBridge.lean proves that the
correctness bits are actual GF(2) polynomial evaluation agreements, and
extends the obstruction to arbitrary finite real-weighted affine families.

The degree-one normal-form map from arbitrary Mathlib MvPolynomial objects
to this representation remains to be proved. The n=5 upper witness is now
separately proved as actual degree-two polynomials with pointwise success,
using direct finite checking rather than an assumed symmetry theorem.
Issue #8 remains open for that general interface, larger n and semantic review.

[Final run 38055370947](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370947)
on code commit 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872 passed the pinned
build, 64-declaration audit and explicit target reports. Read
[ASSUMPTIONS.md](ASSUMPTIONS.md) and the retained report for exact dependencies.

## Historical generic verification

[Run 37940286899](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940286899)
on commit 97c459e04204b35f970f58b8cbab959986daa98e originally passed.
Its actual logs showed 11 declarations and the target's dependency list
[propext, Classical.choice, Quot.sound]. The generic source was re-fetched
with blob SHA c3f299b0c4a086042fd4228c93545a1993b2a589.
Semantic self-review is not independent human review, and no second kernel
checker was run. This standard weak-duality argument is not claimed novel.

## Relation to other finite results

The n=6,7,8 certificate arithmetic remains Python-checked rather than
Lean-instantiated. The n=5 progress must not silently promote those results,
or a general P-versus-NP claim, to formal verification.
