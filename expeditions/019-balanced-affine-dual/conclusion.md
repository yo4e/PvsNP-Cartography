# Conclusion: generic real-algebra bound verified; counting bridge remains open

Approved2026-10-20 JST session. This expedition has two distinct outputs:
a completed formal theorem in real algebra and a precisely bounded exact
computational check of its proposed affine-score interpretation.

## Formally accepted statement

For real n>=7 and0<=k<=n, define t=n-2k and

S(n,k)=1/2+t*(n^2-t^2)/(4*n*(n-1)*(n-2)).

Lean proves1/3<S(n,k)<2/3, complement symmetry S(n,n-k)=1-S(n,k),
a rational cubic envelope, and S(6,1)=2/3. The uniform algebraic proof uses
nonnegative polynomial products and a sum-of-squares decomposition, not a
finite enumeration. See derivation.md for the human-readable calculation.

Repaired source dde6151abd4a4a272a2bdcbbd277c7296487d2c5 passed actual formal
run39381768668/job118492254315: pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
--wfail9044 jobs,518 audited namespace declarations and six auxiliary target
reports inside the foundational allowlist. All18 existing n11 targets were
also reprinted. Full completed logs, repaired source and commit/tree were
re-fetched. ci-evidence.md and axiom-report.txt preserve exact provenance.

## What is NOT yet formalized

The intended application puts half the input mass uniformly on Hamming weight1
and half on weight3. An explicit informal counting argument gives, for the
constant-zero affine row of coefficient weight k,

(n-k)/(2n)+[k*choose(n-k,2)+choose(k,3)]/[2*choose(n,3)].

Expanding gives S(n,k); constant-one predictions complement this probability.
The generic finite-set counts, input normalization, casts and actual polynomial
evaluation connection are NOT yet a compiled Boolean-cube theorem. Issue #12
tracks that bridge and the subsequent structural-normal-form/finite-real-dual
application. The algebra theorem must not be labelled a completed generic
MOD3 result by skipping this missing proof.

A larger-arity degree-one obstruction can alternatively be obtained by a
correct zero-coordinate restriction from a small-arity obstruction. Therefore
no new asymptotic lower-bound discovery is asserted; the contribution is an
explicit reusable dual formula and an audited algebraic component.

## Exact replication and adversarial boundaries

The standard-library checker compares33147(n,k) pairs for n3..256, and full
input cubes/all affine rows by Walsh and direct canonical sums for n3..12.
Normal/-O outputs equal saved JSON in successful run39381262415/job118490656488
at ea1f4e04. The actual completed log and stored result were re-fetched.
These tests do NOT prove a generic counting statement.

Extending the strict equal-half dual bound down to n6 fails: k1 scores exactly
2/3. At n5,k1 it scores7/10. graveyard018 preserves the specific dead route;
it does not refute existing n5/n6 degree equalities or prove an affine family
feasible. The n6 boundary itself is also accepted in Lean.

The first algebra build failed on computability annotation and a hypothesis
warning. Its log remains in graveyard019. The repair retained every theorem
statement, domain, threshold and audit requirement, and passed production.

## Classification and next frontier

Pure real-algebra lemma: formally-verified under recorded assumptions.
Generic Boolean-cube counting bridge: not yet formally verified.
Finite computational comparisons: finite-evidence at the recorded ranges.
Novelty: unknown. Independent human semantic review (#8) and a second proof
kernel remain absent. Complete numerical MOD3 degree equalities are n5..11;
this does not assert n12 degree equality or an all-n degree2 upper bound.
No minimum-support, general circuit lower bound, barrier escape or P-vs-NP
claim follows. The session ends at this verified-lemma/explicit-frontier milestone.
