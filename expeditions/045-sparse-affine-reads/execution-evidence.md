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

| Script | Stored output | SHA256 |
|---|---|---|
| check_compiler.py | compiler-checks.json | ebf02aa785ea0b1755350ae55997297286536b436aa6654d4fb2ae35e8856e3a |
| attack_sparse.py | attack-results.json | b26e7b12b9b33ee8d688afe450e593f86a10ceae4ab7fcd32cccbc441d700408 |
| check_difference_cover.py | difference-cover-checks.json | c7ca245157a2b2995d7e22bedc2602fd6f7ded18237f869b27442520b15365f3 |
| check_connectivity.py | connectivity-checks.json | d65cac0dcfdc18ee74a8a02452d3405747e8a8ad92fc76066c8349e8802883ef |
| check_degree.py | degree-checks.json | 852ae8afaf6764d4da250017adec8552d530686efb40f0f8f9e4cbea07e4ac91 |

The compiler compares 165 actual field assignments at128 seeds for each
of two instances and three schedules (126,720 scalar/Boolean verdicts),
then verifies private-copy correspondence and full clause replays for the
named noncodes. Gate charging, not this finite collection, supplies the
universal mixed-error upper bound.

The degree audit checks the complete2^22-bit transform inversion, scalar
subset conventions and direct ANF evaluations. Its target is the named
honest YES proof with all unused padding zero. The resulting degree18 is
not a minimum over padding or satisfying proofs.

## Remote execution status at this initial checkpoint

A pinned finite replay workflow is included, using ubuntu-24.04, Python3.13.5
and the same checkout/setup-python action revisions as Expedition044.
It will compare normal and -O output for all five scripts.

A completed remote run and new-commit readback have **not yet** been
recorded in this initial evidence file. The subsequent record update must
name the actual code commit, completed run/job, retrieved output and exact
file-hash comparison. A prepared workflow is not remote verification.

## Trust boundary

The reviewers share model lineage and exchanged findings. Their role
separation is useful criticism, not blind external mathematical review.
The source papers supply background and the inherited geometry, not
certification of this changed verifier. No publication novelty claim is made.
