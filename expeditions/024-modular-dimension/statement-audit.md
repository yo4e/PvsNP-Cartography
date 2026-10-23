# Author adversarial statement audit

This audit is by the author, not a new independent AI or human review.

The formal core quantifies over arbitrary fields K, arities n, nonzero grid
values a,b, actual MvPolynomial R and total-degree upper bound d. For each
subset S it constructs ONE polynomial Q before the universal point y.
Only on y in the stated grid AND R(y)=product y does Q agree with the squarefree
monomial. The condition n+d<=2t+1 is the exact integral threshold used in the
high-support branch, not a sampled arity or an assumed agreement bound.

The R(y)=product y premise is the definition of the agreement set to be bounded,
not an assertion that it is large or that the target lower bound already holds.
No theorem assumes the compression or desired dimension inequality. Both the
small monomial and complement-inverse constructions are explicit. Actual
MvPolynomial.totalDegree bounds are proved before the evaluation conclusion.

Nonzero a,b are essential for cancellation. Distinctness is unnecessary for the
core identity, so its omission is not a gap. The subsequent dimension argument
and probability fraction DO require distinctness and introduce it explicitly.
The zero-grid attack breaks the proposed extrapolation at n3,R=0:7 agreements
versus4 in the incorrect formula. Characteristic2 does not identify alpha with
its inverse in GF4. Equality outside the agreement set is not asserted.

Formal scope: squarefree and inverse-product degree bounds, actual inverse
identity, complement reduction/evaluation, generic compression, one rational
zero-grid counterexample, and the finite majority15 binomial identity.
Not formalized: arbitrary-grid multilinear reduction/interpolation/rank theorem,
finite REAL product distribution amplification, GF4 residue/root adapter, or the
n299 consequence. Python rank tests and the exact numerical inequality do not
fill those formal gaps. No theorem name or proof status may obscure this split.

The finite checker independently represents sparse polynomials and evaluation
matrices over GF4; it does not call Lean. Small-n exhaustive cases are bounded
corroboration only. Its majority Mobius transform is separate from the binomial
identity, and its binomial recurrence is separate from math.comb. These are
independent implementations by the same author, not independent semantic review.

A further author source attack found a real stale-iterator defect in the first
rank checker despite its green CI. Graveyard038 preserves both2x2 counterexamples.
Accepted rank evidence must use the repaired source with256 determinant controls;
the old run is not retroactively certified. The formal core is independent of
that Python implementation and never imported its computed ranks.
