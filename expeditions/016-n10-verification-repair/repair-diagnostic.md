# Actual repair diagnostic: split kernel cases succeeds

Completed run39138440340, job117707686566, codece4fda646dbd40ced956a3c6450602cc2be6185b.
Full completed log inspected. Lean4.35.0-rc4 and pinned Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8; prerequisite --wfail build9034 jobs passed.

The first targeted strategy changes ONLY the proof of layer_tickets_exact:

```lean
  intro w
  fin_cases w <;> decide +kernel
```

No theorem statement, coefficient, success threshold, quantifier, heartbeat or
axiom allowlist changed. No cbv tactic or increased step budget was adopted.
The bounded-cbv alternatives in the probe were NOT executed, because the first
strategy passed. The previous night shutdown cause remains unknown.

Actual layer-only check:133.100 seconds, exit0, no timeout.
Actual full candidate check:152.043 seconds, exit0, no timeout, all15 explicit
Mod3Ten targets printed and checked against exactly the foundational allowlist.
No sorryAx or Lean error occurred. This is an actual diagnostic success, not
an inference from the aggregate workflow status.

Actual final target excerpt:
'PvsNPCartography.Mod3Ten.pdeg_eq_two' depends on axioms: [propext, Classical.choice, Quot.sound]

Candidate production source SHA256:
5d6aa5a2df006cee95a9d43b0707505298f431d38f0c984440fb5b0d1553b571
Full diagnostic including the15 appended reports SHA256:
bc5e32adc81bb91c4eb585f7d32f73a3e167d12726130776c14686dd6418ed24
Layer-only source SHA256:
e4ad993c2b15cee447e51dece2612983d7e5dafd69192b7a2eb8b30d5ff89275

Artifact12140851866, n10-proof-repair-diagnostics,7 files,9230 bytes.
Zip SHA256:58ed9c397b57401c78c4b4fc189431c6829e428bc4b4ae7bfba7fd05165a60fb.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39138440340

This commit applies the exact candidate to production and updates ONLY the
source-hash field of the independent finite result. Final promotion still
requires completed production --wfail/root build, namespace audit, target
reports and matching source/commit re-fetch. Those later results belong in
conclusion.md and the formal assumption ledger, not fabricated here.
