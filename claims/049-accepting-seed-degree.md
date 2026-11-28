---
id: 049-accepting-seed-degree
status: candidate-survives
statement: Under the stated honest cutoff and field margin, the BV canonical A preserves the satisfying assignment's Boolean degree, the forced quotient B and one public outer circuit have controlled degree overhead; compiler-created distance obstructions need not obstruct actual low-degree clause counting.
dependencies:
  - Ben-Sasson and Viola TR14-017 equations 2–5 and Claims 5.4–5.5
  - Carlet Boolean Functions for Cryptography and Coding Theory Proposition 6
  - expeditions/038-recursive-query-fibers/source-compiler.md
  - expeditions/041-two-level-distance/two_level_oracle.py
  - expeditions/048-recursive-row-normalization/normalization.md
novelty: novelty-unknown
last_attacked: 2026-11-28
---

## Written claims, not formal acceptance

1. On an affine domain U, the unique ordinary-degree-less-than-|U|
   interpolant of any field-valued assignment preserves its Boolean vectorial
   degree. An affine-subspace selector `Z_H/Z_U` has exact Boolean degree
   `dim H-dim U`; a public Frobenius circuit controls its intermediates.
2. For monic affine-linearized L of degree S, long division lowers the
   `floor(e/S)+popcount(e mod S)` filtration by at least one. If
   `Q=LB` and `deg Q<3S<|F|`, then `deg_2 B<=deg_2 Q`.
3. In the displayed BV outer residual, a satisfying A of ordinary degree
   at most `S/2` and Boolean degree r gives `deg_2 B<=D0`, where
   `D0=max(c+3r,1+r)` and c is the clause-selector codimension. One public
   polynomial-size Boolean outer circuit has honest gate degree at most
   `D0+1`. This is not a claim about the full recursive verifier.
4. Fixed-node q-adic expansion preserves binary-weight degree. In the actual
   two-level GF(256) oracle, its fixed low spaces and affine coordinates imply
   degree preservation for all honest root polynomials of degree less than
   32. No arbitrary-depth conclusion is inferred.
5. A shared live cancellation cone preserves the exact raw minimum of a
   unit-weight signed verifier while changing honest gate rows. The explicit
   bent control has minimum affine proof-distance charges exceeding the raw
   NO gap, but minimum actual affine failure eight below the half-gap sixteen.
   Thus the sufficient approximation criterion is not necessary.

## Evidence and attacks

See [the derivation](../expeditions/049-accepting-seed-degree/linearized-degree.md),
[accepting family](../expeditions/049-accepting-seed-degree/accepting-family.md),
[extension proof](../expeditions/049-accepting-seed-degree/honest-extension-degree.md)
and [signed controls](../expeditions/049-accepting-seed-degree/auxiliary-artifacts.md).
Finite enumerations are separately recorded in four inspectable programs and
their exact outputs. The source constants, field arithmetic reuse and scope
are explicit. The lead inspected all branches; same-model branches are not
independent external review. No Lean acceptance is claimed.

The preserved failures include uncontrolled quotient ratios, interpolation
error expansion, an affine-A toy mistaken for a growing Boolean assignment,
compiler-independent degree inference, and the reverse implication from
approximation distance to actual counting failure. See the
[graveyard](../graveyard/2026-11-28-night-witness-degree-shortcuts.md).
