# Actual execution and persistence evidence

Approved session executed2026-10-27 JST. Source and evidence classes are separate.

## Accepted source

Commit5acf085fa43f1fa4578252c1653033d3f523e753;
tree12c1e9ab938e823a15566c7921fdc6550217d1e6;
parent270cf3773274c5e1455874c57f80166bbd1c6e07.
The actual Git commit was re-fetched after successful verification. All three
Lean modules and the exact checker/result were re-fetched at this SAME commit.
Locally computed Git blob hashes match the returned blobs:

- GF4Transport.lean: e39be642b9a022e3d8bda92855d1dd071ddeae94,9417bytes.
- Mod3ProductBound.lean: a0a6e469e159a8160ffc435adb34bda0799213a4,4316bytes.
- TransportExamples.lean: 45f527e60f055ca6ecb2d451c84834f20fce8ff0,1711bytes.
- verify.py: d2efbaddc4e95c61851c25b464c83cdadac0d467,8638bytes.
- result.json: af566500bb643a1cb764c0816bb5e97ef9b19c66. Repository JSON
  formatting differs from the local pretty print; parsed objects agree.

## Formal execution

https://github.com/yo4e/PvsNP-Cartography/actions/runs/40430504329
Job121946718143, completed SUCCESS; all required job steps completed successfully.
Full decoded output and completed step states were retrieved and inspected.
Resolved Lean4.35.0-rc4, commitc29b6dda4f7c20e3eeaa717c4e565663c5cfa364;
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
Whole-root --wfail9060 jobs. axiom-audit v0.1.2,
commit46024e005996495c65ef609368e11ab39c4222e3, inspected875 namespace declarations;
all stay within [propext,Classical.choice,Quot.sound]. All23 new explicit target
reports and previous reports completed. axiom-report.txt preserves exact actual
output excerpts, not a complete raw-log archive or source-generated transcript.
The normal Actions dependency/build cache was used, including artifacts from
the successful repair270cf377; this is not a claimed clean-cache or second-kernel
execution. No sorry/admit/new axiom/native_decide or warning-policy relaxation.

## Exact finite execution

https://github.com/yo4e/PvsNP-Cartography/actions/runs/40430504271
Job121946717619, completed SUCCESS at the same5acf085f. Full decoded output and
completed steps retrieved. Actual excerpts:

2026-10-27T01:05:49.8916200Z 5acf085fa43f1fa4578252c1653033d3f523e753
2026-10-27T01:05:49.8926957Z Python 3.12.3
2026-10-27T01:05:50.7528042Z PASS: normal/-O byte equality and actual/saved JSON equality

The complete printed JSON was compared with the re-fetched result.json.
Local normal/-O reruns also match each other and the stored parsed result.
3680 polynomials,18304 input evaluations,126 nonuniform mixture controls and
144 field checks pass. Polynomial substitution, Boolean source evaluation and
quotient/table arithmetic are separate implementations BY THE SAME AUTHOR.
They do not establish an independent semantic review or a generic theorem.

## Failure and environment boundaries

First formal source73d562a7, run40429493278/job121943428570, completed FAILURE;
full actual diagnostics were inspected and retained in graveyard042. Repair270cf377
passed completed run40430105650/job121945416414; its job/steps were inspected,
but its full log was not separately retrieved. Final5acf085f above supplies the
fully inspected acceptance evidence, including the extra concrete application.
Local git clone failed DNS; local Lean/lake were absent. Connected writes and
Actions worked. No permission blocker or unapplied patch remains. Subsequent
documentation commits do not constitute a new mathematical execution.
