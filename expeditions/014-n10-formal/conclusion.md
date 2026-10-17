# n10 conclusion: exact audit complete, formal acceptance blocked

Final checkpoint for the approved 2026-10-17 JST session. Complete numerical
Lean coverage remains n=5..9. The n10 module is a CANDIDATE, not a formally
verified extension.

## Completed work

Code d25c6cd777c7585d2765682baf34a94e38a9d6bc adds the genuine-degree n10
interface, root import and 15 explicit target axiom reports. The candidate
retains GF(2) MvPolynomial.totalDegree, normalized nonnegative REAL weights,
one family before every input, the full permutation/layer adapter and
structural degree-one coverage. Endpoints include feasible_degree_iff,
least_feasible_degree and pdeg_eq_two. Their source presence is not acceptance.

The independently reconstructed eight coefficient rows agree on all 1024
inputs with block evaluation and Mobius coefficients. All 11 layer counts
and all 2048 affine scores agree; 448 single-coefficient mutations are detected.
Exact upper minimum2123/3000>2/3 and affine dual152/240=19/30<2/3 are unchanged.
Normal and optimized Python match the saved result in successful semantic
run39037298636/job117409604280, code baa1d976a45c4f74d10dcbb55f7195e7c0ae0744.
Actual completed logs, source and result were inspected separately.

Re-fetched n10 source Git blob6840ecfdd7786b583a7cc089e17da8c2f34e30e0,
SHA256bd998f8ad908a1622cac393dd3b68e62505f2bc01dd2ef9010b9cb7e5c948e93.
See ci-finite-evidence.md and statement-audit.md for the exact finite scope.

## Failed execution gate

Formal run39037050907 at d25c6cd7 was attempted twice. Attempt1 job117408893626
and the one rerun, attempt2 job117411619247, both ended CANCELLED with runner
shutdown and exit143. Namespace and explicit target axiom audits did not finish.
Both full completed logs were fetched. Lean4.35.0-rc4 and pinned Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8 resolved. --wfail and the original
[propext,Classical.choice,Quot.sound] allowlist were not weakened.

The shutdown cause is unknown from these logs. No completed n10 elaboration
verdict, namespace declaration count or target axiom report is available.
Do not infer mathematical failure OR formal success. No third identical rerun
was requested. See graveyard/015-n10-formal-runner-interruption.md for both
attributed failure excerpts. The local container has no Lean; GitHub writes work.

## Attack, record and frontier

The raw eight seeds without coordinate symmetrization fail at mask832 with
success1/50; graveyard013 preserves the counterexample. Uniformly omitting a
coordinate to lift n10 to n11 fails at weight10 with success61/220; graveyard014
preserves that separate failure. Neither refutes the correctly symmetrized
n10 certificate or the fresh successful n11 mixtures.

Issue #10 remains OPEN: diagnose interruption and obtain one completed pinned
build plus both axiom audits before promotion. Resource profiling or splitting
closed computations may help, but has not been implemented or validated here.
Do not change theorem meaning to make a check pass. Only after that gate, use
Issue #11's three-orbit [1,4,2]/7 n11 finite witness for a new formal interface.
Independent human semantic review remains open in #8. Novelty is unknown; no
all-n MOD3 bound, barrier escape or P-vs-NP conclusion follows.
