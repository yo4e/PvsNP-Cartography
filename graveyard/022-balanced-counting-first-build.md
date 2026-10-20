# Failed first generic-counting build

Code a34c3775a5efd6b99979f5884c103ec009ddfeea, formal run39507291359,
job118919300321. Completed FAILURE, exit1 at2026-10-20T22:22:34Z. Full actual
log was retrieved. Namespace/explicit target audits were skipped.

Errors were implementation errors, not mathematical counterexamples:
- Distinct was opaque to Decidable synthesis in theorem statements.
- Expanding products of sums reordered bound indices instead of proving the
  intended factorization; explicit factoring is needed.
- Compressed nested `by` syntax misplaced the final linarith tactics.
- A Fin2 indicator cast was not distributed through its if-expression.
- Generalizing coefficient applications before simplifying pair projections
  left the original applications in goals, so the bit case split was irrelevant.

The compiler introduced error-recovery placeholders in failed declarations.
Those are NOT accepted proofs, and the failed run was never promoted. Repair
must restore the same statements, actual target semantics and normalization;
retain --wfail and the foundational axiom allowlist. The repair uses a reducible
predicate, explicit DecidableEq for the generic finite type, factored sums,
multiline arithmetic subproofs and separately proved two/four-bit sign lemmas.

Every Fin n application has decidable equality. The generic moment lemma's
DecidableEq instance is an implementation parameter, not a new mathematical
hardness hypothesis. A future successful run does not erase this failure.
