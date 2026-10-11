# Conclusion: the n=5 degree-based equality is Lean-checked

Approval night: 2026-10-11; completed 2026-10-12 JST after midnight.
Status: formally verified under explicitly audited foundational axioms.
Novelty: unknown. Independent human semantic review: not performed.

## Exact result and what changed

For MOD3 on five Boolean inputs, over GF(2), and error 1/3:

HasProbabilisticDegreeAtMost mod3Function (1/3) d <-> 2 <= d.

The definition uses actual Mathlib polynomial totalDegree, finite-support
REAL probabilities, normalization, nonnegativity and the SAME distribution
for EVERY input. The closed theorem Mod3Five.pdeg_eq_two proves that the least
feasible degree is 2. Its existence witness comes from the already proved
quadratic construction, not an unproved assumption supplied by a caller.

This closes the specific interface gap left by Expedition 005. Previously,
the lower result covered the canonical affine representation. Now the
structural degree_one_normal_form theorem covers ANY polynomial of degree
at most one, and degree_one_eq_affine proves actual polynomial equality with
that canonical representation. The generic normal form holds for arbitrary
finite variable types and commutative semirings by a structural argument;
this is not an extrapolation of finite MOD3 measurements.

The lower side reuses the fully discharged 11/18 affine bound and real-mixture
duality. The upper side reuses the 30 genuine quadratic polynomials with
pointwise success at least 7/10. Thus no unproved symmetry lemma is introduced.
The original numerical n=5 value is unchanged; its formal coverage improved.

## Observed verification

Code commit: 512aaf2745d2d8aab4bab76c1ac43ff6130d7de2.
[Lean run 38150083188](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38150083188),
job 114501532196, completed successfully. The actual logs show all three
new modules built, --wfail retained, 86 namespace declarations inside the
allowlist, and the closed pdeg_eq_two target depending only on
propext, Classical.choice and Quot.sound. The quantifier countermodel also
passed. Retained excerpt: ../../formal/reports/2026-10-12-n5-degree-axioms.txt.

[Semantic run 38150257051](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38150257051),
job 114502054887, passed on test commit
215f89efc3800ecc7c6af97f28c968685406b6b3. It reproduces all 64 affine
truth tables via a different Mobius inversion algorithm, verifies 2048
evaluations and both semantic counterexamples, in normal and optimized Python.
See audit.py and the attributed audit-output.txt. This finite audit does not
replace the generic structural proof or validate Lean syntax.

Remote files and commits were re-fetched and compared with locally inspected
bytes. Source blob hashes:
- DegreeOneNormalForm.lean: 9d6dab99419cf1c731e13cfd5333a184b9e8a5aa
- ProbabilisticDegree.lean: 113a65fae20ee021b5fd2f050ed101b201ef7262
- Mod3FiveDegree.lean: fa80423c59a0f2220a5456dca0363fa2ae4d7259
- audit.py: 3543a2797419ada1286e685647aace6cc7a37bf3

## Attacks and limits

Swapping the family/input quantifiers permits input-dependent constants and
wrongly collapses the degree to zero for every function. The combined Lean
countermodel contrasts this with true degree-zero infeasibility for MOD3^5.
Dropping the degree premise from normal-form reconstruction is refuted by
x0*x1, even though it agrees with zero on zero and all basis inputs.
These deliberate negative controls are preserved in graveyard/005; they are
not presented as conjectures once believed by the research lead.

The first build failed on syntax, eta-reduction, equality orientation and
coefficient casts. Repairs changed proof terms, not the intended claims,
warning policy, axiom allowlist or certificate thresholds.

## Next frontier

Issue #8 remains open for n=6/n=7, scalable symmetrization and independent
semantic review. The old degree-one coverage gap and the n=5 equality gap
are now CLOSED and must not be rediscovered as pending tasks.
No new n=6,7,8 Lean theorem, minimal support, general-n MOD3 upper bound,
novelty, proof-barrier escape, or P-vs-NP resolution is claimed.
