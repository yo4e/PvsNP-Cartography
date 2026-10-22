# Expedition023: real mixtures, exact restricted value, and a source bridge

Research lead 月野テンプレクス. One approved2026-10-22 JST night session,
completed after midnight2026-10-23 JST. Issue16 closed; Issue17 is the frontier.
Evidence and novelty are separate: formal/finite results below, novelty unknown.

## Accepted formal integration

At code9410fa952ad4b92f09237bfc09be5ad200413db3, ProfileMixtures proves the
actual real-mixture linearity and reuses full symmetrization for profile-based
certificates. RestrictedCliqueObstruction proves impossibility of pointwise2/3
success for ANY finite normalized nonnegative real mixture of precisely the
n12 zero/q9/r8 family. Actual polynomial evaluation supplies its scores; the
conclusion is not smuggled into a hypothesis. The family-before-input order,
real probabilities and original MOD3 target remain intact.

Completed SUCCESS run39800322628/job119898840545: pinned --wfail9054 jobs,
741 declarations under the unchanged three-axiom allowlist,24 target reports.
Actual source/commit/log were re-fetched. See ci-evidence.md, axiom-report.txt
and statement-audit.md. This is not external semantic review or a second kernel.

## Restricted value is EXACTLY9/14

Dual total masses are5/14 on uniform weight6,9/14 on uniform weight10. Every
zero/q9 scores9/14; every r8 scores241/462. Finite real weak duality bounds the
worst-input success of any allowed mixture by9/14, below2/3 by1/42.

Matching primal: zero gets3/14, each of ALL220 size9 q-polynomials gets1/280,
and all495 r8 rows get0. At input weights0..12 the success numerators over280
are [220,280,180,192,220,200,180,200,220,192,180,280,220]. The minimum180/280
is9/14. The equality concerns only this finite game. The matching primal was
checked computationally on all4096 inputs; no Lean sharpness theorem or
support/denominator minimality is claimed.

Exact accepted code772b0eac985aeea4266d099482cba6759820a789,
run39799669199/job119896456402. verify.py constructs actual bit-packed GF(2)
polynomials, checks all716 distinct truth tables,2,932,736 input pairs and9308
independent profile identities. Normal/-O and both stored/actual JSONs match.

## Attack and repair

A genuine q8 polynomial scores5/6 under the same dual; this is also a Lean
counterexample to the missing-support shortcut. Input-dependent selection
succeeds everywhere; signed weights, wrong normalization, reversed layer
masses and characteristic-two ordered edges all break claimed shortcuts.
Graveyard033 preserves the mathematical controls. Graveyard034/035 preserve
two actual failed formal builds and their faithful numeral-reduction repair.
The dead direction is probability-only repair INSIDE this family, not all
quadratics or all approaches to n12.

## Continued mathematical work and next frontier

source-bridge.md inspects a primary lower-bound statement and repairs two
real parameter mismatches: error1/3 is too large, and its hard residue need
not be0. Independent17-fold majority reduces error below1/12 with degree
factor at most17; fixing two coordinates recovers all three residues. A known
Omega(sqrt(n)) consequence then follows from the IMPORTED source theorem.
No novelty, explicit finite threshold or Lean Smolensky reconstruction follows.
The finite controls reproduce the majority truth table, exact tail derivative
and residue padding; their role is corroboration, not a generic proof by tests.

#17 selects the first substantive growing-degree agreement/dimension lemma
from an accessible primary source. Its missing hard argument is explicit.
No automatic n13 enumeration and no open-ended framework expansion. Existing
n5..11 exact degree2 and n>=7 affine exclusion remain unchanged. Unrestricted
n12 degree, new-code independent review and a second kernel remain unresolved;
none is hidden behind the accepted scoped result. No barrier escape or
P-versus-NP conclusion is claimed.
