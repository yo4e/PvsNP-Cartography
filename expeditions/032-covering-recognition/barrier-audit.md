# Source comparison and barrier audit

Research lead 月野テンプレクス, 2026-11-02 JST. This is a scoped author audit. It does not certify novelty or an escape from any proof barrier.

## Primary source records

1. Razborov and Rudich, Natural Proofs, ECCC TR94-010, Section2. Official PDF https://eccc.weizmann.ac.il/report/1994/010/download/ was retrieved and printed page2 was visually inspected. Constructivity is measured in truth-table length; largeness and usefulness are independent requirements. General-circuit impossibility conclusions retain their cryptographic hardness assumptions.

2. Srikanth Srinivasan, FSTTCS2013, DOI10.4230/LIPIcs.FSTTCS.2013.201, Definitions4/6 and Fact7 on printed page204. Official PDF https://drops.dagstuhl.de/storage/00lipics/lipics-vol024-fsttcs2013/LIPIcs.FSTTCS.2013.201/LIPIcs.FSTTCS.2013.201.pdf was retrieved and that page visually inspected. The distributional-to-probabilistic equivalence quantifies over EVERY input distribution. One uniform or one balanced measure is not that theorem. The finite covering argument only uses its elementary forward averaging direction; no general minimax converse is claimed formalized here.

3. Emanuele Viola, New lower bounds for probabilistic degree and AC0 with parity gates, ECCC TR20-015 revision5, dated2021-01-12. Pinned primary PDF https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . The title and text of Section2.2, Theorem12 and Lemmas13/14 were retrieved and rechecked. PDF screenshot requests failed; no visual inspection of this source is claimed. The official journal listing was found, but its full version could not be opened, so this comparison is explicitly to the2021 revision, not a claim to have checked the latest journal text.

The preprint uses modulus amplification and a fast subset transform to count accepting assignments of a GF2 polynomial. Those steps motivate our next bounded reconstruction; they do not by themselves provide our implementation's correctness or a new runtime theorem. The larger explicit-function lower bound in that source concerns E^NP and infinitely many input lengths; it is not a theorem about NP or MOD3 at every large length. We have not reconstructed its hierarchy/PCP bridge.

## Relativization

The accepted statement counts finite functions with specified polynomial approximation, not a P-vs-NP class relation. No claim is made that the construction proves a separation under arbitrary common oracles. A future algorithms-to-lower-bounds argument must specify which circuit classes, algorithms and hierarchy steps survive oracle substitution; merely citing a nonrelativizing source does not transfer its scope.

## Natural Proofs

For d1, the uniform affine-far property is constructively recognizable in polynomial truth-table time and, by a separate written estimate, has density>1/2 for n>=7. Its usefulness against P/poly is FALSE: the paired quadratic counterfamily has linear-size circuits and lies in it for every n>=4. This is an explicit failure of one required condition, not a barrier escape or a contradiction of Razborov-Rudich.

For growing d, direct coefficient enumeration's cost may cease to be polynomial in truth-table length. We have not proved that every other recognizer is slow. Neither largeness alone nor efficient affine recognition establishes general-circuit usefulness. The uniform detector also misses MOD3 at infinitely many lengths, so its explicit-target premise fails independently.

## Algebrization

The work uses low-degree algebra, but that does not establish the asymmetric Boolean/algebraic oracle properties in Aaronson-Wigderson. There is no full proposed P-vs-NP deduction here to certify as nonalgebrizing. The next modulus-counting lemma alone supplies no such certification.

## Scope and disposition

Known-method reconstruction: positive-support averaging, finite-dimensional row counting, Hamming covering, Walsh recognition, paired quadratic counterexamples, and the proposed modulus amplifier. Mathematical novelty remains unclaimed. The finite-to-general and average-to-pointwise shortcuts are explicitly excluded. Dispose of the naive uniform-cover route as a sufficient general-circuit detector; retain its valid one-way lemma. The next target is an algorithmic correctness bridge, not a declaration that the proof barriers have been crossed.
