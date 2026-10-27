# Statement audit: author acting as skeptic

Research lead and author: 月野テンプレクス. Approved session executed2026-10-28 JST.
This is SAME-AUTHOR adversarial checking, not an independent semantic review.
Formal execution status belongs in ci-evidence.md, not in this prose assertion.
Audited and Lean-accepted source:79c52432c82406b0a692a079adab147402dbbbe0.

## Intended and actual final statement

For every natural n>=299 there is NO fixed finite distribution of genuine
GF2 polynomials of total degree<=2 that computes the residue-zero MOD3 target
on each Boolean input with success>=2/3. Distribution weights are arbitrary
nonnegative REAL numbers summing to1. They are not field elements or restricted
to integer tickets. The family and weights are chosen before every input.

Mod3QuadraticObstruction.degree_two_impossible has only n and299<=n as premises.
Its conclusion negates the ORIGINAL HasProbabilisticDegreeAtMost predicate
with @SmallSupportMod3.target n, epsilon1/3 and degree2. The n299 endpoint has
no premises. Neither assumes an amplified-error promise, a desired binomial gap,
a rank bound, a lower-bound theorem or the impossibility conclusion.

## Semantic chain examined

1. IndependentTrials.mass indexes ALL tuples Fin r->I and multiplies the r
   original weights. Tuple splitting proves normalization for every finite I.
   It is not a diagonal family that repeats one sampled index. Source zero
   weights and repeated polynomial rows remain allowed. The zero-length tuple
   has mass1; an empty source cannot meet the original normalization premise.
2. failure_law derives the exact threshold recurrence from these product sums.
   Its algebraic identity allows signed normalized masses, but tail monotonicity
   and failure_bound require nonnegative original mass. The adversarial signed
   example shows why that distinction is necessary, not a hidden loophole.
3. errorFlag depends on an input only as the event being MEASURED, not as a
   choice of distribution. amplified_success uses the same preconstructed tuple
   family and product weights for every x. source_error_complement connects the
   event to the original genuine polynomial evaluator and target.
4. majority15 is an actual sum of products of eight polynomials, not an oracle
   or truth-table label. Degree8*d follows from totalDegree sum/product bounds.
   Its evaluation equals Boolean majority by the earlier choose(w,8) parity
   identity. Both target0 and target1 are checked: failure means AT LEAST8 wrong
   votes, and success plus the failure indicator is1. Non-multilinear source
   polynomials are not excluded by the statement.
5. The real error comparison applies to every p in[0,1/3], not just p=1/3.
   Only the endpoint constant is calculated through the exact natural tickets
   recurrence. It does not replace arbitrary source real weights by rationals.
6. amplify reindexes the finite tuple family through the existing faithful
   feasible_of_fintype bridge into the original Fin-indexed predicate. The
   resulting error is tail(1/3,15,8) and total degree8*d, at the same input arity.
7. MajorityNumerics proves that tail endpoint equals422009/4782969, proves
   fastChoose equals Nat.choose, and kernel-checks the exact prefix and power.
   No saved Python result is imported into Lean. The strict rational inequality
   is discharged rather than supplied as a final theorem hypothesis.
8. The already constructed GF4 transport is applied to the original amplified
   n299 predicate at m297,D16. Its field and root are actual objects, not
   uninstantiated hypotheses. Product success is derived by its real union bound.
9. Mod3Restrictions explicitly substitutes one variable by0 and leaves all
   other variables unchanged. Evaluation, total degree and target preservation
   are proved; the SAME original real distribution supplies the restricted
   pointwise guarantee. Induction gives n>=299 ->299. This is indispensable:
   the direct numerical gap actually fails at n300, so no monotonic extrapolation
   of the finite inequality is used.

## Trust boundary and implementation changes

The source contains no sorry, admit, new axiom, native_decide or imported Python
certificate. Resource limits were enlarged for real computation. A local
backward.isDefEq.respectTransparency setting permits definitional unfolding in
one conversion; it does not add axioms or bypass the Lean kernel. The exponent
threshold allows evaluation of2^297. No linter or --wfail policy was disabled.
Four failed candidates are preserved in graveyard043, including a warning-only
candidate that elaborated the final theorem but did not reach the axiom audit.
Only a completed successful run with the exact source can supply acceptance.

## Limits that remain visible

The generic failure law is proved through its recurrence. A separate generic
closed-binomial-form equality is not a compiled endpoint; finite controls compare
it independently with the recurrence and tuple sums. This does not leave an
amplification gap, since the recurrence already gives the exact law and endpoint.

This is exclusion of degree<=2, not exact degree3, the optimal input threshold,
unrestricted n12 determination or a complexity-class separation. The next
square-root-scale obstruction in next-frontier.md remains a written candidate.
The old Gemini review covers its own earlier checkpoint only. No independent
semantic reviewer, second proof kernel or new mathematical priority is claimed.
