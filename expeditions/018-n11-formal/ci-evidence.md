# Re-fetched n11 formal and finite evidence, 2026-10-20 JST

## Formal production run

Code9733d800128ad6d92b1f1293e453a4c8d5188f34, treeec4b8aa8bbfab9b5bc6d4e134acde3c785f6475f.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/39380310454
Job118487684638 completed SUCCESS, including root --wfail, compiled namespace
allowlist and explicit target reports. The full completed job log was retrieved.
Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8;
9043 build jobs,508 namespace declarations,18 explicit n11 axiom targets.
Only propext,Classical.choice,Quot.sound are used. See axiom-report.txt.

After the actual logs, re-fetched both the coefficient definitions and the final
upper/lower, feasible_degree_iff, IsLeast and pdeg_eq_two theorem statements at
the exact commit, then the Git commit/tree. Source blob
1eb242d53c74bb546a3547d9107b8074cb40caa3; SHA256
 eb8c4bc823cf0b370ae09746ef3c63ab5d4d7403e1ab0a11f0a4b7257087f00a.
No acceptance was inferred from merely writing a source file or queuing a run.

## Complementary exact semantic audit

Code9238f5a13f541bd1a3da6457a9ec219a9b7aabca.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/39380579421
Job118488536922 completed SUCCESS. Full actual log inspected, including normal
and optimized outputs, bytewise comparison and parsed saved-result equality.
CPython3.12.15. Re-fetched finite-result.json blob
c4d5926702bbf395d4de544f90c91409edae196a matches the actual output.

Selected actual output:

```
2026-10-20T06:28:50.9116065Z   "coefficient_mutations_detected": 201,
2026-10-20T06:28:50.9116666Z   "expanded_formula_evaluations": 1015808,
2026-10-20T06:28:50.9124136Z   "lean_source_sha256": "eb8c4bc823cf0b370ae09746ef3c63ab5d4d7403e1ab0a11f0a4b7257087f00a",
2026-10-20T06:28:50.9148502Z   "upper_minimum": "158/231"
2026-10-20T06:28:55.4439537Z Actual finite audit equals saved output; Lean acceptance is a separate gate.
```

All2048 inputs,4096 affine rows,12 layers,201 coefficient changes and five
source-data/target mutations are checked by algorithms not relying on Lean.
The finite output deliberately remains labelled a finite audit even after the
separate formal run succeeds. These are complementary, not interchangeable,
evidence classes. They do not satisfy independent human semantic review #8.
