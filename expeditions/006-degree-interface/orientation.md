# Expedition 006: degree-based interface and coverage

Approved nightly session following the 2026-10-10 checkpoint; Issue #8.
Initial status: candidate formal code, CI not yet observed for this change.

Read AGENTS.md and all five required documents, current open Issues,
recent commits and the 2026-10-10 session log. Starting head:
845eceb717bc498f1bfe8cccaa0e9a4d7ea757b3.

The immediate target is the missing structural normal form: every actual
Mathlib MvPolynomial of totalDegree <= 1 must equal a member of the complete
affine coefficient representation. The deterministic bound from Expedition
005 must be discharged, never reintroduced as an assumed target conclusion.
Then assemble the standard finite-support, real-probability, pointwise
probabilistic-degree predicate and prove its n=5 degree threshold is exactly 2.

Primary definition: Srinivasan, Tripathi, Venkitesh, FSTTCS 2019, Definition 1,
https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28 (page 28:2 inspected).
The definition permits finite-support distributions and requires the same
distribution for every input. Probabilities are real, not restricted to rationals.
Official mathlib documentation and the pinned source were inspected for
MvPolynomial degrees and the Finsupp/multiset exponent correspondence.

Local runtime has no Lean/Lake and raw GitHub network resolution failed.
Use the existing pinned GitHub Actions build and axiom audit for execution.
A commit is not a successful proof until the actual completed CI output is read.
No novelty, new finite value, general-n complexity conclusion or P-vs-NP claim.
