# Actual execution evidence and correspondence

Approved 2026-10-23 JST session. These records distinguish formal source
acceptance, repaired finite checks and author-written mathematical reasoning.

## Formal acceptance

- Source de8913e7c1058844354f376ae8a72a2a2abddfa9; tree5b9639c71fbcab3706fcb4780e390e3520b5bca4.
- Completed SUCCESS run39964232854, job120449783214.
- Workflow .github/workflows/lean.yml, unchanged blob d07695edcdaf77656204c204963049808a61c22a.
- Actual root `lake build --wfail`:9055 jobs. Namespace axiom audit:759 declarations.
- Nine new explicit reports, plus all earlier reports, within [propext,Classical.choice,Quot.sound].
- TwoPointCompression.lean re-fetched blob e22c7cffd1e893575301d13863e1703aeeafcd43; matches local5607-byte source.
- No sorry/admit/new axioms/native_decide or warning-policy relaxation introduced.
- Full decoded job output and completed steps inspected; actual excerpts archived in axiom-report.txt. The full raw job log is NOT claimed to be archived here.

Resolved environment from the actual log:
Lean4.35.0-rc4, commit c29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8;
Ubuntu24.04.5, image ubuntu-24.04 version20261012.334.1, runner2.338.0.
actions/checkout@v4 resolved11d5960a326750d5838078e36cf38b85af677262;
leanprover/lean-action@v1 resolved24581d74d674803a25a81b10b059c5c0cdd344c6;
actions/cache resolvedcaa296126883cff596d87d8935842f9db880ef25;
axiom-audit v0.1.2 resolved46024e005996495c65ef609368e11ab39c4222e3.
The complete lake-manifest was printed and inspected. No container digest or
second independent proof kernel is claimed.

## Repaired finite execution accepted separately

Source531f3a86b602a7a1b272138e55e051279598f28f;
treec6ddeb8c251b11c8b34ad1e6c0b66dd756ee5890.
Completed SUCCESS run39965200654/job120453135024 under modular-dimension.yml.
Full decoded job output and all steps inspected. Actual output excerpts:

```
2026-10-23T13:55:13.8692048Z 531f3a86b602a7a1b272138e55e051279598f28f
2026-10-23T13:55:13.8705309Z Python 3.12.3
2026-10-23T13:55:18.7746013Z PASS: normal/-O byte equality and actual/saved JSON equality
2026-10-23T13:55:18.7794067Z   "compression_input_checks": 53942,
2026-10-23T13:55:18.7841781Z   "independent_matrix_checks": 256,
2026-10-23T13:55:18.7855994Z   "rank_checks": 18020,
2026-10-23T13:55:18.7856282Z   "root_encoding_cases": 8191
```

The complete printed JSON was compared with re-fetched result.json, including
all11 exhaustive configurations,32768 majority inputs, exact positive gap and
explicit nonclaims. The script/result/Git commit were re-fetched after execution:
verify.py blob3e06d549bc9c7d7295838a565e04665b09eaea0d matches local10006-byte source;
result.json blob5720b2781e52a2a9f4f23e9408b0db409c09137b matches parsed local output.
Local Python reran both normal and -O successfully after repair. Both CI and local
checks retain critical assertions under -O using explicit RuntimeError checks.
Formal source is unchanged by this finite-check/docs commit; its acceptance
continues to refer to de8913e7, not an invented new formal run at531f3a86.

## Why the earlier green exact run is quarantined

Initial run39964233049/job120449783272 atde8913e7 completed SUCCESS and was read
in full. Source audit nevertheless found a stale-iterator rank bug. Its structured
test pass does not validate rank evidence. Graveyard038 gives both concrete2x2
counterexamples; only the repaired run above is accepted for ranks. The finite
checker is not a dependency of the Lean proof. Formal implementation failures
and their actual inspected runs are preserved in graveyard037.

## Reproduction and limits

From formal/: `lake build --wfail`; `./scripts/axiom_report.sh`; run the unchanged
production namespace audit. From this expedition: `python verify.py`,
`python -O verify.py`, compare byte output and parsed result.json.
The final record-only documentation commit is not a new mathematical execution.
All counts are verification metadata, not a distance-to-P-vs-NP measure.
No independent semantic reviewer, second kernel, novelty or complete Lean n299
result is implied by either accepted run.
