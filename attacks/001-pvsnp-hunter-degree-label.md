# Attack 001 — Is “minimum 1/3-approximate degree” actually computed?

Target: GISMO-1/p-vs-np-hunter finite-degree claims.

Status: **preliminary attack survives**

## Claim under attack

Natural-language outputs describe values as minimum degree 1/3 approximations over GF(2) and GF(3).

## Attack

Trace the computation from public table generation to the numeric primitive.

## Result

For parity, majority, PHP, and other non-graph functions:

- the `error` parameter is discarded
- no coefficient search occurs in `minimum_approx_degree()`
- hard-coded function-specific formulas return the values
- values after n=8 are extrapolated

For graph functions:

- exhaustive truth-table evaluation occurs
- the computation returns exact multilinear polynomial degree
- this is a different mathematical quantity from the label used elsewhere

## Why this matters

If two different quantities are placed into one table and interpreted as one approximation-degree notion, fitted growth exponents do not have a single mathematical meaning.

A power-law fit can be numerically correct for the generated sequence while being irrelevant to the claimed complexity-theoretic interpretation.

## Not yet concluded

We have not yet:

- reproduced the whole table independently
- proved the intended approximation notion cannot be recovered from another code path
- evaluated the exact mathematical relationship between the graph-function degree and the intended lower-bound heuristic

Therefore this attack is recorded as a **definition / implementation mismatch**, not yet as a full refutation of all associated conclusions.
