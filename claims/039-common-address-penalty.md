---
id: projection-slot-common-address-penalty
status: candidate-survives
statement: For fixed signed-clause projection queries and unrestricted local answer tables, the minimum summed local rejection plus pairwise common-address disagreement at the smaller incidence mass equals the minimum summed global rejection.
dependencies: Uniform seed; physical proof bits shared globally; one table per literal occurrence; signed projection images with uniform fibers; unnormalized sum over clauses.
novelty: novelty-unknown
last_attacked: 2026-11-13
---

Choose a maximum-mass incident slot at each physical address. Changing any other occurrence to agree with it costs at most the smaller mass already paid for their discrepancy. Restricting any global minimizer back to its slots gives the reverse inequality. Two opposite units force the full smaller mass at a single split address. The cost comparison for restricted-degree guesses uses only the rounding inequality and explicit YES approximants.

[Derivation, sharpness and counting](../expeditions/039-unary-overlap-counting/weighted-overlap.md) · [Finite exhaustive local/global comparisons](../expeditions/039-unary-overlap-counting/overlap-checks.json) · [Failure of independent collision sampling](../graveyard/039-padding-and-collisions.md)
