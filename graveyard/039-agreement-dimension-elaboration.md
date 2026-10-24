# 039: agreement-dimension implementation failures and faithful repairs

Author: 月野テンプレクス. Approved 2026-10-24 night session, executed 2026-10-25 JST.
These are implementation failures, not counterexamples to the mathematical
statement. The unchanged --wfail and axiom policies remain binding.

## First failed candidate

Source e91ecfd14ac3f844fa23398ab6f515a13e89d5f4, run40106942238,
job120910479991. Completed FAILURE; full actual job log inspected.
Lagrange indicator statements used if x=z without a Decidable equality during
statement elaboration. A proof-local classical tactic is TOO LATE for the
statement. Deprecated if_pos/if_neg names generated strict-build warnings.
Finset.coe_toFinset was not the actual name; Finset.toFinset_coe was intended.
Downstream diagnostic placeholders printed as sorry were compiler recovery,
not source proof placeholders and not acceptance evidence.

## Second failed candidate

Source2dcb53fc1e27a365c9eb2167d75806df5a1b26f2, run40107571288,
job120912334405. Completed FAILURE; full actual log inspected.
A remaining Lagrange branch needed the reverse inequality b!=a explicitly.
Deprecated push_neg and an unused eq_comm simp argument violated --wfail.
A finite-span coercion proof also had a hidden-instance mismatch despite
identical printed types. The repair uses the pinned direct finite-set span
bound, consistent classical proposition decidability, explicit reverse
inequality, push Not and removal of the unused simp argument.

## Third failed candidate: warning-only full build

Source6bbb93af87d382f81e65b83a27ca39c1d91d3715, run40108267893,
job120914398144. Completed FAILURE; full actual log inspected.
AgreementDimension built successfully. AgreementConsequences had no proof
errors but two unused-section-variable warnings: its grid_card and
grid_same_card proofs do not need a Field instance. The strict whole-root
build failed as intended, and the axiom audit/target reports did not run.
This partial success is NOT the final acceptance record.

Repair8e5be8ce59b069c278ec32839552dad712de04e1 adds omit [Field K] only to
these pure grid-counting lemmas. It neither disables the warning nor weakens
the agreement theorem's nonzero/degree/field premises or the real-mixture
probability contract. Its completed build and reports must independently
confirm acceptance; see Expedition025/ci-evidence.md for the final verdict.

All failed sources remain in Git history. Do not report the three failures as
successful formal verification, and do not use old green finite tests as a
substitute for the new universal proof and axiom checks.
