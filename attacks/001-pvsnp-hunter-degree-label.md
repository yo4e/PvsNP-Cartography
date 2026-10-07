# Attack 001 — Is “minimum 1/3-approximate degree” actually computed?

Target: GISMO-1/p-vs-np-hunter finite-degree claims.

Status: **confirmed definition/implementation mismatch with exact counterexamples**

Target revision:

`ee4a4b80f8df505def85304af882a8bbff7de194`

## Claim under attack

Natural-language outputs describe values as minimum degree 1/3 approximations over GF(2) and GF(3).

## Code-path attack

For parity, majority, PHP, and other non-graph functions:

- the `error` parameter is discarded;
- no coefficient search occurs in `minimum_approx_degree()`;
- hard-coded function-specific formulas return the values;
- values after n=8 are extrapolated from n=6,7,8.

For graph functions:

- exhaustive truth-table evaluation occurs;
- a finite-field Möbius transform computes the unique multilinear representation;
- the reported value is exact **algebraic degree**, a different quantity from the label used elsewhere.

## Exact counterattack

`expeditions/001-audit-pvsnp-hunter/reproduce_degree_table.py` performs an exact finite search using the target repository's dormant helper semantics: prediction is 1 iff a GF(p) polynomial is nonzero, and uniform Boolean-cube misclassification must be at most 1/3. Unlike the target helper, the audit enumerates the complete degree-d monomial basis.

It finds, among other discrepancies:

| function | n | field | target report | exact audit minimum |
|---|---:|---|---:|---:|
| parity | 2 | GF(2) | 2 | 1 |
| parity | 3 | GF(2) | 3 | 1 |
| parity | 4 | GF(2) | 4 | 1 |
| parity | 4 | GF(3) | 2 | 1 |
| majority | 2 | GF(2) | 1 | 0 |
| majority | 3 | GF(3) | 2 | 1 |
| majority | 4 | GF(2) | 2 | 0 |
| majority | 4 | GF(3) | 2 | 0 |

The GF(2) parity contradiction needs no search heuristic: `x1 + ... + xn mod 2` is an exact degree-1 representation.

Thus the common “minimum 1/3-approximate degree” label is not merely unverified. It is false for concrete tiny instances under the codebase's own apparent approximation semantics, and false for GF(2) parity even as an upper-bound claim on ordinary exact finite-field degree.

## PHP-specific attack

The PHP degree path never constructs a PHP Boolean encoding.

The active formula explicitly injects a GF(3)-specific increment for n>=7. The n>8 extrapolator then derives slopes:

```text
GF(2): (d6,d7,d8)=(3,4,4) -> growth=1
GF(3): (d6,d7,d8)=(3,5,5) -> growth=2
```

So the published cross-field gap and the larger GF(3) fitted exponent arise mechanically from the heuristic.

The generic `_truth_table()` helper would map `"php"` through its fallback `sum(bits) == 0`, not through a pigeonhole-principle encoding. A separate SAT PHP generator exists but is disconnected from this degree pipeline.

## Dormant-helper attack

Even if `_can_approximate()` were connected, it takes all degree-d monomials and then searches coefficients only for the first `n+3`. Therefore it is a bounded proxy, not an exhaustive exact-minimum solver.

## Why this matters

If different mathematical quantities are placed into one table and interpreted as one approximation-degree notion, fitted growth exponents do not have a common complexity-theoretic meaning.

A power-law fit can perfectly reproduce a generated sequence while providing no empirical evidence about the named Boolean function.

## Surviving portion

The graph-function rows survive a narrower interpretation:

> exact multilinear algebraic degree over GF(p) of the implemented half-vertex-threshold CLIQUE / Independent Set predicate for graphs on 3..6 vertices.

That is a legitimate finite computation. It is simply not what the common table label says.

## Verdict

**Attack succeeds against the shared approximate-degree interpretation and against the PHP empirical-asymmetry interpretation.**

It does not refute every other result in p-vs-np-hunter.
