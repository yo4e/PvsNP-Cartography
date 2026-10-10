# Formal assumption ledger

Status: **verified n=5 certificate components, scaffold and finite duality;
abstract degree-based interface and larger-n formalization pending**.

## Project-specific axioms

None are intentionally declared. Every future project-specific axiom needs
an explicit entry and must not be described as a proved theorem.

## CI allowlist and audit command

The compiled namespace audit permits only propext, Classical.choice and
Quot.sound. Anything else under theorem targets fails CI unless the policy
is deliberately revised and documented. Closed finite checks in the n=5
modules use decide +kernel, not native_decide.

Run from formal/:

```bash
lake build --wfail
./scripts/axiom_report.sh
```

The explicit target list is maintained in PvsNPCartography/AxiomAudit.lean.
The report is produced by Lean's #print axioms, not source-text inspection.

## Verification state: 2026-10-10

Code commit: 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872.
[Formal run 38055370947](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370947),
job 114222616643, completed successfully in pinned Lean 4.35.0-rc4 with
Mathlib 9e6b3aac99b624d10c84653ab9c5357283b9b3b8. The --wfail build,
compiled namespace audit and explicit target report all passed.
The namespace audit covered 64 declarations, all within the allowlist.

New concrete components in the Mod3Five namespace:

- mass_sum, affine_integer_bound, affine_gf2_semantics;
- no_affine_approximation for all normalized real coefficient mixtures;
- upper_integer_bound, upper_field_correct, upper_degree;
- exists_quadratic_approximation with actual MvPolynomial objects;
- affine_field_correct, no_affine_polynomial_family for finite families;
- zero_mass_is_not_probability, a deliberate semantic countermodel.

Every printed new target depends only on propext, Classical.choice,
Quot.sound. The two original reduction sanity lemmas still need no axioms;
the other original targets use those same three foundational assumptions.
See the [actual retained report](reports/2026-10-10-mod3-five-axioms.txt).

A [separate semantic CI](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370864)
reproduces the 64-row affine bound, 30-row upper witness, full 120-permutation
orbit multiplicities, two polynomial evaluators and negative controls.
This is data checking, not a replacement for Lean's proof checking.
The code commit and source blobs were re-fetched and matched locally
inspected files before recording verification.

### Current formal boundary

The lower class is the canonical binary affine representation, with its
actual polynomial evaluation proved equivalent to the finite checker.
A general normal-form theorem reducing any Mathlib MvPolynomial of
`totalDegree <=1` to this representation is not yet integrated. The
abstract probabilistic-degree equality theorem is not assembled.

The upper theorem DOES supply genuine degree-at-most-two polynomials
with a normalized real finite-support distribution and the actual
pointwise agreement property. It proves every input directly, without
assuming an unproved symmetry lemma. n=6,7,8 have not been formalized.
Issue #8 remains open. No new finite value, novelty or P-vs-NP result.
No extra proof kernel or independent human mathematical reviewer was used.

### Observed implementation failure and repair

Initial upper commit fcbe841f60feb3d4f3db8f2b0ba887e770b7b31a failed
[run 38054868045](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38054868045)
solely due to an unused `MvPolynomial.eval_sum` simp argument warning.
Commit 782979d0ade9359107c9a576d055895a5b08c084 removed the redundant
argument. Neither --wfail, the linter, the axiom allowlist nor the theorem
statement was weakened. The final code then passed the audited run above.

## Historical generic-bridge checkpoint: 2026-10-09

FiniteDual.lean was compiled with the same pinned Lean and Mathlib.
[Run 37940286899](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940286899)
on commit 97c459e04204b35f970f58b8cbab959986daa98e passed --wfail,
namespace audit and explicit target reports. Job 113852624241 logs were
retrieved. That audit covered 11 declarations. At that time the concrete
MOD3 instantiation was absent; the new n=5 components advance that state.

The two reduction sanity lemmas required no axioms. The disagreement-count
lemmas and finite_dual_obstruction used propext, Classical.choice,
Quot.sound. See [historical report](reports/2026-10-09-finite-dual-axioms.txt).
The generic lemma accepts arbitrary REAL distributions and requires its
supplied deterministic-row bound to be separately proved.
See [FINITE_DUAL_SCOPE.md](FINITE_DUAL_SCOPE.md).

## Historical scaffold checkpoint: 2026-10-08

The pinned scaffold built with --wfail and passed the namespace audit in
[run 37789136586](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789136586)
on commit 146ea42f862a8c5539faa5f5fb5e429a81ece78e. That audit covered
10 declarations; its four original target reports are unchanged.

The preceding failed [run 37696584897](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37696584897)
was caused by a legacy-style module importing new-style Mathlib and issuing
a compatibility warning under --wfail. formal/lakefile.toml explicitly
sets allowNonModules=true as a temporary compatibility policy. This does
not remove --wfail or the axiom audit. Any future migration to the module
visibility system needs its own statement-fidelity review.
