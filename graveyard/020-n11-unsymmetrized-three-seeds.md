# Failed shortcut: use the three canonical n11 seeds without permutations

Approved2026-10-20 JST session. This is a formally checked counterexample to
one shortcut, not a refutation of the valid n11 quadratic distribution.

## Claim and attraction

Claim: the three canonical GF(2) seed polynomials with weights[1,4,2]/7 already
succeed with probability>=2/3 at every Boolean input, without randomizing
coordinate positions. Attraction: their weighted Hamming-layer averages are
all above2/3, making it easy to mistake layer averages for raw pointwise success.

Canonical lexicographic55-edge coefficient rows are
(0,0,0), (1,2047,38605195639935), (1,1920,1151998655551).
The second seed equals1+sum_i x_i+sum_{i<j<8}x_i*x_j. The third equals
1+sum_{i>=7}x_i+sum_{i<j<7}x_i*x_j. All operations in these polynomials are GF(2).

## Exact counterexample

Input x=[1,1,1,1,1,1,0,0,0,0,0], little-endian mask63, has Hamming weight6,
so MOD3(x)=1. The zero seed returns0. The second seed returns
1+6+choose(6,2)=22=0 in GF(2); the third returns1+0+choose(6,2)=16=0.
Thus EVERY canonical seed is wrong, and raw mixture success is exactly0.

This is checked independently by Expedition018/audit.py on all2048 inputs and
by accepted Lean theorems Mod3Eleven.raw_seed_counterexample and
Mod3Eleven.raw_seed_mixture_is_not_pointwise in source9733d800128ad6d92b1f1293e453a4c8d5188f34.
Formal run39380310454/job118487684638 completed SUCCESS with --wfail,
508-declaration foundational allowlist and18 explicit n11 reports. The later
integrated run39381768668/job118492254315 also printed these accepted targets.
Actual logs and the exact source/commit were re-fetched; see Expedition018's
axiom-report.txt and ci-evidence.md. No new execution is claimed by this record.

## Failure point, lesson and salvage

Averaging correctness across all inputs of one Hamming weight does not make
the unsymmetrized mixture pointwise correct. The valid construction first
chooses a seed with the fixed stated probability, independently chooses a
uniform coordinate permutation, then evaluates the renamed polynomial.
The existing proved permutation/Hamming-layer bridge supplies precisely that
missing step. The resulting n11 degree equality is formally verified.

This counterexample kills only omission of symmetrization from these three
canonical seeds. It proves neither global support minimality nor impossibility
for arbitrary three-polynomial distributions. Independent human review and
mathematical novelty remain unfulfilled; no general-n or P-vs-NP claim follows.
