# Expedition 025: the actual agreement bound and real-mixture consequence

Research lead: 月野テンプレクス. One freshly approved 2026-10-24 night session,
executed after midnight on 2026-10-25 JST. The conversation failed to deliver
its final response, but the research commits persisted. On 2026-10-25 morning,
the same conversation resumed for recovery, verification and completion records.
This is not a second nightly authorization and implies no background work.

## Mathematical milestone

For any field K, natural n,d, nonzero a,b and actual polynomial R of total
degree at most d, let H be the actual set of y in {a,b}^n where
R(y)=product_i y_i. We now have the Lean-accepted bound

  |H| <= B(n,d) = sum_{j=0}^{min(n,floor((n+d)/2))} choose(n,j).

This is not a rank condition assumed as a premise. AgreementDimension constructs
power interpolation on the two-point grid, bounded squarefree evaluation spans,
product Lagrange indicators and interpolation of every function on H. Reusing
TwoPointCompression compresses all squarefree monomials into the low-degree
span; finite-dimensional counting then supplies the displayed inequality.
The power reduction is evaluation-level, not a claimed executable polynomial
normalizer. Actual MvPolynomial.totalDegree controls the support bound.

The original construction uses a!=b, but AgreementConsequences additionally
handles a=b: the actual grid is then a singleton and B(n,d)>=1. Thus distinctness
is not necessary for the cardinality conclusion itself. It IS needed to count
2^n distinct inputs in the probability consequence. This corrects an overstrong
necessity statement in the preceding exposition, rather than weakening the target.
Empty H, n=0, either threshold parity and d>=n require no extra exclusions.

## Continued result beyond the deterministic bound

For any fixed finite family of actual degree<=d K-polynomials and arbitrary
nonnegative REAL weights summing to one, total correctness over the actual grid
is <=B(n,d). If a!=b and every input has success>=eta, then

  eta * 2^n <= B(n,d).

The family and probabilities precede all inputs. Coefficient arithmetic in K is
not confused with probability arithmetic in R. Signed or input-dependent weights
are not silently admitted. The row scores are derived from the actual agreement
theorem, not assumed. These real-mixture endpoints are also Lean accepted.
Their target is the coordinate product, NOT yet the original GF2 MOD3 predicate.

## Actual acceptance and independent implementations

Formal source 8e5be8ce59b069c278ec32839552dad712de04e1, completed SUCCESS
run40108908554/job120916298894: pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9057 jobs,812 namespace declarations inside unchanged
[propext,Classical.choice,Quot.sound],21 new explicit reports. During recovery,
the completed state, full decoded output, two actual modules and matching Git
commit/tree were re-fetched and inspected. See ci-evidence.md and axiom-report.txt.
No source sorry/admit/new axiom/native_decide or warning-policy relaxation was
introduced. This is the existing kernel, not a second kernel or independent review.

Exact source a62add7e08387a4231f7092f108b59964a00feca passed completed
run40107805754/job120913025271. Its full actual log confirms normal/-O byte
identity and actual/stored JSON equality. The script/result blobs at that source
match those retrieved at recovered HEAD c9a92948. Controls cover 11,910 affine
and constant polynomials in 140 configurations over GF3/GF4/GF5,971 independent
rank controls,22,230 reduction evaluations,3,230 Lagrange indicators and684 power
interpolations. These same-author separate implementations corroborate, but do
not prove, the general theorem. The Lean theorem never imports Python ranks.

## Attack and repair

R=0 on {0,1}^3 gives seven agreements instead of the invalid nonzero-free bound
four. Input-dependent constants give eight instead of four. On a one-dimensional
nonzero grid, signed normalized constants with weights [1,1,-1] give apparent
success one despite the valid probability bound one-half. Graveyard040 preserves
these shortcuts and the distinctness correction. Graveyard039 preserves three
failed formal candidates and faithful repairs; a partial warning-failing build
is not accepted evidence. Recovery inspected the retained failure record, not
new downloads of every historical failure log.

## Decision and precise next frontier

Issue18's actual agreement-dimension milestone is complete. Issue19 targets the
actual GF2 MOD3-to-GF4 product transport already derived in next-bridge.md.
Two residue restrictions can use the SAME sampled polynomial index; the real
union bound gives success>=1-2delta without independence between the residues.
The GF4 linear encoding preserves degree D, not 2D. Actual field construction,
polynomial restrictions, embedding and affine substitution remain to be formalized.
This written continuation is not itself a Lean-accepted transport theorem.

Independent majority15 draws remain a separate requirement. Consequently the
n>=299 degree-two exclusion from Expedition024 is still an author-reconstructed
candidate, not end-to-end Lean acceptance, independent review or an optimal
threshold. Exact degree2 n5..11 and affine exclusion n>=7 remain unchanged;
unrestricted n12 degree is unresolved. No novelty, new circuit lower bound,
proof-barrier escape or P-vs-NP result is asserted. Review tracks #8/#15 retain
their separate, older scopes. No permission blocker or unapplied patch was
encountered in recovery. Local Lean remains absent; actual execution used Actions.
