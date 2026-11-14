# A paired two-level verifier that rejects at least the root distance

Fix the BV14-style physical RS tree (k,a)=(8,3) with all fresh tapes enumerated at every selected node. Compare the original bundled RS predicate V(v,u) with

    W(v,u) = V(v,u) AND V(v, u XOR 9).

Both calls use the same global assignment, including every parent/child and row/column alias. The high four bits v label the outer row. Write u=8p+b with p∈{0,1} and 0≤b<8. The XOR flips p and toggles the low bit of b. Root symbols lie in F=GF(256), the external address is x∈F in its binary basis, and θ+x is its shifted coordinate in the extension field E. At both levels use distinct BV14 row ordinates, their common rectangle of abscissae, and their actual field interpolation nodes. A binary basis can be extended inside a sufficiently large E at the child as in Expedition 038. Inner symbols may be arbitrary elements of E. This argument needs only the stated decompositions, leaf degree limits and physical aliases. [BV14 §6.1, equations (8)–(9) and Proposition 6.1, and §6.2](https://eccc.weizmann.ac.il/report/2014/017/download/)

## Acceptance implies agreement on the selected points

For a fixed v the selected outer row has dimension seven. Each unpaired u checks the eight inner rows of parity p and the four common inner columns indexed by residue b. The paired call checks **all 16 inner rows and eight distinct common inner columns**. If W(v,u) accepts, these checks pass on the physical word. Each passing inner row is a polynomial in its physical abscissa of degree <8. Each of the eight columns is affine in the actual row ordinate. Use any two inner rows to define Q₁(X,Y) by interpolation in Y between their row polynomials. On each of the eight common abscissae, the affine column agrees with Q₁ at the chosen two ordinates, hence at every ordinate. Each inner row agrees at eight distinct abscissae with Q₁ restricted to that row; the degree limit extends agreement everywhere on it. In particular all underlying outer-row symbols, reached through the parent redirects, agree with Q₁(X,q₁(X)) on their true domain. Here q₁ is the subspace vanisher of degree eight for this particular child (the inner basis may depend on v). Its bidegree bound gives outer-row degree at most 7+8=15. Thus even one paired success in v recovers a full low-degree outer row, including its physical outer common rectangle. This is an implication; a codeword in that row with inconsistent auxiliary cells may still fail.

Let A be the set of accepted public seeds for W, let R be the set of v appearing in A, and U the set of their low indices. The map u↦u XOR 9 is a fixed-point-free involution preserving A at each v, so |U| is even. For a fixed u∈U, all four outer columns indexed by its group (u,h), 0≤h<4, are passing affine polynomials on the 16 outer ordinates. This statement is independent of which v supplied the accepting seed: the selected column leaf queries its *entire* word. Distinct groups give disjoint sets of common abscissae.

If |R|≤1, at most 16 seeds accept. If |U|≤2, at most 32 do. For *any* F-valued word on 256 inputs there exists an F-polynomial of degree at most 31 matching any preselected 32 distinct entries, by Lagrange interpolation. In either sparse case preselect all accepting sites and extend to 32 interpolation sites. The resulting external codeword agrees on every accepting site.

Otherwise |R|≥2 and, by evenness, |U|≥4. Interpolate two recovered outer-row polynomials in their distinct ordinates to define Q₀ with degrees at most (15,1). At every one of the at least 16 passing outer common abscissae, its affine column equals Q₀ at all 16 ordinates, because it does so on the chosen two. Every recovered outer row in R now agrees with Q₀ at ≥16 abscissae, so it agrees everywhere. Thus the single polynomial

    T(x) = Q₀(θ+x, q₀(θ+x))

agrees with the physically stored root values at *every* accepting seed and indeed everywhere in each recovered v. Its degree is at most 15+16=31. Here q₀ is the outer subspace vanisher of degree 16, constant on each parent coset. T has coefficients in E; apply to them any F-linear λ:E→F restricting to the identity on F. For x∈F, evaluation of λ(T) at x equals λ(T(x)), preserving all agreements with actual F-valued root sites.

Write δ for the normalized Hamming distance of the root to degree-<32 F-polynomials. The sparse and interpolation cases both give Pr[W rejects]≥δ. An honest external codeword extends consistently by the bivariate decomposition at both levels and passes all paired checks.

## A sharp positive-distance witness

Set every one of the 16 external symbols in a single outer coset v₀ equal to the F-symbol one, every other external symbol zero, and every free outer/inner extension symbol zero. The zero polynomial has exactly 16 errors. A nonzero degree-≤31 polynomial has at most 31 zeros, and can gain agreement on at most the 16 changed inputs; it cannot match the 240 agreements of the zero polynomial. Hence δ=16/256.

All shared outer common columns are zero, and all inner words for v≠v₀ are zero. For v₀, the physically changed 16 outer-row addresses w=0,…,15 occupy the eight parent sites of each of its inner rows j=0 and j=1. Every one of those length-64 rows has 56 zero symbols and eight ones, so neither is degree <8. An original u selects all inner rows of its parity, including exactly one of j=0 and j=1. Every W seed in v₀ rejects and all 240 other seeds accept. Paired rejection equals δ on this witness (as does original rejection here). Correct symbol multiplicity, genuine aliases and all fresh tapes are essential in this construction.

## Consequences and cost

For a fixed original assignment let E₀ be its original rejection set, let τ(v,u)=(v,u XOR 9), and let p=|E₀|/256. With exactly correlated public seeds,

    δ ≤ |E₀ ∪ τ(E₀)|/256 = 2p − |E₀ ∩ τ(E₀)|/256.

In particular the original schedule rejects with probability at least δ/2. This argument does not establish that 1/2 is the original optimal constant. Every mask 8+b′ with 1≤b′≤7 works by the same proof. Mask 8 by itself cannot supply eight distinct inner common columns; a mask changing only the low three bits cannot supply both parities. These are precise hypotheses of the repair, not impossibility claims about all other tests.

The pair uses the same eight public bits. Each fixed-tape address is an original query map precomposed with a constant translation on the seed cube, preserving its marginal fiber sizes and degree or projection locality. Evaluating the RS predicate twice costs at most twice the raw leaf reads and two predicate evaluations plus their AND. Shared reads may be cached. Only the RS predicate is paired here; no ACSP constraint is repeated or inferred. A Boolean compilation must price its gate, pin, and clause multiplicities separately. A bound on the fraction of failed *single clauses* does not follow with this same denominator. The distance and equality concern this finite topology with shared physical words. No asymptotic recursion or stronger result for the unmodified schedule follows solely by treating the two calls as independent.
