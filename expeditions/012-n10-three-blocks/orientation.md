# Expedition 012: n=10 restricted three-block single-orbit attack

Date: 2026-10-16 JST, after the verified n=9 milestone. This is a small
**restricted negative exploration**, not a proof of n=10 probabilistic degree.

For n=10 MOD3 over GF(2), enumerate every one-orbit quadratic polynomial
that is invariant within 1, 2 or 3 nonempty variable blocks. For m blocks,
there are 1+2m+choose(m,2) GF(2) coefficients: constant, block-parity,
within-block e2, and pairwise block products. Each coefficient mask defines
one polynomial whose full-variable-permutation orbit is used uniformly.

Exact integer layer counts determine the worst-input success of its orbit.
The search covers 14 descending block-size partitions and 8520 coefficient
patterns, with zero numerical tolerance and without any optimizer.

**Observed:** no candidate reaches 2/3; the best within this class is
(4,3,3), mask727, minimum62/105 < 2/3. Its full 1024-input truth table is
separately recomputed and matches the combinatorial count. This excludes
only a precisely specified single-orbit, <=3-block family, not any
multi-orbit mixture, four-block partition, or arbitrary quadratic witness.

Reproduce with `python expeditions/012-n10-three-blocks/scan.py`,
including `python -O`. Verify CI success before promoting executable checks.
Historical failure and frontier are recorded in graveyard/012.
