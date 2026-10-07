# Graveyard 001 — “minimum approximate degree” / PHP empirical-asymmetry interpretation

Status: **refuted as stated**

Buried object: the interpretation of the audited p-vs-np-hunter non-graph degree table as computed minimum 1/3-approximate degree, especially the PHP GF(2)/GF(3) gap as empirical evidence from PHP instances.

Target revision:

`GISMO-1/p-vs-np-hunter@ee4a4b80f8df505def85304af882a8bbff7de194`

## Claim

The reported PHP, Majority, Parity/XOR values are finite computations of minimum degree 1/3 approximations over GF(2)/GF(3), and their cross-field patterns can therefore be read as empirical signatures of the corresponding Boolean functions.

## Attraction

The table looks like measured finite mathematics:

- values are indexed by n and field;
- fitted growth exponents are reported;
- the prose carefully warns that finite data is not an asymptotic proof;
- the surrounding repository cites Razborov and Smolensky.

This makes it tempting to treat the table as a noisy but genuine experimental probe.

## Failure point

The active implementation never performs the named search for non-graph functions.

`minimum_approx_degree()` discards the error parameter and returns hard-coded formulas. For n>8, a separate estimator extrapolates linearly from n=6,7,8.

For PHP there is no Boolean PHP encoding in the degree-analysis path.

The GF(3) PHP formula itself adds a field-specific term from n>=7, which changes the extrapolated slope and generates the widening field gap.

## Exact counterexamples

Under an exhaustive version of the codebase's own dormant average-error/nonzero-classifier semantics:

- parity over GF(2), n=2,3,4 has minimum degree 1, not 2,3,4;
- majority n=4 has minimum degree 0 for both GF(2) and GF(3), not 2, because the constant-zero classifier has error 5/16 <= 1/3;
- majority n=3 over GF(3) has minimum degree 1, not 2.

The parity result is particularly robust: the exact polynomial `x1+...+xn mod 2` has degree 1 for every n.

## Lesson

**Reproducibility of a sequence is not validation of its semantics.**

Before fitting or interpreting experimental numbers, trace them to:

1. the actual mathematical input object;
2. the actual optimization/search problem;
3. the exact implementation;
4. the theorem connecting that quantity to the claimed complexity consequence.

The target table passed (3) only in the weak sense “the code deterministically regenerates it,” while failing the intended identification between (1), (2), and the prose label.

## Possible salvage

The implementation can be made scientifically useful by separating the quantities:

- rename the current non-graph values as **heuristic scores**;
- remove language claiming an exact/minimum 1/3 degree;
- define an explicit Boolean encoding for PHP;
- define one approximation notion mathematically before coding it;
- build an exact solver for tiny n with the complete monomial basis;
- use approximate/heuristic solvers only after validating them against exact tiny cases;
- keep graph algebraic degree in a separately labelled table;
- state and verify the precise Razborov-Smolensky transfer theorem before making circuit-hardness interpretations.

The dead interpretation should remain buried even if a corrected experiment later produces interesting data.
