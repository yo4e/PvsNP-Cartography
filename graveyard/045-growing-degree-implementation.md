# 045: growing-degree implementation failures

Author: 月野テンプレクス. Approved session executed2026-10-29 JST.
This is an implementation failure, not a mathematical refutation.

## First candidate36af2ee825c363eeeeff21193b89c9a6f6d9d141

Completed FAILURE run40843560074/job123345505156. The full decoded actual
job output was retrieved and inspected. Lean4.35.0-rc4 and pinned Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8 resolved. The build used --wfail;
its axiom audit and target reports were skipped after failure.

The single failure was a wrong multiplication-order lemma API in central_square:
`(mul_le_mul_right hp).mp hgoal` treats a monotonicity function as an equivalence.
The recurrence, parity identities and other candidate source elaborated without
reported errors, but no whole-chain verification is claimed from that fact.
Repair uses positivity of the cancelled factor and an explicit contradiction,
not a weaker invariant, warning waiver or extra axiom.

Actual diagnostic excerpts (not a full raw archive):
2026-10-29T08:41:46.2789737Z error: PvsNPCartography/CentralBinomialBound.lean:56:41: Invalid field `mp`: The environment does not contain `Function.mp`
2026-10-29T08:41:46.2791146Z error: PvsNPCartography/CentralBinomialBound.lean:56:37: Application type mismatch

The next candidate also connects the actual capped prefix and original-predicate
all-degree endpoint. It needs its own completed strict audit before promotion.

## Second candidate0dbf0e83b668a57b0ed08a7d4269a4f3fcadf62b

Completed FAILURE run40844869515/job123349784652. Full decoded actual log
retrieved and inspected. CentralBinomialBound compiled, but the full audit did
not run. The new definition used `prefix`, a reserved Lean parser keyword.
The cascade of parse errors came before the intended real partial-sum proofs.
The `sorry` printed in recovery goals is a compiler recovery placeholder, not
an accepted proof or a source admission. Rename the definition `partialSum`;
keep every mathematical condition and the strict build policy unchanged.

2026-10-29T08:51:37.2052417Z ✔ [9064/9068] Built PvsNPCartography.CentralBinomialBound (6.7s)
2026-10-29T08:51:41.4109864Z error: PvsNPCartography/BinomialPrefixBound.lean:11:3: unexpected token 'prefix'; expected identifier

## Third candidate ce6e9394180b15d97c61d4d18fd4b30ed52951f6

Completed FAILURE run40845559395/job123352057310. Full decoded actual output
retrieved and inspected. CentralBinomialBound compiled again. Two errors remained
in BinomialPrefixBound: the pinned `add_le_add_left` adds the common term on the
right, and `add_le_add_right` on the left. The proof used the opposite convention.
Repair uses `add_le_add le_rfl h` and `add_le_add h le_rfl` directly, making both
positions explicit. No mathematical statement, axiom policy or warning gate changes.

Actual diagnostic excerpts:
2026-10-29T08:57:43.1397675Z error: PvsNPCartography/BinomialPrefixBound.lean:67:2: Tactic `apply` failed
2026-10-29T08:57:43.1401583Z error: PvsNPCartography/BinomialPrefixBound.lean:92:6: Type mismatch

The earlier independent exact-control job passed, but it is not a replacement
for this failed generic proof build. Full acceptance requires the repaired build,
unchanged namespace audit and all explicit endpoint reports to complete.
