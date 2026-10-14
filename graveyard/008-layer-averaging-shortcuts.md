# 008: layer coverage is not uniformity; seed averages are not pointwise bounds

Approval night: 2026-10-14 JST. State: refuted by exact finite countermodels.
Author/attacker: 月野テンプレクス. Same-author checks, not independent review.

## A. Covering every layer input is insufficient

Tempting claim: any collection of distinct coordinate permutations that reaches
every input of a Hamming layer has the same average as the uniform layer mean.

Take n=3, x=(1,0,0), and these four distinct permutations, written as images of
coordinates 0,1,2:

```
(0,1,2), (0,2,1), (1,0,2), (2,1,0)
```

Use the established pullback convention y_i=x_{p(i)}. Their output multiplicities
are (1,0,0):2, (0,1,0):1, (0,0,1):1. The layer is covered completely, but the
indicator of (1,0,0) has mean1/2 instead of the uniform layer mean1/3.
Thus even distinct permutations and full coverage do not establish uniformity.

Repair: use the entire permutation group with uniform mass, prove transitivity
and invariance, and discharge exact fiber cardinality w!*(n-w)! rather than
assuming it. Arbitrary subcollections require a separate weighted-balance proof.
Deduplicating outputs can give a uniform layer mean when it is intentionally
renormalized; it does not preserve the original permutation-indexed weights
unless those multiplicities are handled correctly.

## B. The four n=8 seeds are not the final witness distribution

Tempting claim: the four polynomials in Expedition004, with weights
[1,3,4,4]/12, already have pointwise success at least2/3 because their weighted
layer averages meet that threshold.

At input integer14, LSB-first bits [0,1,1,1,0,0,0,0], only one of twelve seed
mass units is correct. The exact seed success is1/12. Among all256 inputs,
82 have raw seed success below2/3. The minimum1/12 and its input are reproduced
by audit.py, not inferred from an optimization solver. The formal candidate
also encodes this input and links its integer ticket count to actual real
probability on actual GF(2) polynomials.

This does not refute the existing n=8 certificate. Its intended distribution
first chooses a seed and then a uniformly random full coordinate permutation.
The valid general layer bridge constructs exactly that distribution. A layer
bound certifies the symmetrized witness, not the unchanged seeds.

## Reproduction and interpretation

From the repository root:

```
python expeditions/009-hamming-layer-bridge/audit.py
python -O expeditions/009-hamming-layer-bridge/audit.py
```

The checker retains both countermodels, all nine n=8 layer means and exact
affine dual scores. Its six certificate/fiber mutations and four mutations of
the actual Lean data are all rejected. Normal and optimized executions agree.
The conclusion and retained CI report, rather than this candidate-stage record,
state the eventual observed Lean verification status.

These are diagnostic examples of invalid bridges, not claims of new mathematical
phenomena. Neither countermodel rules out every smaller-support witness, gives
an asymptotic lower bound, or decides P versus NP.
