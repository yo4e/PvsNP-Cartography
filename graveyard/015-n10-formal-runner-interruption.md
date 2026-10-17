# Interrupted verification attempt, not a mathematical refutation

Code:d25c6cd777c7585d2765682baf34a94e38a9d6bc.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/39037050907
Attempt1, job117408893626. Completed status:CANCELLED, build step FAILURE,
explicit target axiom printing SKIPPED.

The full completed log was fetched. Pinned Lean4.35.0-rc4 and
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8 resolved successfully. Build
was invoked with --wfail. The relevant ending is:

```
2026-10-17T13:43:07.1912528Z ##[error]Process completed with exit code 143.
2026-10-17T13:43:07.1914696Z ##[error]The runner has received a shutdown signal. This can happen when the runner service is stopped, or a manually started runner is canceled.
```

The available log does not identify why the shutdown occurred and supplies no
completed n10 elaboration/axiom result. Neither formal success nor a mathematical
counterexample follows. Do not speculate about infrastructure versus manual cause.
The allowlist and theorem statements were not changed in response.

Repair action: one rerun of the same job was requested, successfully accepted.
Attempt2 job117411619247 was observed building. Its final result belongs in the
expedition conclusion and formal report; this file preserves the failed first
attempt regardless of what the later run does. No safety-layer write denial
occurred and no blocked write was retried.
