# Conclusion: n10 degree equality is formally verified

Approved night session2026-10-18 JST; completed after midnight on2026-10-19 JST.
Investigator: 月野テンプレクス. The n10 GF(2), pointwise error1/3 MOD3
probabilistic degree is now formally verified to equal2. Complete formal
numerical coverage is n5..10. #10 is closed as completed; #11 is next.

## Evidence, not source-shaped confidence

Production code1739ccfa2ebe5997e568135cdfacf06e9f6d1f87, tree
693fff576290749ebbd023d861041e53ca0a9812. Actual source blob
cf6c6ec257f0a5c20e9b12f3c265864db57e58ca and SHA256
5d6aa5a2df006cee95a9d43b0707505298f431d38f0c984440fb5b0d1553b571 were re-fetched
and matched to the successful tested candidate and committed proof-only diff.

Completed SUCCESS formal run39139432083/job117710608870: Lean4.35.0-rc4,
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8, --wfail root build9042 jobs,
420 namespace declarations within the unchanged foundational allowlist and
all15 explicitly printed n10 targets using only propext, Classical.choice,
Quot.sound. The full completed log was inspected. No unchecked project axiom,
sorryAx, native_decide or CBV tactic was accepted. Actual output is preserved
in formal/reports/2026-10-18-n10-axioms.txt.

Separate SUCCESS semantic run39139432110/job117710608842 at the same code
reproduces1024 canonical-input evaluations,2048 affine rows,11 layer sums and
448 coefficient-mutation checks. Normal/-O output equals the saved result,
including the production-source hash. Source statements and commit/tree were
re-fetched after completed validation, not inferred from an upload.

## Repair and attacks

The prior two cancelled builds are not erased or reinterpreted. Their shutdown
cause remains unknown. The first diagnostic found the kernel lower prefix
already succeeds; blind default decide_cbv substitution instead fails its step
budget and propagates sorryAx. Those failed outputs are in graveyard017 and
first-diagnostic.md. A green diagnostic recorder was not treated as a proof.

The successful repair changes only layer_tickets_exact to:

```lean
  intro w
  fin_cases w <;> decide +kernel
```

All eleven closed weight cases are still covered. Statements, coefficients,
quantifiers, probabilities, thresholds, heartbeat limits and axioms are unchanged.
The targeted diagnostic passed layer-only133.100s and full candidate152.043s
with all15 allowed reports. Other proposed CBV strategies were not executed,
because this first split-kernel strategy succeeded. It then passed production.

## Exact formal/informal correspondence

Upper: genuine degree<=2 GF(2) MvPolynomials, original eight normalized REAL
seed weights, ALL coordinate permutations, and every input. Lower: strict
152/240=19/30<2/3 dual, proved coefficient-permutation coverage and structural
normal form for ALL actual degree<=1 polynomial objects and finite REAL mixtures.
The complete degree classification and least-degree equality are derived from
both, not assumed. Independent finite minimum2123/3000>2/3 is unchanged.
The raw unsymmetrized seed mixture's1/50 counterexample is also Lean-checked.

## Continuing frontier and limits

This session also removes redundant labels from n11's SAME finite measure:
Expedition017 gives496 distinct rows/denominator1155 instead of1925 indexed
entries/27720, without reducing any input's success. That n11 result is still
finite evidence, not a compiled n11 theorem. #11 is the next unblocked formal
interface task. #8 remains independent human semantic review; no second proof
kernel, mathematical novelty, global support minimum, all-n result, barrier
escape or P-vs-NP conclusion is claimed. No write blocker or unapplied patch
remains. Future sessions require their own approval.
