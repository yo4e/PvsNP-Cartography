# Expedition 001 Log

## 2026-10-07 — code-path audit

Inspected:

- `agents/lower_bound_hunter/agent.py`
- `docs/FINDINGS.md`
- `lean/pvsnp_hunter/PvsNP/LowerBounds.lean`

### Preliminary finding A — minimum_approx_degree does not search minimum approximate degree

In the current source, `PolynomialApproximator.minimum_approx_degree()` immediately discards the `error` parameter:

```python
del error
```

It then returns function-specific closed-form heuristics, e.g.:

- parity / xor: `n` over GF(2), roughly `n/2` over GF(3)
- majority: roughly `sqrt(n)`, with a parity adjustment over GF(3)
- PHP: roughly `0.6 n`, with a field-dependent adjustment

The method does **not** call `_can_approximate()`.

Therefore values generated through this path are not established by the code as exact minima of a 1/3-approximation search.

### Preliminary finding B — n > 8 values are extrapolated

For non-graph functions, `DegreeComplexityEstimator._estimate_for_field()` uses `minimum_approx_degree()` only at n=6,7,8 and extrapolates beyond n=8 with a linear growth increment.

Thus the published n≤15 tables for PHP and Majority are, at least for n>8, deterministic extrapolations from heuristic seed formulas, not exhaustive finite-n approximation-degree calculations.

### Preliminary finding C — graph functions compute a different quantity

For CLIQUE and Independent Set, the estimator takes a different path:

`graph_function_degree()`

It evaluates the Boolean graph property on all graphs for a small vertex count, applies a finite-field Möbius transform, and returns the highest-degree nonzero multilinear coefficient.

That is the **exact degree of the represented Boolean function as a multilinear polynomial over GF(p)** for those small instances.

It is not automatically the same object as minimum 1/3-approximate degree.

### Preliminary finding D — output labels blur the distinction

The lower-bound result uses labels such as:

`bound_type="approximate_polynomial_degree"`

and prose such as:

> Computed minimum degree 1/3-approximation over GF(2), GF(3)

This wording appears stronger than what the implementation establishes for the non-graph paths.

### Preliminary finding E — formal layer is currently scaffolding

The inspected Lean file includes major lower-bound landmarks as axioms and several target propositions whose body is effectively:

```lean
forall (n : Nat), n > 0 -> True
```

This is explicitly marked with TODO comments in the source, so it should be treated as scaffolding rather than a formal proof of the named lower bounds.

## Interpretation

This does **not** establish that every public finding in p-vs-np-hunter is false.

It establishes a narrower and important point:

> The current implementation does not support interpreting the full published degree table as exact minimum 1/3-approximate-degree computation.

The next step is independent reproduction and exact small-n comparison.

## Next actions

1. Extract the exact published table.
2. Reproduce the current generator output.
3. Implement an exact small-n definition for a clearly specified approximation notion.
4. Determine whether the intended GF(p) approximation notion itself is stated correctly for Razborov–Smolensky use.
5. Compare exact/proxy/heuristic values.
6. Write a fair final conclusion distinguishing:
   - code-label mismatch
   - heuristic modeling choice
   - any actual mathematical error
