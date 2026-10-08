# Expedition 003 research log

## 2026-10-08 (JST): observe → orient → act → verify → attack → repair → record

**Observe.** Expedition 002 reproducibility and Lean scaffold CI were
repaired and their Issues #6 and #3 closed. Next natural frontier:
the n=8 value, without extrapolating n=5,6,7.

**Orient.** Define quadratic coefficient masks and orbit pointwise
success exactly as in Expedition 002. Enumerating all 2^37 polynomials
was outside this session's bounded resources.

**Act.** Sample 10,000 coefficient vectors (NumPy 2.3.5,
default_rng seed 20261008) plus 16 deterministic structured vectors,
compute all 256 truth-table values per candidate, and aggregate 9
Hamming-weight success counts. Deduplicate to 6,407 distinct vectors.
A SciPy 1.17.0 HiGHS LP returned approximate max-min 0.630820399113.

**Verify.** Convert the discovered primal/dual solutions to exact
rational certificates. In the sampled set, a 9-orbit mixture attains
569/902 in every layer; a dual layer distribution with denominator
23452 upper-bounds all sampled candidates by 569/902. The repository
checker verifies these results by exact counts and scaled integer
arithmetic. The mathematical statement is ONLY about this pool.

**Attack.** Deliberately attempt to use the dual q against polynomials
not in the pool. A fresh random search (seed 20261009) found a
quadratic polynomial (1,255,60548413), outside the pool, whose
exact q-average correctness is 27376/41041 > 2/3. A separate
standard-library enumeration of all 256 inputs confirmed its counts
[1,8,17,34,39,28,21,6,1] and the strict rational inequality.

**Repair.** Retract the imagined *universal* degree-2 lower
certificate. Preserve the valid sample-restricted LP statement;
archive the invalid generalization in graveyard/ and record the
adversarial counterexample in attacks/.

**Continue.** An exploratory (not proof-grade) column-generation loop
using new candidate draws increased a sampled LP objective through
approximately 0.662782, but this was not an exhaustive or formal
n=8 result. Do not promote it. The next expedition needs either a
concrete exact pointwise 2-degree witness, or a universal lower
certificate with an exhaustive/full-class checking strategy.

Reproduce committed evidence:
python3 expeditions/003-n8-sampled-dual/verify_n8_sampled_dual.py
python3 expeditions/003-n8-sampled-dual/verify_n8_sampled_dual.py --optimize

Second command uses NumPy==2.3.5 and SciPy==1.17.0; only the
discovery optimizer is numerical. The certificate comparisons are exact.
