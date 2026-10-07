# Expedition 002 — Exact finite probabilistic degree of MOD_3 over GF(2)

Status: **active / exact finite certificates**

Date: 2026-10-08

Issue: #6

## Target

For a Boolean function `f : {0,1}^n -> {0,1}`, define `pdeg_epsilon(f)` over a field F as the least degree d for which there is a finite-support distribution over degree-at-most-d polynomials P such that, for every Boolean input x,

`Pr[P(x) = f(x)] >= 1 - epsilon`.

This expedition fixes:

- field: `GF(2)`;
- target: `MOD_3^n(x)=1` iff Hamming weight `|x| ≡ 0 (mod 3)`;
- error: `epsilon = 1/3`;
- first exact sizes: n=5,6,7.

This is the standard pointwise-error probabilistic-degree definition. It is not deterministic average-case approximation, exact algebraic degree, a nonzero/zero classifier, or a fitted sequence.

## Literature context

The standard definition and asymptotic context are consistent with Srinivasan–Tripathi–Venkitesh, *On the Probabilistic Degrees of Symmetric Boolean Functions* (ECCC TR19-138; FSTTCS 2019; SIDMA 2021).

That work characterizes broad symmetric-function probabilistic degrees up to polylogarithmic factors. This expedition asks a different, deliberately finite question: exact small-n values with explicit rational certificates.

Targeted searches on 2026-10-08 did not locate a published table for the exact n=5,6,7 values below. This absence is **not** a novelty claim. Novelty remains unknown.

## Certificate strategy

### Degree-1 lower certificate

Choose a rational distribution q over Hamming-weight layers. Inside each layer, sample uniformly.

If every deterministic affine polynomial over GF(2) has expected correctness strictly below 2/3 under q, then no distribution over affine polynomials can achieve pointwise correctness at least 2/3.

Reason: pointwise success >= 2/3 would imply q-average success >= 2/3, while convex mixtures cannot beat the maximum q-average success of their deterministic support.

The checker enumerates every affine polynomial, so no symmetry reduction is trusted for the lower bound.

### Degree-2 upper certificate

For each quadratic representative P, use the uniform distribution over all variable permutations of P. For a fixed input x of weight w, this success probability equals the fraction of weight-w inputs on which P agrees with MOD_3.

A rational mixture of such permutation-orbits therefore has pointwise success determined exactly by its layerwise success vector.

The checker enumerates all Boolean inputs for each representative and performs every probability calculation with `fractions.Fraction`.

## Exact certificates found

### n=5

Lower layer distribution:

`(0, 1/3, 1/6, 7/18, 1/18, 1/18)`

Every affine polynomial has expected success at most `11/18 < 2/3`.

A single symmetrized quadratic representative with masks

- constant = 1
- linear mask = 27
- quadratic mask = 829

has layer success

`(1, 4/5, 7/10, 7/10, 1, 1)`.

Hence the exact value is 2.

### n=6

Lower layer distribution:

`(0, 11/36, 0, 7/18, 2/9, 1/12, 0)`

Every affine polynomial has expected success at most `11/18 < 2/3`.

A single symmetrized quadratic representative with masks

- constant = 1
- linear mask = 59
- quadratic mask = 31421

has layer success

`(1, 5/6, 2/3, 7/10, 2/3, 5/6, 1)`.

Hence the exact value is 2.

### n=7

Lower layer distribution:

`(0, 2/15, 1/10, 13/30, 1/30, 3/10, 0, 0)`

Every affine polynomial has expected success at most `17/30 < 2/3`.

The upper certificate uses eight symmetrized quadratic representatives with exact rational mixture weights. The independent checker verifies that the combined success on **every** Hamming layer is exactly

`10825/15922 > 2/3`.

Hence the exact value is 2.

The full rational coefficient tables, including the previously missing eight n=7 orbit representatives, are preserved in the [full exact certificate tables](certificates.md). The Python checker is still pending direct GitHub upload. An independent Walsh-transform and explicit-permutation recheck of these numbers passed on 2026-10-08.

## Verification boundary

The discovery process used numerical linear programming and random candidate search for some upper witnesses. Those tools are **not** part of the final proof.

The repository certificate is accepted only through the independent standard-library rational checker, which:

- enumerates the Boolean cube;
- evaluates explicit GF(2) polynomials;
- enumerates all affine polynomials for the lower bound;
- checks all layer distributions sum to 1;
- checks all mixture weights sum to 1;
- checks the exact inequalities with rational arithmetic.

## What this does not establish

These finite equalities do not imply:

- an asymptotic formula for `MOD_3^n`;
- a new circuit lower bound;
- an escape from relativization, Natural Proofs, or algebrization;
- novelty of the exact values.

The current theorem class is simply: **exact finite computation with explicit certificates**.
