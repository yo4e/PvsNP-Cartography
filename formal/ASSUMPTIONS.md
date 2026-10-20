# Formal assumption ledger

## Current checkpoint: generic balanced affine obstruction, 2026-10-21 JST

Numerical MOD3 exact degree2 equalities cover n5..11 over GF(2), pointwise
error1/3. A new structural theorem additionally excludes degree<=1 for every
integer n>=7. It uses the original actual MvPolynomial.totalDegree predicate,
normalized nonnegative REAL probabilities and one finite family before every
input. It is not a degree2 upper bound for arbitrary n.

## Actual accepted production execution

- Code dc58ea7dd4d3e2ed36ca5b7d8276de651d95aa08.
- Tree17bb48e8d3c1e44db10fa09cc30934ae7abd1355.
- [SUCCESS run39510465687](https://github.com/yo4e/PvsNP-Cartography/actions/runs/39510465687), job118929907745.
- Pinned Lean4.35.0-rc4, Mathlib9e6b3aac99b624d10c84653ab9c5357283b9b3b8.
- Root --wfail build9048 jobs;589 namespace declarations and29 explicit new
  targets use only [propext,Classical.choice,Quot.sound]. Previous numerical
  and algebra targets also completed. No project-specific axiom or recovery
  placeholder was accepted. Warnings were repaired rather than suppressed.

The completed status and full actual job log were inspected. All four source
files and matching Git commit/tree were then re-fetched. Actual timestamped
output is in [Expedition020/axiom-report.txt](../expeditions/020-balanced-counting/axiom-report.txt);
source correspondence is in [ci-evidence.md](../expeditions/020-balanced-counting/ci-evidence.md).

| New source | Re-fetched Git blob |
|---|---|
| BalancedAffineCounting.lean | 48ce5f97ed03856c17554d524bd4b23ec1a63442 |
| BalancedAffineObstruction.lean | 8384c6e245ef779a580ea9ceb3618d3a8fbd92c0 |
| BalancedAffineBinomial.lean | 4e30d4ea65187121efaf1857541409373e05d2d3 |
| BalancedAffineInputMeasure.lean | ff01e87a09444e9d8fdeca61c9cec27bb471fe62 |

## Faithful mathematical chain

For n>=3, sampleMass is a normalized nonnegative REAL measure on singleton
coordinates plus ordered triples. Distinct triples get mass1/(2n(n-1)(n-2));
repeated-coordinate triples get zero. sampleInput maps to actual Boolean inputs.

The generic finite real identity S^3-3QS+2R is proved structurally. It supplies
the triple count and, for coefficient signs1-2b_i, the actual affine score.
Original affineValue/target evaluation is rewritten before the sign identity
is applied. The target remains1 iff integer Hamming weight is divisible by3.
For coefficient weightk, the constant-zero score is
1/2+(n-2k)*(n^2-(n-2k)^2)/(4n(n-1)(n-2)); constant-one score is complementary.

Pascal induction proves choose2 and choose3 cast identities including small
sizes. Actual singleton success count is n-k, and ordered-triple success count
is6*(k*choose(n-k,2)+choose(k,3)). actual_score_binomial links the binomial
expression to actual weighted correctness, not a freely defined surrogate.

For each n>=7, the common bound
B(n)=1/2+(2n^3/5)/(4n(n-1)(n-2))<2/3 covers all coefficient rows and constants.
Structural degree_one_eq_affine then covers every actual totalDegree<=1
polynomial, and existing finite_dual_obstruction covers any finite REAL mixture.
The final no_degree_one_family and degree_one_impossible assume neither the
score identity nor the desired conclusion. The final predicate is unchanged.

inputMass is also explicitly defined on the actual cube by summing all sample
fiber masses. Its positivity, normalization and expectation transport for ANY
real function are proved. Injectivity is not required and duplicates are not
silently discarded. polynomial_input_bound supplies the actual-cube bound.

## Precisely separated residual

The separately named closed point-mass formula (half uniform on weight1 and
half uniform on weight3) is not yet a compiled fiber-cardinality theorem.
#13 tracks that representation interface and further Hamming-layer intersection
counting. It is NOT a premise of the accepted sample, pushforward or obstruction
proof. #12's core objective is completed via this valid alternative representation.
The actual n6 balanced-dual tightness is formally checked; its equality2/3
refutes only this measure's strict gap at n6, not previous n6 degree results.

## Complementary evidence and failures

Exact code317784842f82b6a1991db664ddd3734d08f72985 passed run39507686566/
job118920623125. Full log and normal/-O byte equality plus actual/saved JSON
equality inspected; source, output and commit/tree re-fetched. Checks cover1093
moment vectors,3031040 affine/input evaluations n3..12 and33147 formula cases
n3..256. These finite tests were not used as an all-n formal proof.

Five candidate builds failed before final acceptance: a34c3775, e96df58e,
cf15c55f (dependent failed prefix),290fd53c,6d91476a. Four primary full failure
logs were inspected; the dependent run's failed metadata was inspected without
claiming its full log was read. Graveyard022..024 preserve precise implementation
failures and faithful repairs. Graveyard021 preserves false diagonal/fiber
accounting with exact counterexamples. No failed source recovery placeholder,
queued workflow or green finite checker was mistaken for formal acceptance.

## Reproduction and remaining gates

From formal/: lake build --wfail; ./scripts/axiom_report.sh. The production
workflow additionally audits the compiled namespace. Local Lean was absent;
actual formal execution used Actions. #8 independent human semantic review
remains open. A second proof kernel and novelty assessment are not provided.

Earlier accepted n11 source9733d800/run39380310454 and pure algebra source
dde6151a/run39381768668 remain unchanged. The earlier496-row n11 quotient is
still separately finite data, not automatically a formal quotient theorem.
The current generic lower obstruction is a useful reusable proof, not a claim
of novel asymptotic complexity, an all-n degree2 upper bound or a P-vs-NP result.

## Preserved historical ledger

The immediately preceding ledger is archived byte-identically as
[2026-10-21-pre-counting-ledger.md](reports/2026-10-21-pre-counting-ledger.md),
Git blob02ca1e5a4391ec986a4eb93a08dd5fb2cd9354a0. It retains n5..11 evidence,
algebra acceptance, all older archived ledgers and prior failures. Old pending
statements are historical. No proof or failed direction was deleted.
