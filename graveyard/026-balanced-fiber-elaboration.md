# Rejected first fiber formal candidate, 2026-10-21 JST

Code9abc8c23cdc6e99e105d052cf75c0fe4aed247ae. Actual completed FAILURE
run39546373832/job119045364935. Full completed job log fetched and inspected.
This is a failed proof implementation, not a counterexample to the intended
point-mass formula and not a defect in the previously accepted obstruction.

The first attempt directly unfolded sampleInput inside dependent conditional
expressions. It left a decidability argument for sampleInput(.inl i)=x where
the rewritten term expected bits{i}=x at implicit transparency. A triple
conditional also remained unsolved after aggressive simplification. Deprecated
if_pos/if_neg and redundant simplification/field tactics produced warnings,
which are rejected by the retained --wfail policy.

Actual diagnostic excerpts:
```
2026-10-21T04:55:02.3785778Z error: PvsNPCartography/BalancedAffineFibers.lean:121:41: unsolved goals
2026-10-21T04:55:02.3790253Z error: PvsNPCartography/BalancedAffineFibers.lean:125:11: `simp` made no progress
2026-10-21T04:55:02.5260856Z ##[error]Process completed with exit code 1.
```

Repair candidate: use the already proved inputMass_mean on a point indicator,
then prove explicit singleton/triple summand identities with change and narrow
conditional rewrites. Use the current ite_eq_left/right names and remove only
redundant tactics. Keep inputMass, sampleMass, bits, theorem statements, n>=3,
full fiber sums, --wfail and the foundational axiom allowlist unchanged.
A later completed run must establish whether this repair succeeds; the act of
committing it is not verification. The generic subset-intersection candidate
is an independent additional module, not a hidden assumption in this repair.
