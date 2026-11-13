# Conclusion • one genuine recursive level

**The shared-cell verifier has a sharp answer on this NO instance.** No global assignment accepts more than 19 of the 128 public seeds. A degree-15 quotient attains 19. Changing one external bit at address 24 gives a noncodeword attaining the same 19, so a soundness argument that presumes global low degree would miss an extremizer. At any seed still eligible to accept, enough shared intersections force the quotient to agree there with a common polynomial of degree at most 15. The outer nonzero residual then has at most 19 roots. [Derivation, attainment and one-level family](soundness.md)

| Generated verifier | Minimum rejected seeds | Minimum failed physical clause–seed pairs |
|---|---:|---:|
| YES, A=1+X and B=X | 0 of 128 | 0 of 10,706,688 |
| NO, including arbitrary gate and proof bits in the clause bound | 109 of 128 | 109 of 10,717,568 |

The minima in the last column count repeated clauses with multiplicity. Attaining witnesses are evaluated by the programs. The lower bounds for arbitrary assignments come from the written interpolation and gate/pin arguments. The 109/128 field-verifier rejection and 109/10,717,568 single-clause rejection are different probabilities.

**What failed.** Separate either the parent or sibling copy of the same physical symbol and a NO instance can accept 127 seeds. For the exhibited assignments the joined implementation accepts zero. Independently, treating the interpolation weights as identical for every row rejects an honest linear polynomial. [Failures](../../graveyard/040-detached-recursive-cells.md) · [Exact output](verifier-checks.json)

**What carries forward.** For the finite one-level RS component, the rejection probability dominates the root's relative distance to the code, with equality at positive distance. This prices the bundled test on every root and every auxiliary assignment. Expedition 038's general inverse-polynomial soundness estimate uses different hypotheses and does not yield this equality statement. For the specifically constructed one-level NO family with k=2a+1, the [separate written calculation](soundness.md) derives the minimum by interpolation rather than by extrapolating these runs. No construction-level conformance claim beyond the generated fixture, novelty promotion, Lean result or unrestricted lower bound is recorded.

**Next mathematical decision.** At k=8, a=3 the parent row itself recurses. A row may then pass only for some inherited low seed coordinates. Determine which partial-agreement or robust-rejection estimate survives this dependence, or give an explicit shared-table counterexample. Repeating the old product of passing rows and passing column groups would assume the very seed-independence that now needs to be tested. [Geometry and sharp distance witness](geometry.md)
