# Finite dual obstruction: exact scope and assumption audit

Date: 2026-10-09. Issue #8.
Status: **generic lemma compiled and axiom-audited; MOD3 application pending**.

`finite_dual_obstruction` proves a finite weighted-sum statement over REAL
probabilities, not just rational ones. Given a real payoff matrix A(i,x),
normalized nonnegative row probabilities mu and input probabilities q,
if every deterministic row has q-average at most b<t, no mixture mu
can have pointwise payoff at least t for every x.

The proof expands and exchanges two finite sums. It assumes no existence
of an optimal strategy, no minimax equality and no asymptotic theorem.
It uses no `sorry`, `admit`, project-specific `axiom`, `native_decide` or
external oracle. Its audited foundational axioms are explicitly listed below.
The deterministic-row bound is an explicit certificate premise, not an
assumption that randomized polynomials are already impossible.

## Statement-fidelity attack

- Row coverage: `forall i` is over the supplied finite type I. If I is a
  sample, the theorem ONLY excludes that sample. It cannot repair the
  sampled-dual failure in graveyard/002 by itself.
- Error semantics: the negated goal quantifies over EVERY input x;
  it is not a deterministic average-case approximation statement.
- Probability domain: mu and q are real-valued, so no illicit exclusion
  of irrational distributions is made.
- Normalization and nonnegativity: both are explicit and used by the proof.
- Degree and field: absent on purpose. This theorem neither defines
  GF(2) polynomials nor proves their degree or coverage.
- Formal application still missing: encode the complete affine class,
  prove that its matrix entries are the actual MOD3 correctness bits,
  discharge the deterministic bound, and separately formalize the upper
  witness and symmetrization. Issue #8 must remain open.

## Observed verification

[CI run 37940286899](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37940286899)
on commit `97c459e04204b35f970f58b8cbab959986daa98e` passed.
The actual job logs show the module build, an 11-declaration namespace
audit, and the target's `#print axioms` output:
`[propext, Classical.choice, Quot.sound]`.

The remote source was re-fetched with blob SHA
`c3f299b0c4a086042fd4228c93545a1993b2a589`. The statement and proof were
reviewed for coverage and probability quantifiers. This semantic self-audit
is not an independent human review; no alternative kernel checker was run.

## Relation to the n=8 result

This is a reusable bridge for the lower-certificate logic. The n=8
finite arithmetic is checked in Python with different evaluators and
full permutations; it is NOT thereby a Lean-verified MOD3 result.

This elementary weak-duality argument is standard. No novelty claim.
