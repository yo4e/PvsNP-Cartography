# 011: all failed <=3-block single-orbit quadratic candidates at n=9

Date: 2026-10-16 JST. State: refuted within an explicitly restricted finite search class.

## Precisely enumerated class
Split nine labelled variables into 1, 2 or 3 nonempty blocks with descending block sizes. On any fixed block partition, exhaust all coefficients of the blockwise-permutation-invariant GF(2) quadratic family: one constant term, one linear block-parity per block, one within-block e2 term per block, and one block-product per unordered pair of blocks. Form one **uniform orbit** under all nine-variable permutations for each candidate.

There are 12 block-size partitions, and 7432 coefficient masks: 8 one-block, 256 two-block and 7168 three-block masks. Every one is checked with exact integer binomial counts on **all ten Hamming layers**; no floating optimization decides acceptance.

Exactly ONE model reaches at least2/3 on every layer: block sizes (4,3,2), binary mask727 in the documented coefficient order, with minimum85/126. All other **7431** masks fail somewhere. The best three-equal-block candidate (3,3,3) has minimum13/21 <2/3; the two-block families also fail.

The single successful block expression for counts a,b,c of ones in groups A4,B3,C2 is
`1+a+b+binom(a,2)+a*b+b*c+binom(c,2) (mod2)`.
Its 1260 unique labelled partitions are independently evaluated on all512 inputs.

Reproduce via `python expeditions/011-n9-one-orbit/scan_blocks.py` and the separate `verify.py --full`; normal and -O checks passed actual GitHub Actions run38909099839.

## False inference rejected
'All simpler block patterns fail, so the certificate needs at least1260 polynomials' is NOT proved. The tested objects are single-orbit, blockwise-invariant families with no more than three nonempty groups. Distributions over multiple orbits, other symmetry groups, arbitrary quadratic coefficient patterns and nonuniform weights lie outside this scan.

Failure is a map boundary, not a lower bound on global support. An even stronger finite n=9 witness or a smaller multi-orbit distribution may exist.
