# 012: one-orbit three-block n=10 exploration does not work

Date: 2026-10-16 JST. Classification: **refuted inside a restricted family**.
Claim killed: a single fully symmetrized degree-two seed with <=3 invariant
coordinate blocks can meet the n=10 MOD3 pointwise success threshold2/3.

Why attractive: n=9 has exactly such a striking one-orbit witness, with blocks
4+3+2, one seed, and finite margin85/126. It would be tempting to extrapolate
one variable higher.

Test: enumerate all14 descending nonempty block-size partitions of10 into
<=3 blocks and every GF(2) coefficient mask constant/linear/intra/inter.
Total exactly8520 seeds, all scored by exact hypergeometric Hamming-layer
counts. None attains2/3 across every layer. Strongest in this restricted class:
size4+3+3, mask727, worst-case **62/105** at input weight4.
Full truth-table enumeration of1024 inputs independently confirms the
candidate's counts [1,7,33,88,124,174,148,72,36,7,1].

Reproducer: expeditions/012-n10-three-blocks/scan.py, plus strict
Python -O mode. Do not call the script's own two evaluators independent
human review.

Limit: a mixture of such orbits, or a less symmetric degree-two family, may
yet satisfy2/3. This scan does not rule out all degree-two polynomials or
prove degree3 necessary. Nor does it generalize the n=9 witness as a theorem.

Salvage: use these failed singles as a pool for a real-probability mixture
search and attack potential duals with explicitly bounded support; exact
fraction reconstruction must verify all1024 inputs before any claim.
