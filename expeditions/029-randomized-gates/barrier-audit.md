# Barrier and prior-art audit

Author/roles: 月野テンプレクス, cartographer and skeptic,2026-10-29 JST.
Evidence: same-author source comparison and adversarial analysis, not independent review.

## Exact route and established scope

This expedition reconstructs actual GF2 gate approximation, the other side of
the repository's already accepted MOD3 growing-degree obstruction. Primary
comparison: Goldreich, ECCC TR23-034 revision1, Section2.2.1, Claim2.1/Lemma2.
See proof-and-scope.md for the source URL and the important distinction between
pointwise randomized approximation and the later input-averaging step. The paper's
MODq polarity differs from our residue-zero target. Parsed text was inspected;
PDF screenshots timed out. No visual verification or local PDF archive is claimed.
Novelty status: novelty-unknown; treat the method as known-method reconstruction.

## Relativization

No step proves an oracle separation or analyzes all relativized complexity
classes. The accepted gates are algebraic objects over GF2 with a specified
finite distribution. Their formalization is not evidence of a nonrelativizing
argument for P versus NP. See map/BARRIERS.md for the primary barrier sources.

## Natural Proofs

The expedition establishes no constructive, large property useful against all
polynomial-size general circuits, nor a contradiction of a pseudorandom-function
assumption. Its next application is a specified restricted-depth algebraic
approximation model. No claimed escape of the Natural Proofs barrier follows.

## Algebrization

Working over GF2, composing actual polynomials and using Lean does not itself
establish a nonalgebrizing step. No oracle-extension separation is supplied.
The route remains restricted-model reconstruction, not a general barrier escape.

## Quantitative limitation and useful decision

The planned DAG approximation degree grows as r^h with nonlinear path-depth h.
That dependence must remain explicit; extending h arbitrarily does not provide
a general P/poly lower bound of the desired strength. The present accepted gate
and shared-union results isolate the missing concrete DAG/depth/first-error
proof, rather than assuming circuit approximability. This is the next useful
mathematical decision, not a quota of additional verification infrastructure.
Four invalid randomness shortcuts are dead in graveyard049; they do not refute
the correctly quantified route. No publication, priority or P-versus-NP claim.
