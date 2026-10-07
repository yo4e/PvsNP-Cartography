# Expedition 001 — Conclusion

Status: **completed**

Classification: **partially reproduced / definition mismatch**

Target revision:

`GISMO-1/p-vs-np-hunter@ee4a4b80f8df505def85304af882a8bbff7de194`

## Executive conclusion

The published finite-degree tables are reproducible, but they do not form a single dataset of “minimum degree 1/3 approximations.”

The audit found three materially different objects under that umbrella:

1. **PHP, Majority, Parity/XOR:** hand-written function-name formulas, followed by deterministic extrapolation for n>8.
2. **CLIQUE / Independent Set:** exact algebraic degree of a specific graph predicate's unique multilinear representation over GF(p).
3. **`_can_approximate()` helper:** an unused, truncated coefficient search for a different average-error nonzero/zero classification problem.

The graph rows survive as exact finite algebraic-degree calculations for the implemented predicates. The non-graph interpretation as exact minimum 1/3 approximate degree does not survive.

## What reproduced

### PHP published table

`reproduce_degree_table.py` independently reconstructs the active formula and extrapolator and reproduces every PHP row for n=2..15.

It also reproduces the published fitted exponents:

- GF(2): `0.9533698286984779`
- GF(3): `1.2079016267666487`

This proves output reproducibility, not mathematical exactness.

### CLIQUE / Independent Set table

An independent truth-table enumerator and finite-field Möbius transform reproduces the four published rows exactly at edge counts 3, 6, 10, 15.

For the implemented predicate, these are exact multilinear algebraic degrees over GF(2) and GF(3).

## What failed

### “minimum 1/3 approximate degree” is false as a common label

For non-graph functions the active method discards the error parameter and never searches polynomial coefficients.

An exact tiny-instance audit under the semantics of the repository's own dormant helper already disagrees with the published/formula values.

Most decisively, parity over GF(2) has the exact degree-1 polynomial

```text
x1 + x2 + ... + xn  (mod 2)
```

so any approximation notion that allows exact GF(2) representation has minimum degree at most 1. The published table instead reports degrees 2, 3, 4, ... for parity.

### PHP “cross-field evidence” is synthetic

The PHP estimator does not evaluate a pigeonhole-principle Boolean function.

Its active seed is a formula with an explicit GF(3)-specific increment from n>=7. For n>8, the estimator extrapolates from d6,d7,d8. This creates extrapolation slopes 1 over GF(2) and 2 over GF(3), which mechanically generates the growing gap and the fitted-exponent difference.

Therefore the reported cross-field PHP pattern is not empirical evidence discovered from finite PHP instances. It is a property of the hand-coded heuristic.

### No PHP degree encoding exists on this path

The polynomial-degree pipeline has no PHP truth table or polynomial representation from an actual PHP encoding.

The generic `_truth_table()` helper would fall back to `sum(bits) == 0` for `"php"`, i.e. a NOR-like predicate, if it were connected without new code.

The separate SAT-oracle PHP CNF generator is not used by the degree estimator.

### The dormant search is not exact either

`_can_approximate()` truncates the monomial set to the first `n+3` monomials. It therefore cannot certify a minimum over all degree-d multilinear polynomials once the full basis is larger.

This issue is secondary because the active estimator never calls the helper.

## Scope of the refutation

This expedition does **not** conclude that p-vs-np-hunter as a whole is mathematically worthless or that every statement in its repository is false.

The narrow conclusions are:

- the public degree table is software-reproducible;
- the graph rows are meaningful exact algebraic-degree computations for the implemented predicates;
- the non-graph rows are heuristics/extrapolations, not computed minimum approximation degrees;
- the PHP field-asymmetry interpretation is not supported as an empirical measurement of PHP;
- no circuit lower bound follows from these rows without a precise encoding, a correct degree notion, and a theorem-level transfer.

## Reproducibility

Run:

```bash
python expeditions/001-audit-pvsnp-hunter/reproduce_degree_table.py \
  --output /tmp/reproduction-results.json
```

The script uses only the Python standard library and includes assertions against the audited published values.

Committed reference output:

`expeditions/001-audit-pvsnp-hunter/reproduction-results.json`

## Research lesson

A table can be perfectly reproducible and still be semantically mislabelled.

For AI-assisted mathematics, provenance must be checked at three levels:

1. **where did the number come from?**
2. **what mathematical object does that computation define?**
3. **what theorem, if any, permits the prose interpretation?**

Expedition 001 succeeded by making those three questions disagree visibly.
