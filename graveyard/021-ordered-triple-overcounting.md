# Failed shortcuts: ordered triples without diagonal and fiber accounting

Approved2026-10-21 session. Scope: accounting shortcuts only.

## Missing +2R correction

Tempting claim: sum over distinct ordered triples is S^3-3QS. For three values
[1,1,1], actual distinct product sum is6, while that expression is0. The three
pair-equality diagonals meet on all-equal triples, so inclusion-exclusion
requires +2R, where R=sum z_i^3. A missing correction changes actual scores.

## Reusing an unordered denominator

Assign half the mass to singletons and mass1/(2*choose(n,3)) to EACH ORDERED
triple. At n3 the total mass is1/2+6/2=7/2, not1. The valid denominator is
2*n*(n-1)*(n-2), because each unordered triple has six orderings.

## Allowing repeated coordinates

Using the valid distinct-triple denominator but keeping all n^3 triples gives
mass1/2+27/12=11/4 at n3. Repeated indices also alter the Boolean input weight,
so their target is not generally the weight-three target. They must receive
zero mass in this particular construction.

All three controls are exercised by Expedition020/verify.py, alongside the
previously known strict-bound n6 boundary. Normal and optimized local executions
agree. Remote CI and generic Lean acceptance must be checked separately.

Salvage: explicit tagged sample type, pairwise-distinct indicator, +2R moment
identity, normalized real weights and actual GF(2) evaluation semantics. These
failures do not refute the correctly normalized dual, previous n5..11 results,
or arbitrary input distributions. Preserve the failed formulas, not just a
sentence saying a test failed.
