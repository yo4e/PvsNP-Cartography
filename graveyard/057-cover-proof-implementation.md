# Failed implementations: finite pointwise covering candidates

Research lead 月野テンプレクス, approved 2026-11-02 JST session. These are proof-description failures, not counterexamples to the counting statement.

## Initial candidate

Source5680b04be181b12363917176f4e9afef5fb11aba, tree4c71561f4010b9a052fb17e3082f0949d7c4edf2. Completed FAILURE run41394833518/job125113810613. Completed states and full actual decoded output were retrieved. All explicit endpoint reports and axiom-audit were skipped; no partial acceptance is inferred.

Five faults: (1) simp did not convert the error-filter cardinality into a real-valued indicator sum; (2) finrank_span_finset_le_card was incorrectly placed in the Submodule namespace; (3) subtype membership did not unfold distance; (4) simplification changed 1/3 to inverse notation and failed to apply the original predicate proof, with an unused-argument warning; (5) card_sdiff was incorrectly applied as a subset-argument function instead of using its intersection form.

Repairab288e7628423a1b9eccadde97b9cf2e1865e575 used explicit sum_filter, the correct theorem namespace, explicit distance unfolding, direct filter membership and the exact difference/intersection cardinality identity. No statements or checks were weakened.

## Concrete-field elaboration timeout

Repairab288e7 completed FAILURE run41395566277/job125116026347. Full decoded completed log and states retrieved. The only primary error was the concrete GF2 span-rank application exhausting 2400000 heartbeats at whnf after87s; missing codebook_card was a downstream consequence. The earlier five faults no longer appeared. Do not count this failed module as accepted.

Next repair extracts the same span-rank argument as a lemma over an abstract Field K, matching the already accepted AgreementDimension proof, then specializes it to ZMod2. The heartbeat cap, mathematical premises, original degree predicate, --wfail and axiom allowlist remain unchanged. This is a performance-oriented proof refactoring, not an assumed rank bound.

Both runs restored the project cache successfully; neither was a credentials or transfer failure. The checkout-action Node.js warning is separate. Acceptance requires a later completed successful whole-root run and actual source/commit/output inspection.
