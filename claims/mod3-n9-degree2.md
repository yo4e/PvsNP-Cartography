---
id: mod3-n9-degree2
status: formally-verified
statement: "For n=9 GF(2) MOD3, standard finite-support pointwise 1/3-error probabilistic degree equals 2"
dependencies:
  - formal/PvsNPCartography/ProbabilisticDegree.lean
  - formal/PvsNPCartography/HammingLayers.lean
  - formal/PvsNPCartography/LayerCertificates.lean
  - formal/PvsNPCartography/Mod3NineDegree.lean
  - expeditions/011-n9-one-orbit/certificate.json
novelty: novelty-unknown
last_attacked: 2026-10-16
---

Pinned --wfail Lean verification at commit807124110f0fc1861504f9ea0bd6fd971a78992e, run38908696378/job116998734457, with356-declaration allowlist audit and14 printed n9 target theorems. The claim's actual GF(2) degree, normalized real probabilities and one-family-before-every-input quantifier are preserved. No caller assumes feasibility.

Upper: one seed (1,127,36505001791) under full coordinate permutations, strict minimum85/126>2/3. Lower: symmetric dual masses28 at weight1 and3 at weight3, sum504, universal affine maximum322/504=23/36<2/3. The generic structural degree-one normal form covers all polynomials of actual degree<=1.

Same-author Python arithmetic independently reconstructs all1260 distinct coefficients, all512 inputs, all1024 affine rows and the full nine-variable permutation orbit. Code/test commit a529afed, run38909099839. Review exact scope in expeditions/011-n9-one-orbit/statement-audit.md.

No general-n, novel-mathematics, minimal support, independent human-review, second kernel, asymptotic complexity or P-vs-NP result is claimed.
