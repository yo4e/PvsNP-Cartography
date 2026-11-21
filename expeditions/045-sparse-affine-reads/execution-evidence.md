# Execution evidence — Expedition 045

## Source and scope

Starting main commit: `fa1dabd4f3a760832e78ca398d1ebedf68853ebe`.
The research snapshot's 836 pre-existing files were matched to live GitHub
blob hashes before edits. Only README.md and docs/CURRENT_STATUS.md change
among those files; the experiment, claims, failures, log and replay workflow
are added separately. Predecessor mathematical code is unchanged.

The executable results are finite implementation/certificate checks.
All-assignment NO soundness, the all-error gate charge and the degree-distance
implication have separate written arguments. No new Lean or independent
proof kernel ran.

## Completed local execution

Python 3.12.14 on Linux x86_64. The bounded workers ran normal and
`python -O` versions and compared complete stdout byte for byte with the
stored JSON. The lead inspected the mathematical arguments and source,
reran all five scripts, and additionally reran the degree audit under -O.
All lead runs completed with exit0 and exact stored-output equality.
[Actual lead replay output](execution-output.txt) records the observed
runtime and digests.

The subsequent padding clarification adds a sixth script. The lead replayed
both normal and -O modes, each matching the complete stored JSON exactly;
[padding execution output](padding-execution-output.txt) records those runs.
The hostile reviewer also used a separate NumPy transform and direct parity
grouping to confirm the completed truth/ANF hashes and all sixteen odd
subcube parities. NumPy is not a dependency of the retained checker or CI.

| Script | Stored output | SHA256 |
|---|---|---|
| check_compiler.py | compiler-checks.json | ebf02aa785ea0b1755350ae55997297286536b436aa6654d4fb2ae35e8856e3a |
| attack_sparse.py | attack-results.json | b26e7b12b9b33ee8d688afe450e593f86a10ceae4ab7fcd32cccbc441d700408 |
| check_difference_cover.py | difference-cover-checks.json | c7ca245157a2b2995d7e22bedc2602fd6f7ded18237f869b27442520b15365f3 |
| check_connectivity.py | connectivity-checks.json | d65cac0dcfdc18ee74a8a02452d3405747e8a8ad92fc76066c8349e8802883ef |
| check_degree.py | degree-checks.json | 852ae8afaf6764d4da250017adec8552d530686efb40f0f8f9e4cbea07e4ac91 |
| check_padding.py | padding-checks.json | d58e287c466914f3913ba2e3b531ce9ca49abe41eb9fc8d49dd27a68ff73c5ef |

The compiler compares 165 actual field assignments at128 seeds for each
of two instances and three schedules (126,720 scalar/Boolean verdicts),
then verifies private-copy correspondence and full clause replays for the
named noncodes. Gate charging, not this finite collection, supplies the
universal mixed-error upper bound.

The degree audit checks the complete2^22-bit transform inversion, scalar
subset conventions and direct ANF evaluations. Its target is the named
honest YES proof with all unused padding zero. The resulting degree18 is
not a minimum over padding or satisfying proofs. The separate padding audit
constructs an exact degree 17 completion preserving all 2,796,160 used bits,
checks every physical clause, and proves a matching lower bound even under
the four-error budget. Its sixteen disjoint odd-parity subcubes lie wholly
in used addresses. No optimization over other satisfying proofs is made.

## Completed initial remote execution

The initial code commit was
`9483c577c8b85d1fb12bd155e660e2af953d837a`, tree
`0b5b5e4a4e7454f839cb0112446677201a14649b`, parent fa1dabd4.
All 32 changed files were re-fetched at that immutable commit and matched
their local text and Git blob hashes. All 834 untouched base files retain
their original hashes. [Readback manifest](initial-readback-manifest.json).

[Run 44911525428](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44911525428),
job 136868186420, completed successfully under Python 3.13.5 on ubuntu-24.04.
Its actual retrieved log identifies the source commit and contains all five
normal/-O comparisons, SHA256 digests and complete stored JSON outputs.
[Complete replay-step output](initial-remote-execution-output.txt).

## Completed integrated remote execution

The padding completion and sixth normal/-O check were committed as
`47910b0aa120794143477268fc02056a72c73b08`, tree
`bd68ff1c665359f153adfd6b103a821605b481cd`, parent 9483c577.
Every one of the 39 files added or changed from the starting snapshot was
re-fetched at this immutable commit and matched its exact local text and
Git blob hash. The 834 untouched original files still match. The full
remote tree contains 873 blobs and was not truncated.
[Source readback manifest](source-readback-manifest.txt).

[Run 44912211021](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44912211021),
job 136870212842, completed successfully at 2026-11-21 14:09:56 UTC
(23:09:56 JST). It used Python 3.13.5 on ubuntu-24.04. All six scripts ran
in both normal and -O modes; every complete output matched the committed
JSON byte for byte. The retrieved log explicitly identifies this source
commit and Python version. Its six printed SHA256 digests match the table
above. [Run metadata](remote-run-metadata.txt).

[The complete replay-step output](remote-execution-output.txt) is 121,991
bytes, SHA256
`65cb64e00c2caf98f624e84affb87b41cb933947a76dbb5620c3f1f588a3bf59`.
It retains the command, comparisons, all six complete JSON outputs and
timestamps. The earlier replay output is 103,075 bytes, SHA256
`2056b23ff212accebb06c9127535b5eac88ead2ddbc6fb35cf5604ce6cbaab84`.

The completion was recorded on [Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34#issuecomment-7063886237),
which is closed as completed. [Issue 35](https://github.com/yo4e/PvsNP-Cartography/issues/35)
records the remaining fully costed family and encoded-degree question.
Issues 8 and 15 retain their separate scopes. This final evidence update
changes documentation and archived execution output, not the tested code.

## Trust boundary

The reviewers share model lineage and exchanged findings. Their role
separation is useful criticism, not blind external mathematical review.
The source papers supply background and the inherited geometry, not
certification of this changed verifier. No publication novelty claim is made.
