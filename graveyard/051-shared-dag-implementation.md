# Shared-DAG implementation failures, not mathematical refutations

Author: 月野テンプレクス. Freshly approved session executed2026-10-31 JST.
Preserve failures before repair. No failed candidate is accepted as a theorem.

## First candidate

Source3c4d5ce1192ac44db831731a962f0d7cd748a6c4, tree7d1f490c42121f75ee7820d9f8ddfd989747a26a.
Run41155490365/job124401254735 completed FAILURE. The completed steps and full
decoded actual job log were retrieved. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac;
whole-root --wfail unchanged. The build failed in SharedDAG and later explicit
axiom reports were skipped. CircuitMod3 was not accepted by that run.

Errors: partial applications of eval_args/args_degree left slot capacity K
unconstrained; dependent empty Fin eliminations needed explicit arguments;
Fin.cons did not infer the motive in a standalone equality; unfolding gate
predicates left decidability instances that failed implicit-transparency
rewrites; the success-complement sum needed an explicit row count r.

Repair: specify existing K/r parameters, use pointwise Fin.cases for table
equalities and explicit empty indices, and transport standalone proved gate
and union indicator inequalities by simplification. Do not alter circuit
semantics, actual polynomial degree, real probability weights, quantifier order,
error budget, warning policy or allowed axioms. The named mathematical
counterexamples are separately preserved in graveyard050. Later execution
outcomes belong in the expedition's actual evidence record.
