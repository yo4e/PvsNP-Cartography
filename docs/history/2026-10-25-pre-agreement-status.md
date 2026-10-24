# Current checkpoint: certified two-point compression and an unpromoted MOD3 consequence

Approved 2026-10-23 JST night session. Research lead: 月野テンプレクス.
**Issue #17 is CLOSED at its bounded core-lemma milestone. Issue #18 is OPEN.**
Read live Issues and RESEARCH_DIRECTION.md; earlier dated snapshots, including
the preceding README checkpoint, do not restart completed tasks. This record
confers no approval for another nightly session.

## Accepted formal core

TwoPointCompression proves an actual-polynomial compression lemma over ANY field.
For nonzero a,b, R.totalDegree<=d and n+d<=2t+1, every squarefree monomial is
represented on H={y in {a,b}^n: R(y)=product y} by one polynomial of degree<=t,
chosen before y. The high-support branch uses R times affine inverses of the
complement coordinates. The result assumes neither compression nor a desired
agreement count. Distinctness is unnecessary for the core, but is essential
for the subsequent two-point interpolation and dimension argument.

Accepted source de8913e7c1058844354f376ae8a72a2a2abddfa9, completed SUCCESS
run39964232854/job120449783214: pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
root --wfail9055 jobs,759 namespace declarations inside unchanged
[propext,Classical.choice,Quot.sound], nine new explicit reports and all old reports.
Full actual output, completed state, matching source and commit/tree were
re-fetched. Source blob e22c7cffd1e893575301d13863e1703aeeafcd43 matches local bytes.
See Expedition024/ci-evidence.md, axiom-report.txt and statement-audit.md.
The separate majority15 binomial identity is also accepted, NOT the entire
probabilistic amplification theorem.

## Written reconstruction and consequence candidate, not full Lean acceptance

Expedition024/proof.md reconstructs the actual agreement-dimension inequality
|H|<=sum_{j<=floor((n+d)/2)}choose(n,j), with a!=b, using interpolation,
compression and degree-preserving multilinear reduction. This full dimension
step is not yet Lean encoded. It is not inferred from finite ranks.

A degree-aware MOD3 adapter uses majority15=e8, degree8d, error
422009/4782969, followed by two restrictions and a linear GF4 root encoding.
The resulting exact necessary binomial inequality is contradicted at n299,d2.
Exclusion for n>=299 is an **AUTHOR-RECONSTRUCTED CONSEQUENCE CANDIDATE**;
end-to-end Lean checking and independent semantic review are absent. Exact
arithmetic alone is not the whole proof. No optimal threshold or novelty claim.

## Accepted finite checks, including a repaired verifier

Repaired source531f3a86b602a7a1b272138e55e051279598f28f passed completed
run39965200654/job120453135024. All256 GF4 2x2 matrices are checked against
determinants, plus18020 exhaustive polynomial-rank cases,53942 compression
evaluations,32768 majority truth values and8191 root encodings. Normal/-O and
actual/stored JSON agree. Re-fetched script/result/commit match local source
hashes and exact output. Separate implementations are not a separate reviewer.

The initial checker passed CI but had a real stale-pivot iterator defect;
old run39964233049 is quarantined as rank evidence. Graveyard038 preserves
both false-positive and false-negative controls and the repair. Graveyard036
records the zero-grid counterexample (7>4), wrong inverses, quantifiers,
rounding and dependence shortcuts. Graveyard037 preserves inspected formal
failures and an immediately repaired typo without fabricating its job outcome.

## Next earliest unblocked frontier: #18

Derive the actual agreement-set evaluation-space/cardinality bound in Lean from
the accepted compression, explicit interpolation and multilinear reduction.
Do not assume its decisive surjectivity or rank bound as a premise. Then connect
only the amplification/field-transport pieces needed by this concrete question.
The n299 candidate supplies a named mathematical use, not an excuse for an
unbounded framework or automatic n13 enumeration. Review of its whole semantic
chain would add evidence that the current core build does not supply.

## Preserved scope and environment

Earlier accepted results remain unchanged: exact degree2 n5..11, affine
exclusion n>=7, and the restricted n12 zero/q9/r8 obstruction. Unrestricted n12
degree is unresolved. No new circuit bound, barrier escape or P-vs-NP conclusion.
Gemini #15 covers only old0e30b5b7; #8 human review remains separate/nonblocking.
New-code independent semantic review and a second kernel are not claimed.

Local Lean is absent and local git network access failed DNS; connected GitHub
writes and Actions worked. No authorization blocker or unapplied research patch
remains. Goldreich TR23-034 revision1 parsed proof was read; failed screenshots
mean visual PDF inspection and a local PDF archive are not claimed. Prior status
is archived byte-identically under docs/history/2026-10-23-pre-compression-status.md.
Session record: logs/2026-10-23-night-modular-dimension.md.
