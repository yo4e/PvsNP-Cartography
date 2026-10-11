# Night research checkpoint: 2026-10-11 approval, completed 2026-10-12 JST

Research lead: 月野テンプレクス. One explicit approval, same session across midnight.
Starting head 845eceb717bc498f1bfe8cccaa0e9a4d7ea757b3.
Read AGENTS.md, mandatory five documents, open Issue #8, latest commits and log.

## Result

The n=5 formal interface gap is closed. DegreeOneNormalForm.lean proves actual
polynomial equality for every degree-at-most-one polynomial, and connects it
to the complete affine class. ProbabilisticDegree.lean gives the finite-support,
real-weighted, input-independent degree predicate. Mod3FiveDegree.lean proves
feasibility iff d>=2, the IsLeast statement, and the closed pdeg_eq_two theorem.
The prior 11/18 lower and 7/10 upper certificates are reused without new assumptions.
This improves formal coverage; it does not discover a new finite value.

## Verify, attack, repair

Initial candidate 6178308d675737d4bcd8115786b5f9d2379734cb failed run38149625181
on syntax/type/coercion details and unused simp arguments. Repaired in
512aaf2745d2d8aab4bab76c1ac43ff6130d7de2 without weakening the theorem or CI.
Run38150083188 / job114501532196 completed successfully: pinned Lean/Mathlib,
--wfail, all86 namespace declarations inside the foundational axiom allowlist,
and actual explicit target reports. New printed targets use only propext,
Classical.choice and Quot.sound. Logs were fetched after completion.

Test commit 215f89efc3800ecc7c6af97f28c968685406b6b3 added a different coefficient
reconstruction algorithm and exact countermodels. Run38150257051 /
job114502054887 passed in normal and optimized Python. All64 affine tables and
2048 evaluations agree. Moving the polynomial choice after the input, or
omitting the degree premise, gives false variants recorded in graveyard/005.
The quantifier contrast also has a checked Lean theorem.

Remote code blobs and commits were re-fetched and matched local file hashes.
See expeditions/006-degree-interface/conclusion.md and statement-audit.md,
plus formal/reports/2026-10-12-n5-degree-axioms.txt for exact evidence.

## Boundary and next frontier

Issue #8 stays open for n=6/n=7, generic symmetry for scaling and independent
human semantic review. The degree-one normal form and complete n=5 equality
are no longer pending. n=6,7,8 retain finite certificates but no complete Lean
degree statement in this checkpoint. No novelty, general-n or P-vs-NP claim.

Local Lean/Lake was unavailable and local network fetching failed; execution
used GitHub Actions. Connector writes worked, with expected-head checking.
No paid compute, publication, credentials or continuing authorization involved.
This closes a natural formalization milestone for the approved session.
