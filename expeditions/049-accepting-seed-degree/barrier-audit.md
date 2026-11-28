# Barrier audit — exact witness degree and compiler dependence

## Scope of the mathematical move

The source-specific deduction concerns the standard honest interpolation and
outer residual in BV14, under explicit degree and field-size margins. The
fixed-node and two-level RS statements concern exact honest extensions. The
Boolean controls show dependence on circuit representation and distinguish
distance from actual violation counts. None is a lower bound on general
circuits or a separation of complexity classes.

## Relativization

Interpolation, exponent filtrations and the signed-clause counterexamples are
explicit finite algebraic/combinatorial statements. They do not supply a
separating step against a common oracle. Any eventual connection still uses
the unrelativized source PCP and the hierarchy/counting ledger from
Expeditions 038–039. Their required relativized forms have not been proved.
No escape from the Baker–Gill–Solovay barrier is claimed.

## Natural Proofs

Exact Boolean degree is a truth-table property, but this work neither proves
its largeness in the relevant proof family nor its usefulness against all
polynomial-size circuits. The exact interpolation lemma says that the
canonical A root preserves the genuine assignment's degree; it does not show
that every satisfying assignment of a hard instance has high degree.
Compiler-created hard auxiliary rows are particularly unsuitable as a
semantic hardness property: an equivalent public implementation can change
them while preserving raw NO soundness. Constructivity alone is not a
Natural Proofs barrier analysis or escape.

## Algebrization

Using characteristic-two arithmetic, subspace vanishers and polynomial
division is not evidence of a nonalgebrizing separation. No comparison under
the asymmetric Boolean/algebraic oracle access of Aaronson–Wigderson is
established. The broad-route disposition remains unknown.

## Limits with operational consequences

- The quotient degree bound needs a formal numerator of degree less than
  `3S<|F|`, not an arbitrarily reduced pointwise function. Outside that ratio,
  division by a linearized polynomial can sharply increase Boolean degree.
- Canonical interpolation preserves exact degree but not Hamming closeness.
  A one-site change on a 16-point assignment domain changes 241 of 256 root
  symbols in the recorded control.
- The outer gate bound is constructive and public, but does not cover the
  full growing recursive proximity circuit. Seed-dependent bases and
  interpolation arithmetic must be analyzed, not priced only by circuit size.
- The three-witness designed residual is completely classified, but its
  affine A cutoff cannot represent a growing arbitrary Boolean assignment.
- A weighted distance lower bound to every satisfying proof is not a lower
  bound on the actual clause-failure objective of all low-degree tuples.
  The live bent control separates these objectives exactly.
- Field rejection counts, including the older 221 example, are not imported
  as Boolean clause gaps for either new fixture.

The result narrows a conditional PCP/counting route. It supplies neither
universal approximation completeness nor the missing hierarchy-family
all-witness obstruction. See [source audit](source-audit.md),
[mathematical derivation](linearized-degree.md), [compiler controls](auxiliary-artifacts.md)
and the repository [barrier map](../../map/BARRIERS.md).
