# Barrier and prior-art boundary

This expedition is exact finite-set probability/counting infrastructure at
arbitrary natural arity. It supplies neither an oracle separation nor a large
constructive property useful against unrestricted circuits nor a demonstrated
non-algebrizing step. Relativization, Natural Proofs and algebrization are not
claimed escaped. The already accepted degree-one obstruction remains unchanged.

The powerset and binomial cardinality lemmas are standard Mathlib infrastructure.
Official Mathlib documentation for Data.Finset.Powerset and Data.Finset.Card
was inspected for cardinality and subset APIs. The implementation is checked
against this project's pinned Mathlib9e6b3aac, not assumed compatible merely
because current documentation shows a lemma name.

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Powerset.html
https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Card.html

The intersection formula is the standard choose-inside/choose-outside count.
No mathematical novelty, minimal support, new asymptotic lower bound, arbitrary-n
degree-two upper bound or P-vs-NP conclusion is asserted.
