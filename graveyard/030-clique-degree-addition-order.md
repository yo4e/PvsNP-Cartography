# Rejected implementation: additive bound had the wrong syntactic order

Candidate d65bfec70538c4b53e6ff2ab741c61da131345d3.
Formal run39614264308/job119270959352 completed FAILURE. Full log inspected.
HammingProfiles built, but no whole-root acceptance or axiom audit completed.

Actual log excerpts:
2026-10-21T14:12:01.9689817Z Built PvsNPCartography.HammingProfiles
2026-10-21T14:12:05.9750049Z error: PvsNPCartography/CliqueProfiles.lean:32:27: Type mismatch: After simplification, term
2026-10-21T14:12:05.9750625Z   Nat.add_le_add_left ih 1
2026-10-21T14:12:05.9751299Z   1 + MvPolynomial.totalDegree (subsetMonomial S) <= 1 + S.card
2026-10-21T14:12:05.9751862Z   1 + MvPolynomial.totalDegree (subsetMonomial S) <= S.card + 1

The proof used simp only without commutativity, so Lean correctly rejected the
mismatched type. Repair: rewrite totalDegree_X explicitly, then let omega use
the same induction hypothesis. No theorem, degree convention, domain, error,
probability, --wfail setting or axiom allowlist was weakened.
This is a proof-implementation failure, not a counterexample to the degree bound.
A subsequent completed build and both audits are required before promotion.
