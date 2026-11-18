# Pack the known powering sampler, then price physical pooling

The original schedule in Expedition 042 used one binary coefficient per power of a field element. The final remark of AGHP §5 permits a whole field coefficient per power. Applying that known construction reduces the number of fixed translations by a squared logarithmic factor in the inverse-polynomial bias regime. For these packed translations, the actual physical overlap geometry also gives a limitation on further pooling. Almost all calls eventually have disjoint physical views.

The bias argument below reconstructs that published remark and supplies an implementation. The pooling argument combines its coefficient layout with the previously derived displacement set of this repository's specific all-fresh-tapes RS test. Its status is a written derivation with finite controls. [Alon, Goldreich, Håstad and Peralta, §5, Construction 3 and final remark](https://www.math.tau.ac.il/~nogaa/PDFS/aghp4.pdf)

## The explicit multiset and its exact guarantee

Fix a seed dimension k≥1, a target 0<λ<1, and the least positive integer m such that, with Q=2^m and d=ceil(k/m),

    (d−1)/Q ≤ λ.

For a rational squared target one can check (d−1)² ≤ λ²Q² entirely with integers. The search terminates by m=k, at which point d=1 and the numerator is zero. It also terminates no later than the old construction's field size, because d−1≤k−1. In particular Q≤2 max(2,(k−1)/λ), so exhaustive polynomial-modulus construction still costs polynomial time in k and 1/λ.

Choose the standard binary basis v_0,…,v_(m−1) of GF(Q). For every ordered pair y,w∈GF(Q), define a mask h(y,w) whose bit at position i=jm+r<k is

    h(y,w)_i = bin(w) · bin(v_r y^j)   over GF(2).

The index order is fixed at construction time. It produces Q² mask occurrences, with known multiplicities. Precomposing a raw signed-projection query with any one of these constant masks preserves the query form and its fiber counts. All calls use one global proof.

For a nonzero character c∈GF(2)^k, its mask parity is the binary pairing of w with

    P_c(y) = Σ_(j<d) (Σ_(r: jm+r<k) c_(jm+r) v_r) y^j.

At least one field coefficient is nonzero, so P_c is a nonzero polynomial of degree at most d−1. Averaging over all w is zero when P_c(y)≠0 and one when P_c(y)=0. The weighted character mean is therefore exactly the number of roots of P_c in GF(Q) divided by Q. It lies in [0,(d−1)/Q]. Truncation of the final block changes neither injectivity of the coefficient map nor this bound.

The centered mixing estimate, conditional accepted-site estimate, and once-evaluated residual inequality of Expedition 042 now apply with this λ. Choose λ²≤εr²/[C(1−r)] for the conditional error ε at rate r=D/N. Choose the earlier word-specific squared biases for the outer residual. These are two different error requirements and keep their previous quantifiers. [Conditional agreement](../042-accepted-sites/accepted-fraction.md) · [Residual estimate](../042-accepted-sites/outer-and-sampler.md)

## Calls, computation and a finite budget comparison

The exact budget is Q² calls, at most Q²L(k,a) raw symbol occurrences, and at most Q²T(k,a)+O(Q²) bit operations after fixed masks are available, where T is the charged original predicate computation including its public field work. Generating the masks directly uses O(kmQ²) bit operations after field multiplication data are available. Trial division for all candidate degree-m binary moduli uses polynomial time in Q and m. The code uses this elementary method. Storing or hardwiring the masks costs O(kQ²) bits. Removing repeated calls from the AND is legitimate, while the Fourier proof retains the multiset weights.

For m>1, minimality at m−1 gives Q<2k/[λ(m−1)]. When k≥2m the success inequality also gives Q≥k/(2mλ). Together with the old field-size upper bound these imply m=Θ(log(k/λ)) whenever λ is inverse-polynomial in k and k grows. Consequently Q=O(k/[λ log(k/λ)]), and the raw-read budget is

    O(L k² / [λ² log²(k/λ)]).

At fixed rate, with the existing polynomial C and inverse-polynomial ε, this becomes O(L k²C/[ε log²(k sqrt(C/ε))]). The exact implicit rule should be used at small k or extreme precision. The claimed logarithmic improvement concerns this polynomial parameter regime.

These integer budget examples compare the same requested character bias for the old and packed powering constructions. They do not equate character bias with conditional error.

| k | Target λ | Old Q² | Packed Q² | Reduction |
|---|---|---|---|---|
| 64 | 1/4 | 65,536 | 4,096 | 16 |
| 256 | 1/8 | 4,194,304 | 65,536 | 64 |
| 1,024 | 1/32 | 1,073,741,824 | 16,777,216 | 64 |
| 4,096 | 1/64 | 68,719,476,736 | 1,073,741,824 | 64 |

