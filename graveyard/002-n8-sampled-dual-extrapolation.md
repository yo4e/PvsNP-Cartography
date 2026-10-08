# Graveyard 002: sampled quadratic LP dual extrapolated to all polynomials

Date: 2026-10-08
Claim status: **refuted inference**, not a refuted n=8 probabilistic-degree value.

## Claim (invalid)

Because a 10,016-candidate n=8 quadratic-orbit pool has maximum
achievable pointwise minimum 569/902 < 2/3, no randomized degree-2
polynomial can approximate MOD_3^8 at error 1/3.

## Why it looked attractive

The pool was large, rational primal and dual witnesses matched exactly,
and its 6,407 distinct layer vectors were checked without floating
point. The dual q looked like a lower-bound certificate.

## Failure point

The LP optimizes over S, not over all 2^37 quadratic coefficients.
A valid universal lower certificate needs to bound **every**
degree-at-most-2 polynomial, not merely the inspected set.

## Concrete refutation of the attempted certificate

A polynomial outside S with (c,a,b)=(1,255,60548413) has q-average
success 27376/41041 > 2/3. Its nine layer-good counts are
[1,8,17,34,39,28,21,6,1]. Thus the sampled dual q is
provably insufficient to exclude all quadratic distributions.

## Lesson

Exact arithmetic does not repair an incomplete universal quantifier.
A rational LP dual may perfectly certify a *restricted* game yet fail
as a certificate for the full class.

## Possible salvage

Retain the exact 569/902 optimum **for S** as a regression test.
Apply counterexample-guided column generation, but do not call it a
complete method until the quadratic best-response oracle has
exhaustive coverage or a mathematical proof of completeness.

The actual value of pdeg_(1/3)(MOD_3^8) remains unknown here.
