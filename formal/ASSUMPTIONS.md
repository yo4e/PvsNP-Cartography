# Formal assumption ledger

## Checkpoint — fixed global proof to actual signed-clause integer counts, 2026-11-10 JST

Research lead: 月野テンプレクス. Issue27 completed under fresh approval. Issue28 records a future research target, not continuing authority. The complete previous ledger is preserved byte-identically at ../reports/2026-11-10-pre-fixed-proof-ledger.md, blob5eccd2ce714229c56b7768cbbd28004757fd5fbd. Prior scope, histories and independent-review gates are not erased.

## Observed formal acceptance

Source443fc96147b8bd616f82250eeb14c1484510e694; tree53d6b566eaa773c8b427e40179dbf152db1e74a8. Completed SUCCESS run42728862159/job129541435980. Actual source, matching commit/diff, ModulusAudit, completed step states and full decoded log were retrieved. Strict --wfail9083 jobs and1594 namespace declarations within unchanged[propext,Classical.choice,Quot.sound]. ModulusAudit printed76 named axiom reports/20 expanded signatures, including33/13 for the adapter. No new axiom, sorry/admit, native_decide, warning waiver or statement weakening was introduced by the repairs.

Lean4.35.0-rc4 c29b6dda4f7c20e3eeaa717c4e565663c5cfa364; Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Resolved lean-action@v1 is ba3fdfe5c4476c925da13bf11a005ddb47e47aee in this run, not the older action revision. Axiom-auditv0.1.2 remains46024e005996495c65ef609368e11ab39c4222e3. Normal cache restored from1a7a25a. There was no clean-room build, independent semantic reviewer or second proof kernel. Full provenance and selected excerpts: ../expeditions/035-fixed-proof-adapter/execution-evidence.md.

## What the source actually proves

FixedProofTransfer keeps one actual pi and one finite family of global functions chosen before all tests. Polynomial instantiation uses the unchanged actual MvPolynomial/totalDegree predicate with arbitrary normalized nonnegative REAL weights. Test weights are likewise normalized and nonnegative. One true signed literal is selected using pi, before the sampled polynomial; the clause-error bound needs no independence between repeated queries. Finite averaging gives a positive-mass sample, not an arbitrary zero-weight row. Soundness is an explicit premise over all global proof functions.

SignedProjection builds real polynomial objects using constants, variables and negated variables, then MvPolynomial substitution. Its degree and evaluation theorems refer to this construction, not a supplied oracle. Negations and repeated coordinates are allowed. The signed-OR polynomial evaluates to the actual clause bit and has totalDegree<=3D.

FixedProofCounting applies the already accepted integer lift/reduction/folding/subset-zeta chain to those actual clause polynomials. It sums actual outputs and proves the count/acceptance identity. Uniform threshold conversion retains a nonempty clause index type and a positive natural denominator v. It compares u*number_of_tests with v*totalOutput using integers; it is not a floating-point approximation. Empty Boolean arities/head/tail remain allowed.

FixedProofDomain proves actual inverse maps between head-subset/tail pairs and the full Boolean randomness cube, not merely equal cardinalities. Uniform acceptance is transported by this bijection. Final cube_threshold, cube_count_witness and cube_rejects_all use number_of_tests=card(I)*2^(a+b), the original pointwise approximation predicate, and global-proof soundness. They do not assume the desired count equality or restrict approximators to enumerated tiny coefficients. The reindexing identity is valid on empty finite domains, but normalized uniform probability/threshold applications retain nonemptiness.

These are extensional correctness statements. They do NOT prove an efficient Python implementation, a compiler refinement, a general PCP theorem, the time hierarchy, or an unrestricted lower bound.

## Failure and finite evidence

The inherited source8feb021e initially failed before compilation on a Lean-download HTTP504. Retrying exposed proof-script representation and ambiguous-sum errors. Repair00b831c still failed a left-inverse simplification. Repair443fc961 uses membership extensionality, explicit Boolean encodings and an explicitly typed real summand. Every theorem statement and strict policy was retained. Failures are preserved in ../graveyard/2026-11-10-fixed-proof-recovery.md.

The targeted Python workflow atb742079296f15da7790a2e9eb711b89031fea57e passed run42730390055/job129546608938. It reproduces9984 exact head counts,25830 threshold checks and67200 finite clause inequalities among other controls. The rational-mixture tests are not the arbitrary-real proof. Normal/-O/stored outputs match; no finite run substitutes for the general kernel result.

## Explicitly outside this formal checkpoint

The query-density counterfamily, real-capacity/weighted-Hall characterization, sharp factor3 deterministic-selection loss, signed error-set characterization and sharp factor4 non-tautological width-three certificate loss are WRITTEN arguments with finite corroboration in Expeditions035/036. They are not covered by the successful Lean build. The factor4 premise excludes positive-weight tautologies; the bound concerns all binary global proofs, not a general low-degree-restricted optimum. A degree-one witness attains the named sharp example only.

The separate written conditional E^NP/infinitely-often hierarchy reconstruction and counting-runtime analysis from Expedition034 retain their external assumptions. No independent semantic approval, second kernel, novelty, unrestricted separation or barrier escape is claimed. Issues8/15 remain open at their earlier scopes. Local Lean/Lake were absent and Git DNS failed; connected GitHub/Actions worked. No write-security denial or unapplied patch remains. Later sessions require fresh approval.
