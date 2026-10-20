# Retrieved verification evidence: balanced affine algebra, 2026-10-20 JST

## Actual formal acceptance

Repaired code dde6151abd4a4a272a2bdcbbd277c7296487d2c5, tree
7c07084a3f867891092e247922a6741d62750525.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/39381768668
Job118492254315 completed SUCCESS, including pinned --wfail root build9044 jobs,
518-declaration namespace allowlist, six auxiliary targets and all18 n11 targets.
Lean4.35.0-rc4 and Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8;
allowlist unchanged: propext,Classical.choice,Quot.sound.

The full actual completed log was inspected. Then the ENTIRE repaired source
and actual Git commit/tree were re-fetched, not inferred from a green badge.
Source blobef92fdecc80241481d9b4578dce596848733ff33; SHA256
5a6bfaa519c10b8205cd0a019d0e87e353f7f8133163cb477c4b407b4a62b335.
The local corrected source independently hashes to that exact Git blob.
See axiom-report.txt for attributed toolchain/build/audit/target excerpts.

The accepted theorems cover real algebra, complement symmetry and the exact n6
boundary. They do not assert the generic Boolean-cube counting identity; #12
tracks that missing connection. Formal numerical degree equalities remain n5..11.

## Separate bounded exact tests

Codeea1f4e04dae7cc6a6041bd192d1bc95880fafb47.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/39381262415
Job118490656488 completed SUCCESS, CPython3.12.15. Entire actual log inspected.
Normal and optimized Python output match byte-for-byte, and parsed actual JSON
equals finite-result.json. Re-fetched result blob720dc3ff2ecc5109f1091720946748609b975033.

Selected attributed actual output:

```
2026-10-20T06:35:33.2797481Z     "strict_bound_n5_k1": "7/10",
2026-10-20T06:35:33.2798688Z     "strict_bound_n6_k1": "2/3"
2026-10-20T06:35:33.2800478Z   "formula_cases": 33147,
2026-10-20T06:35:34.2909885Z Exact bounded tests agree; general counting bridge and Lean are separate gates.
```

Scope:33147 formula comparisons for n3..256 and every integer0<=k<=n;
full Boolean cubes and all affine rows through Walsh/direct checks for n3..12.
These are bounded checks, NOT proof of the all-n counting identity. The saved
result keeps its original finite-evidence label after algebraic acceptance.

## Preserved failed build

Initial formal run39381262500/job118490657553 at ea1f4e04 failed on missing
noncomputable for the real-valued definition and an unused-hypothesis warning.
The full failure log was inspected and preserved in graveyard019. Repair changes
only computability annotation and explicit use of the existing hypothesis. No
statement, threshold, linter, --wfail or axiom policy was weakened. A successful
Python run at the failed formal commit was never counted as Lean success.
