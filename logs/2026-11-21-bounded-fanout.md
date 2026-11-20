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

The implementation commit and completed GitHub execution are pending at the
time of this source commit. They will be recorded after the actual commit,
files and completed job output have been retrieved and compared. No success
or saved full allocation certificate is asserted by this pending entry.

## Remaining frontier

The full A test reads every symbol at every seed and imposes mu=N. Lowering
that physical load requires changing the predicate and re-establishing its NO
minimum; exact membership alone is insufficient. The new encoded proof needs
its own approximation guarantee. The full recursive gate census, secondary
unpaired GF(256) optimum, novelty and new Lean acceptance remain unresolved.
