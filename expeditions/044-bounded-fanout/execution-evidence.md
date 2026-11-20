# Verified implementation and actual GitHub replay

The implementation commit is
[`cb7d76f9df7f8fa94cc3194c46afbf9af5de7873`](https://github.com/yo4e/PvsNP-Cartography/commit/cb7d76f9df7f8fa94cc3194c46afbf9af5de7873),
tree `7dad957ce0b6bd87b6802c0dfaee9fc064e5be84`, parent
`062f8bb57ce1860026538dc92ca08919bf69d30a`. The actual GitHub commit metadata,
its exact 21-path diff and every committed file were re-fetched. All file
contents matched the submitted local manifest byte-for-byte.

[Run 44766593485](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44766593485)
and [job 136392727923](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44766593485/job/136392727923)
completed with **success**. The job started at 2026-11-20 15:46:15 UTC and
completed at 15:47:17 UTC, respectively November 21 00:46:15 and 00:47:17 JST.
The actual checkout revision matches the implementation commit. Python was
3.13.5 on Ubuntu 24.04. The actual job logs were retrieved after completion.

The workflow ran every script normally and with `-O`, compared both outputs
to their committed expected JSON, then printed the hashes and complete JSON.
All six comparisons succeeded. The complete printed results and all three
hashes were independently matched to the local expected contents after
removing the GitHub timestamp prefixes from the retrieved log.

| Result | SHA-256 |
|---|---|
| fanout-checks.json | `7feeac192c71f8500b42efbdd0bcf938b7f492516a0ea45ee5027065f6f551b2` |
| query-map-checks.json | `49a90a46f2aca22585fa4c1491ae301f55ec3058efbc769a5a91bcbf179794d3` |
| weighted-copy-checks.json | `f24100f5b023f42883c1348e988d029d33464b70ed1fe238371fa9217e23949c` |

The local lead also reran the actual fanout script with scalar address checks
under Python 3.12.14, and reran the query-map and weighted controls with `-O`;
their complete outputs matched. The compiler author independently ran normal
and optimized modes before integration. These are Python replay and written
proof checks, not a Lean or external human semantic certificate.

The full old true-address allocation is not saved as a standalone certificate.
Its deterministic completion stream can be regenerated; its recorded digest is
`becc1e2eeaf805be83f5e92cab6fbdbc92b7ec0315a22ea4bafed255bf39e81c`.
The executed output confirms maximum load 288 and mass 10,706,688.

[Actual replay output](execution-output.txt) · [File and commit read-back manifest](readback-manifest.txt)

Later documentation adds the integer-error/mixture limitation proved in
[zero-error-regime.md](zero-error-regime.md), plus the completed evidence and
Issue frontier. Those are written deductions and records; this successful run
is attached to the stated implementation SHA, not retrospectively to a later
documentation commit. No source script or expected result changed afterwards.
