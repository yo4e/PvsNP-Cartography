# Expedition018: faithful n11 MOD3 degree interface

Status: candidate; no n11 formal acceptance yet.
Approved session: 2026-10-20 JST. Investigator: 月野テンプレクス.
Base: 3b6eaff5e567143a79bca096eb5f3eb305f424da. Current open gates: #8 and #11.

Read AGENTS.md, all five mandated documents, current open Issues, recent commits,
and logs/2026-10-18-night-verification-and-subsets.md. n10 is already formally
verified at production1739ccfa; #10 is completed. Do not repeat that repair.
The earliest unblocked task is #11, not the human-review requirement in #8.

## Target

Prove HasProbabilisticDegreeAtMost for GF(2) MOD3 on exactly11 variables at
error1/3, then degree-one impossibility, feasible_degree_iff, IsLeast and numerical
pdeg_eq_two. Use genuine MvPolynomial.totalDegree and normalized nonnegative REAL
probabilities, choosing one finite polynomial family BEFORE every input.

Use the existing three-seed/full-permutation witness, not an unproved quotient
transport: coefficient rows (0,0,0), (1,2047,38605195639935),
(1,1920,1151998655551), lexicographic55 edges, triple weights[3,12,6]/21.
All12 layer totals must be discharged, with threshold14. The lower dual is
15 per weight-one input and1 per weight-three input, denominator330, bound207.
Prove coefficient permutation coverage and apply structural degree-one normal form.

## Verify and attack

Independently reconstruct coefficients by low-weight truth queries and compare
explicit monomial evaluation with subset-count formulas on all2048 inputs.
Recheck all4096 affine rows, direct and Walsh scores, canonical-orbit coverage,
all12 layer totals and altered-coefficient controls. Test omitted symmetry and
incorrect denominators. Run pinned Lean --wfail, namespace allowlist and explicit
target axiom reports, then re-fetch actual Git files/commits and completed output.
No success is inferred from theorem-shaped source or a green recorder job.

## Environment and scope

Local github.com DNS fails and lean/lake are absent. Connected GitHub is the
repository interface and Actions is the available formal execution environment.
This first useful record also tests actual write capability; no paid resources
are requested. Preserve failures in graveyard and keep #8 human review separate.
No novelty, optimal support, all-n MOD3 bound, circuit lower bound, barrier escape
or P-vs-NP conclusion. This approval authorizes only the present session.
