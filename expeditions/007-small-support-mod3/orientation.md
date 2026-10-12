# Expedition 007: small-support MOD3 witnesses and the n=6/n=7 degree interface

Date: 2026-10-13 JST. Roles: cartographer, explorer, experimentalist, formalist,
skeptic, archivist, all performed by 月野テンプレクス in one approved session.
These role changes do not constitute independent human review.

## Starting point

Read AGENTS.md, its five mandatory documents, open Issues, recent commits,
logs/2026-10-11-night-degree-interface.md and the formal source dependencies.
Starting main was 0772e621e1ab5686877be257b58b2410b8c3df11. Issue #8 was the
only open issue and identified n=6/n=7 formalization as the earliest unblocked
frontier. The complete n=5 theorem and generic structural normal form were
already verified; rebuilding them would not advance the frontier.

Expedition002 supplies exact finite n=6/n=7 certificates. The previous
n=7 upper witness uses eight full permutation orbits. Our bounded target is
the genuine degree-based equality at n=6 and n=7, with exact certificates small
enough for kernel computation, not a numerical optimization or general-n claim.

## Acceptance conditions

Produce one input-independent finite REAL distribution on actual GF(2)
polynomials of degree <=2 with pointwise success >=2/3. Rule out every degree
<=1 family using the structural normal form and a fully covered finite dual.
Connect both bounds to feasibility iff 2<=d, IsLeast and a closed numerical
degree equality. Build with pinned Lean/Mathlib, --wfail, namespace axiom audit
and actual #print axioms. Re-fetch sources, commits and successful job output.

Independently structured executable checks must compare all Boolean inputs,
field evaluations and polynomial coefficients, reject damaged data, and work
with Python assertions disabled. Preserve failed compression directions with
actual counterexamples. Keep novelty and independent review status separate.

## Candidate discovery and proof separation

search.py uses SciPy linprog and bounded MILP to find small cyclic mixtures.
The exploratory environment used Python3.13.5 and SciPy1.17.0. Solver support
choices and timeout outcomes are not trusted, and may vary across versions.
The actual witness is the fixed certificate.json, interpreted by audit.py
with only the standard library, then by the Lean source independently of SciPy.

The surviving construction has four symmetric polynomials and two seven-row
cyclic orbits, eighteen distinct polynomials and24 tickets total. n=6 is
obtained by zero restriction and is also verified separately over its whole
cube. One cyclic orbit with fixed twelve-ticket masses fails exhaustively.
See graveyard/006-single-cyclic-orbit.md and the complete audit output.

## Reading order

statement-audit.md gives exact quantifiers and semantic boundaries;
barrier-audit.md limits the relation to complexity barriers;
log.md records the executed loop; conclusion.md records only the verification
actually observed. No independent semantic reviewer or second proof kernel
is supplied by the experiment.
