# Execution evidence — 2026-11-05 JST

Research lead: 月野テンプレクス. Fresh steward approval covered this session only. All claims below distinguish observed execution from written argument and independent review.

## Accepted formal source

Commit `51a86b10cb0f493b0c093aa81dba734400cb0118`, tree `c04b4412f9426b633c6e8c1d57f29af737dc0e01`.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/42038613103
Job https://github.com/yo4e/PvsNP-Cartography/actions/runs/42038613103/job/127283180450

The completed job summaries and full decoded job output were retrieved through the connected GitHub tools. Source checkout in that output is exactly the commit above. The actual commit/diff, repaired source at this immutable ref, and ModulusAudit were re-fetched. The job concluded SUCCESS, including all previous reports and the new folding/zeta reports.

The following are **selected verbatim message excerpts**, not an archive of the full raw log:

```text
2026-11-05T13:48:20.4152787Z ✔ [9076/9079] Built PvsNPCartography.FoldedBlockCount (7.2s)
2026-11-05T13:48:24.6188469Z ✔ [9077/9079] Built PvsNPCartography.SubsetZeta (4.2s)
2026-11-05T13:48:28.5274252Z Build completed successfully (9079 jobs).
2026-11-05T13:49:22.2369054Z axiom-audit: audited 1466 declaration(s) under 'PvsNPCartography'; all within the allowlist [propext, Classical.choice, Quot.sound].
2026-11-05T13:50:55.9775904Z 'PvsNPCartography.SubsetZeta.exact_count' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Actual strict build used `--wfail`. ModulusAudit printed43 named axiom reports and7 explicit signatures, including the final original-polynomial count endpoint. No new axiom, sorry/admit, native_decide, goal-as-hypothesis, or warning waiver was introduced by the two-line repair. Existing default foundations were not widened.

Lean4.35.0-rc4 commit `c29b6dda4f7c20e3eeaa717c4e565663c5cfa364`; Lake5.0.0-src+c29b6dd; Mathlib `9e6b3aac99b624d10c84653ab9c5357283b9b3b8`. Resolved lean-action `fe408643ea7367d8c0404a8be3975bb145f5fb64`; axiom-auditv0.1.2 `46024e005996495c65ef609368e11ab39c4222e3`. Runner2.338.2, Ubuntu24.04.5 image20261101.360.1. Normal cache was restored from574a3da. This is NOT a clean-room build, second-kernel check, or independent semantic review.

Source blobs retrieved in the session:

| File in formal/PvsNPCartography | Git blob |
|---|---|
| ModulusAmplification.lean | c68f8baac5b175cc7f5a8db0e733c6cbb0c834bc |
| IntegerPolynomialLift.lean | a87e961e7f7021c7acd45b2b0cb9ea0627e44868 |
| BooleanIntegerReduction.lean | f0c86b30ef53a39cf34c645db705209e685aa183 |
| FoldedBlockCount.lean | 46472044700be38d79600f7e4cba3e4a71334a7b |
| SubsetZeta.lean | c2091ed34234a06516ab374e92af08c3e4f59724 |

`formal/ModulusAudit.lean`: `4b8a8171bc05d3349ccd6af660f96458ffa8b9b4`.
Later code-test and record commits are not additional Lean execution evidence; no Lean source was changed after51a86b10 in this session.

## Finite replication and new cost controls

Local environment: Python3.13.5. Each script was run normally and with `python -O`; each pair of complete stdout files was byte-identical. `python -m py_compile verify.py runtime_audit.py` also succeeded. Checks use explicit exceptions and therefore remain active under optimization. No finite run is promoted to a general theorem.

Unchanged `verify.py`:8516bytes, Git blob `86fd6619fb243bb898689934c42aa7782df554bc`. Both replication outputs exactly reproduce existing `checks.json`:1531bytes, Git blob `5d935979891c625028645edabf46bd2be7ee6488`, SHA256 `aab3cce3bcad18ba0ff7ec734ea4b5dd11e66618ff7478bea1ca4fc215134931`. It checks1548 signed integer instances and75295 exact head counts across15039 polynomial/block cases. Repeated variable powers, signed lifts, empty/full blocks, constants and known wraparound controls are included.

New `runtime_audit.py` at `7eb2f25aa57b676f55f36a9648cd5212e9678ed4`:9541bytes, Git blob `965bbe7f2dd78a9e8927edc0b5aee12ab5e4d248`, SHA256 `55f4c61a65dc756221f6a73227aa52aea2cb950e1c40f85335880ec1d5a2d115`. The actual immutable remote file was re-fetched and its blob matched the executed local bytes.

Its complete stdout is `runtime-audit.json` at `0762832f6e5bf8c27c83ee63a7ff7ac68078209f`:6615bytes, Git blob `57d40f665dfb6451844ee098c676fae742a811ab`, SHA256 `bed7456bce29bc5670eb5c3179716132185228edd1b1d272d5a14550991670fb`. The remote result was re-fetched and its blob matched both local runs. It reports373 source cases,1747 source/block cases,22719 exact head counts,26616 exhaustive signed modular tables,604 finite parameter-budget checks, and the explicit duplicate-coordinate/overwrite controls. n<=3 source ANFs are exhaustive; n4..8 use named deterministic samples and constant/linear controls, NOT exhaustive enumeration.

The runtime code uses a distinct deterministic sort-and-aggregate coefficient construction and a true shared table, compared against brute source evaluation and the earlier quotient implementation. All are same-author checks; no independent semantic reviewer is claimed.

## Evidence boundary

`cost-and-fidelity.md` at `ccc22bf79e6adde2af99d95c81a20f4959bd4db0`, blob `52fd8fd45005f67a339bd64fa2c4cfd854daa7da`, contains the written general cost derivation and exact exponent budget. It was re-fetched after writing. That argument and the Python-to-specification refinement are NOT Lean cost theorems. The build acceptance proves the extensional integer-polynomial statement, not a compiler, a wall-clock speedup, novelty, or an unrestricted lower bound.

Local Lean/Lake were absent and git clone failed DNS. Connected GitHub writes and Actions execution worked. The failed previous build and rejected shortcuts are preserved separately in graveyard. No security-layer write denial or unapplied patch occurred in this session.
