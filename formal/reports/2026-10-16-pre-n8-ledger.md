# Formal assumption ledger

Current checkpoint: **2026-10-13 approval night**. Complete degree-based MOD3
equalities for n=5,6,7 and the generic full permutation-symmetrization interface
are verified under the recorded Lean assumptions. Hamming-layer counting,
complete n=8 formalization and independent human semantic review remain pending.

## Policy and reproducible commands

No project-specific extra axiom is declared or intentionally accepted. The
compiled namespace audit permits only propext, Classical.choice and Quot.sound.
A new axiom requires explicit disclosure and is not to be called a proof.
Closed finite arithmetic uses decide +kernel, not native_decide.

Run from formal/:

```bash
lake build --wfail
./scripts/axiom_report.sh
```

The script prints both PvsNPCartography/AxiomAudit.lean and
PvsNPCartography/SymmetryAxiomAudit.lean. Reports below are retrieved actual
#print axioms output, not conclusions drawn solely from source-text searches.
The existing allowNonModules compatibility policy is unchanged.

## Current verified code and actual output

Code commit: ac61ba1b2888de029b8fc567187ff3a4dbb263c0.
[Formal run38414011388](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38414011388),
job115353465722, succeeded under pinned Lean4.35.0-rc4 and
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Actual output records --wfail,
205 namespace declarations within the allowlist, and 21 explicit symmetry
targets using only the same three foundational axioms.

[Actual attributed report](reports/2026-10-13-full-symmetrization-axioms.txt),
[statement audit](../expeditions/008-full-symmetrization/statement-audit.md),
[conclusion](../expeditions/008-full-symmetrization/conclusion.md) and
[claim008](../claims/008-full-symmetrization.md) retain the exact scope.

The generic result uses genuine GF(2) MvPolynomial objects, actual totalDegree,
nonnegative REAL probabilities summing to one, and one family before every
input. It proves the exact success/orbit-average identity and full success
invariance. The orbit-certificate equivalence adapts to the original degree
predicate rather than redefining it. A closed n=6/n=7 MOD3 application derives
feasibility from previous proofs; it does not assume the desired result.

Re-fetched and locally matched source blobs:
PermutationTransport.lean 8bb3a9eddf18d81e382d956ea395b8592ca54bb2;
FiniteSymmetrization.lean 42685e01f5c65442164615ffc39d8f76230aad2c;
SymmetryApplications.lean 69d079fcfbe128b400976d4facce8f5cfb5ae803.
The final commit/tree and completed job logs were separately retrieved.

## Distinct executable checks and repairs

Core proof c1ff9c8639e9aef0a83f9492f087934085fd5c83 first passed
run38412149245/job115346960273, with 188 declarations and 16 targets.
[Semantic run38412385402](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38412385402),
job115347783200, passed at b2602bb5269bdbbda85cc1fc57610bd0208c2a72.
Normal and -O Python outputs match local reproduction; the two core source
hashes are unchanged in the final code. This earlier semantic run does not
pretend to be a run on a later commit. Seven countermodels and four malformed
probability/group inputs are checked. Three counterexample components are
also formalized; the precise coverage is not overstated as seven Lean proofs.

The first core candidate75ce55de failed on an overloaded sum_comp name.
Repair c1ff9c86 specifies Equiv.sum_comp. The first application7093b107 failed
on an unresolved characteristic-two constant; repair ac61ba1b proves it by
kernel computation and then rewrites division. Neither statement, threshold,
warning policy nor axiom allowlist was weakened. Failures remain in history.

## Current boundary

The general full permutation transformation is complete. The uniform
Hamming-layer mean formula, including orbit coverage and equal permutation
fiber counts, is NOT yet proved in Lean. It is the next interface before the
existing n=8 certificate is connected. Finite n=7 layer tests do not fill it.

Numerical degree equalities are unchanged: n=5,6,7 are complete in Lean; n=8
has its previous exact executable certificate. No all-n MOD3 degree bound,
new numerical value, support minimality, novelty, barrier escape or P-vs-NP
result follows. Independent human semantic review remains outstanding.
No second proof kernel was run. Same-author algorithms and different CI
machines are not independent mathematical reviewers.

## Preserved historical ledger

The complete pre-symmetrization ledger is preserved byte-for-byte as
[2026-10-13-pre-symmetrization-ledger.md](reports/2026-10-13-pre-symmetrization-ledger.md),
Git blob1e4ecd7e7df12bc1a91a2bad696d0d217c88d35b. Its historical pending
statements describe those earlier checkpoints, not the current frontier.
It contains all former detailed verification histories and failure repairs:

- n=6/n=7 small-support proof: code8899e756, run38307092042, 145 declarations.
- n=5 complete degree interface: code512aaf27, run38150083188, 86 declarations.
- n=5 concrete components: code0150b864, run38055370947, 64 declarations.
- finite real-mixture duality: code97c459e0, run37940286899, 11 declarations.
- original pinned scaffold: code146ea42f, run37789136586, 10 declarations.

Original attributed reports remain at their existing paths. No historical
proof artifact or failed attempt was deleted by this ledger refresh.
