# n=10: bounded <=3-block single-orbit search, inconclusive globally

2026-10-16 JST. Status: *refuted within restricted class*, not settled for n=10.

All 8520 GF(2) blockwise-invariant quadratic coefficient patterns with
at most three nonempty coordinate groups and ONE uniformly permuted orbit
failed to guarantee 2/3 success on every ten-bit input. Best was
block sizes(4,3,3), binary mask727, with minimum62/105.
The exact layer-good vector for this row is
[1,7,33,88,124,174,148,72,36,7,1] for weights0..10.
A separate direct evaluation of all1024 inputs confirms it.

This DOES NOT show degree two is impossible for n=10: convex mixtures,
quadratics with more than three blocks, and families with other orbit
structure were not checked. Do not promote a finite restricted search
to a universal dual obstruction.

Reproducer scan.py, expected count8520, normal/-O consistency in CI.
Next try a mixture over multiple good candidate orbits with an exact rational
LP reconstruction, or derive a genuine universal quadratic dual.
The n=9 degree theorem remains intact; it does not imply the n=10 result.
No new theorem or P-vs-NP implication is claimed.
