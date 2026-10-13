# Conclusion: full symmetrization with the original degree semantics

Approval night: 2026-10-13 JST. State: formally-verified under the recorded
Lean assumptions. Independent human semantic review: pending.
Novelty: not established; reconstruction and integration of standard tools.

## Completed milestone

For arbitrary finite arity n, a finite family of genuine GF(2) polynomials
with normalized nonnegative REAL probabilities can be fully symmetrized
without increasing actual polynomial degree or worsening its pointwise
success guarantee for a symmetric target. The same construction turns a
bound on every full permutation orbit into a pointwise certificate.

The exact success identity and full permutation invariance are proved.
feasible_iff_orbit_average connects orbit certificates to the repository's
unchanged HasProbabilisticDegreeAtMost definition. One fixed family precedes
all input quantification; probabilities are not field coefficients.

The construction is applied to the existing n=6/n=7 MOD3 results without
assuming their feasibility as a new premise. Three counterexample components
are also kernel-checked. This completes the generic permutation/full-group
symmetrization stage, not the next Hamming-layer counting stage.

## Actual verification

Final code commit: ac61ba1b2888de029b8fc567187ff3a4dbb263c0.
[Formal run 38414011388](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38414011388),
job 115353465722, completed successfully. The actual logs show pinned
Lean 4.35.0-rc4, Mathlib 9e6b3aac99b624d10c84653ab9c5357283b9b3b8,
--wfail success, all 205 namespace declarations within the foundational
allowlist and all 21 explicit symmetry targets depending only on propext,
Classical.choice and Quot.sound. The report is an attributed excerpt of
retrieved output, not inferred from source inspection.

The earlier core-only proof passed run 38412149245/job 115346960273 at
c1ff9c8639e9aef0a83f9492f087934085fd5c83, with 188 declarations and 16 targets.
The final application repair does not change either core source file.

[Semantic run 38412385402](https://github.com/yo4e/PvsNP-Cartography/actions/runs/38412385402),
job 115347783200, passed at b2602bb5269bdbbda85cc1fc57610bd0208c2a72.
Its normal and optimized Python outputs match local reproduction and contain
the exact core source hashes used by the final formal result. The application
file was added later; do not describe this earlier semantic run as occurring
at the final code commit. Its mathematical countermodels cover those examples.

Re-fetched source/commit evidence:

- PermutationTransport.lean: 8bb3a9eddf18d81e382d956ea395b8592ca54bb2.
- FiniteSymmetrization.lean: 42685e01f5c65442164615ffc39d8f76230aad2c.
- SymmetryApplications.lean: 69d079fcfbe128b400976d4facce8f5cfb5ae803.
- audit.py: f690d417f64b82cbfba8327b3241d18aad3dfefc.

These blobs agree with locally inspected bytes. The final commit/tree and
actual successful CI steps and logs were retrieved separately.

## Replication and falsification

The exact checker exhausts all 278 squarefree polynomials and 278 Boolean
score tables for n=0 through 3, checks higher exponents and nonuniform
mixtures, and rejects four malformed probability/group inputs. It contains
no assert-based safety checks, so python -O produces the same result.

For the previous n=7 certificate it literally renames 18*5040=90,720
polynomial/permutation pairs, retaining multiplicities in 2,524 distinct
polynomials. All 128 inputs satisfy the transformed guarantee. Success by
Hamming weight is [2/3,2/3,2/3,11/15,2/3,2/3,2/3,2/3]. The minimum stays 2/3;
this is not an improved worst-case error or a new degree value.

Seven invalid shortcuts have concrete countermodels in graveyard/007:
missing target symmetry, whole-cube averaging, inverse pullback, cyclic
subgroups, nonbijective renaming, functional versus actual degree, and
coefficient-field averaging. Only the three components explicitly named
in statement-audit.md are separately encoded in Lean. No claim that all
seven are individual formal theorems is made.

Two implementation failures were repaired without weakening statements:
the initial core build selected the wrong sum_comp overload; explicit
Equiv.sum_comp fixed it. The first application build left characteristic-two
arithmetic unresolved; decide +kernel proves the field constant before
rewriting the division. Both failed commits remain in history.

## Remaining frontier and blockers

No GitHub write blocker or unapplied patch remains. Local Lean was unavailable;
actual formal execution used the existing GitHub Actions workflow. Independent
human semantic review and a second proof kernel were not supplied.

Next prove the general identity between a full permutation-orbit average and
the uniform mean on a Hamming layer, including coverage and equal fiber
multiplicity w!*(n-w)!. Then connect the existing n=8 certificate through that
interface. That identity was checked on finite data here, not proved in Lean
for arbitrary n. It must not be silently treated as a completed premise.

Complete numerical MOD3 degree equalities in Lean remain n=5,6,7. n=8 has its
previous exact Python certificate only. No all-n MOD3 degree bound, support
minimality, novelty, asymptotic circuit lower bound, barrier escape or P-vs-NP
conclusion is asserted. See prior-art.md and barrier-audit.md for exact scope.
