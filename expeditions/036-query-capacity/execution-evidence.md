# Exact capacity and signed-gap controls — execution evidence

2026-11-10 JST. Research lead: 月野テンプレクス. Written finite proofs and finite calculations are separate. No independent semantic review or Lean validation of the new capacity/signed-gap arguments occurred.

## Source and successful remote run

Final mathematical/control checkpointb742079296f15da7790a2e9eb711b89031fea57e, treefb71bdd7eea96de3bf39eacec5409275e8f70de6. Initial capacity work was committed atf8e0db47ea6ef1a602bb4671f35c4801c74af302. The complete code and both stored JSON outputs were re-fetched from the immutable final ref; Git blobs match locally executed bytes. Actual commit/tree and completed execution were re-fetched.

Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/42730390055
Job https://github.com/yo4e/PvsNP-Cartography/actions/runs/42730390055/job/129546608938

All steps completed SUCCESS, including both inherited035 checkers and both new036 checkers. Normal and python -O complete stdout are byte-identical and match the stored JSON; py_compile succeeds. The full decoded log was retrieved and its checkout hash equals the source above. New scripts also passed local CPython3.13.5 normal/-O/compile checks. Checks use explicit exceptions, not disabled assertions.

Actual remote CPython3.13.5; runner2.338.2, Ubuntu24.04.5 image20261101.360.1; checkout11d5960a326750d5838078e36cf38b85af677262; setup-pythona26af69be951a213d495a4c3e4e4022e16d87065. Node-action warnings remained visible. Another runner is replication, not an independent mathematical reviewer.

## Exact fingerprints

| File | Git blob | SHA256 |
|---|---|---|
| verify_capacity.py | 6d76388ceb09cd8e0e0601e9249af088f17e2015 | 885fc7a094629688166a022383e819c4ce0ea3835285cfa35a1b06c3a3341041 |
| checks.json | a6bfa308cab90f598c62737594f5d5b614be6aec | 8a5564e6040877437dee1ce1ece8f1e70ae120281fd13ae2d358080227de79bd |
| verify_signed_gap.py | 724ed3bf13ed044cad8db27ea4b635fb7ba5c32c | 4aa75bc471e55283a557c667be3177a90a38286571faee2a0d05d1404bf3b64a |
| signed-gap.json | 68404a07f05071dcadb0206938d789abe79226b2 | 7d260a7e3f4cccba28647a9f28dc982f28876dcdca66af5533b3f22a8db2a081 |

Selected actual log excerpts (NOT a full raw-log archive):

```text
2026-11-10T00:43:09.8492858Z b742079296f15da7790a2e9eb711b89031fea57e
2026-11-10T00:43:24.2457217Z expeditions/036-query-capacity/verify_capacity.py: OK
2026-11-10T00:43:24.2474711Z /tmp/query-capacity.json: OK
2026-11-10T00:43:24.8210631Z expeditions/036-query-capacity/verify_signed_gap.py: OK
2026-11-10T00:43:24.8228372Z /tmp/signed-gap.json: OK
```

## Coverage and limits

Capacity suite:11736 exhaustive graphs (address sizes1..4, up to3 tests when size<=3 and up to2 when size4, integer weights0..2 with positive sum);300 seeded graphs on sizes4..6; one named fractional/deterministic countermodel. Total12037 graph cases,24074 graph-suite flow runs,114536 positive-error-set comparisons. This count excludes separate flow calls used in signed tests. Integer residual flow/cut certificates are compared to two separately enumerated cut formulas and exhaustive tiny deterministic selectors. A strictly suboptimal capacity is also rejected.

Signed suite:2151 satisfied signed-test families,16036 error-set comparisons and2151 normalized global-mixture checks, including repeated addresses, tautologies, zero masses, sampled weighted families and the named non-tautological certificate-optimality counterexample. Six malformed graph inputs are rejected. These small rational tests do not prove the arbitrary-real capacity or averaging result.

Sharp-gap suite:3146 exhaustive one/two-test families on address sizes1..3 with weights0..2,200 seeded four-test families on sizes4/5, plus the named seven-clause factor-four example and the excluded tautology. It directly evaluates signed literals, all error sets and random-half-subset expectations. It does not import the flow implementation. Both scripts are authored by the same researcher; this is not independent review. Seed20261110 for both.

The original capacity script was kept unchanged when the stronger factor-four idea was split into its own checker; the final local original bytes were restored and re-run against the committed hash. No exploratory local candidate is presented as the committed output. Local working directory: /mnt/data/pvsnp-2026-11-10/.

## Evidence boundary

capacity-and-transfer.md contains the real-weight max-flow/weighted-Hall derivation, one-global-sample bound, factor3 rounding and signed-optimality counterexample. sharp-signed-gap.md contains a separate general half-thinning argument and exact sharp example. Neither document is certified by the unrelated successful Lean adapter build. No novelty, source-specific PCP congestion bound, efficient succinct selector, hierarchy theorem or P-versus-NP consequence is claimed.
