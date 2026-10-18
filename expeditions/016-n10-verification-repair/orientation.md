# Expedition016: diagnose and repair n10 formal execution

Approved session: 2026-10-18 JST. Research lead: 月野テンプレクス.
Base main: 9739517a174699fd729df98b3974d584c92fce3c. Priority gate: open #10;
next finite frontier #11, independent human semantic review #8.

Read AGENTS and its five required documents, current open Issues, latest commits,
and the 2026-10-17 night log. The existing n10 source is a faithful candidate but
both previous builds were cancelled with exit143 before the axiom audits. This
session does not reinterpret those cancellations as either proof or refutation.

First experiment: isolate exact closed computations, measure time and return
codes, and compare kernel reduction with proof-producing call-by-value decision.
The primary Lean reference describes decide_cbv as producing proofs using only
standard axioms, unlike native_decide. This is a hypothesis about usable tooling,
not a claim that the pinned version or this particular file succeeds.
Reference checked 2026-10-18:
https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference

The diagnostic uses the existing n10 file with a fixed SHA256, does not modify
its statements, coefficients, probability threshold, quantifiers or allowlist,
and does not import the unverified main root. Temporary profile files are NOT
promoted to theorems. Capture all outputs and exact generated source hashes.
A repair can be promoted only after the actual production source is committed,
compiled under the pinned toolchain, axiom-audited, and re-fetched with its CI.

Local check: lean and lake are absent; github.com DNS resolution fails. Use
connected GitHub writes and Actions for formal execution. No paid resources,
publication claims, new approvals or new recurring tasks are authorized here.
