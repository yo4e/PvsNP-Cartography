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

## Second candidate d2cede2c

Source d2cede2c30fe06ce721ff78683ed6dae4f819d65; completed FAILURE
run40533297666/job122291663655. Full decoded log retrieved and inspected.
IndependentTrials built, but this is not whole-chain acceptance. Other failures:
- the dependent Fin.cons expression needed its Boolean codomain made explicit;
- m+(n-m)=n was not rewritten by a lemma about a differently parenthesized sum;
- GF2 natural-value casts were not definitionally normalized by broad simp;
- broad simplification reversed inequality indicators before local hypotheses
  could rewrite them, and one conversion exhausted its default heartbeat budget;
- norm_num did not reduce the large real exponent2^297 automatically.

Repairs give zero padding an explicitly typed definition, prove the elementary
natural equality directly, use the actual ZMod cast/value lemma and explicit
indicator rewrites, and prove the natural power by kernel reduction before
casting it to the reals. A local heartbeat budget increase supplies computation,
not an extra axiom. The actual target, real probabilities, degree, --wfail and
axiom allowlist are unchanged. Finite numeric identities that already elaborated
are not treated as a substitute for the still-unfinished full proof chain.

Later repairs require their own completed evidence. A successful elaboration
of downstream declarations using compiler recovery is not proof acceptance.

## Third candidate 088bd61c

Source088bd61c9fe01062a90fa5eb30f64ea91c712c4b; completed FAILURE
run40534788715/job122296987803. Full decoded output was retrieved and inspected.
The natural arity equation was true but simp did not transport the dependent
implicit target parameter in restrict_le. The majority complement conversion
also had a definitional-instance mismatch despite identical printed types.
The numerical strict gap had an exponentiation-threshold warning at297 versus
the default256. Whole-root --wfail correctly failed; no axiom audit ran.

Repair: obtain n=m+k before applying restrict_add, use a local definitional
transparency conversion in the actual majority complement, and permit the
real computation with exponentiation.threshold512. These are elaboration and
resource changes, not assumptions, goal changes or warning-policy disabling.

## Fourth candidate eb8e503c: a warning-only failure

Sourceeb8e503cd4141142a4b258dcf7956ad4af3af44f; completed FAILURE
run40536001033/job122301279401. Full decoded output was retrieved and inspected.
All five mathematical modules, including the final n>=299 theorem, elaborated.
However, one conversion had redundant <;> sequencing and an unreachable rfl.
The strict build failed before the axiom audit and explicit reports. This
partial success was NOT accepted as the completed formal milestone.

Actual diagnostic excerpts:
2026-10-27T16:00:07.7626006Z warning: PvsNPCartography/MajorityAmplification.lean:120:68: this tactic is never executed
2026-10-27T16:00:07.7628195Z warning: PvsNPCartography/MajorityAmplification.lean:119:74: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
2026-10-27T16:00:07.7630422Z warning: PvsNPCartography/MajorityAmplification.lean:120:68: Unused tactic linter: `rfl` does nothing
2026-10-27T16:00:11.7626254Z ✔ [9063/9065] Built PvsNPCartography.Mod3QuadraticObstruction (3.9s)
2026-10-27T16:00:15.7672656Z error: build failed

Repair79c52432 removes only the redundant tactics. All warning checks stay on;
the mathematical statement, field, degree, real probability contract and
foundational axiom policy stay unchanged. Its OWN completed output determines
acceptance: run40536961983/job122304691322 completed SUCCESS, with full --wfail
build, unchanged axiom audit and27 new explicit reports. See Expedition027's
ci-evidence.md for the independently inspected execution record and its limits.
Here independently inspected means inspected separately from the repair claim,
not an independent semantic reviewer or a second proof kernel.

All four failed sources remain in Git history. None is relabeled successful.
