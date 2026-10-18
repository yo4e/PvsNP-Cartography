---
id: mod3-n11-degree2
status: finite-evidence
statement: Exact n11 GF(2) MOD3 pointwise quadratic certificates at error1/3 and a strict exhaustive affine-row dual, including an equivalent496-row measure.
dependencies: [expeditions/015-n11-mixture/compact-certificate.json, expeditions/017-n11-subset-compression/verify.py, expeditions/017-n11-subset-compression/result.json]
novelty: novelty-unknown
last_attacked: 2026-10-18
---

The three seed orbits with fixed weights[1,4,2]/7 retain success>=158/231>2/3
at all2048 inputs after full symmetrization. The new quotient gives exactly
the SAME probability measure on496 distinct degree<=2 polynomials, denominator
1155, instead of1925 labelled entries/27720. Zero has mass165/1155, each8-subset
row4/1155 and each7-subset row1/1155. It is not a uniform measure.

Code8ff6df0ba8362966f2df76d90e5fbe3a84d8f2a5, successful run39137936272/
job117706176557. Exact old/new coefficient-row mass dictionaries, all2048 point
scores,1,013,760 subset-formula/monomial evaluations and12 layer counts agree.
All4096 affine rows retain dual69/110<2/3. Normal/-O outputs equal saved JSON.
Actual full logs, source/result and commit/tree re-fetched. Four invalid
weighting/symmetry/encoding controls are rejected; graveyard016 preserves them.

The earlier nine-orbit witness and compact three-orbit files remain unchanged,
with their original CI evidence in Expedition015. The generated496-row table
is an Actions artifact reproducible from the committed generator, not a
checked-in full support table. See Expedition017/ci-evidence.md.

NOT a compiled n11 Lean degree theorem or formal quotient transport lemma.
After separately completed n10 (#10), #11 is the next formal task. Independent
human semantic review (#8), novelty and a second kernel remain unfulfilled.
No support/denominator optimality, all-n MOD3 bound or P-vs-NP conclusion.
