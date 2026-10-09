# Expedition 004: exact MOD3 probabilistic degree at n=8

Date: 2026-10-09 (JST). Issue: #7.
Status: **exact finite certificate; local checks and remote CI passed**.
Novelty: unknown. No Lean MOD3 or asymptotic claim.

## Target and prior state

For f(x)=1 iff the Hamming weight of x is divisible by 3, over GF(2),
the least degree supporting a polynomial distribution with
Pr[P(x)=f(x)] >= 2/3 for EVERY Boolean input x is exactly 2 at n=8.
The definition matches Srinivasan, Tripathi and Venkitesh, FSTTCS 2019,
Definition 1 (https://doi.org/10.4230/LIPIcs.FSTTCS.2019.28), and
Srinivasan, A Robust Version of Hegedus's Lemma, Definition 2.3
(https://arxiv.org/abs/2202.04982).

Expedition 003 only optimized a sampled family and refuted its dual's
universal interpretation. That historical record stays intact. This
expedition supplies a positive witness, which needs no exhaustive search
of all quadratic polynomials.

## Certificate

The polynomial encoding is c + sum a_i x_i + sum b_ij x_i x_j (mod 2).
Bits i of a index variables 0..7. Bits of b index lexicographically ordered
pairs combinations(range(8),2), least-significant bit first.
Choose one of four rows in certificate.json with probabilities
1/12, 1/4, 1/3, 1/3, THEN choose a uniform permutation of all eight
variables. Omitting the permutation step changes the distribution and fails.

Lower certificate: choose input weight 1 or 3 with probability 1/2,
then choose uniformly inside that layer. Every affine polynomial has
expected correctness at most 9/14 < 2/3. Enumerating all 512 affine
polynomials and a separate hypergeometric formula agree.

Upper certificate: the four symmetrized rows yield layer successes
[2/3,17/24,125/168,2/3,2/3,115/168,17/24,2/3,2/3].

The full finite convexity and orbit argument is in [conclusion.md](conclusion.md).
The generic weak-duality step is separately Lean-checked, but its MOD3
instantiation and the upper witness are not yet formalized.

## Verification

python3 expeditions/004-exact-mod3-n8/verify.py --permutations

This stdlib-only checker uses exact fractions, two polynomial evaluators,
all 40320 permutations at all 256 inputs, full affine enumeration, and
six negative controls. Validation remains active under python -O.
Discovery optimizers are not part of certificate acceptance.

[Run 37940070467](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940070467)
on commit 7355f4e5b826a1b34e0f48d891c208495c821cca passed both the complete
permutation audit and optimized-Python checks. Actual logs were retrieved.
