# Recovered actual execution evidence

Approved 2026-10-24 night session; acceptance recording recovered on 2026-10-25
morning JST after the conversation failed to deliver its final response.
These are retrieved execution facts, not source-generated proof reports.
Full decoded successful job logs were read. Committed transcripts below and in
axiom-report.txt are explicitly EXCERPTS, not complete raw-log archives.

## Formal execution

- Source: 8e5be8ce59b069c278ec32839552dad712de04e1
- Tree: 474f4a9a18940dcba367416d3136ece1990af624
- Run: https://github.com/yo4e/PvsNP-Cartography/actions/runs/40108908554
- Job: 120916298894, formal, completed SUCCESS; every required step completed.
- Workflow: .github/workflows/lean.yml; push run70, created2026-10-24T15:51:54Z.
- Command: whole-root lake build --wfail, namespace axiom-audit, scripts/axiom_report.sh.
- Lean4.35.0-rc4, commit c29b6dda4f7c20e3eeaa717c4e565663c5cfa364.
- Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8; Lake5.0.0-src+c29b6dd.
- Ubuntu24.04.5; runner2.338.0; image ubuntu-24.04 version20261012.334.1.
- Resolved checkout11d5960a326750d5838078e36cf38b85af677262;
  lean-action24581d74d674803a25a81b10b059c5c0cdd344c6;
  cachecaa296126883cff596d87d8935842f9db880ef25;
  axiom-auditv0.1.2 at46024e005996495c65ef609368e11ab39c4222e3.

Actual output: --wfail9057 jobs successful,812 namespace declarations inside
[propext,Classical.choice,Quot.sound],21 new explicit target reports and all
previous reports successful. See the timestamped axiom-report.txt excerpt.
No second proof kernel was enabled. The disabled nanoda configuration is not
an execution or trust claim. The action-level Node20 deprecation notice does
not change the successful Lean --wfail result.

Re-fetched source blobs at the accepted commit:
- formal/PvsNPCartography/AgreementDimension.lean:
  fcc41c89ac91813966c5a13cca41c0fbcb233add
- formal/PvsNPCartography/AgreementConsequences.lean:
  3e4a71205ebff281d79a4fb8744eee3a5f3a1c0b

Both full modules were read, including the actual theorem premises and bodies.
The final recovery documentation commit does not itself assert a new formal
execution. Accepted source identity stays pinned to the commit above.

## Exact execution

Source a62add7e08387a4231f7092f108b59964a00feca,
tree0392c8ab902f4b53fbbe464d2ab2dc06a02a07c8.
Run https://github.com/yo4e/PvsNP-Cartography/actions/runs/40107805754
Job120913025271, exact, completed SUCCESS; all required steps completed.
Workflow .github/workflows/agreement-dimension.yml, push run1.
Python3.12.3, Ubuntu24.04.5, runner2.338.0/image20261012.334.1.
Commands were python verify.py, python -O verify.py, cmp, parsed JSON comparison
against result.json, and cat actual.json. These commands and their output were
inspected in the retrieved full decoded log during recovery.

Exact actual output excerpts:

```text
2026-10-24T15:37:21.9608949Z a62add7e08387a4231f7092f108b59964a00feca
2026-10-24T15:37:21.9620086Z Python 3.12.3
2026-10-24T15:37:22.8859881Z PASS: normal/-O byte equality and actual/saved JSON equality
2026-10-24T15:37:22.8899320Z   "agreement_configurations": 140,
2026-10-24T15:37:22.8899772Z   "agreement_polynomials": 11910,
2026-10-24T15:37:22.8907415Z   "collapsed_grid_cases": 100,
2026-10-24T15:37:22.8907774Z   "independent_rank_controls": 971,
2026-10-24T15:37:22.8908151Z   "lagrange_indicator_checks": 3230,
2026-10-24T15:37:22.8914881Z   "power_interpolation_checks": 684,
2026-10-24T15:37:22.8915165Z   "reduction_evaluations": 22230,
```

Full actual JSON, including all fields and negative controls, was compared with
the retrieved result.json. verify.py blobc4fedf9e0485e40249577e0cddbbc9ce34d0b480;
result.json blob2e6e5129db982b927906a9d5942e4a77796e098c. The source directory
at a62add7e reports these same blobs as the full contents read at recovered
HEAD c9a9294899e079d85b1f9715c3dd2df804379ec3. No additional local Lean run or
independent reviewer is claimed. Finite fields/ranks are corroboration only.

## Failure provenance and recovery limit

Graveyard039 records inspected failures at e91ecfd1/run40106942238,
2dcb53fc/run40107571288 and6bbb93af/run40108267893. Recovery read that retained
record; it did not re-download all three full failure logs. Their sources and
records remain preserved, without promoting partial or warning-failing builds.
The successful production log and exact-control log above WERE retrieved fully
in recovery. A green run alone was not substituted for reading the statements.
