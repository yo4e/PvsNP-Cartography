# Source trace and a rank-based sufficient condition

2026-11-10 JST, later session. Author: 月野テンプレクス. Source observations, our deductions and missing implications are separated. The rank argument below is author-written mathematics, not a new Lean theorem or a completed reconstruction of the entire PCP.

## Primary sources actually read

[BV14] Eli Ben-Sasson and Emanuele Viola, Short PCPs with projection queries, ECCC TR14-017, 2014-02-09. https://eccc.weizmann.ac.il/report/2014/017/download

Source trace: Lemma1.6, pp4-5 adds auxiliary bits indexed by seed and variable number. The ACSP queries are field translations (Theorem4.2 and p5). Section4.4 repeats shifted seeds. Section6, pp17-21, uses tree labels, leaf queries and redirection to siblings/parents; p20 fixes O(log k) examined control bits and describes remaining permutations. These do not alone state a common binary-address fiber bound. Relevant page images 1,5,13,19,20,21 were inspected; an initial p19 screenshot timeout was later resolved. No fresh implementation of the complete source verifier was executed.

[V21] Emanuele Viola, New lower bounds for probabilistic degree and AC0 with parity gates, ECCC TR20-015 revision5, 2021-01-12. https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/

Lemma11 selects one clause from the projection-PCP, retaining an inverse-polynomial rejection gap. Section2.3 (pp13-15, p14 image inspected) first amplifies POINTWISE error, then fixes the language input x, and extracts one polynomial for all queries. Its lower-bound conclusion retains E^NP and infinitely-often lengths. The following average-error substitutions are our proposed changes, not steps asserted by the paper.

## Exact affine-fiber calculation

Let q(z)=Az+b map the uniform r-bit seed cube to an m-bit ADDRESS cube. If A has GF2 rank d, each nonempty fiber is a coset of its kernel, with exactly 2^{r-d} elements. Thus q is uniform on an affine image of size 2^d and its maximum density relative to the full address cube is

    D(q)=2^{m-d}.

For any nonnegative error function e on addresses,

    E_z e(q(z)) <= D(q) * E_y e(y).

This follows by expanding both finite sums and comparing each point mass; it applies to real e, not only indicator errors. A bias b has no effect. Neither input permutation nor invertible affine relabeling of the output changes rank. The number of nonconstant OUTPUT bits is not the rank: q(z)=(z_0,...,z_0) has rank one regardless of m.

## From actual queries to one fixed polynomial

Let clause types i have normalized nonnegative weights nu_i. Each type has three signed queries q_ij(z)=A_ij z+b_ij, with uniform z. Suppose pi satisfies every tested clause. Fix a true occurrence for each (i,z), before sampling any approximating polynomial. Its selected-address mass at y is at most the TOTAL occurrence mass

    L(y)=sum_i nu_i sum_{j=1}^3 Pr_z[q_ij(z)=y].

For a normalized finite nonnegative real distribution mu on GLOBAL candidate polynomials, let e(y)=Pr_mu[P(y)!=pi(y)] and delta=E_uniform e. An unsatisfied clause must get its selected true literal wrong. Therefore

    E_mu[test failure] <= sum_y L(y)e(y) <= Lambda*delta,
    Lambda=2^m max_y L(y)
           <= B=sum_i nu_i sum_j 2^{m-rank(A_ij)}.

One positive-mass polynomial has failure at most B*delta by finite averaging. Its degree bound is inherited from the same sampled polynomial, not from independently chosen answers. Comparing to Expedition036 gives C<=kappa<=Lambda<=B. This is a sufficient, potentially loose bound; B is not the optimal certificate or signed-error constant.

If every map has rank at least m-h, then B<=3*2^h. Unlike an exponentially large true-literal flow problem, B can be computed from explicitly supplied affine query matrices by Gaussian elimination. Matrix-description length, type count and rational weight bit lengths must be charged; this is not a claim about generating those matrices for a hidden or exponentially represented family. For the original counting transfer one still needs B*delta strictly smaller than the ACTUAL soundness gap, and affine substitution/count construction costs.

verify_rank_transfer.py tests this chain against actual finite signed-clause failures for128 seeded synthetic families, all-one targets and all error sets. It does NOT instantiate BV14's construction.

## Why the full-address encoding matters

Our deductions for simple source-shaped components: a k-bit translation is uniform WITHIN its block. If its full address adds h fixed block/field-bit tags, its density relative to the whole k+h-bit cube is 2^h, not one. Likewise (z,i) for fixed i is injective in z, but its fixed index/tag bits must still be counted. Merely reading a field-word coordinate and ignoring the field-bit index does not establish bit-proof smoothness.

For the recursive PCPP a leaf's local coordinate is not the whole address: the root-to-node labels are also part of the location. Conversely, a long temporary path does not guarantee a high-rank FINAL address after redirection/aliasing. A source-dependent rank proof must track which original seed bits remain recoverable from the final canonical node label plus local coordinate, after control-bit fixing, all leaf queries, upward redirection, binary field encoding, tags, auxiliary bits and padding. The inspected O(log k)-control description suggests this is a tractable target, but is NOT a completed proof of rank >=m-O(log m). We make no adverse claim about the original construction's actual congestion.

Required next output for Issue28: either a concrete common encoding with a proved recoverability invariant and a polynomial B bound, or an actual generated query/cut disproving the desired bound. Do not replace this obligation by another arbitrary rank-deficient projection example. The present numerical families do not fill it.

## A separate obstruction: fixing x and amplifying a uniform-average promise

Let x have n bits and y any nonempty Boolean address cube. A JOINT uniform error promise for a candidate P against f gives, at a specified x*, only

    E_y [P(x*,y)!=f(x*,y)] <= 2^n * E_{x,y}[P(x,y)!=f(x,y)].

The factor is sharp: f(x,y)=[x=0^n] and P=0 have joint error 2^{-n} but error one at x=0^n. The candidate is a genuine degree-zero polynomial and the target is explicitly easy. This is a counterexample to the implication, not a claim about the canonical PCP proof function itself. Even perfectly uniform queries in y would not remove it.

Independent repetition also cannot generically turn uniform-average error into small pointwise error: take a point-mass distribution on that P. Every odd majority of independent samples remains P, including on the completely wrong slice. Independence of samples is not a bound on the per-address failure probability.

Repair conditions are explicit: require a slice-wise average promise for every relevant x, plus B*delta below soundness; or supply a different encoding/hardness-amplification argument with its costs and quantifiers. A low-error joint promise strong enough to absorb the factor2^n is another, much stronger hypothesis. No such premise is silently added to V21. Finding polynomial query congestion alone would not justify replacing V21's constant pointwise-error assumption by constant uniform-average error.

## Disposition

The tagged-copy smoothing branch is refuted by an exact invariance argument; removing labels breaks completeness in a two-address example. The rank-based repair is explicit, but its complete source instantiation and an adequate fixed-input error promise remain OPEN. Issue28 is therefore kept open. External PCP/hierarchy theorems, existing Lean endpoints, these written arguments and finite controls remain separate evidence classes. No novelty, unrestricted lower bound or P-versus-NP conclusion is claimed.
