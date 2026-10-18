# Failed shortcuts after quotienting n11 partition labels

Attraction: once duplicates are removed, treat every distinct row alike, or keep
only one copy's old mass. Both lose the original probability measure.

1. Uniform weighting of the496 distinct polynomials has success281/496 at
input mask15 (weight4), strictly below2/3. The correct distribution is not uniform:
zero has mass165/1155, each8-subset row4/1155, each7-subset row1/1155.
2. Keeping only one old copy's mass without aggregation leaves total304/1155.
The three orbit fibers have sizes110,3,4 and cannot be discarded for free.
3. Using only the three canonical rows without any symmetrization has success0
at input mask63 (weight6), even though all twelve symmetrized layers pass.

Exact normal/-O controls are in Expedition017/verify.py. These examples kill
only the stated shortcuts. They do not refute the correct496-row measure, the
old indexed certificate or arbitrary quadratic mixtures. Nothing is inferred
about minimal support or asymptotic complexity.
