# Failed implementation: finite pointwise covering candidate

Research lead 月野テンプレクス, approved 2026-11-02 JST session. This is a proof-description failure, not a counterexample to the counting statement.

Initial source 5680b04be181b12363917176f4e9afef5fb11aba, tree 4c71561f4010b9a052fb17e3082f0949d7c4edf2. Completed FAILURE run41394833518/job125113810613. Completed states and the full actual decoded output were retrieved. All explicit endpoint reports and axiom-audit were skipped; no partial acceptance is inferred.

Five diagnosed faults: (1) simp did not convert the error-filter cardinality into a real-valued indicator sum; (2) finrank_span_finset_le_card was incorrectly placed in the Submodule namespace; (3) a subtype membership proof did not unfold distance; (4) simplification changed 1/3 to inverse notation and failed to apply the original predicate proof, producing an unused-argument warning; (5) card_sdiff was incorrectly applied as a subset-argument function instead of using its intersection form.

Repair candidate: explicit sum_filter, correct theorem namespace, explicit distance unfolding, direct filter membership, and the exact difference/intersection cardinality identity. Statements, probability assumptions, original degree predicate and strict --wfail/axiom policy remain unchanged. Do not disable the warning or assume the desired cardinality bound.

The project cache restored successfully. This run was not blocked by credentials, transfer limits or a missing toolchain. The recurring Node.js checkout-action warning is separate from the Lean compilation faults. Acceptance requires a later completed successful whole-root run and actual source/commit/output inspection.
