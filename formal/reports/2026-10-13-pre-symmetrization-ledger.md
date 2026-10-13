# Formal assumption ledger

Status: **complete degree-based n=5,6,7 equalities, scaffold and finite duality
verified; n=8, generic symmetry infrastructure and independent human semantic
review pending**. Historical sections below retain the state at their dates.

## Project-specific axioms

None are intentionally declared. Every future project-specific axiom needs
an explicit entry and must not be described as a proved theorem.

## CI allowlist and audit command

The compiled namespace audit permits only propext, Classical.choice and
Quot.sound. Anything else under theorem targets fails CI unless the policy
is deliberately revised and documented. Closed finite checks in the n=5,6,7
modules use decide +kernel, not native_decide.

Run from formal/:

```bash
lake build --wfail
./scripts/axiom_report.sh
```

The explicit target list is maintained in PvsNPCartography/AxiomAudit.lean.
The report is produced by Lean's #print axioms, not source-text inspection.

## Verification state: 2026-10-13 JST

Code commit: 8899e75646a443415d5a2346d3c8f48d62c7bb79.
[Formal run38307092042](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38307092042),
job115003654751, completed successfully under pinned Lean4.35.0-rc4 and
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8. Actual completed output
records --wfail success, all145 namespace declarations within the allowlist,
and thirteen newly printed target reports, each using only propext,
Classical.choice and Quot.sound.

SmallSupportMod3.lean now supplies actual field-valued target/evaluation,
structural coverage of arbitrary degree-one polynomial families, normalized
real-mixture duality, actual quadratic polynomial degree/evaluation, and
full-cube kernel arithmetic for n=6 and n=7. The combined feasible_degree_iff,
least_feasible_degree and closed pdeg_eq_two do not assume feasibility or the
answer. The new 18-polynomial upper witness has denominator24 and minimum16/24.
The n=6 and n=7 affine dual bounds are respectively660/1080 and595/1050.

[Actual attributed target report](reports/2026-10-13-small-support-axioms.txt),
[statement audit](../expeditions/007-small-support-mod3/statement-audit.md),
and [conclusion](../expeditions/007-small-support-mod3/conclusion.md) retain
scope and verification details. Source blob7f2e5ecdac08af19ba461d986c84711c13cd980a,
certificate data and code commit/tree were re-fetched and matched local bytes.
[Semantic run38307092049](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38307092049),
job115003655051, passed normal and optimized Python at the same code commit.
Two evaluators, Mobius and Walsh reconstruction agree; all six altered claims
are rejected. All360 attempted fixed-mass single-cyclic-orbit compressions fail,
with the precise scope and a counterexample retained in graveyard/006.

The initial formal candidate92df9d85e2d0a6de7fac21c8c1807758b6415ec8 failed
run38306271041/job115000959315 on a constant-polynomial degree obligation.
The repair explicitly applies totalDegree_C and changes no coefficients,
thresholds, theorem statements, --wfail setting or axiom allowlist.
No failed build was promoted and no native_decide dependency was introduced.

### Current formal boundary

The complete degree-based equality is verified for n=5,6,7. n=8 still has
finite executable certificates but no complete degree-based Lean theorem.
Issue8 stays open for generic full symmetrization infrastructure and independent
human semantic review. The completed upper proofs check every input directly;
an unproved generic symmetry lemma is not one of their premises.
There is no second proof kernel or independent human reviewer in these checks.
Support novelty and minimality are unknown. No new numerical value, general-n
MOD3 theorem, barrier escape or P-vs-NP conclusion is claimed.

## Historical degree-interface checkpoint: 2026-10-12 JST (2026-10-11 approval night)

Code commit: 512aaf2745d2d8aab4bab76c1ac43ff6130d7de2.
[Formal run 38150083188](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38150083188),
job 114501532196, completed successfully under pinned Lean 4.35.0-rc4 and
Mathlib 9e6b3aac99b624d10c84653ab9c5357283b9b3b8. The actual completed logs
show the --wfail build, all 86 namespace declarations inside the allowlist,
and explicit target axiom reports. All newly printed targets depend only on
propext, Classical.choice and Quot.sound.

