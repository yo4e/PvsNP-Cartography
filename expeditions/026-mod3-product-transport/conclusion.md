# Expedition026: the original MOD3 problem now reaches the agreement bound

Research lead 月野テンプレクス. One fresh approval, execution2026-10-27 JST.
Issue19 is CLOSED as completed; Issue20 names the next mathematical frontier.
This record does not authorize further nightly work.

## What mathematical uncertainty changed

The previously verified bound concerned the coordinate product over a two-point
field grid. We have now derived its required hypotheses from the ORIGINAL GF2
MOD3 probabilistic-degree predicate, using actual polynomials and a concrete GF4.
The theorem constructs the coefficient embedding, two constant restrictions,
linear root encoding and inverse affine input substitution without increasing
total degree. The same polynomial index and original finite nonnegative normalized
REAL weights are preserved. Correctness is derived by a union bound, not assumed.

For all m,D and real delta, original MOD3 on m+2 inputs approximable at error
delta and degree D implies

 (1-2delta)*2^m <= sum_{j=0}^{min(m,floor((m+D)/2))} choose(m,j).

The final necessary_inequality assumes only the original approximation predicate,
not root existence, transported success, a rank bound or a lower-bound theorem.
The Boolean/grid maps are proved inverses. No squarefree or rational-weight
restriction on the original family is hidden in the statement.

## Continued closed application

seven_small_error_impossible proves that seven-variable MOD3 has NO fixed finite
nonnegative REAL mixture of actual GF2 polynomials of total degree<=2 achieving
pointwise error<=1/12. Its numerical contradiction is26<80/3, checked by Lean.
This is a smaller error than1/3 and does not contradict earlier n7 degree2
feasibility at error1/3. It is not an optimal threshold or novelty claim.

## Verification, attack and repair

Accepted source5acf085fa43f1fa4578252c1653033d3f523e753, completed SUCCESS
formal run40430504329/job121946718143: pinned --wfail9060 jobs,875 namespace
declarations within the unchanged foundational axiom allowlist,23 new target
reports and all old reports. The completed steps, full decoded output, actual
sources and matching Git commit/tree were re-fetched and inspected. Local source
blob hashes match GitHub. ci-evidence.md and axiom-report.txt preserve provenance.
This is actual Lean acceptance, not a second kernel or an independent reviewer.

Exact run40430504271/job121946717619 at the SAME source passed normal/-O and
saved/actual equality, with local reruns agreeing:3680 actual polynomials and
18304 input evaluations, plus nonuniform mixtures and independent arithmetic
implementations. These finite checks corroborate but do not prove the universal
statement. No Python result is imported into the Lean proof.

Graveyard041 preserves genuine polynomial counterexamples: each padded answer
can have success2/3 while their same-index joint answer succeeds only1/3, not the
invented independence estimate4/9. Signed normalized weights[2/3,2/3,-1/3] can
have apparent source success>=2/3 everywhere but transported success0. Wrong
padding, root coefficients and substituting ZMod4 for GF4 also fail. These are
failed extensions, not an optimal degree/error classification.
Graveyard042 preserves the first real build failure and faithful repair. No
mathematical statement, warning flag or axiom policy was weakened to obtain green.

## Decision and remaining frontier

The bridge alone is too weak at error1/3, because B(m,D)>=2^(m-1) for m>=1.
Thus #20 targets actual independent majority15 amplification, its degree8
composition and real product-measure error bound, then the exact m297,D16
contradiction and restriction to all n>=299. This is a named end-to-end use,
not an open-ended framework or automatic n13 enumeration. Reusing the same index
for residue restrictions is valid; repeating one draw15 times is not amplification.

The n>=299 original error1/3 quadratic exclusion is STILL an author-reconstructed
candidate pending that missing chain. General n12 degree is unresolved. Earlier
exact degree2 n5..11 at error1/3 and affine exclusion n>=7 remain unchanged.
No novelty, optimal threshold, new circuit bound, barrier escape or P-vs-NP
conclusion is asserted. #8/#15 retain separate older review scopes. No independent
semantic reviewer or second kernel was used for this code. No write blocker or
unapplied patch remains. This is the natural milestone ending this approved session.
