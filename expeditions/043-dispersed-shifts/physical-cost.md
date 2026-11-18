# Pooling physical reads saves at most a fixed-rate factor

Use the original shared RS test of Expedition 038 with rate exponent a and the original-token blocks in [Expedition 042](../042-accepted-sites/exact-overlap.md). Let W_z be the distinct physical symbol addresses read by the all-fresh-tapes test at z. Translation covariance makes u=|W_z| independent of z.

A *physical cell* y has a canonical owner. A root cell can be reached only by the all-row shape. A nonroot owner ends in a row edge wR. Only two complete down shapes can reach it, namely wR followed by row edges to a leaf, or wC followed by row edges to a leaf. A deeper column would stop the ascent at its own sibling. The second path is available precisely on the common rectangle, where the owner's row-coordinate marker equals one.

Trace the saved labels and the point of y in the original-token layout. They specify one k-bit word φ(y). Fresh positions are excluded. A complete shape with leaf block I can read y exactly at the seeds φ(y)+E_I, where E_I permits arbitrary changes on I. Necessity follows by reading every original bit outside the leaf from the saved edge labels. For sufficiency change only those leaf bits, then select the same absolute leaf coordinate using its appropriate XOR offset. Fresh choices are enumerated, so the canonical address is still read.

For a root or a nonrectangle row cell the reader set is one such coset. For a rectangle it is the union of the two cosets from its two possible shapes. The distinct leaf blocks are disjoint. Hence the multiplicity is respectively

    2^|I|, or 2^|I| + 2^|J| − 1.

Each leaf has at most 2a original coordinates. An all-row tail entered through a row edge retains at most a: its last internal dimension is 2a+1 and its last row split keeps a old coordinates. This includes an immediate leaf after the first row edge. Thus the uniform upper bound is B_a=2^(2a)+2^a−1. This is independent of k and is attained by a common-rectangle cell at root dimension 4a with original bits present in all root positions. It concerns one distinct seed per base call; repeated occurrences within a call have already been pooled.

The same last-row observation sharpens the old displacement radius. A single leaf block has size at most 2a. In each internal-node pair, the row-tail block has size at most a and the column-tail block at most 2a. Consequently every displacement in K has Hamming weight at most 3a. The pair at root dimension 4a attains 3a. The previous bound 4a remains valid but is not sharp.

For t **distinct** masks and any external seed z, sum the sizes of W_(z+h). There are t u incidences, while no physical cell can appear more than B_a times. Therefore

    t u / B_a ≤ |union_h W_(z+h)| ≤ t u.

At fixed rate, pooling physical symbols cannot remove the order-t growth from adding t distinct translated tests. In particular an exponential improvement in call count cannot be obtained by pooling the original physical cells. This statement prices symbol reads. Boolean coordinate packaging, queries at repeated slots and field arithmetic have additional costs. It gives no universal lower bound on equivalent algorithms with a different proof representation.

## Executed check and an exact small fingerprint

The checker obtains each full physical view from the previous independent literal-coordinate router, inverts these views by cell, and compares the **entire** set of seeds reading each cell with the formula above. The construction of φ(y) uses the final canonical owner and never imports a claimed down path. It checks all cells at k=7,8,9,10 with a=3, including parent and sibling aliases.

| k | Distinct cells per base seed | Distinct cells in the full proof address set | Maximum base seeds reading one cell |
|---|---:|---:|---:|
| 7 | 124 | 1,024 | 23 |
| 8 | 604 | 16,384 | 23 |
| 9 | 668 | 32,768 | 39 |
| 10 | 4,508 | 524,288 | 39 |

The generic bound B₃=71 is loose for these four cases. The stored incidence histogram also double-counts exactly 2^k u. A separate k=12 common-rectangle cell has exactly 71 readers by the formula: the checker independently confirms membership for all 71 predicted readers and nonmembership for 16 outside seeds with the literal router. It does not enumerate every outside seed in that last control. Shape bounds are also checked for a=3,…,7 and 2a≤k≤64a. The all-parameter statements rely on the derivations above, with no Lean or external review certificate. [Executable](check_incidence.py) · [Exact output](incidence-checks.json)
