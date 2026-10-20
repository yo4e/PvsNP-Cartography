# Rejected generic obstruction integrations and faithful repair

## Candidate290fd53

Code290fd53ca91e9d28b6d15aac4ea9e770c9c4ae22; completed FAILURE in
run39508917678/job118924741871, exit1 at2026-10-20T22:36:22.7060940Z.
The full completed log was fetched. No namespace or target axiom audit passed.
The counting prefix elaborated but --wfail rejected an unused one_mul argument.
Obstruction failed on conditional mass reduction, addition order and Fin literal
matching. Those were repaired without changing mathematical statements.

## Candidate6d91476

Code6d91476aab2c11cb3c7d70223ac08ca5adca5aef; completed FAILURE in
run39509854045/job118927885156, exit1 at2026-10-20T22:43:54.8838326Z.
Full log fetched. The log reported successful builds of BalancedAffineBinomial
and BalancedAffineCounting before the integration failed. Actual error excerpts:

```
2026-10-20T22:43:51.3360047Z warning: PvsNPCartography/BalancedAffineObstruction.lean:60:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
2026-10-20T22:43:54.7385991Z error: PvsNPCartography/BalancedAffineInputMeasure.lean:75:6: Type mismatch: After simplification, term
```

Obstruction proofs elaborated but deprecated if_pos and unnecessary sequence
focus warnings caused rejection under --wfail. The new actual ordered success
count had a positive Distinct hypothesis not eliminating ifs through broad simp.
Final repair dc58ea7d uses the compiler-recommended ite_eq_left explicitly and
ordinary sequential tactics. No linter or warning policy was disabled.

## Final outcome and failure boundary

Final source dc58ea7dd4d3e2ed36ca5b7d8276de651d95aa08 subsequently passed actual
run39510465687/job118929907745, --wfail9048 jobs,589 namespace declarations and29
new targets under the unchanged foundational allowlist. Full completed log and
actual source/commit were re-fetched. See Expedition020/axiom-report.txt.
This success does not erase the failures or retroactively validate them.

Neither failed run is a mathematical counterexample or formal acceptance.
The earlier dependent cf15c55 candidate also completed FAILURE in39508392914;
only its failed metadata was inspected. It carried the preceding broken prefix.
Do not count source presence or error-recovery placeholders as proof.

Every repair preserved targets, actual GF(2) evaluation, polynomial degree,
REAL probabilities, family-before-input quantifiers, the common strict bound
and normalization. Independent finite CI success is a separate evidence class.