The completed chain at that checkpoint included:

- exponent_sum_le_one and degree_one_normal_form, a structural normal form
  for arbitrary degree-at-most-one polynomials over a commutative semiring;
- Mod3Five.degree_one_eq_affine and no_degree_one_family, covering actual
  degree-one polynomial objects rather than only a canonical coefficient list;
- HasProbabilisticDegreeAtMost, the finite-support real-probability predicate
  with one family chosen before every input, and its degree monotonicity;
- Mod3Five.feasible_degree_iff, classifying feasibility exactly by 2 <= d;
- Mod3Five.least_feasible_degree and the closed Mod3Five.pdeg_eq_two;
- input_dependent_constant and Mod3Five.swapped_quantifiers_are_strictly_weaker,
  a deliberate countermodel to reversing the input/family quantifiers.

The least-degree definition requires an existence proof. The closed n=5
statement constructs it from the verified quadratic witness; it assumes
neither the answer nor feasibility without proof. The normal form proves
actual polynomial equality using monomial degree bounds, not sampling of
input values. The earlier lower and upper certificate premises remain proved.

See the [actual attributed axiom excerpt](reports/2026-10-12-n5-degree-axioms.txt)
and [statement-fidelity self-audit](../expeditions/006-degree-interface/statement-audit.md).
The three new formal source files and code commit were re-fetched after
compilation and matched the inspected bytes. A distinct finite reconstruction
algorithm and countermodels passed [semantic run 38150257051](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38150257051),
job 114502054887, on test commit 215f89efc3800ecc7c6af97f28c968685406b6b3,
in normal and optimized Python. This is supplementary data/semantic checking,
not an independent human review or a second proof kernel.

The first candidate 6178308d675737d4bcd8115786b5f9d2379734cb failed
run 38149625181 on syntax/type/coercion details and unused simp arguments.
The repaired 512aaf2 proof retained the theorem statements, --wfail, linters,
axiom allowlist and certificate thresholds. No failed build was promoted.

### Formal boundary at the 2026-10-12 checkpoint

The degree-one coverage and complete n=5 degree-equality gaps were CLOSED.
n=6,7,8 had finite certificates but no complete degree-based Lean theorem
at that checkpoint. Issue #8 remained open for the larger cases, general
symmetrization infrastructure and independent human semantic review.
The n=5 upper proof directly checks every input, so an unproved generic
symmetry lemma is not a premise. No new numerical value, novelty, general-n
MOD3 theorem, proof-barrier escape or P-vs-NP result is claimed.

## Historical component checkpoint: 2026-10-10

Code commit: 0150b8642ed5708b8ce3109c6d85fc0d4f5e7872.
[Formal run 38055370947](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38055370947),
job 114222616643, completed successfully in pinned Lean 4.35.0-rc4 with
Mathlib 9e6b3aac99b624d10c84653ab9c5357283b9b3b8. The --wfail build,
compiled namespace audit and explicit target report all passed.
The namespace audit covered 64 declarations, all within the allowlist.

New concrete components in the Mod3Five namespace at that checkpoint:

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

### Formal boundary at the 2026-10-10 checkpoint

The lower class was the canonical binary affine representation, with its
actual polynomial evaluation proved equivalent to the finite checker.
A general normal-form theorem reducing any Mathlib MvPolynomial of
`totalDegree <=1` to this representation was not yet integrated. The
abstract probabilistic-degree equality theorem was not assembled.
Those two gaps are closed by the later checkpoints above.

The upper theorem supplied genuine degree-at-most-two polynomials
with a normalized real finite-support distribution and the actual
pointwise agreement property. It proved every input directly, without
assuming an unproved symmetry lemma. n=6,7,8 had not been formalized.
Issue #8 remained open. No new finite value, novelty or P-vs-NP result.
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
