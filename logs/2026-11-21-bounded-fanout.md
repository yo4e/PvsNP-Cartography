# November 21 JST: bounded fanout and uniform proof-bit precision

Fresh one-session approval; baseline main `062f8bb57ce1860026538dc92ca08919bf69d30a`.
Issue 33 was the earliest unblocked target. Issues 8 and 15 retain their separate
review requests. The nightly approval schedule is unchanged.

## Research result

The actual GF(128) fixture now has a cap-126 private-copy compiler with exact
unrestricted YES sensitivity 128, versus exact 288 for the named original
honest reference. Both YES and NO fit the old Q=4,194,304 cube, and NO retains
its minimum 109 raw failed pairs. The sufficient error threshold improves by
exactly 9/4, to 109/536,870,912. The old upper value is checked by regenerating
a true-literal assignment of every one of its 10,706,688 clause–seed pairs;
only its digest and reproduction code are stored. [Full result and scopes](../expeditions/044-bounded-fanout/conclusion.md)

The general private compiler has sigma<=max(mu,f+2), equals mu when mu>=f+2,
preserves the original field minimum, and uses at most four times the old cube.
Symmetric weighted shared copies cannot improve their optimized unshifted
baseline; an asymmetric counterexample prevents overgeneralizing that claim.
The dead designs and omitted-copy mutants are preserved in two graveyard notes.

The final attack found a substantive limitation: both finite error thresholds
are below 1/Q. Deterministic approximants must be exact, and a qualifying
mixture must contain an exact polynomial with positive probability. Thus the
existential approximation class is not enlarged for the respective encoded
function. The retained full-A test forces sigma>=N and V_NO<=N in the stated
private encoding. [Proof and frontier](../expeditions/044-bounded-fanout/zero-error-regime.md)

## Reproduction

From `expeditions/044-bounded-fanout`:

```bash
python check_fanout.py --scalar
python -O check_fanout.py --scalar
python check_query_maps.py
python -O check_query_maps.py
python check_weighted_copy.py
python -O check_weighted_copy.py
```

Expected outputs are `fanout-checks.json`, `query-map-checks.json` and
`weighted-copy-checks.json`. The workflow reruns normal and optimized modes,
compares each byte-for-byte, and prints the actual revision, Python version,
result hashes and complete JSON. Local execution is separate from remote CI.

## Persistence and remote verification

Implementation commit
[`cb7d76f9df7f8fa94cc3194c46afbf9af5de7873`](https://github.com/yo4e/PvsNP-Cartography/commit/cb7d76f9df7f8fa94cc3194c46afbf9af5de7873),
tree `7dad957ce0b6bd87b6802c0dfaee9fc064e5be84`, passed completed
[run 44766593485](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44766593485),
job 136392727923, Python 3.13.5. All three scripts matched their stored full
outputs in normal and optimized modes. The lead retrieved the actual commit,
its complete changed-file list, all 21 files, completed job status and actual
job logs. Every submitted file and all three complete result objects/hashes
matched. Local replay used Python 3.12.14.

[Full evidence](../expeditions/044-bounded-fanout/execution-evidence.md) includes
the actual replay output and file read-back manifest. The later documentation
commit records this evidence and the zero-error limitation, without changing
the tested scripts or outputs. No full allocation file is claimed saved.

[Issue 33](https://github.com/yo4e/PvsNP-Cartography/issues/33#issuecomment-7043941266)
is closed/completed for the scoped ratio improvement and obstructions.
[Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34) is open for the
remaining physical-reader/zero-error frontier. Issues 8 and 15 stay open in
their older review scopes. No write/security blocker or unapplied patch remains.

## Remaining frontier

The full A test reads every symbol at every seed and imposes mu=N. Lowering
that physical load requires changing the predicate and re-establishing its NO
minimum; exact membership alone is insufficient. The next useful target is
V_NO>sigma, preferably growing in a costed family, or a justified smaller
degree-restricted error sensitivity. The new encoded proof needs
its own approximation guarantee. The full recursive gate census, secondary
unpaired GF(256) optimum, novelty and new Lean acceptance remain unresolved.

This approval ended with the session. It does not authorize another night.
