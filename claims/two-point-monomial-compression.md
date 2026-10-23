---
id: two-point-monomial-compression
status: formally-verified
statement: For nonzero a,b in any field, actual R of total degree at most d and n+d<=2t+1, each squarefree monomial has a fixed degree-at-most-t polynomial agreeing on the actual agreement set of R with the full coordinate product on the two-point grid.
dependencies: [Mathlib total-degree and evaluation lemmas, finite complement product identity]
novelty: novelty-unknown
last_attacked: 2026-10-23
---

Endpoint: PvsNPCartography.TwoPointCompression.compress_monomial.
Accepted source de8913e7c1058844354f376ae8a72a2a2abddfa9, completed SUCCESS
run39964232854/job120449783214. Source/commit/output re-fetched; unchanged
three-axiom allowlist, --wfail and nine target reports. See Expedition024.

This reconstructs a core step of a known method from Goldreich's author exposition;
no claim of mathematical novelty is made. The witness is chosen before each input.
Its evaluation is restricted to the actual agreement set, not all field points.
Distinctness is unnecessary here; nonzero coordinates are essential.

The full agreement-cardinality bound and the n299 probabilistic-degree consequence
are NOT included in this formal status. They remain author-written reconstructions
with explicit missing formal links and absent independent semantic review.
Counterexamples and checker failures are retained in graveyard036..038.
