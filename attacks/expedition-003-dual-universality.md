# Adversarial review: n=8 sampled dual is not universal

Date: 2026-10-08. Role: Skeptic.

## Candidate attack target

From a 10,016-polynomial sampled set, an exact dual distribution
q was extracted from an LP whose optimum within the set is 569/902.
An alluring but INVALID next step is to assert:

> Every degree-at-most-2 polynomial on eight bits has q-average
> success at most 569/902 (and therefore below 2/3).

The finite pool has 6,407 unique layer profiles, not the full class
of 2^37 coefficient tuples. There is no exhaustive coverage lemma.

## Refutation (exact integers, independent of floating point)

q[w] = [207,1983,6550,4969,3150,1085,3482,1901,125][w]/23452.

Take constant=1, linear_mask=255, quadratic_mask=60548413.
Quadratic mask bit j denotes the j-th lexicographic pair in
combinations(range(8),2).

Explicitly checking all 256 inputs gives successful counts by weight
w=0,...,8:

[1, 8, 17, 34, 39, 28, 21, 6, 1].

For each layer, divide the count by binom(8,w) and weight by q[w].
The exact rational total is

27376/41041 = 2/3 + 46/123123 > 2/3 > 569/902.

This is a deterministic quadratic polynomial; no n=8
pointwise randomized upper certificate follows from this fact.
It refutes **that dual q's universal upper bound**, not the
conjecture that n=8 degree 2 might be sufficient.

## Independent verification

- Original numerical sampled LP and a fresh unseeded-candidate
  search with fixed seed 20261009 found the omitted polynomial.
- A second evaluator used only standard-library integer bit operations,
  Fraction, and combinations to recheck its entire truth table.
- Repository-resident verifier also checks the 9-orbit sampled primal,
  the sampled dual, and the adversarial omitted polynomial.

## Required repair

No promotion from a sampled pool to the complete polynomial class
without a coverage theorem and exact verifier. Preserve this
counterexample whenever a later sampling optimizer emits a convincing
looking dual.
