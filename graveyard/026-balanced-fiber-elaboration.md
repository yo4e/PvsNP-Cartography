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
which are rejected by the retained --wfail policy. The build exited1; namespace
and explicit target acceptance were not completed.

Repair: use the already proved inputMass_mean on a point indicator, then
prove explicit singleton/triple summand identities with change and narrow
conditional rewrites. Use current ite_eq_left/right names and remove only
redundant tactics. The second candidate still failed in one conditional block,
separately preserved in graveyard027. The final explicit-conjunction repair
598d54ed passed whole-root production39547776930/job119049747106,639 namespace
declarations and12 new explicit targets; the complete real log was inspected.

inputMass, sampleMass, bits, theorem statements, n>=3, full fiber sums,
--wfail and the foundational axiom allowlist were unchanged. The generic
intersection module is independent, not a hidden assumption in this repair.
This record preserves the original failure despite the later successful repair.
