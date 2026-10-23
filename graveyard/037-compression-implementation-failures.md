# Preserved compression proof-implementation failures

Approved 2026-10-23 JST. These failures did not refute or weaken the theorem.

Source058d7a090f6e8aff1b391911cc3472064f2aea1e, completed FAILED
run39962214807/job120442780461. Full decoded job output was inspected.
Actual error excerpts (not a full log archive):
2026-10-23T13:36:24.2588072Z error: PvsNPCartography/TwoPointCompression.lean:37:45: unsolved goals
Goal: (MvPolynomial.C a + MvPolynomial.C b).totalDegree <= 1
2026-10-23T13:36:24.2593078Z error: PvsNPCartography/TwoPointCompression.lean:89:41: `simp` made no progress
Cause: broad simplification expanded a constant; complement-cardinality needed
an explicit theorem. Repair used totalDegree_C/totalDegree_X and card_compl.

Intermediate7a672435dc41c03c0fb8473d44ffcaaff492cc0a accidentally concatenated
`hy hR` into the nonexistent name `hyR`. Source-level typo was immediately
corrected by7f039dba58c50a1bdfab3b8781849d0e1062f804. No independent run verdict
is claimed for the intermediate typo revision because its job was not inspected.

Source7f039dba58c50a1bdfab3b8781849d0e1062f804, completed FAILED
run39963303353/job120446559981. Full decoded job output inspected.
2026-10-23T13:44:38.1561389Z error: PvsNPCartography/TwoPointCompression.lean:37:45: unsolved goals
Remaining goal: max 0 1 <= 1.
The restricted norm_num simplification did not close the decidable maximum fact;
the next repair supplies `decide`. No statement, degree, grid hypothesis,
quantifier, warning rule, toolchain or axiom allowlist was changed.

Lesson: a successful source write is not a proof acceptance. Inspect the actual
remaining goal, keep repairs implementation-only, and archive failed revisions.
