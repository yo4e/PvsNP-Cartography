# Failure of distance domination at the first two-level root

The one-level result in [040](../040-recursive-verifier/geometry.md) charges the relative distance of an external root to its Reed–Solomon code against the probability that the verifier rejects. At root dimension 8 and rate exponent 3, this inequality can fail on a single, consistently shared assignment. The example concerns the all-fresh-tapes public-seed schedule used in this repository and the RS component alone.

## One assignment on the root and its descendants

Use F=GF(256) with modulus t⁸+t⁴+t³+t+1. Integers denote binary polynomial-basis coordinates. The translated domain of the root is θ+F over the quadratic extension E. Write x=16v+u in integer coordinates, with u,v in {0,…,15}, and put dᵥ=v mod 2. The global external F-word at x is

- dᵥ when floor(u/8)=dᵥ,
- the field power x³² at the other points.

Outer row v has 128 coordinates w. For w<16, address w is the actual external root symbol at x=16v+w. Give every other position in outer row v value floor(w/8) mod 2. Inner row j inside v sees eight parent positions w=8j+i, i=0,…,7. Put dᵥ at all its other physical positions. Both levels read their column symbols by redirecting to the corresponding shared rectangle in these rows. This defines one global assignment.

At public seed z=16v+u, the verifier inspects eight inner rows j=floor(u/8)+2f, f=0,…,7, and four inner columns. If floor(u/8)=dᵥ, all eight rows are the constant dᵥ, including the parent sites. Every inner column is also constant dᵥ. Each of the four outer columns selected by u has constant value floor(u/8), as the values at its rectangle sites w=64+c depend only on bit 3 of c. Thus the seed passes. If floor(u/8) differs from dᵥ, at least the checked inner row with f=1 has eight parent values equal to the opposite bit and 56 remaining values dᵥ. No degree-<8 polynomial can agree with the latter 56 values without being identically dᵥ. The seed rejects. There are exactly 128 passing and 128 rejecting seeds.

This uses the row/column intersection and shared parent semantics of Ben-Sasson and Viola §6.1, Definition 6.2, and the fresh-bit partition in §6.2. The field layout and assignment are finite instantiations, not assertions that the source claims distance domination. [Primary source](https://eccc.weizmann.ac.il/report/2014/017/download/)

## A distance certificate that covers every candidate

The root consists of three disjoint blocks. Their sizes are 64 zeros forced by the rule, 64 forced ones, and 128 evaluations of X³². For any nonconstant P∈F[X] of degree <32, agreements on the three blocks require a root of P, P+1, and P+X³², respectively. Each polynomial is nonzero. Their degree bounds give at most 31+31+32=94 agreements. A constant can agree at at most 64 forced positions and one position in the Frobenius block, since x↦x³² is a permutation. Direct enumeration gives 64 as the actual maximum for constants in this fixture. These statements also apply after translating the root abscissas by θ and projecting E-coefficients to F, because any agreement with an F-valued symbol survives the projection.

Consequently the nearest-codeword distance in symbols lies in [162,192]. The upper bound uses the zero polynomial. The exact distance within that interval is unnecessary: rejection is 128/256 whereas relative distance is at least 162/256. Any lower estimate of the form p≥cδ valid across these tables must have c≤64/81. This witness leaves open the best such coefficient.

## What a second shifted query actually detects

If acceptance requires both the checks at z and z XOR s to pass, then this assignment still rejects exactly half the seeds whenever bits 3 and 4 of s coincide, and rejects every seed otherwise. In particular XOR 1 preserves the bad example. XOR 8 detects it on all seeds. Checking all 256 shifts of this one proof does not establish a bound for arbitrary proofs.

There is a separate XOR 8 counterexample when the compiler allows other legal auxiliary bases at the inner node. Keep the outer geometry, the field and the seed partitions. All outer rows except v=0 are zero. In that one row's recursion take inner auxiliary (c₀,c₁,c₂)=(16θ,17,32), with the last two **base-field** elements specified by their integer coordinates. They are binary independent of the inner shift and main basis: the low base components 17,32 add independent directions modulo span{1,2,4,8}; 16θ adds a new high component. All other nodes can retain their original basis.

Set S=16θ+span over GF(2) of {17,32}, and D(X)=∏_{s∈S}(X+s). For inner rows j=0 and j=1 of outer row zero, set their whole tables equal to D evaluated at their actual field abscissas. Every other inner row is identically zero. The eight parent sites in each of rows 0 and 1 are exactly the sixteen external points θ+x, x=0,…,15. They give legitimate nonzero F-symbols: the set of roots of D(θ+X) is θ+S, invariant under the nontrivial F-automorphism θ↦θ+1, since conjugation changes its origin by 17∈span{17,32}. None of those roots is in F. All outer extension sites are zero, since they occur among the remaining inner rows. Every shared cell therefore has just one value.

All inner rows pass (degree four or zero), as do all outer columns. The four inner columns in residue b=0 lie at the four abscissas S, so they are identically zero. At any other residue b=1,…,7 the four common abscissas lie in S+b, disjoint from S. Each such column has two nonzero entries and 14 zeros, excluding degree <2. The rejected public seeds are precisely the 14 with v=0 and u mod 8 nonzero. XOR 8 preserves this set. The root has sixteen nonzero values and 240 zeros. A nonzero degree-<32 polynomial disagrees at at least 240−31=209 zero sites, hence the zero polynomial is nearest with distance 16. Thus the paired verifier has 14/256 rejection versus distance 16/256 for this alternative basis. This exhibits a failure for basis-independent repairs. Its construction alone does not settle XOR 8 for the standard inner basis (16θ,32θ,64θ).

For a check on the change of basis, fix residue zero and retain the sparse pattern with only inner rows 0 and 1 eligible to be nonzero. Each such row polynomial must vanish at all four common abscissas to let the column group pass. Factor it as D(X)T(X) with degree(T)<4. Its eight coefficients over F (four coefficients over E) must make the high θ coordinate of D(x)T(x) vanish at each of eight external parent points. For the ordinary (16θ,32θ,64θ) auxiliary basis these two 8-by-8 homogeneous F systems both have rank eight, so this particular sparse construction cannot be transplanted. The rank calculation is specific to row zero, residue zero and the prescribed pattern; more general assignments are unrestricted.

The [standalone certificate](distance_certificate.py) recomputes the external word, constant histogram, uniform shift classification, and the alternative physical column values. The degree bounds on arbitrary polynomials use the polynomial root theorem. No exhaustive search over the 256³² candidate polynomials, kernel verification, or unrestricted PCP result is claimed.
