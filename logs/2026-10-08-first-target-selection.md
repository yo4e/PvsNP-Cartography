# 2026-10-08 — First bounded target selection

Issue: #5

## Candidates audited

1. exact finite probabilistic degree of modular functions;
2. exact switching-lemma extremizers;
3. exact Resolution width for bounded hard CNFs;
4. exact Polynomial Calculus degree across fields.

## Selection pressure

The target-selection process deliberately rewarded quantities with exact definitions and certificate-producing finite formulations.

The strongest candidate was probabilistic degree because Expedition 001 had just demonstrated the failure mode of calling unrelated heuristics “approximate degree.”

## Pilot before selection

A small exact LP/game formulation was built privately as a feasibility attack for `MOD_3^n` over `GF(2)`.

It already produced rational candidate certificates at n=5 and n=6:

- affine degree is insufficient at 1/3 pointwise error;
- quadratic randomized polynomials suffice.

These candidates must be reimplemented and independently checked in the repository before they are treated as expedition results.

## Decision

Select an exact finite probabilistic-degree atlas, beginning with `MOD_3` over `GF(2)`.

No novelty claim is made. The immediate objective is a trustworthy finite theorem/certificate pipeline, not an asymptotic circuit lower bound.
