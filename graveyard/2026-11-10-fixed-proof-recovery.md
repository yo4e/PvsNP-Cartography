# Fixed-proof domain recovery: environment failure, then two proof-script failures

2026-11-10 JST. Research lead: 月野テンプレクス. These are execution/proof-script failures, not counterexamples to the final mathematical statement.

## Inherited failure was not proof feedback

At source8feb021eadc32cb448424947eb43a97b5848c1fa, run42571547351 attempt2/job129010841391 stopped while downloading pinned Lean4.35.0-rc4 with HTTP504. Build and axiom stages were skipped. Neither a failed download nor success of earlier modules validates the new endpoint. The exact log was retrieved; one new retry was requested under the fresh session approval.

## Retry exposed actual type/representation defects

Retry job129535545790 reached the compiler. The two Boolean encodings FoldedBlockCount.bits and Symmetrization.bits have the same intended function, but the inverse proof did not explicitly bridge their unfolded representations. The reindexed finite sum also left the additive result type ambiguous. The target was the actual head/tail-to-full-cube equivalence, not just cardinality equality.

Attempt00b831c3791c84fe06abd08579d91dd7403d4685 used explicit Boolean-definition simplification and an explicitly typed real summand for e.sum_comp. Run42728284436/job129539460542 still failed the left-inverse simplification. It was not accepted on the strength of repaired neighboring goals.

Repair443fc96147b8bd616f82250eeb14c1484510e694 proves that left inverse directly: extensional membership, followed by simplification of ones/join/bits. The right inverse keeps explicit encoding alignment; the sum retains its real type annotation. Completed run42728862159/job129541435980 then succeeded, with strict --wfail and unchanged axioms. Source and actual output were re-fetched.

## Lesson and disposition

Equal intended encodings are not a license to skip the inverse laws. Preserve the original-domain connection and repair the proof rather than weaken the endpoint to cardinality or add a goal-equivalent hypothesis. All original statements, positive-denominator/nonempty-test guards, actual polynomial construction and global-proof soundness remain. No sorry/new axiom/warning waiver was introduced.

The earlier semantic guard failures remain in 2026-11-09-fixed-proof-adapter-guards.md. New mathematical capacity countermodels are in 2026-11-10-capacity-optimality.md. Kernel acceptance of the repaired adapter does not validate the separate capacity arguments, independent semantics, runtime analysis or external PCP/hierarchy proofs.
