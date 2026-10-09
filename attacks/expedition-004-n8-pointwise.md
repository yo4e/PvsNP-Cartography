# Attack: n=8 certificate quantifiers, masks, symmetry and probabilities

Date: 2026-10-09. Role: Skeptic. Target: Expedition 004.

1. Hidden sample restriction in lower bound? No. Every one of 512 affine
coefficient choices is checked, and a separate formula for k=|a| agrees.
No enumeration of all quadratics is required for the existential upper bound.
2. Average-case substituted for pointwise? The upper distribution includes
uniform variable permutations. Every image of a fixed weight-w input has
multiplicity w!(8-w)!, so layer fractions become pointwise probabilities.
Literal permutation enumeration checks this argument independently.
3. Symmetrization unnecessary? Refuted by the raw mixture: x=14, target 1,
only the first row agrees, giving success 1/12. See graveyard/003.
4. Coefficient ordering error? Bit-based truth evaluation agrees with a
second tuple-based evaluation on all 256 inputs and all four rows.
5. Invalid degree/probabilities? Range, nonnegativity and normalization
checks are explicit. Negative weight and out-of-range term mutations fail.
6. Did a numerical LP certify the result? No. Discovery used floats,
but certificate acceptance uses exact fractions, actual truth tables and
complete permutation enumeration on an independent GitHub runner.
7. Irrational affine mixtures missed? No. The finite weighted-average
contradiction works for arbitrary real mixture probabilities, not only
those represented by the rational upper witness.
8. Is the worst-case 2/3 a global optimal success value? Not claimed.
It is the guarantee of this compact witness only. Likewise four orbit
rows are not claimed minimal for the whole quadratic class.
9. Has Lean checked MOD3? No. The generic finite-duality lemma is separate;
polynomial encodings, degree, truth-table certificates and group action
must still be connected formally.
10. Is the result new? Unknown. Primary-source definition checks and a
small exact-table search do not substitute for comprehensive prior-art
work or external mathematical review.

Verdict: finite n=8 certificate survives this algorithmically diversified
self-audit and remote reproduction. This is not independent human review.
