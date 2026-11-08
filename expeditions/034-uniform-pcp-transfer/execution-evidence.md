# Execution evidence — exact controls and a cost repair

2026-11-08 JST. Research lead: 月野テンプレクス. This file records observed executions, not an independent review or a new Lean theorem.

## Immutable source and completed remote execution

Code commit9afb67d1d1061558cea1a7a7d085236a59504087, tree581ff84daa3092b0396e93f48857746f4a183f47. Completed SUCCESS run42437159862, job128598359545, workflow `.github/workflows/pcp-transfer.yml`.

Run: https://github.com/yo4e/PvsNP-Cartography/actions/runs/42437159862
Job: https://github.com/yo4e/PvsNP-Cartography/actions/runs/42437159862/job/128598359545

Re-fetched the actual commit/tree, repaired source, new verifier and stored checks. Their Git blobs agree with locally executed bytes. Re-fetched completed run/job states and the full decoded job log. The checkout hash and printed execution hash match the code commit above. All inherited/new normal and -O executions, comparisons and py_compile completed successfully.

Actual CPython3.13.5; runner2.338.2, Ubuntu24.04.5 image20261101.360.1. Resolved checkout11d5960a326750d5838078e36cf38b85af677262; setup-python@v5 resolveda26af69be951a213d495a4c3e4e4022e16d87065. Hosted Python archive release3.13.5-15601068749 was downloaded. No container digest, independent interpreter implementation or clean-room theorem verification is claimed. Node-action deprecation warnings were present but no check was bypassed.

Selected actual message excerpts (NOT a full raw-log archive):

```text
2026-11-08T02:07:36.8657892Z Python 3.13.5
2026-11-08T02:07:36.8673498Z 9afb67d1d1061558cea1a7a7d085236a59504087
2026-11-08T02:07:50.1975521Z inherited.json aab3cce3bcad18ba0ff7ec734ea4b5dd11e66618ff7478bea1ca4fc215134931
2026-11-08T02:07:50.1976849Z runtime.json 4bbc707da4e17d5ecccaa90f69ae4988ce012500c84bcb6c26bfda78f8021527
2026-11-08T02:07:50.1977869Z transfer.json 2ed85502d15381dc187906831e3da68c85c85c99d053b8e9bf3604f665a7a987
2026-11-08T02:07:50.1978669Z PASS: historical numeric outcomes unchanged; normal/-O/stored hashes agree
```

The log includes all three complete JSON outputs. `checks.json` is the full new transfer stdout. `replication-manifest.json` pins all three output hashes. The old033/runtime-audit.json remains the historical November5 output; its numerical fields match the repaired run exactly, while its self_sha256 correctly remains the old source fingerprint. No historical output was edited to masquerade as a new run.

## Exact source fingerprints

| File | Bytes | Git blob | SHA256 |
|---|---:|---|---|
| 033/verify.py | 8516 | 86fd6619fb243bb898689934c42aa7782df554bc | 63658eb2227820cfec364a879c6c295986ab484d973a097f732c8860b34441a3 |
| 033/runtime_audit.py, repaired | 9914 | debab1bef0bf8e56af2cd66d704cc6cba6599469 | c9a537fd2ab3f1b714a00c65800f81046f03fc39b3ae99844496be8cd4fe0a89 |
| 034/verify_transfer.py | 11952 | 1bb7e990ff5695f515860182a001730eacbc08f7 | 7fdbd7bf3fcbfc683b6bfdca43911b62964558db28179c1ca26639286f46f904 |
| 034/checks.json | 2643 | b9395496b41f191f22232aecca5370b489b13e3b | 2ed85502d15381dc187906831e3da68c85c85c99d053b8e9bf3604f665a7a987 |

## Finite coverage, not universal mathematics

Inherited verification reproduces75295 exact head counts and1548 signed integer checks. The repaired runtime suite reproduces22719 exact counts,26616 signed modular tables and604 finite parameter budgets. Both old suites' complete normal/-O stdout agrees byte-for-byte, with the runtime source digest updated as recorded above.

The new verifier exhausts all ANFs and all constant/literal coordinate substitutions at source/query arities(0,0),(1,1),(2,2),(3,2):55890 substitutions and223522 pointwise comparisons. It then uses seed20261108 at source arities0..3/query arities0..4, five sources per arity pair and all eight sign triples:800 signed clause cases,2400 clause/block cases,9120 exact head counts. Those larger clause cases are seeded tests, not exhaustive over all clauses/polynomials.

It also checks1120 one-true-literal inequalities across20 valid three-row mixtures,20 nonuniform-test averaging cases,1366 explicit small-CNF prefix-search cases,378 exact majority-tail inequalities, six hash-collision validation sizes and five malformed-input rejections. The hierarchy-overhead constants in the toy budget are explicitly synthetic. These tests do not build a general PCP, solve SAT efficiently, or establish an asymptotic hierarchy theorem.

## Local execution and limitations

Local Python3.13.5 normal/-O/py_compile runs agree with the completed remote outputs. Workspace: `/mnt/data/pvsnp-2026-11-08/`. A local postprocessing path error initially looked for a comparison file relative to the wrong parent; changing to the absolute current working directory fixed it. This occurred after numerical tests and did not alter their outputs or expected data.

Local Git DNS failed and Lean/Lake were absent. Connected GitHub writes and the targeted Python workflow worked. No write-permission/security denial or unapplied code patch remains. No Lean file or axiom policy changed; earlier kernel evidence remains at51a86b10 and is not transferred to the new written PCP/hierarchy argument. Same-author alternate paths plus another runner are replication, not independent semantics or a second proof kernel.
