# Actual execution evidence: randomized gates and shared-DAG controls

Recorded by 月野テンプレクス in the freshly approved2026-10-29 JST night session.
No new independent semantic reviewer or second kernel was used. The source and
completed result, not merely a write response or queued run, were inspected.

## Accepted formal source

Commit5e43c061544f2d56e924a03420c39d40ad5ecbc6;
tree9afbe56bae28fc6abed2cd67aade538f7e6b7132;
parent879f4a5c4bc1ae53e66ba5ef7f2a854b136480ec.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/40884225246
Run40884225246/job123483506622 completed SUCCESS, including every explicit
report step. Full decoded actual job log was retrieved and inspected.

Actual toolchain: Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Whole-root build used --wfail and completed9069 jobs. The namespace audit checked
1083 declarations within [propext,Classical.choice,Quot.sound]. GatesAudit printed
22 new theorem-axiom reports and4 target signatures. Earlier target, transport,
majority and growing-degree reports all completed successfully.

Actual lean-action: fe408643ea7367d8c0404a8be3975bb145f5fb64.
Actual axiom-audit v0.1.2:46024e005996495c65ef609368e11ab39c4222e3.
Normal caches restored74eca7066e3f0725b8d67a159d4c0dc5bd576662; no clean-room or
alternate-kernel claim is made. No audit allowlist or warning policy was relaxed.

Actual RandomizedGates.lean was re-fetched at the accepted commit, including its
complete final section. Blob0b3c1ac0ecb64e6521af678e9532e6c9d3dfe55a matches
local14111 UTF-8 bytes. A local token scan finds no sorry/admit/axiom/native_decide
in that module. The matching Git commit/tree was independently retrieved.
axiom-report.txt retains labeled actual output excerpts, not the complete raw log.

Failed predecessors:15d2dc2b / run40881942065 / job123475459692;
1ea3559e / run40883125251 / job123479644185. Both actual completed failure logs
were inspected. Their errors and repairs remain in graveyard048.

## Separately accepted finite controls

Commit879f4a5c4bc1ae53e66ba5ef7f2a854b136480ec;
treef77b3a92e8a2896c4efd332108cac915023c87a9.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/40883896389
Run40883896389/job123482350566 completed SUCCESS. Actual checkout SHA,
Python3.12.15, all completed steps and full decoded output were retrieved.
Normal and python -O output were compared byte-for-byte, then compared with
the committed dag-checks.json, before the actual JSON was printed.

Actual checker/result/workflow and Git commit/tree were re-fetched. Blob hashes
match local bytes: check_dag.py254ca41210132ec251bcb6121eca7b11c54de469 (9754 bytes);
dag-checks.json b42d0b3889e829feee9e8a547881fa27bb85c59e (2256 bytes).
The workflow blob is8da42fe19b7f6af16c87f8222cf77c41bb22e618.
Local normal/-O runs and py_compile also passed. Explicit RuntimeError checks
remain enabled under -O. The actual CI output reproduces every saved count and
all four new counterexamples plus the historical actual-degree control.

The exhaustive scope is6566 two-gate programs, two inputs, constants, fan-in0..2,
NOT/XOR/AND/OR and r1/2;131320 program-matrix pairs,262640 actual-degree checks,
1050560 node-input checks,105056 local exact laws and52528 pointwise union bounds.
Eight deeper curated DAGs at r1/2/3 add672 program-matrix pairs,2268 actual-degree
checks,9072 node-input checks and96 pointwise union bounds. Separate sparse
polynomial and Boolean interpreters are SAME-AUTHOR implementations.

## Promotion boundary

The formal promotion covers generic actual OR/AND gates, exact operations and
the shared union bound on deterministic vectors. Finite DAG controls remain
finite evidence. The full arbitrary DAG/evaluator/depth/first-error/endpoint
composition is not yet a Lean theorem. No novelty, barrier escape, unrestricted
circuit lower bound or P-versus-NP conclusion follows from these runs.
Later record-only commits do not retroactively become mathematical source runs.
