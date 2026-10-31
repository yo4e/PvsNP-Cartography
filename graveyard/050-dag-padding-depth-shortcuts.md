# Three invalid shared-DAG shortcuts and an unrolling control

Author: 月野テンプレクス; freshly approved session executed2026-10-31 JST.
Exact reproducer: expeditions/030-shared-dag/check_slots.py, attacks().
These refute the named shortcuts, not the correctly stated circuit theorem.

## Zero padding for AND

At input x=1, AND(x) is1. Padding a spare argument with0 changes it to AND(1,0)=0. The attraction is a common zero-padding helper for every gate. The failure is semantic, even before probability. Repair: AND pads with1, so its complemented OR-hash vector pads with0. OR/XOR pad with0. The finite checker attacks slot gaps and empty fan-in.

## Count only the final output gate's local error

The two-node program NOT(OR(x)) at x1, r1 has an exact NOT output node, hence no local error at that node, yet output error1/2 inherited from its OR predecessor. A zero error bound obtained by counting only the output node is false. Repair: first-error inclusion plus a union bound over original nonlinear nodes (or a separately justified ancestor set), not the local error of the final gate alone.

## Add r per nonlinear layer instead of multiplying degrees

With one argument, r3 and all coefficients1, Q(x)=x+x^2+x^3. Compose the same construction twice. Its leading term is x^9, so actual degree9, not the alleged r*h=6 at h2. On Boolean inputs it still computes x, which does not reduce its genuine MvPolynomial degree. Repair: degree multiplication at composition gives r^h; a Boolean multilinear-reduction theorem would be a separate step, not permission to relabel the existing polynomial.

## Bookkeeping control, not a false inequality

A six-node chain in which each OR reads the previous output twice has6 original nonlinear nodes but63 occurrences after formula unrolling. Counting63 gives a looser bound, not an invalid bound. It is invalid to claim that a proof with63 counts has established the promised6-node estimate without an additional argument. The concrete program stores each original node once and the union proof uses its additive original-node cost.

Historical repeated-hash, wire-identity, correlated-error, adaptive-input and r0 counterexamples remain in047/049. Local normal/-O checks pass; CI acceptance is separately recorded only after an actual completed run is retrieved. No general theorem is inferred from these finite checks.
