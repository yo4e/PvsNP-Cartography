# Expedition 024: a verified compression core and an explicit unpromoted consequence

Approved 2026-10-23 JST night session. Research lead: 月野テンプレクス.
Issue #17 is complete at its bounded first-substantive-lemma milestone.
Issue #18 is OPEN for the actual agreement-dimension theorem.

## What mathematical uncertainty changed

The hard ingredient is no longer merely an imported theorem name. Starting
from Goldreich's author exposition of the approximation method, we reconstructed
the complement-inverse compression step for arbitrary fields, arities and genuine
polynomials. For nonzero a,b, a polynomial R of total degree at most d, and
n+d<=2t+1, every squarefree monomial agrees on the actual agreement set
H={y in {a,b}^n: R(y)=product y} with ONE polynomial of degree at most t.
The witness precedes the universal input. No agreement count or desired rank
bound is assumed. Actual degree and evaluation are derived from explicit formulas.

This core is Lean accepted at de8913e7c1058844354f376ae8a72a2a2abddfa9:
completed SUCCESS run39964232854/job120449783214, pinned --wfail9055 jobs,
759 declarations under the unchanged foundational allowlist and nine new targets.
Actual source, matching Git commit/tree, completed state and full decoded output
were re-fetched. This is the existing proof kernel, not a second kernel or an
independent semantic review. See ci-evidence.md and axiom-report.txt.

## Continued derivation, with a precise acceptance boundary

proof.md supplies a complete written interpolation, multilinear-reduction and
dimension argument giving |H|<=sum_{j<=floor((n+d)/2)}choose(n,j), with the sum
capped at n and a!=b additionally required. This whole dimension step is NOT yet
Lean formalized. The finite rank checks corroborate it; they do not prove it.

The same document reconstructs a sharper concrete adapter to the original
GF(2), finite REAL pointwise probabilistic-degree predicate. Majority15=e8
has composition degree8d and error delta=422009/4782969. Two restrictions encode
all three residue roots by a linear GF4 combination, without doubling degree.
The dimension bound would force

  1-2delta <= 2^(-m) sum_{j<=floor((m+8d)/2)} choose(m,j), m=n-2.

Exact independent integer calculations contradict this at n299,d2. The ensuing
exclusion for n>=299 is recorded as an AUTHOR-RECONSTRUCTED CONSEQUENCE CANDIDATE,
not an end-to-end Lean theorem or an independently reviewed new result. The
missing formal links are the dimension theorem, generic real-distribution
amplification and actual GF4 transport. No optimal threshold or novelty is claimed.
The previous17-copy bridge is not refuted; this is a different degree-aware use.

## Attacks and a real checker defect

Dropping nonzero grid coordinates is false: R=0 on {0,1}^3 agrees at seven
points, whereas the incorrectly extended bound is four. Wrong inverses on GF4,
equality outside H, excessive rounding, one-bit root encoding and dependent
repetition also fail. Graveyard036 preserves these dead shortcuts.

Two inspected formal failures were implementation failures, repaired without
weakening the statement, field, quantifiers, axiom policy or --wfail. An intervening
source typo was immediately repaired; no uninspected job outcome is invented.
Graveyard037 retains all these distinctions.

The first Python rank routine passed its structured tests and CI but was WRONG:
rebinding a row inside enumerate(row) used stale pivots. Explicit2x2 examples
showed both undercounted rank and invented pivots. Its old green run39964233049
is quarantined as rank evidence. Graveyard038 records the defect and repair.

Accepted finite evidence uses repaired source531f3a86b602a7a1b272138e55e051279598f28f,
completed SUCCESS run39965200654/job120453135024. All256 GF4 2x2 matrices are
checked against independent determinants;18020 polynomial-rank cases,53942 actual
compression evaluations,32768 majority truth values and8191 root encodings pass.
Normal/-O outputs and actual/stored JSON agree. Source/result/commit were re-fetched;
local source Git blobs and exact output match. These are separate implementations
by the same author, not a second reviewer. The Lean core never imported Python ranks.

## Decision and remaining frontier

Continue with #18: derive the ACTUAL evaluation-space/cardinality bound from
compression, interpolation and degree-preserving grid reduction. Do not replace
that theorem by an abstract adapter that assumes its decisive rank hypothesis.
The n299 candidate is a concrete mathematical use for this work, not permission
to restart an unbounded numerical staircase. Independent review of its complete
chain would add evidence not supplied by the current formal core.

Numerical accepted exact degree2 remains n5..11; generic affine exclusion remains
n>=7. Unrestricted n12 degree is unresolved. No circuit-size lower bound, proof-
barrier escape, novelty or P-vs-NP conclusion is claimed. #8/#15 retain their
separate old review scopes. No write blocker or unapplied research patch remains.
Parsed author-source text was read; screenshot failures prevent claiming visual
PDF inspection. This is the natural stopping point for this one approved session.
