# Expedition 006: degree-based interface and coverage

Approval night: 2026-10-11. Work and verification completed after midnight,
on 2026-10-12 JST. Issue #8.
Status: n=5 degree-based equality compiled and axiom-audited; larger-n work remains.
Novelty: unknown; this formalizes a previously recorded finite result.

Read AGENTS.md and all five required documents, current open Issues,
recent commits and the 2026-10-10 session log. Starting head:
845eceb717bc498f1bfe8cccaa0e9a4d7ea757b3.

The target was the missing structural normal form: every actual Mathlib
MvPolynomial of totalDegree <=1 must equal a member of the complete affine
coefficient representation. Then assemble the standard finite-support,
real-probability, pointwise definition and prove the n=5 least degree is 2.
The deterministic bound from Expedition 005 is discharged, not assumed anew.

Primary definition: Srinivasan, Tripathi, Venkitesh, FSTTCS 2019, Definition 1,
https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28 (printed page 28:2 inspected).
The definition permits finite-support distributions and requires the same
distribution for every input. Probabilities are real, not restricted to rationals.
Official mathlib documentation and the pinned source were inspected for
MvPolynomial degrees, Finsupp/multiset exponents, ZMod casts and Nat.find.

Local runtime has no Lean/Lake and raw GitHub network resolution failed.
Formal execution used the existing pinned GitHub Actions build and axiom audit.
Initial commit 6178308 was a candidate, not a completed proof; its failed build
was repaired in 512aaf2. Actual completed logs were read before promotion.
See conclusion.md, log.md and statement-audit.md for evidence and boundaries.
