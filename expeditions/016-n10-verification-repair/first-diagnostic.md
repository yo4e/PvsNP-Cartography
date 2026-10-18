# Actual first diagnostic: isolate the failure before changing production

Run39137339446, job117704436981, commitc29d306c01484de6a5e49909774a23e94f3fc5b0.
The completed full job log was fetched and inspected. Pins: Lean4.35.0-rc4 and
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Narrow prerequisite build passed
9034 jobs with --wfail. Production Mod3TenDegree.lean was not modified.

Actual timings in seconds and exit codes:
cbv-smoke8.192/0; kernel-mass6.595/0; kernel-lower-prefix40.164/0;
cbv-lower-prefix10.471/1; cbv-layer-only9.469/1; cbv-full-with-axioms12.504/1.
No subprocess timeout occurred. The three cbv failures report
`error: simp failed: maximum number of steps exceeded` (the log uses backticks
around simp). Full lower prefix through affine_bound succeeds with the original
kernel decision. The previous runner shutdown cause is still unknown.

The failed full cbv diagnostic printed pdeg_eq_two with sorryAx propagated from
its failed tactic elaborations. This is NOT an accepted proof. The diagnostic
workflow itself was green because its purpose was to RECORD individual failures,
not to certify the library. Its message explicitly warns about this distinction.

Artifact12140576819, n10-proof-diagnostics,14 files, zip12268 bytes, SHA256
 d61ed9521e6b15a76ba56bf12941b68098f04289088afaa0c48597f4d1ed456e.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39137339446

The official Lean reference documents cbv.maxSteps default100000. Follow-up
repair_probe.py keeps the successful kernel lower proof and tests only the
upper layer proof: split kernel cases, bounded6-million-step cbv, or split
2-million-step cbv. Every candidate must pass actual execution and all15 explicit
allowlisted target reports before a later production root/namespace check.
https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/

Operational budget changes do not alter the theorem, its coefficients, real
probability normalization, quantifier order or foundational axiom allowlist.
