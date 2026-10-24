# Actual agreement dimension and its finite-real-mixture use

Research lead: 月野テンプレクス. One approved 2026-10-24 night session,
executed after midnight 2026-10-25 JST. This is a reconstruction of a known
polynomial-method argument, not a novelty claim. The final conclusion and
execution evidence distinguish authored code from actual Lean acceptance.

## Precise target

Let K be any field, n,d nonnegative integers, and R an actual multivariate
K-polynomial in n variables with totalDegree(R)<=d. Let a,b be nonzero.
Define G as the SET of actual vectors in {a,b}^n, not a multiset of encodings,
and H={y in G: R(y)=product_i y_i}. Set t=floor((n+d)/2) and
B(n,d)=sum_{j=0}^{min(n,t)} choose(n,j).
The target is |H|<=B(n,d). No rank, surjectivity, or agreement-cardinality
hypothesis is permitted. When a!=b, |G|=2^n. When a=b, |G|=1 instead.
There is no probability convention in this deterministic statement.

## 1. Degree-preserving grid reduction

For distinct a,b and any integer k>=0, on x in {a,b},

 x^k = ((a^k-b^k)/(a-b))*x + (a*b^k-b*a^k)/(a-b).

Substitution of a and b and cancellation of a-b prove the identity over ANY
field. No ordering or characteristic restriction is used. In particular this
is not the false replacement x^2=x on {1,omega} in GF4.

For an exponent vector e, apply this identity at coordinates in support(e),
and expand the product of affine factors. Every resulting squarefree support
S is contained in support(e), hence |S|<=|support(e)|<=sum_i e_i. The zero
exponents contribute1 and do not introduce variables. For a genuine polynomial
P with totalDegree<=t, each nonzero coefficient exponent has sum_i e_i<=t.
Linearity therefore puts eval(P) in the span of the squarefree coordinate
monomials of support size<=t, on every finite subset of the grid.

Lean's `eval_mem_low` proves precisely this evaluation-preserving bounded-span
reduction from actual P and totalDegree. It does not export a separate executable
polynomial normalizer. `affine_product_mem` explicitly gives its coefficients
by expansion over subsets, so the reduction is constructed, not postulated.

## 2. Compression on the actual agreement set

Reuse the accepted `TwoPointCompression.compress_monomial`. For every S,
choose one Q_S before the input. If |S|<=t use the squarefree monomial itself.
Otherwise use

 Q_S = R * product_{i outside S} ((a+b-Y_i)/(a*b)).

On G, each inverse factor is y_i^(-1), since a and b are nonzero. On H, R(y)
is the full coordinate product, so Q_S(y)=product_{i in S} y_i. Its actual
degree is at most d+n-|S|<=t because n+d<=2t+1 and |S|>=t+1.
Apply step1 to Q_S: every squarefree monomial, not just the low-degree ones,
therefore belongs to the low-degree evaluation span on H.

## 3. Interpolation without an assumed rank hypothesis

For z in H, the product over coordinates of

 (b-y_i)/(b-a) if z_i=a, and (y_i-a)/(b-a) if z_i=b

is1 at z and0 at every other point of H. Each factor is affine. Expanding
these actual Lagrange indicators places them in the squarefree span of degree
at most n. Every function f:H->K equals sum_z f(z)*delta_z. Thus the full
squarefree evaluation span is ALL of K^H. Step2 puts this full span inside the
span of monomials of degree<=t. This derives the spanning conclusion; it does
not assume it as an input condition.

## 4. Count degrees of freedom

The dimension of K^H is |H|. A span of a finite family has dimension at most
the number of its generators; duplicates in the evaluation image only lower
that number. The number of subsets S of {0,...,n-1} of size<=t is B(n,d), by
partition into cardinality fibers. Therefore |H|<=B(n,d).

The Lean endpoint `agreement_bound` constructs the full actual agreement set.
An intermediate theorem for arbitrary finite agreement subsets has the premise
R(y)=product y for y in H; this merely describes H, not its cardinality or rank.
The final endpoint contains no such externally supplied subset or rank premise.
Empty H, n=0, odd/even n+d and d>=n are included without additional assumptions.

## 5. Repair the distinctness necessity claim

The preceding exposition in Expedition024 and #18 overstated that a!=b was
necessary for the cardinality CONCLUSION. If a=b, G is the singleton constant
vector. H has at most1 point and B(n,d)>=choose(n,0)=1. The count bound survives.
`agreement_bound_allow_equal` handles this separately; the divided-difference
proof and the normalization |G|=2^n still require distinctness. In contrast,
allowing zero among distinct endpoints really is false: R=0 on {0,1}^3 has7
agreement points while B(3,0)=4. Graveyard040 keeps these separate lessons.

## 6. Fixed finite REAL mixtures

Let I be any finite index type, P_i actual K-polynomials all of total degree<=d,
and mu_i nonnegative REAL weights summing to1, fixed before the input. Define
s(y)=sum_i mu_i*[P_i(y)=product y_i], where brackets denote a real0/1 indicator.
Finite sum interchange and the deterministic bound give

 sum_{y in G} s(y) = sum_i mu_i*|H_i| <= sum_i mu_i*B(n,d) = B(n,d).

For a!=b, if s(y)>=eta at every input, then eta*2^n<=B(n,d). Thus eta>B/2^n
is impossible for ANY such mixture, including nonuniform, irrational weights,
duplicate polynomials, and arbitrary finite support. This is an actual
consequence of the dimension proof, not a wrapper assuming row-score bounds.
Signed normalized coefficients can violate it; input-dependent choice can
violate it. Both have explicit finite controls in graveyard040 and verify.py.

This result targets the coordinate product on the two-point grid. It is NOT
by itself the original GF2 MOD3 probabilistic-degree statement.

## Named next use and evidence limits

Expedition024's n299 candidate additionally needs a faithful actual GF2-to-GF4
polynomial transport and generic finite-real majority amplification. The new
agreement/mixture chain removes the dimension/averaging gap, not those other
links. Separate finite checks cannot certify them for arbitrary distributions.
No n12 determination, optimal threshold, new circuit bound, barrier escape,
independent semantic review, second proof kernel, or novelty is inferred.

Primary author source: Oded Goldreich, On teaching the approximation method for
circuit lower bounds, ECCC TR23-034 revision1 (2023-03-25), Section3.1's
interpolation/monomial-complement argument and Section3.2's modular application.
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download
Parsed text was inspected again; screenshot requests failed, so visual PDF
inspection is not claimed. This finite binomial formulation is our explicit
reconstruction, not a claim to quote the inaccessible 1987 original.
