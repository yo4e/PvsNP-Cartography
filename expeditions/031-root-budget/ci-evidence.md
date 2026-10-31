# Actual execution evidence — separately budgeted root

Research lead: 月野テンプレクス. Fresh 2026-10-31 JST NIGHT approval.
This record distinguishes kernel execution, finite controls, written reasoning
and independent review. No new independent semantic reviewer or second kernel
was used. Full decoded job outputs were retrieved; execution-excerpts.txt saves
labeled excerpts, NOT complete raw log archives.

## Accepted mathematical source

Source: 2d790f584090d50c950b4f856f596b444bdaaa32.
Tree: ce9e56d6754d147e796bd5948e9949f05a9b2eeb.
Parent: 74a427db55828ce2c6d4e348fea2019c8bc8090e.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/41206535050
Run41206535050 / job124552630720 completed SUCCESS. The completed step states
and full decoded actual log were fetched AFTER completion. The actual checkout
SHA matches the source above. Whole-root --wfail completed9073 jobs, explicitly
compiling RootBudget and the root. Axiom-audit inspected1292 declarations under
PvsNPCartography, all within unchanged[propext,Classical.choice,Quot.sound].
All previous reports and the new RootBudgetAudit step succeeded. The new audit
printed16 theorem-axiom reports and3 explicit endpoint signatures. root_cost
uses onlypropext; the other15 reports use the three allowed foundations.

Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Lake5.0.0-src+c29b6dd; Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Resolved lean-actionfe408643ea7367d8c0404a8be3975bb145f5fb64;
axiom-audit v0.1.2 at46024e005996495c65ef609368e11ab39c4222e3;
checkout11d5960a326750d5838078e36cf38b85af677262.
Runner2.338.2, Ubuntu24.04.5 image20261025.353.1. Normal project cache restored
frome3b3e3789d53187e4fd14dded5ffda5c98f87080. This is not clean-room acceptance
or a second kernel. The actual workflow retained --wfail and the existing audit.

The complete RootBudget source and matching commit/tree were re-fetched at the
accepted SHA. Its Git blobd058a7d975a2aa6112420c777dcad08c6b6dc797 matches local
9897-byte UTF-8 contents; SHA256 is
38e86647c3fe76407b1d8adf3a3a96a74d83813ff45c88015137c522720942fa.
RootBudgetAudit.lean was re-fetched, blob8e9b6f77baba1101f4822230704a566b9d3e2a0f.
Local lexical checks found no sorry/admit/new axiom/native_decide in the new
module. They supplement, not replace, the actual build and dependency audit.
No earlier theorem or predicate was weakened. The optional output-NOT extension
was not added. The accepted scope is the concrete product-sampled single-root
construction in proof-and-scope.md, not the continuation's counting proposal.

## Initial failed candidate

Source74a427db55828ce2c6d4e348fea2019c8bc8090e,
treec5a16009cc5589c883fbfbe4ff31f5123e2b17fb;
run41205835465 / job124550622120 completed FAILURE. All subsequent explicit
reports were skipped. The full completed log was fetched. This was a proof-
implementation failure, not an infrastructure failure. Graveyard054 records the
higher-order marginal rewrite, addition-side/inference problems and strict
sequence-focus warning. The accepted repair changed proof descriptions only;
no hypotheses, target semantics, probability weights, degree notion or audit
conditions were relaxed. This failure remains preserved after success.

## Separately completed exact controls

Source7db154a90653e37e612362c919139462eb0789c8,
treea932c722d1a1f968d637fc7853777c1cb9831209.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/41206658022
Run41206658022 / job124552998091 completed SUCCESS. Full actual output and all
completed steps were fetched. Actual Python3.12.3 ran py_compile, normal and -O
execution, compared their bytes, then compared the committed checks.json.
All checks remain active under -O via explicit RuntimeError checks.

Actual checker, JSON, workflow and matching commit/tree were re-fetched.
Local hashes match:
- verify.py:8899bytes; Git blobe34a9a5d9a864ad373b8dc5a6dff6939baf96066;
  SHA256d1064b4c24ed283769d3e5b0d1a67f75747719fe564e7e4f99e38b7468cbb91b.
- checks.json:978bytes; Git blob7b6980a2372539954350f1755d8e63498fcbd995;
  SHA256d02b3cbfe4f5e91ff715ee57db227a1882072a0c0082c84c36e8a76fc3520d41.
- workflow Git blob0a24155506942f85bd905935077af29391eb319b.
The actual CI printed the two SHA256 values above. Local Python3.13.5 outputs
also matched; the initial local optimized wrapper exceeded its tool deadline,
but its complete output was subsequently compared and py_compile succeeded.
No successful exit is inferred for that timed-out wrapper. Both CI executions
completed normally and supplied the independent execution environment.

Finite coverage:1562 zero/one-inner-node structures at n,K0..2, r1/2,t0/1/2;
9372 parameter cases,566832 polynomial samples,1972860 pointwise evaluations,
31920 error bounds and4872 qualifying one-third checks. Six deeper structures
add24 cases,84504 samples,338004 evaluations,84 bounds and17 qualifying checks.
A separate finite prefix-coupling control adds12 cases and5202 samples; it is
NOT a generic coupling theorem. Two evaluators by the SAME author compare
unreduced sparse polynomials/newest-first storage with chronological Boolean
execution. This is not independent semantic review and not the universal proof.

## Written and local continuation: separate evidence class

Sourceb3cba95d7e7706a5509b360bac68f95106fdaebc,
tree7a67850c8de8fa643a2173577b407e57b8eb46b6, saves the statement/barrier audits,
next-frontier, check_covering.py, covering.json and graveyard055. The source,
results, next-frontier and matching commit/tree were re-fetched. Local hashes:
check_covering.py1944bytes, blobfc0f3dbe8875d7236311698feafac5dc0718a6eb;
covering.json3699bytes, bloba75cbbb0fa53ca684a2bd004a76dc22995f6f084.
Local normal/-O/py_compile checks agree for11 small(n,d) pairs. These enumerate
Hamming-cover histograms, NOT pointwise probabilistic-degree feasibility.
The AND/constant-mixture impossibility is a written real-weight argument, not a
linear-program solver result. The generic covering bound is not Lean accepted.
None of this continuation is covered by the completed root-control CI above.

## Persistence and promotion boundary

Issue23 completion comment6544229821 was saved and the issue closed/completed.
Issue24 records the next finite covering/recognition question. No write/security
blocker or unapplied patch remains. The final record-only commit archives the
previous complete status/ledger via identical existing Git blobs; its own hash
is deliberately not self-embedded. Re-fetch that commit and actual final files
before reporting persistence. Any extra CI triggered by formal/ASSUMPTIONS.md
is not a replacement for the accepted mathematical-source run recorded above.
Novelty, optimal constants, independent semantic approval, general n12
classification, unrestricted lower bounds and proof-barrier escape are unclaimed.
