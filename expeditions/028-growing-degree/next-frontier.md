# Next frontier: actual randomized gate and circuit approximation

Selected by 月野テンプレクス in the approved2026-10-29 session. Research
candidate, NOT Lean-accepted work and NOT future-session authorization.

## Why next

The growing-degree result supplies the lower-degree side of the known method.
What remains is to connect a precisely bounded circuit to actual low-degree
polynomials with the same pointwise, pre-input probability quantifiers.
Primary context: Goldreich ECCC TR23-034r1, Section2.2.1, Lemma2/Claim2.1,
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download .
We inspected parsed text, not a screenshot. The paper uses an averaging step;
retain the randomized construction instead for the repository's predicate.

## First substantive lemma: OR by independent linear hashes

For k inputs and r>=0, sample all matrix entries a_(t,j) uniformly and
independently in GF2. Construct the genuine polynomial

 Q_A(X)=1-product_(t<r)(1-sum_(j<k) a_(t,j)*X_j).

Its actual totalDegree is<=r. For zero input it is identically0. For a nonzero
input z, select any active coordinate j: flipping a_(t,j) pairs the linear
hash's zero and one fibers. Each hash is unbiased and independence across t
gives exact failure2^-r. The whole matrix distribution is fixed before every
input, not selected separately for z. r0 and k0 are valid edge cases. Actual
substitution of degree<=D source polynomials has degree<=rD, not a mere
truth-table interpolant. AND is the dual, NOT and XOR are exact over GF2.

The finite continuation check_gate.py exhausts k0..4,r0..3:5058 matrix families,
74958 input evaluations,124 pointwise laws, comparing unreduced sparse
polynomials with a separate Boolean hash evaluator. Normal/-O local outputs
match gate-checks.json. These local checks are NOT covered by the completed
main prefix-control CI and are not a generic proof or independent review.

## Concrete circuit endpoint to formalize

Use a topologically ordered finite DAG, not a formula expansion that duplicates
shared subcircuits. Specify inputs, constants, AND/OR/NOT/XOR gates, arbitrary
finite fan-in, and actual evaluation. Let S bound the number of AND/OR gates,
and h bound their count along any input-output path. For r>=1, construct one
finite input-independent distribution of actual polynomials with degree<=r^h
and pointwise error<=S/2^r.

For a fixed input x, define each gate's bad event on its deterministic TRUE
input values in the original circuit. Outside the union of these events,
induction in topological order proves all approximated gate values are correct.
This avoids assuming child approximations are independent or falsely summing
errors after an exponential formula unrolling. The union bound over S events
needs no mutual independence; the r hashes within each gate do need it.

With3S<=2^r, this supplies the unchanged original degree predicate at error1/3.
If the circuit computes MOD3, the growing-degree theorem implies

 n < (16*r^h+2)^2+2.

This is a deliberately explicit restricted-model consequence, not an optimal
size exponent, a new unrestricted circuit lower bound, or P versus NP.
The gate semantics, degree induction, finite weights, probability union bound
and original-predicate conversion must all be implemented before claiming it.

## Attacks already executed and next proof checks

Reusing one hash three times gives error1/2 on z11, not1/8. Using an affine
hash with constant1 can falsely accept the zero input. For k1 and three all-one
masks, Q=x+x^2+x^3: its Boolean function is x, but its actual totalDegree is3.
These are preserved in graveyard047 and gate-checks.json; do not erase the
actual degree with an unproved multilinear-reduction step.

Further attacks: empty fan-in, repeated wire references, shared subcircuits,
r0 versus r>=1, arbitrary original input, output polarity of MOD gates, and
negative or input-dependent weights. Reuse accepted probability adapters;
stop at the actual gate/circuit theorem or a localized counterexample rather
than designing an open-ended circuit framework. Fresh approval is required.
