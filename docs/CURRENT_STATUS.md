# Current checkpoint — growing cross and coefficient-labelled proof rows

November 24, 2026 JST. Expedition 046 parameterizes the designed one-level
cross compiler, reproduces the exact GF(128) census and generates GF(512).
For s=2^a, k=2a+1, the written all-assignment argument gives
V_NO=2s^2-2s-3, sigma=3s-1; compact Q lies between Omega(s^4 k) and
O(s^5 k^2). The actual two cubes are 2^22 and 2^27, with NO minima
109/477, sensitivity 23/47 and arbitrary-bit radius 4/10.
This is not a general recursive verifier census.

The named compact honest references have exact and budgeted minimum degree
17 and 20 over free padding. Direct odd-parity certificates in wholly used
subcubes force at least 16 and 64 wrong bits at one lower degree.
A new injective coefficient-tag layout reduces the exact degree to 15 and
16 at 16x/64x address-cube cost; GF(512) also has an unequal-prefix
completion of degree <=17 at 16x cost. The basic written family scheme
achieves degree O(log k) at Q'=O(s^7 k^2) for the explicit known reference.
The approximation rate worsens, and the layout depends on the honest row
signatures. It does not apply automatically to unknown witnesses.

A fixed-layout counting obstruction for unrestricted independent constant
rows shows why the universal low-degree generalization fails. It does not
exclude structured satisfying proofs. Shared-field and inverse-sibling
attacks were replayed. Code [6d632a3e](https://github.com/yo4e/PvsNP-Cartography/commit/6d632a3e5392bde5fc4b005d4790e52747f8e47e)
was re-fetched at its immutable commit and executed in V8 with exact full
JSON readback equality. The direct parity and gate-charge checks are recorded.
No new CI or Lean run, independent external review or novelty claim.

[Conclusion](../expeditions/046-growing-cross/conclusion.md) ·
[Derivation](../expeditions/046-growing-cross/derivation.md) ·
[Execution evidence](../expeditions/046-growing-cross/execution-evidence.md).
#35's scoped milestone is complete. Next frontier [#36](https://github.com/yo4e/PvsNP-Cartography/issues/36):
witness-independent structural encoding of a nontrivial proof family or
a precise obstruction. #8 and #15 are unchanged. No P-versus-NP separation.
This checkpoint does not authorize another nightly session.

# Previous checkpoint — sparse A reads and four-error precision

November21,2026 JST evening. Expedition045 replaces the whole-A membership
check with23 fixed offsets forming the union of complementary binary
subspaces. Every two passing stars overlap twice, so one affine polynomial
explains all A values used at accepting seeds. Together with the unchanged
shared B recovery this retains the exact NO raw minimum109 over arbitrary
field/gate/copy/public assignments.

The actual cap21 compiler has exact uniform unrestricted signed sensitivity23
and the same padded Q=4,194,304 for YES and NO. Its strict uniform-error
threshold109/96,468,992 improves the previous cap126 budget by128/23, and
any four physical YES-bit errors yield at most92 failed pairs, below the
NO minimum109. This removes the old automatic zero-error quantization
obstruction. It does not construct a useful low-degree approximant or
transport the old encoded proof function's approximation guarantee.

Eight- and29-offset Hamming-ball alternatives were attacked with globally
consistent noncode A and honest shared B tables. They admit106 and108
NO-rejection witnesses; carrying over109 from their exact affine kernel
would have been false. The selected cross rejects those splices128 and124
times. Their counterexamples and the graph certificates for surviving weaker
bounds remain in the expedition and graveyard.

A direct algebraic audit distinguishes padding from approximation error.
The named honest YES proof with zero-filled padding has exact GF(2) degree
18 on 22 address bits. Its used addresses form a downward-closed prefix.
Deleting ANF coefficients outside that prefix preserves all queried bits
and supplies a degree 17 completion. This is optimal over every padding
choice: the fully fixed 21-dimensional subcube x21=0 has degree 17, so
every degree 16-or-lower polynomial makes at least 16 errors on used bits.
That also excludes every fixed mixture at the strict 109/23 mean-error
budget. Thus both exact and budgeted minimum degree over padding are 17
for this named physical proof. Other satisfying proofs and growing-family
degree costs remain unresolved. [Zero-padding audit](../expeditions/045-sparse-affine-reads/degree-notes.md)
· [Completion](../expeditions/045-sparse-affine-reads/padding-notes.md)
· [Padding-independent bound](../expeditions/045-sparse-affine-reads/padding-bound-notes.md).

The designed one-level family has a written extension with s=2^a,
V_NO=2s^2-2s-3 and canonical reader load3s-1. Its actual parameterized
compiler census, padded Q_a and low-degree approximation behavior remain
unresolved; only GF(128) is fully compiled here. The full recursive source
family requires its own B recovery and costs. Issues8/15 remain separate.

[Conclusion](../expeditions/045-sparse-affine-reads/conclusion.md) ·
[Derivation](../expeditions/045-sparse-affine-reads/theory-notes.md) ·
[Execution evidence](../expeditions/045-sparse-affine-reads/execution-evidence.md)

[Code 47910b0a](https://github.com/yo4e/PvsNP-Cartography/commit/47910b0aa120794143477268fc02056a72c73b08)
passed completed [run 44912211021](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44912211021),
job 136870212842, Python 3.13.5. All six normal/-O outputs matched; all 39
added/changed files were re-fetched and matched their text and Git blob
hashes. Actual replay output and manifests are archived in the evidence.
Issue 34 is complete. The next research target is
[Issue 35](https://github.com/yo4e/PvsNP-Cartography/issues/35): price the
growing one-level family and the degree of its actual proof functions.

This checkpoint records written arguments and finite executable checks,
not new Lean acceptance, novelty, external review, a general circuit lower
bound or P-versus-NP separation. Fresh approval is needed for another night.

## Previous checkpoint — exact compiler gain and the zero-error obstruction

November 21 JST. Expedition 044 changes the actual GF(128) compiler's exact
unrestricted signed sensitivity from 288 for the named original honest YES
reference to 128. Cap 126 adds 2,603 private copy rows while retaining the same
Q=4,194,304 cube on both YES and NO. The NO raw violation minimum remains 109.
The sharp linear sufficient error budget improves by exactly 9/4 to
109/536,870,912. The old upper bound is a regeneratable true-literal allocation;
the new one is an all-error gate charge with an attaining singleton.

**This finite budget is still below 1/Q.** A deterministic approximant must be
exact. A qualifying polynomial mixture must contain an exact polynomial with
positive probability, so the existential approximation class is not enlarged
for the respective encoded truth function. The retained full-A predicate
forces sigma>=N in the stated private encoding, while V_NO<=N. Private fanout
optimization alone cannot escape this regime. [Proof](../expeditions/044-bounded-fanout/zero-error-regime.md)

The general compiler derivation gives sigma<=max(mu,f+2), preserves the field
NO minimum, and costs at most four times the old cube under explicit canonical
query/private-row hypotheses. Symmetric weighting of shared decision buffers
cannot improve its optimized unshifted baseline; a preserved asymmetric
counterexample limits that statement. These are written arguments with finite
controls, not new Lean or externally reviewed results. [Scopes and attacks](../expeditions/044-bounded-fanout/conclusion.md)

[Code cb7d76f9](https://github.com/yo4e/PvsNP-Cartography/commit/cb7d76f9df7f8fa94cc3194c46afbf9af5de7873)
passed completed [run 44766593485](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44766593485),
job 136392727923, Python 3.13.5. All three normal/-O outputs matched. Actual
commit metadata, all 21 committed files and completed job output were retrieved
and compared. [Session evidence](../logs/2026-11-21-bounded-fanout.md)

[Issue 33](https://github.com/yo4e/PvsNP-Cartography/issues/33#issuecomment-7043941266)
is completed in this scope. [Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34)
is the earliest unblocked research frontier: change the full-A reader burden
while retaining enough NO rejection to reach V_NO>sigma, preferably growing
in a costed family, or justify a smaller degree-restricted error sensitivity.
Exact code-space characterization alone is insufficient. Issues 8/15 retain
their separate review scopes; the full recursive gate census and unpaired
GF(256) optimum remain unresolved. No write blocker or unapplied patch remains.
This checkpoint does not authorize another session.

## Previous checkpoint — dispersed shifts and their Boolean cost

November 18 JST. Expedition 043 reconstructs the packed AGHP sampler, reducing the previous explicit fixed-translation budget by a squared logarithm in the fixed-rate, inverse-polynomial error regime. The exact physical-cell reader multiplicity is at most 2^(2a)+2^a−1, so distinct-call pooling saves only a rate-dependent factor. Packed masks eventually have almost entirely disjoint physical views.

A dense, full-rank, pairwise-separated mask family still permits near-total acceptance of any prescribed root. A separate shared decision-buffer compiler can erase amplified field rejection at one copy violation per original failed decision. These failures explain why the next useful quantity is gamma N/(Q sigma): actual NO rejection over address storage and signed failure sensitivity. Private replication can amortize shared overhead, so no universal compiler impossibility is asserted.

[Expedition 043: exact scopes and four replays](../expeditions/043-dispersed-shifts/conclusion.md) · [November 18 evidence](../logs/2026-11-18-dispersed-shifts.md). [Issue 32 is completed](https://github.com/yo4e/PvsNP-Cartography/issues/32#issuecomment-6970482138); [Issue 33 is the next frontier](https://github.com/yo4e/PvsNP-Cartography/issues/33). For a changed compiler use the actual precision V_NO/(Q sigma_YES), re-establishing its NO violation numerator. [Code60290f6a](https://github.com/yo4e/PvsNP-Cartography/commit/60290f6aea4d57df4708863b456e55386ca1d8c5) passed [run44247492467](https://github.com/yo4e/PvsNP-Cartography/actions/runs/44247492467); all four normal/-O outputs, actual job logs and re-fetched files matched. The packed sampler is prior art. General model-specific deductions are written arguments with bounded controls; novelty, new Lean checking and external review are not claimed. The full recursive Boolean gate census and the secondary unpaired GF(256) optimum remain unresolved. Issues8/15 retain their distinct review scopes. This checkpoint does not authorize another session.

## Previous checkpoint — agreement on accepting root sites

November 17 JST. Under any polynomial-size fixed-translation schedule at constant rate and unbounded depth, one physically shared proof can accept many zeros and a conflicting one. A two-polynomial splice also exceeds the honest outer residual's root cap. At GF(256), 67 joint acceptances are possible on the unpaired designed NO fixture, versus at most 35 for an honest polynomial.

A quantified repair obtains one polynomial on a 1−ε fraction of accepting sites with polynomially many fixed masks for inverse-polynomial ε. The unchanged two-level verifier has sharp uniform rejection-to-distance coefficient 2/3. The base physical-read overlap now has an exact shape formula and grows linearly with seed dimension at fixed rate. Sublinear-rank translations allow near-total acceptance of any prescribed root, including a far word of exact distance 1−2^(−a) and a reciprocal witness for the designed NO residual. This excludes polynomial-size subgroup schedules as a route to constant soundness at unbounded depth. [Next cost frontier, Issue 32](https://github.com/yo4e/PvsNP-Cartography/issues/32). These generic statements are written derivations; the finite witnesses and reconstructions have separate executable checks. [Expedition 042](../expeditions/042-accepted-sites/conclusion.md) · [Verification and frontiers](../logs/2026-11-17-accepted-sites.md) · [Issue 31](https://github.com/yo4e/PvsNP-Cartography/issues/31)

## Previous checkpoint — recursive rejection versus distance

The November 14 JST session gives a positive-distance counterexample to the unmodified bundled verifier for two recursive levels. Over GF(256) it rejects 128 seeds, while every degree-31-or-lower polynomial differs on at least 162 of its 256 root symbols. A second fixed XOR-translated test on the same proof restores sharp rejection at least equal to distance. The general two-level derivation treats both affine and cubic outer columns. On the designed GF(256) field-constraint NO instance the resulting sharp minimum is 221 rejected seeds; a YES witness passes every seed. These counts concern symbol-level public seeds.

Four translated reads also give a written three-level result for rate exponent three and dimensions ten and eleven. The dimension-ten route enumeration covers every seed. For unbounded dimension, the cost of certifying a whole outer row from a single acceptance is exponential; the frontier is a polynomial-cost accepted-site argument. [Scope of this obstruction](../expeditions/041-two-level-distance/whole-row-limit.md)

[Expedition 041](../expeditions/041-two-level-distance/conclusion.md) · [Completed Issue 30](https://github.com/yo4e/PvsNP-Cartography/issues/30#issuecomment-6878101552) · [Next research question, Issue 31](https://github.com/yo4e/PvsNP-Cartography/issues/31) · [Chronological evidence](../logs/2026-11-14-two-level-distance.md)

## Previous checkpoint — a shared recursive verifier

The November 13 JST session generated and checked one recursive level over a translated GF(128) root. On a designed NO instance the sharp minimum is 109 failed physical clause–seed pairs out of 10,717,568. An honest YES witness has zero failures. The physical sharing of parent and sibling cells matters: either detached-copy mutant can accept 127 of 128 seeds on a proof that the joined verifier rejects everywhere. The exact finite witness replay is separate from the written lower-bound argument for arbitrary assignments.

[Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6856525926) is complete in its scoped source-variant and conformance sense. [Issue 30](https://github.com/yo4e/PvsNP-Cartography/issues/30) asks for the two-level rejection–distance tradeoff. A single changed auxiliary cell already shows why the first-level row-wide verdict cannot be reused at the next depth. [Expedition 040](../expeditions/040-recursive-verifier/conclusion.md) · [Session evidence](../logs/2026-11-13-recursive-verifier.md)

## Previous checkpoint — unary counting and a generated base verifier

The November 12 night session produced two generated GF(32) base instances with exact minimum rejection counts 0 and 25 out of 469,056 clause–seed pairs. The occurrence and line-interpolation arguments give costed inverse-polynomial uniform-error implications on infinitely many occupied YES lengths for separately encoded E^NP proof functions. Their status is a written derivation using published theorems. The five finite suites passed on the pinned code; there is no new Lean result.

[Issue 29 is completed](https://github.com/yo4e/PvsNP-Cartography/issues/29#issuecomment-6828212368). [Issue 28 remains open](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6828211809) for the first end-to-end recursive child with shared parent and sibling cells. [Expedition 039](../expeditions/039-unary-overlap-counting/conclusion.md) · [Verification and session log](../logs/2026-11-12-unary-and-verifier.md)

## Previous checkpoint — recursive query fibers

## Expedition 038

The written BV14 variant retains every root seed bit for fixed XOR-offset leaf reads. Seed-pin clauses retain all but one. The remaining transfer compares the density and soundness losses to a sufficient approximation precision; the unary construction avoids conditioning on a general binary instance. The full compiler has not been executed. [Conclusion](../expeditions/038-recursive-query-fibers/conclusion.md) · [November 11 log](../logs/2026-11-11-recursive-query-fibers.md) · [Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28) · [Issue 29](https://github.com/yo4e/PvsNP-Cartography/issues/29)

## Expedition 037

Full XOR-tagged copies preserve the fixed-degree error ratio. In the BV14 report, the parent-membership marker printed in §6.3 is reversed for the row origin displayed there. A one-level coordinate check resolves the convention; the final binary-address fiber bound and adequate fixed-input approximation remain open in [Issue 28](https://github.com/yo4e/PvsNP-Cartography/issues/28). See the [conclusion](../expeditions/037-source-query-audit/conclusion.md) and [nightly log](../logs/2026-11-10-source-query-audit.md).

## Previous checkpoint — fixed global proof and query capacity

Freshly approved 2026-11-10 JST session. Research lead: 月野テンプレクス. **Issue27 is CLOSED/completed; Issue28 is the next source-dependent research question.** Issues8/15 retain their older independent-review scopes. This checkpoint is not authorization for another session.

## Accepted formal result

The actual pointwise GF2 polynomial-mixture predicate now connects to one positive-mass polynomial shared across all signed three-query OR tests. Actual constant/variable/negated-variable substitutions preserve evaluation and degree; the signed OR has degree at most3D. Actual subset-zeta outputs equal the accepting counts, and proved inverse maps connect the head/tail enumeration to the ORIGINAL full randomness cube. The final rational threshold is an exact integer comparison. Soundness explicitly ranges over all global proof functions, not independently resampled answers.

Accepted source **443fc96147b8bd616f82250eeb14c1484510e694**, tree53d6b566eaa773c8b427e40179dbf152db1e74a8. Completed SUCCESS run42728862159/job129541435980: strict --wfail9083 jobs,1594 namespace declarations within unchanged[propext,Classical.choice,Quot.sound]. ModulusAudit has76 named reports/20 explicit signatures, of which33/13 concern the new adapter. Actual source/commit/diff/audit and full completed output were retrieved. This is kernel acceptance and author statement inspection, not independent semantic review, second-kernel checking or a costed executable proof.

The substantive November9 work was recovered from live history despite the missing final chat report. An inherited HTTP504 download failure was followed by actual proof-script diagnostics. Two repairs fixed representation/reindexing without weakening statements. See ../expeditions/035-fixed-proof-adapter/execution-evidence.md and ../../PvsNP-Cartography/graveyard/2026-11-10-fixed-proof-recovery.md (repository-local equivalent: ../graveyard/2026-11-10-fixed-proof-recovery.md).

## Written mathematical continuation, outside Lean scope

Expedition036 derives the finite real-weight capacity criterion for allocating each test's mass to its true addresses: kappa=N*max_S forced_true_mass(S)/|S|. It gives one-global-polynomial expected failure <=kappa*uniform-error. Deterministic selectors lose at most a sharp factor3.

The certificate optimum is NOT the actual signed-error optimum: false literals impose additional constraints. Writing C for the exact unrestricted global-proof error constant, C<=kappa always; for non-tautological width-three clauses the separate written argument gives **C<=kappa<=4C**, with factor4 attained by seven weighted clauses and an actual degree-one polynomial on a two-bit address cube. This quantifies certificate loss, not a runtime speedup or a guarantee for the external PCP construction.

These are author-written finite derivations and exact controls, not independently reviewed or Lean-verified theorems. No novelty promotion is made. Core arguments: ../expeditions/036-query-capacity/capacity-and-transfer.md and sharp-signed-gap.md. Countermodels: ../graveyard/2026-11-10-capacity-optimality.md. Arbitrary projection maps still allow concentrated queries that defeat uniform-average error.

## Completed finite evidence

Code checkpoint **b742079296f15da7790a2e9eb711b89031fea57e**, treefb71bdd7eea96de3bf39eacec5409275e8f70de6, passed completed SUCCESS run42730390055/job129546608938. All four normal/-O/stored-output comparisons and compilation checks succeeded. Inherited adapter controls include9984 exact head counts and25830 threshold comparisons. New capacity tests cover12037 graphs and2151 signed families; the sharp-gap checker covers3146 exhaustive plus200 seeded families and named countermodels. Exhaustive scope is explicitly bounded. Actual new code/results/commit, local hashes and completed remote output were compared. See both expeditions' execution-evidence.md files.

No write/security blocker or unapplied patch remains. Local Git DNS and missing Lean/Lake were bypassed only by the already-authorized connected GitHub/Actions route. No axiom policy or paid-resource setting was changed. Later record commits are not additional mathematical execution evidence.

## Next decision

Issue28 asks whether the ACTUAL projection-PCP construction, or a specified soundness/degree-compatible modification, has a useful query-congestion or signed-error bound. A max-flow on an explicit exponentially large graph is not an efficient succinct selector. True-address sets may depend on the unknown satisfying proof. A useful loss must beat the soundness gap; uniform-average error does not automatically admit pointwise amplification. Inspect source structure before adding generic infrastructure, and park the route if a source-level obstruction defeats it.

External PCP/hierarchy proofs, costed Python refinement, independent semantics and a second kernel remain separate gaps. Earlier MOD3/counting/circuit results and failed uniform-cover usefulness are retained. No E^NP-to-NP substitution, unrestricted separation, barrier escape or P-versus-NP result is claimed.

Previous complete status: history/2026-11-10-pre-fixed-proof-status.md, original blob8d5d6a05334e391bafdb92dcd276623874bc05ea. Previous complete formal ledger: ../reports/2026-11-10-pre-fixed-proof-ledger.md. Session log: ../logs/2026-11-10-fixed-proof-query-capacity.md. Further work requires fresh approval.
