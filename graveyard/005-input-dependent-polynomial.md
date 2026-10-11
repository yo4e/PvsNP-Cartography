# Graveyard 005: selecting a polynomial after seeing the input

Approval night: 2026-10-11; verified after midnight on 2026-10-12 JST.
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

For the genuine definition, consider the all-zero input (target1) and a
weight-one input (target0). A fixed mixture placing probability p on the
constant1 succeeds with probabilities p and 1-p respectively. Both cannot
be >=2/3. The distribution giving these two inputs mass1/2 each bounds
both deterministic constants, hence every real mixture, by1/2.

The stdlib audit verified the concrete target values and rational dual rows
in run38150257051. Lean's input_dependent_constant and the combined
Mod3Five.swapped_quantifiers_are_strictly_weaker contrast this with the
correct predicate; their actual build and axiom report passed run38150083188.
See ../formal/reports/2026-10-12-n5-degree-axioms.txt.

## Companion degree-premise control

A polynomial x0*x1 agrees with zero on the zero vector and all five basis
vectors, but not at input mask3 (both x0 and x1 are one). Keeping only
constant and linear coefficients therefore does NOT reconstruct arbitrary
polynomials. The totalDegree<=1 premise in the normal-form theorem is essential.
The executable audit checks this controlled counterexample on all32 inputs.

## Salvage

Keep the original order: exists m,P,mu, then forall x. Keep normalization,
nonnegativity, actual field equality and actual polynomial degree constraints.
Use a structural normal-form proof, not interpolation on only basis inputs.
The correct n=5 result survives; only these deliberately weakened variants die.
