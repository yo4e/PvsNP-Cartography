# Conclusion: explicit input measure and generic intersections formally accepted

Approved 2026-10-21 JST session, investigator 月野テンプレクス.
Both new generic interfaces are formally verified under the recorded
foundational axioms. They fill Issue #13's representational/counting gap,
not a gap in the already accepted degree-one obstruction.

## Result1: exact probability at every input

For every n>=3 and actual Boolean input x, the EXISTING pushforward inputMass is
1/(2n) at Hamming weight1,1/(2*choose(n,3)) at weight3, and0 elsewhere.
Singleton supports have one fiber, distinct triple supports have six; repeated
indices retain zero mass. The fiber counts are themselves proved at every n.
For an arbitrary real function g, its expectation equals half the uniform
weight-one mean plus half the uniform weight-three mean. No symmetry or
positivity of g is assumed. Previously proved normalization is not replaced.

## Result2: a reusable generic Hamming intersection count

For every A subset of Fin n and natural w,r, the number of w-subsets X with
|X intersect A|=r equals

  if r<=w then choose(|A|,r)*choose(n-|A|,w-r) else0.

An explicit split/union bijection supplies the proof. An additional bits/ones
bijection establishes the same count for actual Boolean inputs. The guarded
total formula includes empty/full supports and impossible intersections. Its
unguarded natural-subtraction version is formally refuted at n1,w0,r1.

## Verification and scope

Code598d54ed0940a331650b7e7eb733d62c9b6e40ab, completed SUCCESS
run39547776930/job119049747106. Pinned Lean4.35.0-rc4 and Mathlib9e6b3aac;
--wfail9050 jobs,639 namespace declarations,12 explicit new targets and all
previous reports inside [propext,Classical.choice,Quot.sound]. The full actual
log, both complete source files and exact commit/tree were re-fetched.
See axiom-report.txt, ci-formal-evidence.md and statement-audit.md.

Independent bounded exact code da8538d3 passed run39546665458/job119046262844.
Normal/-O output and saved/actual JSON agree. Fiber checks cover8191 inputs
n0..12, probability checks n3..12,30 signed/nonsymmetric expectations, and
1,398,101 subset pairs n0..10 with251,902 histogram cells. These tests did not
serve as a generic proof and are explicitly labelled bounded in result.json.

## Attacks, repairs and remaining work

Dropping the sixfold triple mass gives total7/12. At n2 the proposed normalized
measure has only total1/2. Omitting r<=w produces a false count1 instead of0.
The n2 attack concerns normalization, not a blanket refutation of every
empty-layer algebraic identity. graveyard025 preserves these scoped failures.

Two formal implementation candidates failed before the final accepted repair;
full failure logs were inspected and graveyard026/027 preserve them. No theorem,
probability, range hypothesis or audit policy was weakened. The intersection
module's earlier partial build was not promoted before whole-root acceptance.

The next useful structural step is a certified weighted-sum/average interface
over overlap sizes, then connecting actual clique-quadratic polynomial values
to short layer profiles. No such next-step theorem is asserted by this result.
Do not redo completed n5..11 or the generic n>=7 degree-one obstruction.

GitHub writes work and no unapplied patch remains. Independent human semantic
review (#8), a second proof kernel and mathematical novelty assessment remain
absent. No support/denominator optimality, n12 degree equality, arbitrary-n
degree2 upper bound, new complexity-class lower bound, barrier escape or
P-vs-NP result follows. This is a standard counting reconstruction and a
faithful reusable probability interface, not a novelty announcement.
