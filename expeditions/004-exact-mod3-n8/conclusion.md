# Conclusion: n=8 has exact probabilistic degree 2

Date: 2026-10-09 (JST). Issue #7.
Evidence: exact finite certificates, different evaluators, exhaustive pointwise
permutation audit, and successful independent-runner CI. Novelty unknown.
Not a Lean-verified MOD3 theorem and not an asymptotic result.

## Statement

Let f:{0,1}^8 -> GF(2) equal 1 exactly when |x| is divisible by 3.
The least d for which a distribution on polynomials of degree at most d
satisfies Pr[P(x)=f(x)] >= 2/3 for EVERY x is exactly 2.

## Upper certificate and quantifiers

Use certificate.json. Choose a row with probabilities 1/12, 1/4, 1/3,
1/3, then choose a uniform permutation of the eight variables. Each
resulting polynomial still has degree at most 2.

For fixed x of weight w, each y of the same weight occurs as its image
under exactly w!(8-w)! permutations: independently biject the occupied
and unoccupied coordinates. Thus the agreement probability of each
symmetrized row is its layer-good count divided by binom(8,w).
This is a distribution on polynomials chosen independently of x.

| Row | Probability | Constant c | Linear a | Quadratic b | Good counts w=0..8 |
|---|---|---|---|---|---|
| 1 | 1/12 | 0 | 0 | 268435455 | 0,8,0,56,70,56,28,0,1 |
| 2 | 1/4 | 0 | 166 | 191494995 | 0,4,26,32,42,44,18,8,1 |
| 3 | 1/3 | 1 | 155 | 254268221 | 1,5,21,37,39,35,17,5,1 |
| 4 | 1/3 | 1 | 127 | 66817983 | 1,7,22,37,52,33,22,5,0 |

Masks use lexicographic unordered pairs and least-significant bit first,
as documented in orientation.md and implemented in verify.py.

The mixed success on layers w=0,...,8 is exactly

[2/3,17/24,125/168,2/3,2/3,115/168,17/24,2/3,2/3].

Every entry is at least 2/3, so degree 2 suffices. This is an existence
proof; there is NO need to exhaust all possible quadratic polynomials.
Four is not claimed to be the minimum possible number of orbit rows.
The witness's minimum 2/3 is not claimed to be a global max-min optimum.

## Lower certificate, independent of earlier expeditions

Choose weight 1 or 3 with probability 1/2 each, then an input uniformly
within that layer. This assigns probability 1/16 to each weight-1 input
and 1/112 to each weight-3 input.

Every degree-at-most-1 polynomial has the form c + a.x over GF(2).
For c=0 and k=|a|, the success is

s(k) = (8-k)/16 + [binom(k,1)binom(8-k,2) + binom(k,3)]/112,

where out-of-range binomial coefficients are zero. The first term counts
zero intersections on weight 1, and the second counts odd intersections
on weight 3. Changing c complements the correctness bit.

| k | c=0 success | c=1 success |
|---|---|---|
| 0 | 1/2 | 1/2 |
| 1 | 5/8 | 3/8 |
| 2 | 9/14 | 5/14 |
| 3 | 33/56 | 23/56 |
| 4 | 1/2 | 1/2 |
| 5 | 23/56 | 33/56 |
| 6 | 5/14 | 9/14 |
| 7 | 3/8 | 5/8 |
| 8 | 1/2 | 1/2 |

Consequently ALL 512 affine polynomials have q-average success at most
9/14 < 2/3, with strict gap 1/42. This table is additionally checked by
complete affine enumeration rather than trusted as a symmetry reduction.

For any distribution on affine polynomials, even with arbitrary real
probabilities, averaging its deterministic-row bound still gives at most
9/14. A mixture that had success at least 2/3 on every input would have
q-average at least 2/3. The two finite sums can be exchanged, producing
a contradiction. Thus degree at most 1 is impossible.

Combining the independent upper and lower certificates gives the result.
The separate Lean finite_dual_obstruction lemma expresses the generic
finite-sum step, but no MOD3 instantiation has been checked in Lean yet.

## Verification evidence

Initial certificate/verifier/CI commit:
7355f4e5b826a1b34e0f48d891c208495c821cca.

[CI run 37940070467](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940070467)
completed successfully on CPython 3.12.15. The job output was fetched and
checked, not inferred from a commit or file upload. It reproduces all
512 affine rows, the exact upper table, two polynomial evaluators,
40320 permutations at each of 256 inputs, and six negative controls.
The verifier also passes under python -O because it does not rely on assert.

The repository blobs were fetched and compared with locally executed bytes:
certificate.json: 45f4c6b63b17ad5f7820512bb01530a93c345885;
verify.py: a2e4cb25e0a95d2fabcb9b80f35bada672a9eb95.

## Interpretation

This resolves the repository's n=8 finite target, not P vs NP. Targeted
literature checks found the standard definition and asymptotic bounds,
not an exact equivalent table. This is NOT evidence of novelty.
The current frontier is faithful Lean instantiation (Issue #8) and,
separately, an n=9 attempt with fresh certificates rather than extrapolation.
