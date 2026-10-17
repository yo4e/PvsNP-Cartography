# Two interrupted verification attempts, not a mathematical refutation

Code:d25c6cd777c7585d2765682baf34a94e38a9d6bc.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/39037050907
Final status of both attempts:CANCELLED. Build step FAILURE; namespace and
explicit target axiom audit completion is absent.

## Attempt1: job117408893626

The full completed log was fetched. Relevant actual ending:

```
2026-10-17T13:43:07.1912528Z ##[error]Process completed with exit code 143.
2026-10-17T13:43:07.1914696Z ##[error]The runner has received a shutdown signal. This can happen when the runner service is stopped, or a manually started runner is canceled.
```

One rerun of that job was requested and accepted. No theorem, coefficient,
threshold, quantifier or axiom-allowlist change was made in response.

## Attempt2: job117411619247

The rerun also ended CANCELLED. Its full completed log was fetched:

```
2026-10-17T13:47:43.2337314Z Lake version 5.0.0-src+c29b6dd (Lean version 4.35.0-rc4)
2026-10-17T13:48:57.0547312Z    "rev": "9e6b3aac99b624d10c84653ab9c5357283b9b3b8",
2026-10-17T13:50:05.5354986Z   BUILD_ARGS: --wfail
2026-10-17T13:54:06.4754254Z ##[error]The runner has received a shutdown signal. This can happen when the runner service is stopped, or a manually started runner is canceled.
2026-10-17T13:54:06.4758136Z ##[error]Process completed with exit code 143.
2026-10-17T13:54:06.5246003Z ##[end-action id=__leanprover_lean-action.build;outcome=failure;conclusion=failure;duration_ms=240995]
2026-10-17T13:54:06.5749989Z ##[end-action id=__leanprover_lean-action.axiom-audit;outcome=skipped;conclusion=skipped;duration_ms=0]
```

No third identical rerun was requested. The local environment has no Lean;
connected GitHub reads/writes work, so this is not a write-permission failure.

## Failure boundary and salvage

Both runs resolved pinned Lean4.35.0-rc4 and Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8. They do NOT supply a completed n10
elaboration verdict, audited namespace count or explicit target axiom reports.
The logs do not establish WHY the runner shutdown occurred. Do not choose
between infrastructure failure and manual cancellation without further evidence.
The available failure is not a mathematical counterexample and not proof success.

Keep the exact independently validated n10 data and candidate source. Keep #10
OPEN for interruption diagnosis and one uninterrupted pinned build plus audits.
Resource profiling and splitting expensive closed computations are possible
next experiments, not changes already tested. Do not weaken the target or the
allowlist. Complete formal numerical coverage remains n5..9.
