---
id: mod3-n10-degree2
status: formally-verified
statement: The GF(2) pointwise probabilistic degree of MOD3 on exactly10 Boolean variables at error1/3 equals2.
dependencies: [formal/PvsNPCartography/Mod3TenDegree.lean, formal/PvsNPCartography/LayerCertificates.lean, formal/PvsNPCartography/SmallSupportMod3.lean, formal/PvsNPCartography/ProbabilisticDegree.lean]
novelty: novelty-unknown
last_attacked: 2026-10-18
---

Approved Oct18 night; actual production run completed Oct19 JST.
Code1739ccfa2ebe5997e568135cdfacf06e9f6d1f87, run39139432083/job117710608870:
--wfail build9042 jobs,420-declaration foundational axiom audit and15 explicit
n10 reports completed successfully. Source blob
cf6c6ec257f0a5c20e9b12f3c265864db57e58ca. Actual statements/logs/commit re-fetched.
See formal/reports/2026-10-18-n10-axioms.txt and Expedition016 conclusion.

One normalized nonnegative REAL finite family of genuine degree<=2 GF(2)
MvPolynomials is chosen before all inputs, including all coordinate permutations.
The strict dual19/30<2/3 plus structural normal form excludes every degree<=1
REAL mixture. Feasible_degree_iff, IsLeast and pdeg_eq_two are actually proved.
The raw unsymmetrized1/50 counterexample is also formally checked.

Independent semantic run39139432110/job117710608842 checks the same sourcehash,
all1024 canonical inputs,2048 affine rows,11 layers and448 coefficient mutations.
Only the layer proof evaluation was case-split; theorem meaning was unchanged.

No independent human semantic review, second proof kernel, mathematical novelty,
minimum support/denominator, all-n bound, barrier escape or P-vs-NP claim.
