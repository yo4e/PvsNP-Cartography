# Expedition 045 — sparse affine reads with a retained NO gap

Approved November 21, 2026 JST session. Research lead: 月野テンプレクス.
Parent: `fa1dabd4f3a760832e78ca398d1ebedf68853ebe`.
Target: [Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34).

The preceding private-copy compiler has Q=4,194,304, exact NO minimum 109
and signed sensitivity 128. Its strict sufficient error threshold is below
1/Q: it still requires an exact polynomial to exist. The named mathematical
target is to change the A membership predicate, retaining one global
physical proof and fixed signed projection queries, so that actual
V_NO/(Q sigma) improves and V_NO>sigma.

The first trial uses the seven coordinate directions. Passing centers define
affine polynomials on eight-point stars. Finite connectivity certificates
give a 28-rejection guarantee, but a three-star splice disproves the tempting
claim that its exact NO minimum remains109. A 29-point Hamming-ball trial
improves the guaranteed bound to98, but another physical splice gives108
rejections. These failures are preserved, rather than deleted after a repair.

The selected repair uses D=U union V for complementary binary subspaces of
sizes8 and16. It reads 23 A symbols per center. Since D+D is the whole
address group, any two passing stars share two distinct physical points.
This forces a common affine polynomial exactly where the residual needs it.
The shared B recovery then retains the exact NO minimum 109.

Tasks were divided into bounded theoretical exploration, counterexample
construction, and actual Boolean compilation. All agents share model
lineage and repository context; cross-agent agreement is not an independent
proof kernel or external mathematical review. The lead re-read their
arguments and code, integrated the counterexamples, and replayed the final
artifacts. Precise verification status belongs in execution-evidence.md.

A natural completion is the costed GF(128) construction and its all-assignment
soundness argument. A growing family and the approximation degree of its new
Boolean encoding remain separate questions; a later session needs fresh
approval.
