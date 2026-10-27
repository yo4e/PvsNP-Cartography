# 041: shared residue indices are not independent repetitions

Author acting as skeptic: 月野テンプレクス, fresh approved session 2026-10-27 JST.

## False shortcut: multiply marginal success probabilities

Let f be the exact three-bit MOD3 residue-zero truth table. Choose uniformly
among f, f XOR delta_000, and f XOR delta_110, all represented by genuine GF2
multilinear polynomials. Every input has success at least2/3. At x=0, the two
padded queries are000 and110, so each is correct with probability2/3 but both
are correct only for f, probability1/3. The injective GF4 answer-pair encoding
therefore succeeds with probability1/3, NOT at least4/9. The union bound1-2delta
is tight here. This refutes a universal independence improvement of this coupling,
not every alternative transport or an optimal MOD3 degree threshold.

Expedition026/verify.py constructs the polynomials by a Boolean Mobius transform
and independently evaluates all eight source inputs. ANF masks are recorded in
result.json, with low-bit-first coordinate order. No heuristic search is used.

## False shortcut: mass one is sufficient without nonnegativity

Use errors{110},{000},{000,110} relative to f, with real weights[2/3,2/3,-1/3].
The total mass is1 and apparent source correctness at every input is between
2/3 and1. Nevertheless transported correctness at y=1 is0, violating the
claimed1/3 bound. Even range-bounded apparent source scores do not repair signed
weights. Nonnegative weights are necessary for summing pointwise inequalities.

## Other dead shortcuts

One-bit padding selects the wrong residue. Swapping the root coefficients breaks
the exact target. ZMod4 has a nonzero nonunit2 and is not the four-element field.
Selecting constants AFTER seeing the input is not a fixed polynomial family.
Repeating a single sampled polynomial15 times leaves its error unchanged; the
independent binomial tail422009/4782969 cannot be assigned to that experiment.
The verifier preserves explicit controls for the first three and the majority
arithmetic; the old quantifier countermodel remains in the repository.

## Salvage

Keep the same index for residue restrictions and use the real union bound,
retaining degree D and the original nonnegative probabilities. Use independent
indices only in the separate majority-amplification construction. These examples
are finite counterexamples, not a generic theorem or novelty assertion.
