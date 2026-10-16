# Expedition 013: eight-orbit n=10 MOD3 finite witness

Date: 2026-10-16 JST, same approved nightly session. Starting point:
Expedition011's fully verified n9 proof, and Expedition012's scoped failure
of 8520 single-orbit <=3-block n10 quadratic polynomials.

## Target
Construct ONE input-independent, normalized distribution on GF(2)
degree<=2 polynomials for n=10 MOD3 with pointwise success>=2/3,
and refute all degree<=1 mixtures by a universal dual.
The explicit n10 Lean instantiation is a separate remaining step.

## Method
Use the exact 8520 row profiles from the earlier restricted scan as
candidate columns of a 11-layer maximin LP, with SciPy only to suggest
supports. Its 3368 distinct success profiles admit a numerical solution
at about0.71184 with eight positive blockwise orbits. Round to the
coarse integer weights **[10,2,39,22,15,6,4,2]/100**, then accept
only after a complete *exact* 11-layer rational check.

A second checker expands the eight selected group orbits into1740
indexed polynomials (repetitions allowed) with integer denominator252000
and evaluates every one of the1024 inputs. Independent field-mask and
block-count evaluations agree. Simultaneously the dual puts input mass12
at weight1 and1 at weight3, total240, checking all2048 affine rows
and a Walsh plus hypergeometric reconstruction.

All source data live in certificate.json. Run verify.py --full in normal
and Python -O modes. CI success and a trusted source hash are prerequisites
for describing saved finite verification.

## Scope
A set of single-orbit candidates can all fail even though their convex
mixture succeeds. This is NOT a contradiction. Candidate LP numeric
coefficients and infeasibility statuses prove nothing by themselves.
This n10 result is exact bounded evidence; unlike n9, its concrete
degree equality has **not yet been separately checked in Lean**.
Support minimality, novelty, and any n>=11 claims remain unknown.
