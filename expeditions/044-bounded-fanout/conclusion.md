# A costed improvement, and the remaining physical-query bottleneck

For the actual one-level GF(128) verifier and the specified honest YES reference,
private copy trees change the exact unrestricted signed sensitivity from 288
to 128. Fanout cap 126 adds 2,603 rows to each instance while both fit the old
4,194,304-bit address cube. The NO minimum remains 109. Consequently the strict
sufficient uniform-error threshold rises from `109/1207959552` to
`109/536870912`, exactly **9/4** times as large. This is an improvement of the
actual raw-failure precision, not just of the earlier loose `6M` estimate.

**The finite threshold remains below 1/Q.** Both sufficient bounds therefore
require zero wrong bits for a deterministic approximant. Even for a mixture,
mean wrong-bit count below one forces an exact polynomial to occur with positive
probability. The existential approximation hypothesis is still exact
representability of the respective encoded function. This calibration does
not establish a broader approximable-function class. Moreover, the retained
full-A predicate forces sigma>=N while truthful NO gates give V_NO<=N, so
private fanout optimization alone cannot escape this regime.
[Proof and exact scope](zero-error-regime.md)

The old 288 upper bound is certified by assigning all 10,706,688 satisfied
clause–seed pairs to originally true addresses with maximum load 288. An actual
one-bit error attains that number. The saved code regenerates the allocation;
the saved result includes its digest and mass, not the full allocation file.
The new 128 upper bound follows from a written all-error gate charge and is
attained by flipping one physical A bit. [Instance, counts, and verification](actual-instance.md)

The general compiler statement, with explicit geometry and private-row
hypotheses, is `sigma <= max(mu,f+2)`, with equality `sigma=mu` when `mu>=f+2`.
It preserves `V_NO=gamma_field N`, adds at most `2G+1` copies, and needs at most
four times the old address cube. Deduplicating actual canonical query maps is
legitimate because they obey one seed-translation action. This part is a written
argument. The two small recursive geometries and the GF(128) implementation are
separate computational controls. [Compiler proof](compiler.md) · [Query controls](query-maps.md)

The cap-two variant is a useful rejected optimization: it reaches the same
sensitivity but doubles the cube, retaining only a 9/8 improvement. Omitting
a physical input copy or a private fanout split permits 250 or 199 failures
from one bit. Charging an AND output only once is false. All three shortcuts
are preserved with their counterexamples in [graveyard](../../graveyard/2026-11-21-fanout-shortcuts.md).

Symmetric weighting of shared decision buffers does restore amplified field
rejection at copy weight equal to the number of translations. It simultaneously
raises sensitivity to twice that number. Even arbitrary private-clause weights
cannot improve the optimized unshifted symmetric baseline under nondecreasing
storage. A claim extending the factor-one-half bound to asymmetric copy weights
is false: the positive-weight four-seed example has ratio 4/5. Its asymmetric
baseline changes as well. [Weighted derivation](weighted-copy-repair.md) ·
[Post-mortem](../../graveyard/2026-11-21-weighted-shared-copy.md)

## Next mathematical decision

The private-copy loss has reached its physical-reader floor. Reading every A
symbol from every center forces `mu=N=128` here. Further lowering private
fanout cannot improve that term. The next target is a changed A membership
test or field verifier that reduces that reader load while retaining enough
NO rejection to improve the fully priced ratio and reach `V_NO>sigma`. The
frontier is [Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34).
A proposed sparse affine test
must face arbitrary noncode A tables and shared B auxiliaries. Merely proving
its exact zero-error code space or counting fewer queries is insufficient.

For a complete instance family, a minimum NO bound and a uniform maximum over
the intended YES references remain necessary. The changed encoded proof also
requires its own approximation guarantee; no old approximating polynomial has
been transported for free. Low-degree-restricted error sensitivity may differ
from the exact unrestricted values computed here. The full recursive Boolean
census, the secondary unpaired GF(256) optimum, novelty, independent human
semantic review and new Lean verification remain open. No barrier escape or
unrestricted complexity separation follows.

Reproduction commands and the completed remote evidence are recorded in the
[session log](../../logs/2026-11-21-bounded-fanout.md).
