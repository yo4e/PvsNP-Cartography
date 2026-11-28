# November 28 approved night — accepting degree and compiler boundaries

Fresh approval: 2026-11-28, following the 22:21 JST request. Research began
at 22:22 JST. This was separate from the afternoon session that completed
Expedition 048. Starting main was `2a546c3781d71cd159b388997bd5312a7ceb78e6`.

## Scientific result

[Expedition 049](../expeditions/049-accepting-seed-degree/conclusion.md) narrows
Issue #38. Canonical interpolation preserves the genuine satisfying
assignment's Boolean degree r. In the source outer residual, under
`deg A<=S/2` and `3S<|F|`, the uniquely forced B has degree at most
`D0=max(c+3r,1+r)`, and a public Frobenius-based outer circuit has honest gate
degree at most `D0+1`. The chi filtration controls formal division; exact
degree transfer does not imply stable approximation.

The new source-shaped two-site residual has exactly three fully accepting
used field proofs, all with affine raw rows. Its affine A restriction explains
that ease and cannot be substituted for a growing Boolean assignment.
Separately, the actual two-level honest RS extension preserves raw degree
for every degree-less-than-32 root polynomial; fixed low spaces and jointly
affine coordinates are essential to the proof.

The live bent Boolean control has raw NO minimum 32 and sensitivity 3, while
its minimum affine signed-charge distance 54 exceeds that gap. Nevertheless
the actual minimum affine failure count is 8, below half-gap 16. Thus a failed
sufficient approximation budget does not exclude a successful low-degree
counting tuple. The complete live AND-chain error curve and a varying-node
vanisher countercontrol preserve related failures.

## Actual saved implementation and execution

- Commit: [`6835b3af0765a72fa0d90e8db0a4288e88221c3a`](https://github.com/yo4e/PvsNP-Cartography/commit/6835b3af0765a72fa0d90e8db0a4288e88221c3a).
- Tree: `48d4d58658a1914855b1ac98c980776e49adca3c`.
- Every one of its 21 files was re-fetched through the immutable GitHub file
  API, compared with intended content, and matched to actual Git blob bytes
  and SHA values after fetch.
- Four suites passed ordinary and optimized Python locally and again from a
  Git archive of the immutable commit: 16 successful, stored-output-equal
  executions. Exact records are in
  [execution evidence](../expeditions/049-accepting-seed-degree/execution-evidence.md),
  [local execution](../expeditions/049-accepting-seed-degree/local-execution.json)
  and [remote readback](../expeditions/049-accepting-seed-degree/remote-readback.json).
- This subsequent record commit changes documentation and evidence, not the
  four programs or their mathematical result files. Its changed files and
  final branch state are re-fetched before the user-facing completion report.

## Issues and next decision

[Issue #38](https://github.com/yo4e/PvsNP-Cartography/issues/38) is closed with
state reason completed; the
[completion comment](https://github.com/yo4e/PvsNP-Cartography/issues/38#issuecomment-7240201619)
records the scoped result.
[Issue #39](https://github.com/yo4e/PvsNP-Cartography/issues/39) is the next
structural task: control the growing recursive RS rows and their Boolean
predicates, with seed-dependent low bases, coordinates and actual violation
objectives explicit. Park affine-toy enlargement and compiler-independent
auxiliary degree claims. Issues #8/#15 remain separate.

No new Lean or CI execution, external review acceptance, novelty claim,
universal low-degree completeness or P-versus-NP separation. There is no
write blocker or unapplied implementation patch. This record does not
authorize another nightly session.
