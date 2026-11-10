# Observed execution — fixed-proof recovery, 2026-11-10 JST

Research lead: 月野テンプレクス. Fresh approval covered this session only. The November9 source was inherited and inspected; it was not presumed accepted from a stale status document or an interrupted chat.

## Accepted formal checkpoint

Commit443fc96147b8bd616f82250eeb14c1484510e694, tree53d6b566eaa773c8b427e40179dbf152db1e74a8.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/42728862159
Job https://github.com/yo4e/PvsNP-Cartography/actions/runs/42728862159/job/129541435980

Completed job states and full decoded output were retrieved. Checkout and source hashes identify this exact commit. All build/audit and earlier report steps succeeded. Actual repaired file, matching commit/diff and ModulusAudit were re-fetched after success. The new declarations and elaborated endpoint assumptions were inspected, not inferred merely from a green status.

Selected actual log excerpts, NOT a full raw-log archive:

```text
2026-11-10T00:34:17.3391631Z ✔ [9078/9083] Built PvsNPCartography.FixedProofTransfer (6.1s)
2026-11-10T00:34:21.7455417Z ✔ [9079/9083] Built PvsNPCartography.SignedProjection (4.3s)
2026-11-10T00:34:25.7531524Z ✔ [9080/9083] Built PvsNPCartography.FixedProofCounting (4.1s)
2026-11-10T00:34:29.5558181Z ✔ [9081/9083] Built PvsNPCartography.FixedProofDomain (3.7s)
2026-11-10T00:34:33.1667458Z Build completed successfully (9083 jobs).
2026-11-10T00:35:22.8978754Z axiom-audit: audited 1594 declaration(s) under 'PvsNPCartography'; all within the allowlist [propext, Classical.choice, Quot.sound].
2026-11-10T00:36:59.1148442Z 'PvsNPCartography.FixedProofDomain.cube_count_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-11-10T00:36:59.1149037Z 'PvsNPCartography.FixedProofDomain.cube_rejects_all' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Strict --wfail was retained. ModulusAudit has76 named axiom reports and20 explicit signatures;33 reports/13 signatures concern the fixed-proof adapter including its full-cube reindexing. The foundations allowlist was not widened.

Actual versions: Lean4.35.0-rc4 c29b6dda4f7c20e3eeaa717c4e565663c5cfa364; Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. lean-action@v1 resolvedba3fdfe5c4476c925da13bf11a005ddb47e47aee; axiom-auditv0.1.2 resolved46024e005996495c65ef609368e11ab39c4222e3; checkout11d5960a326750d5838078e36cf38b85af677262. Runner2.338.2, Ubuntu26.04.1 image20261101.186.1. Normal cache restored from1a7a25a. No clean-room build, independent semantic reviewer or second kernel is claimed.

Inspected source blobs under formal/PvsNPCartography:

| File | Git blob |
|---|---|
| FixedProofTransfer.lean | ddb02de1a8e5ed864178eae3aa0e0c0dc7b233c0 |
| SignedProjection.lean | 6d9bf5213a4a7b3ddfa1e2a2cfdcac264cc4b188 |
| FixedProofCounting.lean | fc7a052b511ba763544066046170a8f50abf4b8b |
| FixedProofDomain.lean | f0af28658d68e58e735f0f48cd3394dc0cdf4c52 |

formal/ModulusAudit.lean blob2375614f448e68b7a041d6f3b946524864e59aa2. No Lean source changed after443fc961 in this session. Later records are not new mathematical-source execution evidence.

## Failed executions retained

Inherited run42571547351 attempt2/job129010841391 failed HTTP504 while downloading Lean; no proof compilation occurred. A fresh retry/job129535545790 reached compilation and exposed FixedProofDomain's encoding and ambiguous-sum errors. Repair00b831c3791c84fe06abd08579d91dd7403d4685 failed run42728284436/job129539460542 at its remaining left-inverse simplification. The accepted repair uses direct membership extensionality rather than a weaker statement. See ../../graveyard/2026-11-10-fixed-proof-recovery.md.

## Finite adapter and query-pressure replication

Code checkpointb742079296f15da7790a2e9eb711b89031fea57e, treefb71bdd7eea96de3bf39eacec5409275e8f70de6; completed SUCCESS run42730390055/job129546608938. All four checker steps, normal/-O comparisons, stored-output comparisons and py_compile succeeded. The full decoded job log and completed steps were retrieved; checkout hash matches the commit. This Python run is separate from Lean acceptance.

Actual CPython3.13.5; runner2.338.2, Ubuntu24.04.5 image20261101.360.1. Pinned checkout11d5960a326750d5838078e36cf38b85af677262 and setup-pythona26af69be951a213d495a4c3e4e4022e16d87065. Node-action deprecation warnings remained visible; no test was waived.

verify_adapter.py SHA2567a4f0ffd6eba562b1a121b9af2b4598240f8f22772db6866f47f086fa9f966c8; full checks.json/stdout SHA256fbf67b97aff45fd24bfdb7eadbfdebc50b13c5c3b5dfb64c619c59cc96aafc42. It reports950 exhaustive substitutions,1536 seeded signed clauses,3840 block cases,9984 exact head counts,2486 ordinary-degree checks and8790 pointwise comparisons;1200 denominator-4 mixtures,3600 normalized test distributions,67200 clause checks and7002 positive witnesses;25830 threshold comparisons including2139 equality boundaries. Seed20261109. These bounded rational controls do not prove the arbitrary-real or universal-polynomial statements.

query_pressure.py SHA2567462090f6f5943ad7d54186e0b619c624d8150a62c0caee0cd68529ebc9f2de5; full query-pressure.json/stdout SHA256791327f5a79ce02ff25205e470ef39f7c80426fda7641adeb0e0b838909705e9. It checks45 concentrated-query family instances for1<=n<=9,1<=k<=n and16 weighted-error controls. The written general family is separate from these tests.

The new capacity and factor-four suites are documented in ../036-query-capacity/execution-evidence.md. Same-author paths and another runner are replication, not independent semantic review. Local Lean/Lake were absent and Git DNS failed; connected writes and Actions worked. No write-security blocker or unapplied patch remains.
