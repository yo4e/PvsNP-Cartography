# 2026-10-29 JST night — actual randomized gates and shared-error control

Research lead: 月野テンプレクス. Fresh approval in this conversation only.
Read live AGENTS, all mandatory references, current open Issues8/15/22, recent
commits, current status/ledger and the growing-degree handoff. Selected Issue22.

## Research result

Completed its natural generic-gate milestone. RandomizedGates constructs actual
GF2 OR/AND polynomials from uniform independent rows and returns the original
fixed-before-input finite REAL-mixture probabilistic-degree predicate for every
arity k and r, including zero: degree<=r, error<=2^-r. Exact error is0 on the
appropriate exceptional vector and2^-r otherwise. Actual substitution gives
<=rD for arbitrary degree<=D sources, with no Boolean degree reduction.
NOT/XOR/constants are exact. One shared matrix also satisfies the union bound
<=S2^-r on S fixed deterministic input vectors, with no inter-gate independence.

## Actual commits and completed verification

6aeb47aa27583eaa8189495d1188e153212c7c64: useful orientation and actual write probe.
15d2dc2b144a54790334c4c9740bbf6ca735074c: first formal candidate; failed run40881942065/job123475459692.
1ea3559ed9c10898dff62c00189d65e91e92a968: repaired/extended candidate; failed run40883125251/job123479644185.
879f4a5c4bc1ae53e66ba5ef7f2a854b136480ec: exact DAG controls, proof derivation and four counterexamples; SUCCESS run40883896389/job123482350566.
5e43c061544f2d56e924a03420c39d40ad5ecbc6: final formal repair; SUCCESS run40884225246/job123483506622.

The accepted formal run used Lean4.35.0-rc4/Mathlib9e6b3aac, whole-root --wfail9069
jobs,1083 declarations within [propext,Classical.choice,Quot.sound],22 new explicit
gate reports and all old reports. The actual source, matching Git commit/tree,
completed steps and full decoded output were re-fetched. Local source blob
0b3c1ac0 matches GitHub. This is kernel acceptance, not independent semantic review.

Exact tests exhaust6566 two-gate programs at r1/2 and8 deeper programs at r1/2/3.
Sparse actual-polynomial and Boolean interpreters agree, pointwise degree/error
and true-input union controls pass. Python3.12.15 normal/-O output bytes and the
committed JSON agree; local reruns and source hashes also match. Finite controls
are not a universal DAG theorem. Full provenance: Expedition029/ci-evidence.md.

## Refutations, repairs and blockers

Graveyard048 preserves two implementation failures and their repairs, with no
weakened statement or audit. Graveyard049 kills four shortcuts: coefficient tying
by source-wire identity (error1), multiplying correlated failures (1/4 not1/16),
fixed-input claims on adaptive inputs (error1 not1/2), and r0 circuit degree
(actual1 exceeds alleged0). Historical repeated-row/affine/degree controls remain.

Local Git DNS failed and Lean/lake were absent; connected GitHub and Actions
worked. No write approval/security blocker, unapplied patch or missing file
remains. No new independent semantic reviewer or second kernel participated.
#8/#15 keep their older review scopes; neither is silently extended to this code.

## Decision and next frontier

Issue22 remains OPEN. The first three generic-gate tasks are completed; the
arbitrary shared-DAG model/depth/first-error/predicate bridge is still unformalized.
Its mathematical derivation and finite controls are saved, not promoted to a
closed Lean theorem. Next entry is Expedition029/next-frontier.md: derive actual
degree<=r^h/error<=S2^-r for original-node count S and r>=1, then the original
error1/3 predicate and restricted-model MOD3 size consequence n<(16*r^h+2)^2+2.

Known-method reconstruction, novelty-unknown. No new unrestricted circuit lower
bound, barrier escape, optimal constant, general n12 classification or P-vs-NP
conclusion. Earlier accepted MOD3 results remain intact. Central status/assumption
ledger are updated with their previous complete versions archived byte-identically.
This session stops at the verified generic-gate milestone; later work requires
fresh approval rather than reuse of this conversation's authorization.
