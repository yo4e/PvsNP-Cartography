# Conclusion — a correct count, and two reasons not to mistake it for general hardness

Research lead 月野テンプレクス. Freshly approved2026-11-02 JST session. Issue24 completed; Issue25 is the next bounded target. This is not authority for later work.

## Mathematical result

The original pointwise finite REAL-mixture predicate implies a positive-support polynomial within Hamming radius floor(2^n/3). Counting the squarefree evaluation span and the union of binary Hamming balls yields, for every natural n,d,

 |L(n,d)| <= 2^(sum(j<=min(n,d),choose(n,j))) * sum(j<=floor(2^n/3),choose(2^n,j)).

This is a standard-method reconstruction in Lean, accepted at16de2eb187960c770e63114b3dadbb1690f08b3f after completed run41396234158/job125118052432. The final statement does not assume the desired cover/count. It retains actual totalDegree, arbitrary nonnegative normalized REAL weights and a family fixed before every input. It is not an exact feasibility classification.

The conditional half-density implication is also kernel accepted. A separate written binomial/induction proof establishes its arithmetic premise for every n>=7,d<=1. That unconditional estimate and the recognition results are not additional Lean endpoints.

## What the attacks changed

A Walsh transform recognizes affine farness efficiently in truth-table length, but a six-periodic residue-count argument shows that constant0 is already close enough to MOD3 whenever n mod6 is2,3,4. Thus the uniform detector misses the intended target infinitely often, without contradicting its pointwise degree lower bound.

More decisively for the general-circuit objective, the paired quadratic function XOR_j(x_(2j)*x_(2j+1)) is affine-far for every n>=4 yet has linear-size circuits. Largeness plus efficient recognition therefore does not give THIS property's usefulness against P/poly. These are written all-n arguments with finite checks, not new kernel theorems or novel lower bounds.

A measure balanced between positive and negative target inputs repairs the trivial constant advantage and gives a written n>=8 affine gap, but it is weaker than our already accepted n>=7 result. Further polishing of that repair is parked.

## Verification and preserved failures

All16 new formal reports and3 explicit signatures, whole-root --wfail and the unchanged namespace axiom audit completed. Actual source/commit/tree and completed output were re-fetched; local hashes agree. Two failed candidates were repaired without weakening statements, increasing the heartbeat cap or waiving warnings. graveyard057 preserves them.

Exact source9eb549897f5e227708ac9e7b73a3f72b0e2db237 passed completed run41396010959/job125117369329. The two evaluators agree on all65814 small target tables, among the other controls. Finite tests corroborate definitions; they are not universal proofs or independent review. graveyard056/058 preserve the semantic failures, and059 preserves the next route's modulus-wrap error. Full evidence boundaries are in ci-evidence.md.

## Decision and next entry

Retain the valid one-way covering tool, but stop treating its uniform degree-one detector as a promising general-circuit route. Issue25 instead targets integer modulus amplification and no-wrap recovery of exact accepting-assignment counts for a GF2 polynomial block. A written construction and a local prototype have been saved at0ea0ec1fd5eb1550c457a2c451bf2f5c662bd830;3673 block counts agree with direct enumeration. Those continuation tests are outside the completed covering CI and not a generic formal proof or speedup claim.

The next question is whether the actual algebraic transformation and finite counting invariant can be reconstructed faithfully before pursuing a complete faster counting algorithm and, separately, its lower-bound consequence. No independent semantic review, second kernel, novelty, unrestricted separation or barrier escape is inferred. No write blocker or unapplied patch remains. This is the natural stop for this approval.
