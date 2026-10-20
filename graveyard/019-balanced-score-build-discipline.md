# Failed first formal build: real score computability and an unused bound

Candidate commit: ea1f4e04dae7cc6a6041bd192d1bc95880fafb47.
Run: https://github.com/yo4e/PvsNP-Cartography/actions/runs/39381262500
Job118490657553: completed FAILURE. The full completed log was retrieved.
This is an implementation failure, not a counterexample to the real inequality.
The separate n11 source had already passed run39380310454 at9733d800.

Relevant attributed actual diagnostics:

```
2026-10-20T06:38:09.7370684Z warning: PvsNPCartography/BalancedAffineDualAlgebra.lean:20:62: Variable name `hhi` is not explicitly referenced.
2026-10-20T06:38:09.7373472Z error: PvsNPCartography/BalancedAffineDualAlgebra.lean:34:4: failed to compile definition, consider marking it as 'noncomputable' because it depends on 'Real.instDivInvMonoid', which is 'noncomputable'
2026-10-20T06:38:09.8359430Z error: build failed
```

The build used --wfail and the existing foundational axiom allowlist; the
namespace and explicit target audits were skipped after failure. Successful
bounded Python tests do not turn this failed Lean build into formal acceptance.

Repair: mark the real-valued score definition noncomputable, and explicitly
use sub_nonneg.mpr hhi for its factor bound. Preserve every theorem statement,
domain, threshold and proof dependency. Do not disable the linter, --wfail or
any axiom check. This file records the first failure regardless of the repaired
run's later outcome. Actual repaired acceptance must be established separately.
