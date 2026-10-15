---
id: mod3-n8-degree2
status: formally-verified
statement: "pdeg_(1/3)^GF(2)(MOD_3^8) = 2 for MOD_3^8(x)=1 iff |x| is divisible by 3"
dependencies:
  - formal/PvsNPCartography/ProbabilisticDegree.lean
  - formal/PvsNPCartography/HammingLayers.lean
  - formal/PvsNPCartography/LayerCertificates.lean
  - formal/PvsNPCartography/Mod3EightDegree.lean
  - expeditions/004-exact-mod3-n8/certificate.json
novelty: novelty-unknown
last_attacked: 2026-10-16
---

Evidence promotion: the pre-existing finite value is now connected to the original
actual-degree, GF(2), finite-support REAL-probability pointwise definition in Lean.
The family is fixed before every input. Feasibility iff2<=d, IsLeast and the
closed numerical equality have proved witnesses and do not assume the answer.

Verified code e034962d3df395a4b82bc00d2ef78aa8d6cb25a4, actual successful formal
run38816877083/job116703673137: pinned Lean/Mathlib, --wfail,305 namespace
declarations and26 new target reports within propext, Classical.choice, Quot.sound.
See formal/reports/2026-10-16-n8-axioms.txt and Expedition010 statement audit.

Upper: four degree<=2 seeds with weights1/12,1/4,1/3,1/3, followed by full
permutation randomization via the proved layer bridge, minimum2/3.
Lower: half-weight1/half-weight3 input distribution, affine maximum9/14.
All degree<=1 objects are covered structurally, not merely a sampled list.

The separately retained939/159-row compact certificates are not the encoded
formal witness and have not themselves received a Lean coefficient verification.
No human independent semantic review, second proof kernel, novelty promotion,
optimal support/error claim or extension to n>=9 is recorded.

Historical finite checkpoint: Expedition004, run37940070467 on
7355f4e5b826a1b34e0f48d891c208495c821cca. That checkpoint was not yet Lean;
its statement and original certificate remain unchanged. The current promotion
improves verification evidence, not the numerical degree value.
