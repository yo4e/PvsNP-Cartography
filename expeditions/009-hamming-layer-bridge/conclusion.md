# Completion checkpoint: Hamming-layer bridge and n=8 degree equality

Started in the Oct14 approval session; formally completed on2026-10-16 JST.
Research lead: 月野テンプレクス. Independent human semantic review remains pending.

The general mean identity is now verified: for Boolean x of weight w and any
real-valued g, the average of g(x composed with e) over all n! permutations equals
the mean of g over the choose(n,w) inputs in the entire weight-w layer.
The proof supplies layer cardinality, equal-weight orbit coverage and exact
fiber multiplicity w!*(n-w)!, including n=0 and extreme weights. The fiber count
is derived from the proved averaging theorem, not assumed by it.

LayerCertificates connects these bounds to the unchanged pointwise probabilistic
degree predicate. Mod3EightDegree proves feasibility iff2<=d, IsLeast and the
closed least-degree equality2 over GF(2), error1/3, for n=8. All normalization,
coefficient/evaluation/degree and arbitrary real-mixture lower-bound obligations
are discharged. The raw four seeds alone are not a valid pointwise distribution;
a formal input14 counterexample has success1/12.

Final verified code e034962d3df395a4b82bc00d2ef78aa8d6cb25a4 passed
https://github.com/yo4e/PvsNP-Cartography/actions/runs/38816877083,
job116703673137. Actual logs record pinned Lean4.35.0-rc4, pinned Mathlib,
--wfail,305 declarations within [propext, Classical.choice, Quot.sound], and
all26 new layer/n8 explicit targets in that allowlist. See
../../formal/reports/2026-10-16-n8-axioms.txt and ../010-n8-recovery/log.md
for actual repair history and verification attribution.

Source blobs after successful verification:
HammingLayers.lean7261f29623c7c9fda84dbc7af9b89fc02c31fb49;
LayerCertificates.lean1ab2fe1f542091fc85013d293694a5c3932c4e8a;
Mod3EightDegree.lean ec288bf49be783ad6ab88954222019247389ce57.
The next session must not treat this bridge as still missing. The numerical
n=8 value was already supported by Expedition004, so no new value or novelty
is claimed. Complete numerical Lean coverage is n=5,6,7,8, not arbitrary n.
The separately computed compact witnesses in Expedition010 are not themselves
Lean coefficient certificates. Human semantic review remains the open gate.
