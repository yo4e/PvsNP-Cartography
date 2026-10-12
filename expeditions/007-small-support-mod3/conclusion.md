# Conclusion: complete finite n=6/n=7 degree equalities with small support

Date: 2026-10-13 JST. State: formally-verified under the recorded Lean assumptions.
Novelty: unknown for the small-support presentation; finite degree values unchanged.
Independent human semantic review: pending.

## Result

For n=6 and n=7, the standard pointwise probabilistic degree of MOD3 over GF(2),
with error1/3 and finite-support REAL probabilities, is exactly2.
SmallSupportMod3.feasible_degree_iff proves feasibility iff2<=d;
least_feasible_degree proves IsLeast; pdeg_eq_two gives the closed numerical
least-degree equality. All finite premises are discharged, not supplied by a caller.
Together with the earlier n=5 result, complete degree-based Lean coverage is now
n=5,6,7. n=8 still has the earlier finite Python certificate, not this Lean theorem.

The n=6 and n=7 upper witnesses each use18 distinct degree-at-most-two
polynomials and24 integer tickets. Their minimum pointwise success is16/24.
The lower certificates exclude all degree-at-most-one polynomial families:
maximal dual success660/1080=11/18 for n=6 and595/1050=17/30 for n=7.
The lower coverage includes arbitrary real mixtures, not only rational candidates.

## Exact executable replication and attacks

All64/128 inputs and128/256 affine rows were exhausted. Two polynomial
evaluators, Mobius coefficient reconstruction and an integer Walsh transform
agree with the direct arithmetic. Normal and -O Python outputs coincide.
Six altered claims are rejected. The saved audit-results.json records every
input numerator, source hash and the exact360-case failed compression search.

A single cyclic orbit of the chosen seed with fixed twelve-ticket masses
always fails; its best minimum is7/12. Two such orbits with24 total tickets
repair it. See ../../graveyard/006-single-cyclic-orbit.md. This is not a proof
that every smaller-support or twelve-ticket construction is impossible.

The compact n=7 witness has only cyclic symmetry: inputs7 and19 both have
Hamming weight3, but success16/24 and20/24 respectively. All114 other minimum
cases still meet2/3. Its14 higher-success inputs form two cyclic orbits,
[19,25,38,50,73,76,100] and[21,37,41,42,74,82,84]. Thus a layer-average argument
would not replace the direct every-input check used here. The old eight-orbit
n=7 certificate has strict slack10825/15922>2/3 and remains useful; the new
certificate trades that slack for a smaller finite proof object.

## Actually observed Lean verification

Code commit8899e75646a443415d5a2346d3c8f48d62c7bb79 passed
[formal run38307092042](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38307092042),
job115003654751. Actual retrieved output records pinned Lean4.35.0-rc4,
Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8, --wfail success,
145 namespace declarations within {propext, Classical.choice, Quot.sound},
and all13 new printed target reports inside that same allowlist.
See ../../formal/reports/2026-10-13-small-support-axioms.txt.

[Semantic run38307092049](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38307092049),
job115003655051, passed at the same code commit. Re-fetched source blob
7f2e5ecdac08af19ba461d986c84711c13cd980a, audit.py blob
928b49456d16f08f6d304fbcae993b12ac5f4dbf and certificate.json blob
c34de5b562d89b0ba19c735d0ca37c0e709c4f8b matched the locally inspected bytes.
The commit/tree and actual successful job output were separately retrieved.

The first formal candidate92df9d8 failed at a constant-degree proof obligation.
The repaired proof explicitly applies totalDegree_C; it changes no mathematical
statement, probability, coefficient, threshold, warning policy or axiom allowlist.
No failed build was called verified. No independent human or second proof kernel
is supplied by separate algorithms or CI machines.

## Frontier

Keep Issue8 open for generic permutation/symmetrization infrastructure and
independent human semantic review, not for redoing the finished n=6/n=7 stage.
An unblocked next target is a degree/evaluation-faithful variable-permutation
lemma and full symmetrization theorem, with cyclic-versus-full symmetry as a
negative control. Use that infrastructure toward the existing n=8 certificate.
No pending patch or write-approval blocker remains from this session.

No new numerical value, support-minimality theorem, uniform/general-n MOD3
result, asymptotic circuit bound, proof-barrier escape or P-vs-NP conclusion
is asserted. See statement-audit.md and barrier-audit.md for the exact boundary.
