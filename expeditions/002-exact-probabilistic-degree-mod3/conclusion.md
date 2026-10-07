# Conclusion — Expedition 002

Status: **exact finite result / novelty-unknown**

Date: 2026-10-08

## Result

For the standard pointwise-error probabilistic degree over GF(2), with error 1/3,

`pdeg_{1/3}^{GF(2)}(MOD_3^n) = 2`

for:

- n=5;
- n=6;
- n=7.

## Lower certificates

Explicit rational distributions over Hamming-weight layers show that every affine polynomial has average success strictly below 2/3:

- n=5: maximum `11/18`;
- n=6: maximum `11/18`;
- n=7: maximum `17/30`.

Since a pointwise-successful randomized affine polynomial would also achieve at least 2/3 under each such input distribution, degree 1 is impossible.

## Upper certificates

Explicit degree-at-most-2 polynomial representatives are uniformly symmetrized over variable permutations.

The resulting pointwise minimum success is:

- n=5: `7/10`;
- n=6: `2/3`;
- n=7: `10825/15922`.

For n=7 the eight-orbit rational mixture is especially strong: every Hamming layer, and under direct permutation enumeration every individual Boolean input, receives exactly `10825/15922` success.

Therefore degree 2 is sufficient.

The entire set of coefficients, layer counts, and orbit weights is now committed in [full exact certificate tables](certificates.md), independent of the still-uncommitted Python checker.

## Independent attack

The upper symmetry argument was checked a second way by explicitly enumerating all variable permutations rather than relying only on layer formulas.

The lower bounds enumerate every affine polynomial rather than trusting an orbit reduction.

The numerical optimizer/search used during discovery is not part of the final argument.

## Literature state

Targeted search recovered the standard definition and asymptotic symmetric-function theory, especially Srinivasan–Tripathi–Venkitesh.

No exact n=5,6,7 table was located in that search.

This does **not** establish novelty. Status remains `novelty-unknown`.

## Research significance

The mathematical result is modest but methodologically useful.

Expedition 001 showed how an AI project can produce plausible finite sequences for the wrong named quantity. Expedition 002 now supplies the opposite pattern:

1. define the standard quantity first;
2. derive explicit finite certificates;
3. verify them with exact rational arithmetic;
4. attack the symmetry/pointwise semantics independently;
5. refuse asymptotic extrapolation.

That gives the repository a clean benchmark for later formalization and automated-mathematics tooling.

## Natural checkpoint

The initial issue target has been exceeded: n=7 was reached exactly rather than merely documenting a scaling barrier.

The next frontier is not to extrapolate from 5,6,7. It is either:

- formalize these compact certificates in Lean once Issue #3 CI is actually green; or
- push exact search to n=8 while preserving certificate compactness and exact verification.

The standard-library checker is prepared and locally verified but its GitHub file write was blocked by the execution safety layer during this run. Its exact pending path is:

`expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py`.
