# Exact rational certificates, n=5,6,7

Date: 2026-10-08
Status: **finite exact certificates; novelty unknown; Lean verification not claimed**

This file makes the full witnesses recoverable **inside the repository**. The witnesses
are independent of the numerical optimizer used during discovery. The executable
[standard-library checker](verify_certificates.py) was committed on 2026-10-08 and
reproduced in [GitHub Actions](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789085813).

## Definition and encoding

The target is `f_n(x)=1` iff the Boolean Hamming weight `|x|` is
divisible by 3. Work over GF(2), with allowable pointwise failure at most 1/3.

A representative polynomial is

`P(x)=c + sum_i a_i*x_i + sum_{i<j} b_ij*x_i*x_j (mod 2)`.

Bits of `linear_mask` index `i=0,...,n-1`.
Bits of `quadratic_mask` index unordered pairs `(i,j)` in lexicographic
order, as produced by Python `itertools.combinations(range(n),2)`.
Bit 0 is the least-significant bit. Bits beyond the listed monomial range
are invalid.

The upper witness first chooses a row with its rational probability and
then chooses a **uniform permutation of all n variables**, applying that
permutation to the selected polynomial. This is a bona fide distribution
over polynomials of degree at most two, not a distribution over input
examples.

The lower witness chooses Hamming weight w with probability q[w] and
then an input uniformly from that layer.

## Lower certificates

The exact layer-mass distributions q, indexed w=0 through n, are:

- n=5: `[0, 1/3, 1/6, 7/18, 1/18, 1/18]`.
- n=6: `[0, 11/36, 0, 7/18, 2/9, 1/12, 0]`.
- n=7: `[0, 2/15, 1/10, 13/30, 1/30, 3/10, 0, 0]`.

For an affine polynomial `a·x+c`, let `k=|a|`. Its absolute correlation
with the target (under q) depends only on k and is given exactly by

`|C_k| = |sum_w q[w] (-1)^f(w) K_k(w)/binom(n,w)|`,

where `f(w)=1` when `w mod 3=0`, otherwise `f(w)=0`, and

`K_k(w) = sum_j (-1)^j binom(k,j) binom(n-k,w-j)`.

Out-of-range binomial terms are zero. The best affine constant c gives
success `(1+|C_k|)/2`. This formula tests **every** affine polynomial:
all 2^(n+1) choices are grouped by k without dropping any.

| k | n=5: C_k | n=6: C_k | n=7: C_k |
|---:|---:|---:|---:|
| 0 | 2/9 | 2/9 | 2/15 |
| 1 | 2/9 | 2/27 | -2/35 |
| 2 | 8/45 | 26/135 | 2/15 |
| 3 | -2/9 | 2/45 | 46/525 |
| 4 | -2/9 | -2/9 | -58/525 |
| 5 | 2/9 | -2/9 | -2/15 |
| 6 | | 2/9 | 2/15 |
| 7 | | | 2/15 |

Thus the maximum success of **any** affine polynomial under these q is

- n=5: `(1+2/9)/2 = 11/18 < 2/3`;
- n=6: `(1+2/9)/2 = 11/18 < 2/3`;
- n=7: `(1+2/15)/2 = 17/30 < 2/3`.

Since mixtures cannot increase this expected success, **no randomized
degree-at-most-one polynomial** can achieve success at least 2/3 on
every input.

## Upper certificates: n=5 and n=6

Each uses a *single* representative with orbit weight 1.

| n | c | linear_mask | quadratic_mask | success by Hamming weight w=0,...,n |
|---:|---:|---:|---:|---|
| 5 | 1 | 27 | 829 | `[1, 4/5, 7/10, 7/10, 1, 1]` |
| 6 | 1 | 59 | 31421 | `[1, 5/6, 2/3, 7/10, 2/3, 5/6, 1]` |

The minimum values are respectively 7/10 and 2/3.

## Upper certificate: n=7

Layer sizes for w=0,...,7 are `[1,7,21,35,35,21,7,1]`.

Each row lists an orbit weight, polynomial coefficients and exact integer
number of correct outputs on each Hamming-weight layer before
symmetrization.

| Orbit weight | c | linear_mask | quadratic_mask | good counts w=0,...,7 |
|---|---:|---:|---:|---|
| 1851/15922 | 0 | 0 | 0 | `[0,7,21,0,35,21,0,1]` |
| 2291/15922 | 0 | 0 | 2097151 | `[0,7,0,35,35,21,7,0]` |
| 955/15922 | 0 | 127 | 0 | `[0,0,21,35,35,0,0,0]` |
| 885/15922 | 1 | 127 | 2097151 | `[1,7,21,35,0,21,0,0]` |
| 4487/7961 | 1 | 71 | 1887847 | `[1,4,15,24,20,12,6,1]` |
| 7/838 | 1 | 8 | 1802215 | `[1,1,13,21,26,17,6,0]` |
| 147/15922 | 1 | 11 | 1855511 | `[1,3,17,21,26,15,2,0]` |
| 343/7961 | 1 | 119 | 1980222 | `[1,6,16,19,20,14,7,0]` |

These weights are nonnegative and sum to 1. For each layer w, multiply
each row's good count by its orbit weight, divide by `binom(7,w)`,
and add the eight terms. The result is *exactly*

`10825/15922 > 2/3`

for **all eight layers**. Uniform permutation makes the same success
probability apply to every one of the 128 individual inputs.

## Independent verification on 2026-10-08

Two distinct finite methods checked the certificates:

1. the original standard-library rational checker enumerates all affine
   polynomials and computes layer success vectors;
2. an independent audit uses a rational Walsh-Hadamard transform for the
   lower certificates and *literal enumeration of all permutations at
   every input* for the upper certificates.

The independent audit recovered

- n=5: affine maximum 11/18; pointwise upper minimum 7/10;
- n=6: affine maximum 11/18; pointwise upper minimum 2/3;
- n=7: affine maximum 17/30; pointwise upper minimum and maximum
  10825/15922.

A negative control that flipped n=5's constant bit invalidated its
upper witness, as it should.

## Epistemic limits and outstanding work

This is an exact finite certificate, not a Lean-checked theorem, not
novelty evidence, and not an asymptotic circuit lower bound.

An earlier verifier file write was blocked; that historical blocker is now resolved.
The committed checker runs with `--permutation-audit` in CI, exhausts all affine
polynomials, checks each rational quadratic witness and full permutation-orbit
pointwise success, and rejects a corrupted constant-bit witness as a negative
control. [Run 37789085813](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789085813)
completed successfully.

The separate Lean scaffold also passed its pinned build and assumption audit in
[run 37789136586](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789136586).
**These MOD3 certificates have not been formalized in Lean.** Next: design a
faithful formal statement for the bounded result or pursue n=8 without assuming
that an observed finite pattern continues.
