# Expedition 003: n=8 quadratic-orbit sample and dual attack

Date: 2026-10-08
Status: **sample-restricted exact result; universal inference refuted**
Novelty: unknown. The exact n=8 probabilistic degree is NOT determined.

## Exact target

Same standard pointwise-error definition as Expedition 002:
MOD_3^n(x)=1 exactly when the Hamming weight is divisible by 3;
GF(2) coefficients; degree-at-most-2 polynomial distributions; every
Boolean input must have correctness probability at least 2/3.

For n=8, each deterministic quadratic polynomial is encoded by:
constant c, 8-bit linear mask a, and 28-bit quadratic mask b whose bits
index unordered pairs in Python combinations(range(8),2) order.
The orbit under uniform variable permutations has a 9-coordinate
layer-success vector, with coordinate w = correct_count[w]/binom(8,w).

## Precisely defined finite subproblem

Build a candidate pool S with 10,000 uniform random coefficient vectors
using NumPy 2.3.5 RNG default_rng(20261008), plus 16 structured rows
(constants, symmetric monomial patterns and eight embedded n=7
representatives). This gives 10,016 polynomials, with 6,407 distinct
layer-good-count vectors. The pool is **not** exhaustive over the 2^37
possible coefficient tuples.

Optimize the minimum layer success under a rational mixture of
permutation-orbits **from S**. This is a finite zero-sum linear program.

## Exact sample-only result

The optimum for S is **569/902**. A 9-orbit mixture attains that
success on each of all nine layers (primal certificate). A rational
distribution q on the input layers gives expected success at most
569/902 for every polynomial in S (dual certificate).

Both rational certificates, all coefficient masks, complete good-count
vectors, deterministic pool regeneration and exact inequality checking
are in [verify_n8_sampled_dual.py](verify_n8_sampled_dual.py).

The dual q has numerators
[207,1983,6550,4969,3150,1085,3482,1901,125] with denominator
23452. This is a valid distribution on nine Hamming-weight layers.

## Full-model adversarial attack

A quadratic polynomial **outside** S with
(c,a,b) = (1,255,60548413)
has layer-good counts [1,8,17,34,39,28,21,6,1].
Its exact q-average correctness is **27376/41041**, which exceeds 2/3
by 46/123123. Therefore q is INVALID as a universal n=8 degree-2
lower certificate. This polynomial does NOT establish a mixture whose
pointwise correctness reaches 2/3.

## Simple monotonicity observation

If a degree-at-most-1 distribution solved the n=8 task, restricting
the eighth variable to zero would give a degree-at-most-1 distribution
for n=7 under the same pointwise guarantee, contradicting Expedition 002.
Therefore the n=8 probabilistic degree is **at least 2**.

The sample experiment does not decide whether it is 2 or larger.
