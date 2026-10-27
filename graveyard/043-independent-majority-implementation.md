# 043: independent-majority implementation failures

Author: 月野テンプレクス. Freshly approved session executed2026-10-28 JST.
This file records implementation failures, not a refutation of the mathematics.

## First candidate f3a5599d

Source f3a5599dbf8f21864f25294025e50bd7c4124091; completed FAILURE
run40531874680/job122286578853. The full decoded actual job log was retrieved.
Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac were resolved. The floating lean-action
v1 resolved to fe408643ea7367d8c0404a8be3975bb145f5fb64 in this execution,
different from the preceding session; its output still uses --wfail and the
unchanged foundational axiom allowlist.

The single proof error is in failures_cons. Unrestricted simp transformed
sum(if predicate then1 else0) into a filtered-set cardinality before the
Fin.sum_univ_succ rewrite could split it. The unused-simp warning accompanied
the unresolved cardinality goal. The repair uses only the intended sum and
Fin.cons rewrites. No theorem condition, conclusion, or warning policy changes.
The failed build did not reach its axiom audit or endpoint reports.

Actual diagnostic excerpt:
2026-10-27T15:35:38.9100407Z error: PvsNPCartography/IndependentTrials.lean:104:47: unsolved goals
2026-10-27T15:35:38.9102426Z ⊢ {x | e (Fin.cons i v x) = true}.card = (if e i = true then 1 else 0) + {x | e (v x) = true}.card

Later repairs require their own completed evidence. A successful elaboration
of downstream declarations using compiler recovery is not proof acceptance.
