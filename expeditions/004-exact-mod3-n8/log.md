# Expedition 004 log

## 2026-10-09: positive witness, simplification, attacks and remote reproduction

Observe: AGENTS.md and the five mandatory documents, open Issues #7/#8,
head 50706ac, the latest night log and expedition 003's log were read.
The earlier sampled-dual refutation is retained. No previous night's
authorization was reused.

Orient: choose n=8 positive-certificate search before attempting an
exhaustive 2^37 negative-certificate calculation. Success is a rational
quadratic-orbit mixture with pointwise success >=2/3.

Act: start with eight symmetric coefficient choices (c in {0,1}, a in
{0,255}, b in {0,2^28-1}) and the earlier refuter (1,255,60548413).
The initial 9-profile LP had numerical value 0.6237623762376239.
C++ simulated annealing used seed 20261009, 2500 restarts, 500 proposals
per restart, then up to 50 greedy one-coefficient improvement sweeps.
This produced a combined pool of 1391 layer profiles. One subsequent
LP returned a seven-row solution with value approximately 0.6859005478882019.
These are discovery numbers, not asserted global optima.

Repair/simplify: pair search in that pool found no feasible pair.
A numerical mixed-integer search for weights in multiples of 1/12
selected a four-row witness with multiplicities 1,3,4,4. Exact Fraction
arithmetic, not the optimizer status, accepted the certificate. No
universal support-minimality claim is made.

Verify: all 512 affine polynomials have maximum success 9/14 under the
simple half-weight-1/half-weight-3 input distribution. A different
hypergeometric computation agrees. The four upper truth tables are
checked by bit parity and independently by explicit tuples/monomials.
Then all 40320 permutations are applied at every one of 256 inputs;
the exact pointwise probabilities match the rational layer table.

Attack: five malformed certificates are rejected: flipped constant,
negative mixture weight, out-of-range monomial, changed target, and an
invalid lower distribution. A sixth semantic negative control omits
permutation randomization: the raw four-polynomial mixture fails at
x=14 with success 1/12. The mutation is preserved as a deliberately
constructed negative control, not portrayed as a historical conjecture.

Record: commit 7355f4e5b826a1b34e0f48d891c208495c821cca and remote
CI run 37940070467 succeeded. Actual job 113851891080 logs, file blobs
and commit were fetched and compared with the local exact outputs.
Local environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, GNU C++.
CI exact checking: CPython 3.12.15, standard library only.

Continue: factor out the generic finite-sum dual obstruction into Lean
as part of Issue #8, over real probabilities. Its semantic coverage
boundary must stay explicit: a theorem over a sampled row type cannot
exclude omitted polynomials. Lean CI/axiom results are recorded separately
in the session log and formal ledger when actually observed.

## Reproduction

Core: python3 expeditions/004-exact-mod3-n8/verify.py --permutations

Discovery sources are in discovery/. Compile search.cpp to an executable
named search in the same directory, then run discover.py and simplify.py.
Discovery is heuristic and floating-point. Replays on different compilers
may find different representatives; only exact witness validation is decisive.
