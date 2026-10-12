# 006: one cyclic orbit is not enough for this twelve-ticket compression

Date: 2026-10-13 JST. State: refuted, exact finite exhaustive self-audit.

## The tempting step

For n=7, take seed (c,a,b)=(1,71,1887847), with binary linear and
lexicographically indexed quadratic masks. Its complete permutation orbit has
2520 distinct polynomials. Four symmetric polynomials are
(0,0,0), (0,0,2097151), (0,127,0), (1,127,2097151).
The attempted compression assigns them ticket masses [1,2,1,1] and replaces
the seed's fully symmetrized contribution by one seven-row cyclic orbit,
with one ticket per row. There are twelve tickets total.

The invalid inference would be: since the target is symmetric, seven cyclic
shifts can replace every permutation without changing the pointwise guarantee.
Cyclic invariance is weaker than full permutation invariance. Inputs of equal
Hamming weight can lie in different cyclic orbits.

## Exhaustive falsification, with a concrete counterexample

The checker enumerates all 5040 permutations, deduplicates the 2520 seed rows,
and partitions them into all 360 possible seven-row cyclic suborbits.
For every candidate it checks all 128 inputs with exact integer arithmetic.
None attains the required minimum of 8/12. The best attained minimum is 7/12.
A best-case cyclic orbit, using the same mask convention, is:

```
(1,15,867559), (1,30,1808851), (1,60,900344), (1,71,1168883),
(1,99,1842871), (1,113,1950970), (1,120,2072083)
```

At input integer 5, or LSB-first bits [1,0,1,0,0,0,0], it succeeds on only
seven of twelve tickets after the four symmetric contributions are included.

Reproduce from the repository root:

```
python expeditions/007-small-support-mod3/audit.py --cyclic-attack
python -O expeditions/007-small-support-mod3/audit.py --cyclic-attack
```

Both commands also reject six altered certificate claims. The same outputs
were observed on the separate GitHub Actions runner in run 38307092049,
job 115003655051, at code commit 8899e75646a443415d5a2346d3c8f48d62c7bb79.

## Repair and limits

Two cyclic orbits of seven rows each, plus symmetric ticket masses [2,4,2,2],
give the surviving 24-ticket, 18-distinct-polynomial witness. All 128 inputs
are checked directly; the formal upper theorem does not assume a symmetry
lemma. The resulting minimum is exactly 2/3, not strictly greater.

This failure rules out ONLY one cyclic suborbit of this particular seed with
these fixed symmetric ticket masses. It does not rule out every twelve-ticket
quadratic construction, prove minimal support, or establish a global optimizer
infeasibility claim. Solver time limits and solver infeasibility messages in
the exploratory search are not mathematical certificates.
