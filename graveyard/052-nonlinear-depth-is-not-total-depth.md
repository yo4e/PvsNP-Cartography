# Blindly deleting one nonlinear depth factor is false

Research lead/skeptic: 月野テンプレクス. Approved2026-10-31 JST session.
This is a mathematical post-mortem of a tempting extrapolation, not a claim
that the correctly stated literature theorem is false.

## Attraction

A source gives degree O((log s)^(d-1)*log(1/epsilon)) for depth-d AC0[MOD_p].
Our current bridge gives r^h with r on the order of log S. It is tempting to
replace h by h-1 in the general SharedDAG endpoint without changing its model.

## Exact failed step

The source's d counts ALL gate layers; our h counts only AND/OR along a path.
An arbitrary final XOR is free in h. These are not interchangeable quantities.
Furthermore, a constant-degree/error allocation for a single final OR/AND
does not apply to every nonlinear node feeding an exact final XOR.

## General counterargument, separate from finite computation

Every Boolean f has an XOR-of-minterms representation. For each satisfying
assignment a, form one AND of the n literals x_i or NOT(x_i) matching a. At
any input exactly one minterm of the full cube is true; hence XOR of only
f's satisfying minterms equals f. These circuits use permitted input,
NOT,AND,XOR gates, arbitrary finite fan-in and h=1. Their size may be
exponential. Constant/empty cases are handled separately.

If the proposed h-1 replacement supplied a universal size-independent degree
D at fixed error1/3 when h=1, it would make every such f feasible at degreeD.
Choose residue-zero MOD3 at n=(16*D+2)^2+2. The accepted
Mod3GrowingDegree.degree_impossible excludes that original predicate.
Thus no such uniform constant-degree conclusion can hold for all our h1 DAGs.
For the illustrative D3, the excluded arity is2502. No finite enumeration of
that enormous minterm circuit is needed for the written argument, and none is
claimed. The minterm representation and its formal translation are NOT Lean
verified by this session's existing endpoint alone.

## Salvage and limitation

Require a single final AND/OR and budget that root separately. The next
candidate has degree t*r^H and error S*2^-r+2^-t, where H bounds the selected
inner-child depths. It is a known-method reconstruction candidate, not a
universal improvement for XOR outputs or an escape from circuit lower-bound
barriers. The source is Limaye et al., MFCS2025, article67, official PDF
pages67:6/67:8, visually inspected; the source's size counts wires and its
depth counts all layers. Its theorem is not contradicted by this post-mortem.
