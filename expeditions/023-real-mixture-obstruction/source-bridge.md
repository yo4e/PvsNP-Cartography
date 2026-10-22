# From the repository predicate to a known growing-degree lower bound

Research lead 月野テンプレクス; approved 2026-10-22 JST night.
Status: primary-source comparison, author-reconstructed adapters and exact
controls. NOT a new lower bound, a Lean-accepted Smolensky reconstruction,
or independently reviewed new mathematics.

## Exact source and mismatch

Srikanth Srinivasan, Utkarsh Tripathi, S. Venkitesh, *On the Probabilistic
Degrees of Symmetric Boolean Functions*, arXiv:1910.02465v1 (2019-10-06),
https://arxiv.org/pdf/1910.02465v1 . Definition1 pp1-2, Fact6 and Lemma9 p6:
text and relevant PDF page images inspected, including the author/title page.
The inaccessible ACM Smolensky1987 original returned403; it was not inspected.
This note uses the specified arXiv version, not an assumed latest numbering.

Lemma9: for2<=b<=m/2, characteristic coprime to b and
2^(-m)<epsilon<1/(3b), SOME residue i has probabilistic degree
Omega(sqrt(m log(1/(b*epsilon)))). The definition uses finite support and a
fixed distribution with error bounded at EACH input. Fact6 amplifies by
independent majority. Our GF(2), actual total degree and finite REAL weights
match. Error1/3 and the specific residue0 do not directly match this lemma.

## Explicit reconstructed adapters

Start with ANY finite nonnegative normalized real distribution mu on actual
polynomials P_j of degree<=d, pointwise error<=1/3 for MOD3,0 on n inputs.
Use17 independent indices. A tuple has weight product_l mu(j_l); finite
sum/product distributivity proves mass1 and positivity is immediate. This
new distribution is chosen before the input. No rational-ticket assumption.

Construct the exact multilinear majority polynomial M on17 Boolean inputs
by interpolation overGF(2). It has degree<=17. Substitution gives actual
Q=M(P_j1,...,P_j17) of degree<=17d. This is polynomial composition, not
coefficient averaging inGF(2). At each fixed input x the independent error
bits have a common real probability p(x)<=1/3, since all GF(2) values are bits.
Their majority error is
B17(p)=sum(k=9..17) choose(17,k)*p^k*(1-p)^(17-k).
The polynomial identity B17'(p)=218790*p^8*(1-p)^8 shows monotonicity on[0,1].
Thus B17(p(x))<=B17(1/3)=1082987/14348907<1/12. This holds for ALL possible
real p(x), not just a sampled grid. bridge-check.py verifies the derivative
identity with integer coefficient arithmetic and the rational tail exactly.
It also checks all131072 majority inputs by an independent GF(2) Mobius
transform; exact degree is16. We conservatively use17d, independent of that
finite optimization. Reusing one sample17 times instead leaves error1/3.

Let m=n-2. For desired residue i=0,1,2 fix the last two coordinates to total
weight s=(-i mod3), namely0,2,1. For EVERY remaining input y,
MOD3,0(y,padding)=MOD3,i(y), by |y|+s=0 mod3 iff |y|=i mod3. Substituting
constants never raises total degree. Restricting a pointwise guarantee
preserves its error and normalized real weights. All three residues on m
inputs therefore have degree<=17d, error1/12 witnesses. The modular argument
is for arbitrary m; the24573 truth-table tests for m0..12 are only controls.
The wrong sign +i fails already for residue1 and input weight1.

For n>=8, m>=6 and the elementary conditions3<=m/2 and
2^(-m)<1/12<1/9 hold. Applying the SOURCE theorem to its selected residue
then gives, asymptotically,17d>=c*sqrt((n-2)*log4), with the source's positive
constant and sufficiently-large-n qualification. Consequently the ORIGINAL
predicate has the KNOWN Omega(sqrt(n)) lower bound. We do not extract an
explicit c or threshold from asymptotic notation. In particular this does
not settle degree2 at n12. The adapters above are reconstructed reasoning;
the difficult lower-bound lemma remains an imported literature result.

## Missing mathematical ingredient and boundaries

First small formal target: finite-product real distributions, actual
polynomial substitution, pointwise error reduction, and residue restriction.
FIRST MISSING HARD INGREDIENT: the universal growing-degree low-degree
agreement/dimension argument underlying Smolensky's lower bound. Existing
layer profiles and degree-one exclusion do not establish it. Assuming the
desired lower bound as a hypothesis is not a reconstruction of that theorem.

The next research cycle should choose an accessible original/author source
for that hard ingredient, extract its actual constants/ranges, and reconstruct
a bounded first lemma. Do not substitute n13 enumeration or more audit tooling.
A circuit lower bound additionally needs the size/depth/error-preserving
AC0[2]-circuit-to-probabilistic-polynomial connection. No such new circuit
result, unrestricted P-vs-NP result, novelty or proof-barrier escape is claimed.
