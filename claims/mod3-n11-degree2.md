---
id: mod3-n11-degree2
status: formally-verified
statement: For GF(2) MOD3 on exactly eleven Boolean variables and pointwise error1/3, the standard finite-support REAL-weighted probabilistic degree equals two.
dependencies: [formal/PvsNPCartography/Mod3ElevenDegree.lean, formal/PvsNPCartography/LayerCertificates.lean, formal/PvsNPCartography/SmallSupportMod3.lean]
novelty: novelty-unknown
last_attacked: 2026-10-20
---

Actual n11 degree equality accepted at9733d800128ad6d92b1f1293e453a4c8d5188f34:
run39380310454/job118487684638 SUCCESS, pinned Lean4.35.0-rc4 andMathlib9e6b3aac,
--wfail9043 jobs,508 namespace declarations and18 explicit targets using only
propext,Classical.choice,Quot.sound. Full completed logs, theorem statements,
source and matching Git commit/tree were re-fetched. See Expedition018 conclusion,
ci-evidence.md, statement-audit.md and axiom-report.txt.

The formal witness uses THREE canonical seed polynomials and all permutations,
weights[1,4,2]/7; all12 layer bounds are kernel checked. Universal lower dual
69/110<2/3 covers4096 affine rows by proved symmetry and ALL actual degree<=1
polynomials via structural normal form. Normalized REAL distributions and the
family-before-input quantifier remain unchanged. feasible_degree_iff, IsLeast
and pdeg_eq_two are proved with actual upper/lower witnesses, not assumptions.

Complementary exact source audit9238f5a1 passes39380579421/job118488536922 under
normal/-O Python, all2048 inputs,4096 affine rows,201 coefficient and5 source
mutations. Raw three seeds without permutations fail0 atmask63, also formally
verified. The existing496-row/denominator1155 quotient has identical probability
measure and minimum158/231, but its separate quotient transport is NOT a new
Lean theorem merely because the full-permutation witness is now accepted.

Preserved history: Expedition017 code8ff6df0b, successful39137936272, quotient
masses zero165, each8-subset4, each7-subset1 over1155. The generated support
artifact and all original nine-orbit/three-orbit certificates remain unchanged
in Expeditions015/017. The different larger-margin nine-orbit witness is not
newly formalized by this theorem. No support/denominator optimality is asserted.

Independent human semantic review #8, a second kernel and novelty assessment
remain outstanding. No all-n degree2 upper bound, barrier escape or P-vs-NP
conclusion follows; this claim is expressly bounded to n11.
