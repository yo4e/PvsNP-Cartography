# Current checkpoint: a growing-degree obstruction for original MOD3

Freshly approved session executed2026-10-29 JST. Research lead 月野テンプレクス.
**Issue21 is CLOSED; Issue22 is the next bounded mathematical frontier.**
Fresh approval is required for later nightly work. Dated README/direction and
old Issue bodies are history, not instructions to restart completed work.

## Accepted mathematical change

For all natural n,d,

 (16*d+2)^2+2 <= n ->
 not HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1/3) d.

This is the ORIGINAL GF2 predicate: genuine totalDegree<=d, a fixed finite
family with arbitrary nonnegative REAL weights summing to1 chosen before every
Boolean input, and success>=2/3 pointwise. No chosen support, rational weights,
assumed multilinearity, prefix inequality or amplified-success premise is added.

CentralBinomialBound proves a uniform central-coefficient square invariant;
BinomialPrefixBound handles the ACTUAL capped prefix and both parities;
Mod3GrowingDegree connects the new3/4 estimate to accepted independent majority,
actual GF4 transport and zero restrictions. The contrapositive states that any
feasible d requires n<(16d+2)^2+2. Each fixed degree is excluded eventually.
This is a deliberately loose known-method reconstruction, not an optimal bound.
The older n>=299 quadratic exclusion is stronger at d2 and remains intact.

## Actual execution evidence

Accepted source5c056776003e4d0d32b0302ed14a6b22cc51ed39,
tree7aaa8b09de46588012216624bad08f95546e6580. Completed SUCCESS formal
run40846564926/job123355388833: Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9068 jobs,1023 namespace declarations within unchanged
[propext,Classical.choice,Quot.sound],20 new explicit reports plus earlier reports.
Completed steps, full decoded actual output,3 actual modules and Git commit/tree
were re-fetched and inspected. Local source blob hashes match. No source
sorry/admit/new axiom/native_decide or warning waiver was introduced.

Exact source6274a1353aa4aa6e2951c6e8042fe6ad4e3617fd passed
run40845239250/job123350996466; normal/-O bytes and actual/saved JSON agree,
including local reruns.12705 prefixes,74305 coefficients and27 larger boundary
checks corroborate rather than prove the universal theorem. Expedition028
contains proof, statement/barrier audits, actual excerpts and ci-evidence.md.

Three implementation failures and repairs are in graveyard045. Graveyard046
contains four false auxiliary estimates: omitted even central atom, unjustified
stronger invariant, linear instead of square size, and missing size hypothesis.
The even-center negative control also passed Lean. Earlier parity gap failure
at n299->n300 remains in044; this theorem does not revive numeric monotonicity.

## Next: Issue22, actual randomized gates and shared DAG circuits

Construct genuine GF2 OR/AND approximators from independent linear hashes,
prove pointwise error2^-r and actual composed degree<=rD, then connect a
specified shared DAG with S AND/OR gates and nonlinear path-depth h to
polynomials of degree<=r^h and error<=S/2^r. Under3S<=2^r, combine with the
accepted lower bound to obtain the explicit restricted-model MOD3 consequence.
Do not assume circuit approximability as a premise or silently unroll sharing.

Expedition028/next-frontier.md and check_gate.py contain the written continuation.
The5058-family/74958-evaluation gate check passed LOCALLY with normal/-O equality;
it is not in the completed prefix CI, a generic proof or Lean-accepted code.
Graveyard047 preserves reused-hash, affine-constant and actual-degree shortcuts.

Earlier exact degree2 n5..11 and affine exclusion n>=7 remain unchanged. General
n12 degree and the generic circuit bridge are unresolved. No novelty, optimal
constant, new unrestricted circuit lower bound, barrier escape or P-versus-NP
result is claimed. No new-code independent semantic reviewer or second kernel
was used;#8/#15 retain older review scopes. Normal caching was used; committed
execution text contains labeled excerpts, not full raw archives.

No write blocker or unapplied patch remains. Local Lean/lake were absent and
local Git read failed DNS; connected Actions supplied formal execution. Previous
complete status is archived at history/2026-10-29-pre-growing-status.md by its
identical blob5db197a2abf397a663cd0ce2649a7d41ccd32605.
Session log: ../logs/2026-10-29-growing-degree.md.
