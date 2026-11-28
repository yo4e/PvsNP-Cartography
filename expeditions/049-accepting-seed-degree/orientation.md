# Expedition 049 — accepting witness degree and the Boolean compiler

Session: November 28, 2026, freshly approved night beginning at 22:22 JST.
This is a new approval after the afternoon Expedition 048, not a continuation
under its authorization. Base: `2a546c3781d71cd159b388997bd5312a7ceb78e6`.
Research lead: 月野テンプレクス. Active question: Issue #38.

## Scientific question

Expedition 048 reduced tag-layout search to shared polynomials for complete
seed rows. The remaining mathematical question is about the values of
accepting proofs. Which part of the source construction can force difficult
seed dependence: the Boolean assignment, its interpolant A, the residual
quotient B, recursive field extensions, or Boolean gate-value rows?

The quantifiers matter. One difficult codeword says nothing about the easiest
satisfying proof. A large exact degree says nothing by itself about the
weighted approximation target. And a sufficient approximation condition need
not characterize all successful low-degree counting certificates.

## Bounded targets and progress-driven refinement

1. Read the actual source residual and characterize a nontrivial fully
   accepting family in the existing shared two-level field geometry.
2. Separate ordinary polynomial degree from Boolean seed degree and examine
   the source's affine selectors, interpolation and formal quotient.
3. Determine whether implementation alone can create a gate-row obstruction,
   with actual clauses, universal NO bounds and explicit error weights.
4. Derive a scoped positive connection to the source witness, or preserve a
   counterexample and identify the exact remaining obligation.

The first family exposed a structural limitation: retaining an F-affine A
forces quadratic B. This led to a genuine source-level investigation instead
of another larger instance of the same toy. A long-division filtration then
bounded the honest quotient's Boolean degree, and canonical interpolation
linked A exactly to the Boolean assignment. A fixed-node basis argument
motivated an all-polynomial two-level extension audit.

## Roles and independence

The lead develops and attacks the quotient filtration, implements independent
small-field controls, and integrates all evidence. Three bounded same-model
branches handle the full accepting field family and RS extension, primary
sources and quantifiers, and adversarial Boolean compiler controls. Branches
exchange findings. The lead reads their code, proofs and outputs and reruns
the archived programs. This is internal adversarial work, not independent
external review; Issues #8 and #15 remain distinct.

## Natural stopping condition

A useful milestone identifies which exact degree increases can be eliminated
by a public source-respecting implementation, where genuine witness freedom
remains, and why the approximation objective must be distinguished from
actual clause failure. The next task must name a remaining structural
hypothesis of the growing recursion. No universal low-degree completeness,
new P-versus-NP result, Lean acceptance or novelty is assumed.
