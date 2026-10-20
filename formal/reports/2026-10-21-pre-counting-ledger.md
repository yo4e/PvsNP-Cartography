# Formal assumption ledger

## Current checkpoint: approved2026-10-20 JST session

Complete numerical GF(2), pointwise error1/3 MOD3 probabilistic-degree equalities
are now formally verified for **n=5..11**. The new n11 theorem uses genuine
MvPolynomial.totalDegree, normalized nonnegative REAL probabilities and one
finite polynomial family chosen before every input. #11 is completed.

A separate generic REAL-algebra score bound is also formally verified. Its
identification with a generic Boolean-cube correctness probability is not yet
formalized; #12 is the next unblocked structural task. #8 remains independent
human semantic review. No n12 degree equality or all-n degree2 upper bound follows.

## Actual n11 production acceptance

Code9733d800128ad6d92b1f1293e453a4c8d5188f34; treeec4b8aa8bbfab9b5bc6d4e134acde3c785f6475f.
[Completed SUCCESS run39380310454](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39380310454),
job118487684638. Pinned Lean4.35.0-rc4 and Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8; --wfail9043 jobs;
508 namespace declarations and18 explicit n11 targets within
[propext,Classical.choice,Quot.sound]. Full completed log inspected; coefficient
data, final theorem statements and Git commit/tree re-fetched afterward.

n11 source blob1eb242d53c74bb546a3547d9107b8074cb40caa3, SHA256
 eb8c4bc823cf0b370ae09746ef3c63ab5d4d7403e1ab0a11f0a4b7257087f00a.
[Actual attributed axiom output](../expeditions/018-n11-formal/axiom-report.txt),
[statement audit](../expeditions/018-n11-formal/statement-audit.md),
[CI evidence](../expeditions/018-n11-formal/ci-evidence.md),
[conclusion](../expeditions/018-n11-formal/conclusion.md).

The three seeds have weights[1,4,2]/7, represented by triple tickets[3,12,6]/21.
All12 layer inequalities use threshold14 and kernel-checked closed sums.
The existing full-permutation/Hamming-layer adapter supplies the pointwise
family. The lower dual207/330=69/110<2/3 covers all4096 affine coefficient
rows through proved permutation coverage; structural degree-one normal form
extends to ALL actual degree<=1 polynomial objects and finite REAL mixtures.
The final feasible_degree_iff, IsLeast and pdeg_eq_two use proved existence.
The raw unsymmetrized three-seed counterexample atmask63 is also accepted.

The separately computed496-row same-measure quotient is not a new Lean quotient
transport theorem. Nor is the original larger-margin nine-orbit witness newly
formalized by accepting this three-seed/full-permutation construction.

## Additional real algebra and integrated audit

Repaired code dde6151abd4a4a272a2bdcbbd277c7296487d2c5; tree
7c07084a3f867891092e247922a6741d62750525.
[Completed SUCCESS run39381768668](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39381768668),
job118492254315: unchanged pinned versions, --wfail9044 jobs,518 namespace
declarations inside the same foundational allowlist. All18 n11 target reports
and six new algebra reports completed. Full logs, ENTIRE repaired algebra source
and matching commit/tree re-fetched. Source blobef92fdecc80241481d9b4578dce596848733ff33;
SHA2565a6bfaa519c10b8205cd0a019d0e87e353f7f8133163cb477c4b407b4a62b335.

For all real n>=7 and0<=k<=n, with t=n-2k, the accepted algebra proves
1/3<1/2+t*(n^2-t^2)/(4*n*(n-1)*(n-2))<2/3, plus complement symmetry and
exact score(6,1)=2/3. This is not a finite-to-general inference: the proof is
real algebra. However, its generic Boolean-cube counting/application bridge is
still unproved and tracked separately in #12. See [actual output](../expeditions/019-balanced-affine-dual/axiom-report.txt)
and [scope](../expeditions/019-balanced-affine-dual/conclusion.md).

## Complementary finite tests and failure preservation

n11 exact source audit9238f5a1 passes39380579421/job118488536922 under normal/-O,
with actual/saved JSON equality:2048 inputs,4096 affine rows,12 layers,
201 coefficient changes and5 source-data mutations, exact production-source hash.
Algebra-interpretation exact codeea1f4e04 passes39381262415/job118490656488:
33147 formula pairs n3..256, full cubes/all affine rows n3..12. Its result is
bounded finite evidence, not a proof of generic counting. Both full completed
logs and saved outputs were inspected and re-fetched.

The initial auxiliary formal build39381262500/job118490657553 FAILED on missing
noncomputable for a real definition and an unused-hypothesis warning. Repair
changed only the annotation and explicit hypothesis use, not any statement,
threshold or audit policy. graveyard019 preserves the actual failure. The false
strict-bound extension to n5/n6 remains in graveyard018. All older n10/n8
failures and original proof artifacts remain in their dated records.

## Reproduction and remaining gates

From formal/: `lake build --wfail` and `./scripts/axiom_report.sh`.
Production CI additionally runs the compiled namespace axiom allowlist.
No project-specific extra axiom, sorryAx, admit, native_decide or decide_cbv
was admitted. The local container lacked Lean; actual formal execution was in
Actions. Independent human semantic review and a second proof kernel remain
absent. No mathematical novelty, support optimality, circuit lower bound,
barrier escape or P-vs-NP conclusion is asserted.

## Preserved historical ledgers

The entire preceding n10 ledger is archived byte-identically as
[2026-10-20-pre-n11-ledger.md](reports/2026-10-20-pre-n11-ledger.md),
Git bloba43efd4ec81015a490b1bfa5f3de40b7180d32f1. It preserves the accepted
n10 production1739ccfa/run39139432083, earlier semantic checks, repair details
and the links to all prior n5..9 ledgers. Its n11-pending statements describe
the historical Oct18 checkpoint, not current status. No historical proof or
failure record was deleted. Documentation-only commits do not replace the
specific code/run acceptance evidence above.
