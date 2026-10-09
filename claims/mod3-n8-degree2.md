---
id: mod3-n8-degree2
status: candidate-survives
statement: "pdeg_(1/3)^GF(2)(MOD_3^8) = 2 for MOD_3^8(x)=1 iff |x| is divisible by 3"
dependencies:
  - expeditions/004-exact-mod3-n8/certificate.json
  - expeditions/004-exact-mod3-n8/verify.py
  - finite convexity and permutation-orbit counting arguments in conclusion.md
novelty: novelty-unknown
last_attacked: 2026-10-09
---

Evidence class: exact finite certificate, complete checking of the required
finite quantifiers, two evaluators and independent-runner CI.

Upper: four degree-at-most-two orbits with weights 1/12,1/4,1/3,1/3
have minimum pointwise success 2/3.
Lower: the half-weight-1/half-weight-3 input distribution bounds every
affine polynomial by 9/14 < 2/3.

CI evidence: run 37940070467 on commit 7355f4e5b826a1b34e0f48d891c208495c821cca.
No Lean MOD3 verification, external mathematical review, novelty promotion,
global success-optimality claim or extension to n>=9 is recorded.