Only parameter arithmetic was performed for the large rows of this table. The masks and spectra in the separate finite controls have their own stated sizes. No optimal small-bias construction is claimed. The costed single-output Boolean compilation continues to use the actual new clause count and encoded width. The field agreement estimate alone does not set those two quantities.

## How much of this packed schedule can physical pooling save?

Let n=floor(k/m) be the number of complete coefficient blocks. First suppose k≥2m. If y,w are nonzero, each complete block is the m-bit description of the nonzero linear functional

    F_j(z) = bin(w) · bin(y^j z).

Knowing two consecutive blocks F_j,F_(j+1) determines y and w. To prove uniqueness, suppose two parameter pairs give the same F_j and F_(j+1). Write F for their common nonzero first functional. Their second equality gives F(yz)=F(y'z) for every z. If y≠y', multiplication by y+y' is bijective, forcing F to vanish everywhere. Hence y=y', then w=w'. This reasoning holds for any consecutive j≥0.

It follows that two distinct pairs with y,w,y',w' all nonzero can have no two consecutive equal full blocks. Their masks differ in at least floor(n/2) original seed coordinates. A mask with y=0 is supported in the first coefficient block, and w=0 always gives zero. A mask from nonzero y,w differs from every such exceptional mask in at least n−1 original positions. The total support size is Q²−Q+1, consisting of (Q−1)² masks from nonzero pairs and Q exceptional masks. All zero-w pairs account for the repeated zero mask.

Write W_z for one physical view of the actual base RS tester. The exact overlap formula in Expedition 042, together with the final-row observation in the current physical-incidence argument, bounds every possible intersecting displacement u of W_z and W_(z+u) by Hamming weight 3a. The paired all-row tail retains at most a original positions and its paired column tail at most 2a, giving this sharper bound. Thus, whenever

    floor(k/m) ≥ 6a+2,

all (Q−1)² views from nonzero parameter pairs are mutually disjoint and disjoint from the exceptional-mask views. Translation covariance gives each the same size |W_0|. Therefore the number q_pool of distinct physical cells read by the entire AND satisfies

    (Q−1)² |W_0| ≤ q_pool ≤ (Q²−Q+1)|W_0|.

This is a bound on actual canonical physical addresses, including parent and sibling aliases. It shows that their pooling factor relative to this schedule's distinct-call physical-read sum tends to one as Q grows. Predicate pooling cannot merge distinct complete leaves across these disjoint views either. The conclusion uses no invariance of the proof's field values and no independence of the calls. [Exact view overlap](../042-accepted-sites/exact-overlap.md)

The new physical-incidence bound also gives q_pool≥t|W_0|/B_a for every t-distinct-mask schedule at every dimension, where B_a=2^(2a)+2^a−1. A physical cell has at most two reader cosets on disjoint original-bit blocks, one of size at most 2^a and the other at most 2^(2a), meeting at their common seed. Thus even unrestricted physical pooling saves at most B_a relative to the distinct-call physical-read sum. The packed construction above sharpens that factor towards one in its eventual parameter regime. The difference between |W_0| and the raw occurrence count L remains an independent base-checker cost. [Generic incidence bound](physical-cost.md)

A weaker condition floor(k/m)≥4a+2 also ensures that deleting any ≤2a positions leaves two consecutive intact complete blocks. The nonzero parameter masks therefore remain distinct after deleting any one leaf's original-bit block. This independently prevents merging their complete leaf families even before the stronger physical-disjointness threshold applies.

## Executable controls and remaining limits

The checker independently evaluates every nontrivial character at k=4,8,12,16 using an integer Walsh transform and direct field-polynomial root counts. It verifies 69,900 characters in total, including the partially filled last coefficient blocks. Its chosen biases are attained at these finite instances.

For a=3 and k=7,8,9 it builds the actual canonical physical views for all 57 masks from GF(8), checks every pair against the exact overlap set, and counts pooled reads. These counts are respectively 992, 15,136, and 26,512, compared with unpooled physical-read counts 7,068, 34,428, and 38,076. The small cases exhibit genuine pooling before the disjointness regime.

For k=160, a=3 and Q=64 the program constructs all 4,096 mask occurrences. The 3,969 nonzero-pair masks have minimum Hamming distance 17 across all 7,874,496 pairs. The exact base overlap set has 2,528 displacements with actual maximum weight 8, below the uniform bound 3a=9. Its 26 complete blocks exceed the required 6a+2=20. Thus the stored masks instantiate the disjointness criterion. This check enumerates masks and shape displacements. It does not materialize the 160-bit field proof or its full physical views. The symbolic pooled-read multipliers are 3,969 and 4,033.

The general bias proof reconstructs a known primary-source construction. The generic pooling argument and its reuse in this tester have no Lean or external review certificate. The open decision is whether a more efficient explicit mask construction improves the whole predicate budget, or whether a different checker structure can improve its base predicate cost while retaining the signed-projection and shared-proof semantics.
