---
id: 047-witness-layouts
status: candidate-survives
statement: Public symbolic dictionaries give scoped uniform proof layouts; shared RS structure obstructs an all-witness extension; globally shared guessed layouts preserve NO soundness subject to cost.
dependencies: Expedition 046 source geometry and compiler; elementary Boolean polynomial counting; explicit public dictionary and single-map hypotheses; cited PCP/counting results only for the conditional resource comparison.
novelty: novelty-unknown; core linear encoding and code dimension mechanisms are standard
last_attacked: 2026-11-25
---

Evidence classes are separate. The universal statements have written
derivations and adversarial scope checks. The twelve-row relation, GF(8)
enumeration, GF(128) code-only witness and shared-map controls have exact
finite execution evidence. There is no new formal proof-kernel acceptance
or independent external review.

See [Expedition 047](../expeditions/047-witness-layouts/conclusion.md).

Surviving statements:

1. Public coefficients c_i in an L-dimensional dictionary of seed degree
   delta yield a fixed injective coefficient/rank layout and exact degree
   delta+1 completion, at explicitly exponential-in-L storage.
2. The original Expedition 046 YES fixture has a unique used proof. Its
   code-only relaxation has 2sk systematic independent bits among satisfying
   witnesses. Polynomial storage and degree O(log k) cannot approximate
   every such witness within O(s) absolute errors eventually.
3. A fixed shared row map and polynomial decode one global old proof. NO
   soundness survives even collisions; full metric equivalence requires
   injection. Occurrence-dependent detachment can destroy soundness.
4. Explicit row-map guessing in the growing one-level compiler costs too
   much for the intended o(N) clock, independent of its low completed degree.

These do not prove that every witness is hard, that the actual source verifier
has a small dictionary, that a succinct guessed map exists, or that any new
complexity-class lower bound follows. The all-witness obstruction and the
existential target must remain distinct.
