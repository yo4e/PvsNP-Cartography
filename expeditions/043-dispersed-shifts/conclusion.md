# Cheaper field amplification, with two concrete limits

The cost question in Issue 32 has a useful bounded answer. A known packed small-bias construction reduces the earlier explicit translated-call budget. Actual physical-cell incidence limits further pooling, while two tempting shortcuts fail: dense full-rank masks need not give soundness, and sharing the final Boolean decision tables need not preserve amplified rejection. All general statements below are written derivations with separately scoped finite controls; no new formal verification or novelty is asserted.

## A cheaper explicit schedule

The final remark of AGHP §5 packs m binary coordinates into one coefficient of GF(2^m). For Q=2^m and d=ceil(k/m), the Q² mask occurrences have character bias at most (d−1)/Q. Choose the least m meeting the desired bias. In the fixed-rate, inverse-polynomial error regime, the old raw-read bound improves to

    O(L k² C / [epsilon log²(k sqrt(C/epsilon))]).

Here L is the original per-seed raw occurrence count, delta≤C p is the inherited distance estimate, and epsilon is conditional disagreement on the accepting external sites. The once-only residual uses its own previously derived bias requirements. For example at k=256 and requested bias1/8 the explicit call budget drops from 4,194,304 to 65,536. This is parameter arithmetic; it does not enumerate a field of 2^256 points. Predicate evaluation and mask generation are priced separately. [Construction, costs and limits](packed-sampler.md)

## Actual shared reads have bounded multiplicity

For every canonical physical cell, the seeds reading it form one leaf-block coset or two intersecting cosets associated with a row and its sibling column. The maximum number of distinct seeds reading one cell is bounded by

    B_a = 2^(2a)+2^a−1,

with equality possible at root dimension4a. Thus any t distinct translations require at least t|W_0|/B_a distinct physical symbols at each center. Pooling cannot remove the linear growth in t at fixed rate. The same final-row argument sharpens the base overlap support radius to3a.

For the packed family, if floor(k/m)≥6a+2, the (Q−1)² views indexed by nonzero parameter pairs are mutually disjoint. Its actual pooled reads lie between (Q−1)²|W_0| and (Q²−Q+1)|W_0|. The remaining base-call difference between raw occurrences L and distinct symbols |W_0| is a separate cost. [Incidence proof](physical-cost.md) · [Packed disjointness](packed-sampler.md)

## Dense and full rank still leave a failure direction

At k=2^r−1 with even r≥4, use zero and the k masks h_y(x)=x·y+1[x=y]. They form a full-rank, self-inverse matrix. Their weights are 2^(r−1)±1 and their mutual distances lie within2 of 2^(r−1). Nonetheless a shared proof can make any prescribed root pass on a 1−O_a(k^(−1/2)) fraction of seeds. In particular x^D stays at distance1−2^(−a) from the code, and the designed reciprocal NO witness has joint acceptance tending to one.

The mechanism is explicit: independent triple parities annihilate the dense simplex part and each perturbed mask changes only one parity. The actual recursive displacement set changes at most3a more. Majority regions have exactly D sites, permitting interpolation of the prescribed word throughout each region and consistent splicing of interior physical views. Reweighting or repeating the same masks cannot fix the all-parities bias. [General criterion](syndrome-obstruction.md) · [Dense counterexample](dense-masks.md) · [Post-mortem](../../graveyard/2026-11-18-dense-masks.md)

## A Boolean bottleneck survives the field improvement

For a fixed failed base-decision set E, shared copy buffers and private AND aggregators have exact minimum violations

    min_Z (|E symmetric-difference Z| + |Z+H|) = |E|.

Setting every shared buffer to true pays one copy violation per original failure and defeats the amplified numerator. The four-seed control turns one base failure into four field failures while retaining a one-clause optimum. At the toy all-one YES reference its signed failure sensitivity is exactly t+1, checked over every gate-error subset in the specified small cases. The actual RS circuit has further inputs, gates and pins; equality for that full circuit is not inferred.

For private replicas the old sufficient precision threshold is beta=gamma N/(6 M Q), with Q the full Boolean address cube. Improvement is impossible whenever M_H Q_H≥t M_1 Q_1, but shared overhead can make a small improvement possible. There is no universal impossibility claim. The sharper quantity is gamma N/(Q sigma), where sigma is the maximum actual failed clause–seed pairs per changed proof bit. It requires an analysis of total fanout and literal signs, not just per-slot fibers. [Compiler derivations and exact controls](compiled-cost.md) · [Post-mortem](../../graveyard/2026-11-18-shared-decision-amplification.md)

## The next decision

This completes the bounded improvement-or-obstruction target of Issue 32. It does not settle the optimal sampler, the full recursive Boolean gate census, or the secondary unpaired GF(256) optimum, still between154 and189 rejected seeds. The next research target is an actual proof-bit precision improvement: obtain a costed bound on gamma N/(Q sigma) for a specified compiler or repair, preserving one physical proof and fixed signed-projection queries. A fresh explicit construction or a scoped obstruction to a well-defined compiler family would decide whether to continue this route. Repeatedly increasing field rejection without this accounting would not.
