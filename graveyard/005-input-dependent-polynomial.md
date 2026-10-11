# Graveyard 005: selecting a polynomial after seeing the input

Session: 2026-10-11 night (work continues after midnight JST).
Status: refuted semantic mutation, intentionally constructed as a negative control.
This is not a previously believed conjecture and no novelty is claimed.

## Invalid replacement

Replace a SINGLE finite probability distribution on degree-at-most-d polynomials,
chosen before the input and correct with probability >=2/3 at EVERY input,
by a statement allowing a DIFFERENT polynomial for each input.
Equivalently, move the existential polynomial family inside the forall-input.

## Counterexample and failure point

For every function f and every input x, the constant polynomial P_x=f(x)
has degree zero and is correct at x with probability one. The weakened
statement therefore incorrectly assigns degree zero even to MOD3 on five bits.

For the genuine definition, consider the all-zero input (target 1) and a
weight-one input (target 0). A fixed mixture placing probability p on the
constant 1 succeeds with probabilities p and 1-p respectively. Both cannot
be >=2/3. The distribution giving these two inputs mass 1/2 each bounds
both deterministic constants, hence every real mixture, by 1/2.

The stdlib audit verifies the concrete target values and rational dual rows.
The new Lean modules contain a generic input-dependent-constant theorem and
a candidate combined theorem contrasting it with the genuine n=5 predicate.
Their formal acceptance must be checked separately in the final CI record.

## Companion degree-premise control

A polynomial x0*x1 agrees with zero on the zero vector and all five basis
vectors, but not at input mask 3 (both x0 and x1 are one). Keeping only
constant and linear coefficients therefore does NOT reconstruct arbitrary
polynomials. The totalDegree<=1 premise in the normal-form theorem is essential.
The executable audit checks this controlled counterexample on all 32 inputs.

## Salvage

Keep the original order: exists m, P, mu, then forall x. Keep normalization,
nonnegativity, actual field equality and actual polynomial degree constraints.
Use a structural normal-form proof, not interpolation on only basis inputs.
