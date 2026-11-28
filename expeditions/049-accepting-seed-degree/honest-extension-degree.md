# Honest RS extension preserves raw degree in the actual two-level fixture

Status: written scoped argument plus exact finite evidence; novelty-unknown.
The field arithmetic, interpolation, physical aliases and leaf predicates are
the actual Expedition041 implementation. Physical normalization is reused
from Expedition048. This note concerns honest raw field proof values, not a
Boolean compiler's gate rows, arbitrary false proofs, a new NO gap, or generic
unbounded recursion.

## 1. Fixed-node degree-filtered basis lemma

Let K=GF(2^m), let s=2^ell with 0<=ell<=m, and let q(X) be a fixed monic
GF(2)-linearized polynomial of degree s. For a polynomial P of degree <2^m,
write its unique q-adic expansion as

    P(X) = sum_{0<=i<s, 0<=j<2^(m-ell)} c[i,j] X^i q(X)^j.

The uniqueness follows from triangularity: X^i q(X)^j is monic of degree
i+s*j, and these leading degrees run through 0,...,2^m-1 without repetition.
The polynomials are therefore a K-basis of polynomials of degree <2^m and,
by the field root bound, of K-valued functions on K.

Give the (i,j) basis element weight wt2(i)+wt2(j). Its Boolean vectorial
degree is at most that weight: X and q(X) are GF(2)-linear; each Frobenius
power is GF(2)-linear; binary expansion of the exponents gives a product of
at most wt2(i)+wt2(j) linear factors. A constant field multiplier is linear
on the output bits and does not increase degree.

For each r, the number of basis elements of weight <=r is

    sum_{d=0}^r binom(m,d),

because the ell bits of i and m-ell bits of j concatenate to m bits. This is
also the K-dimension of all K-valued Boolean polynomials of degree <=r on m
input bits. The low-weight basis elements are independent and belong to
that space, so they span the entire space. Uniqueness of the full basis
expansion then gives, for every nonzero P,

    deg_Bool(P) = max{wt2(i)+wt2(j): c[i,j] != 0}.

The zero polynomial has degree -1 by convention. The special case of the
ordinary monomial basis gives deg_Bool(P)=max{wt2(e): [X^e]P != 0} for the
unique univariate representation of degree <|K|.

Consequently the bivariate polynomial

    Q(X,Y) = sum c[i,j] X^i Y^j

has Boolean degree at most r=deg_Bool(P). Substituting any jointly affine
maps X(z),Y(z) into K preserves the upper bound r. The coefficients and q
must be fixed independently of the varying seed z in this conclusion.

## 2. What is actually fixed in Expedition041

The root field is F=GF(256), with the existing 0x11B binary basis, and the
extension field is E=GF(65536). The root's physical abscissa is theta+x.
The actual internal nodes are the dimension-eight root and its sixteen
dimension-seven row children. Column children are leaves; there is no
third decomposition stage in this fixture.

The root vanisher uses the fixed low space span_F2{1,2,4,8}:

    q0(X)=X^16 +167 X^8 +129 X^4 +80 X^2 +119 X.

Every row child's vanisher uses the fixed low space span_F2{1,2,4}:

    q1(X)=X^8 +102 X^4 +86 X^2 +49 X.

The displayed coefficients are encoded field elements, not integer
arithmetic. Both vanishers are monic and GF(2)-linearized. Their coefficients
are independent of the varying outer-row label v.

It would nevertheless be false to say that all full node bases depend only
on path shape. Let C0,C1,C2 be the fixed outer auxiliary directions, let
D0,D1,D2 be the fixed inner auxiliary directions, and put beta=theta+16v.
An outer row has full basis

    (1,2,4,8,C1,C2,C0+beta),

and an inner row with origin delta has full basis

    (1,2,4,D1,D2,D0+delta).

Thus the full bases vary with seed-dependent node labels. The exact census
contains sixteen distinct outer full bases and 136 distinct inner full
bases. Only the relevant lower spaces used for q0 and q1 are fixed. This
is sufficient here because the remaining physical coordinate dependence
is affine after fixing a normalized fresh-coordinate row.

## 3. A scoped argument for every honest degree-<32 root polynomial

Let P in F[X] have degree <32, and let

    r=max{wt2(e): [X^e]P != 0}.

This equals the root's vectorial Boolean degree. The same polynomial P has
degree below both |F| and |E|, so the canonical binary-exponent-weight
identity gives the same Boolean degree r on E as on F. This conclusion
uses that polynomial representation, not a generic extension of a function
from a subspace. Set T(X)=P(X+theta). Translation preserves Boolean degree
over E, so T also has degree r. The preceding lemma, now with K=E, gives

    T(X)=R0(X)+R1(X)q0(X),  deg Ri<16,
    Q0(X,Y0)=R0(X)+R1(X)Y0,

with total binary-weight degree <=r. For a fixed actual outer row v, set
Y0=q0(beta). On all sixteen parent abscissae, q0(X)=Y0. Thus
Q0(X,Y0) agrees with the stored root values there and has X-degree <16.
By interpolation uniqueness, it is exactly the outer row polynomial
produced by the actual honest extension algorithm.

Apply the fixed-node lemma to each Ri using q1. This gives

    Ri(X)=S0i(X)+S1i(X)q1(X),  deg Sti<8,

and hence

    Q1(X,Y1,Y0)=sum_{t,i in {0,1}} Sti(X) Y1^t Y0^i.

Its total binary-weight degree is still <=r. To see the bound explicitly,
the coefficient polynomial of Y0^i in Q0 has Boolean degree at most
r-wt2(i); its q1-adic expansion preserves that bound. Restoring the factor
Y0^i gives total weight at most r.

For a fixed inner row with origin delta, substitute Y1=q1(delta), retaining
the outer row's Y0. On its eight shared parent abscissae, q1(X)=Y1. The
polynomial Q1(X,Y1,Y0) therefore agrees with the actual outer row there and
has X-degree <8. It is exactly the interpolated inner row polynomial.
This identifies the actual recursive extension; it does not substitute the
generally incorrect global value P(X+theta) at high-degree child points.

Now fix a normalized outer fresh tag p=(p0,p1,p2) and, for an inner row,
an inner fresh tag b=(b0,b1,b2). Write the root seed as z=u+16v, with
u in{0,...,15}; let z3 be its fourth low bit. The actual abscissae are

    beta = theta+16v,
    X_R = (1+p2)beta +u+p0 C1+p1 C2+p2 C0,
    delta = (1+p2)beta +8 z3+p0 C1+p1 C2+p2 C0,
    X_RR = (1+b2)delta +(z mod8)+b0 D1+b1 D2+b2 D0.

For fixed tags these are affine maps of the eight root bits into E.
So are Y0=q0(beta) and Y1=q1(delta), because the two vanishers are fixed
linearized polynomials. Substituting them into Q0 and Q1 proves that every
normalized physical bit row of the actual honest extension has degree
at most r. The root is among these rows and attains r, so the maximum over
all physical rows is exactly r.

This statement covers every P of degree <32, not only monomials or the
three accepting proofs from the separate residual-constrained fixture.
It does not assert that every such root satisfies that residual. Actual
offset queries are fixed-row seed translations after normalization, so
the same raw-value degree bound also holds after those query substitutions.

## 4. Exact finite audit

The standalone checker calls the existing legal_extension(e) for each
e=0,...,31, runs all actual leaf predicates, transports all 16,384 symbols
through the canonical physical normalization, and computes every vector
ANF and every actual raw bit-row degree. It also expands (X+theta)^e by
the two fixed vanishers and checks the polynomial reconstruction identities
and coefficient weights. The actual point and ordinate functions are
independently checked to be affine on each of the64 normalized rows.

All32 monomials pass every leaf. Every physical raw row has degree at most
wt2(e), and the root supplies equality. Both q-adic coefficient expansions
have maximum weight exactly wt2(e) as well.

| Maximum raw degree | Monomial exponents with that degree |
|---|---:|
| 0 | 1 |
| 1 | 5 |
| 2 | 10 |
| 3 | 10 |
| 4 | 5 |
| 5 | 1 |

In particular e=8 and e=16 retain degree one even though their honest
recursive extension must be computed by row interpolation. Exponent31
has degree five; it is not an exception to preservation.

The finite audit checks26,624 actual leaves,32,512 raw bit rows,
8,323,072 bit truth values, and524,288 vector ANF coefficients. These
are exhaustive finite checks for this implementation, not a substitute
for the scoped argument above or an independently reimplemented source
theorem. No Lean acceptance or novelty is claimed.

## 5. Why the fixed-node lemma alone cannot justify generic recursion

A varying vanisher can invalidate the inference even when its coefficients
vary affinely. For a simple countercontrol, choose alpha in K outside GF(2),
let z1,z2 be Boolean variables, and put

    a(z)=alpha+z1,
    q_z(X)=X^2+a(z)X.

Every q_z is the monic linearized vanisher of the two-point subspace
{0,a(z)}. For P(X)=X^2, which has Boolean degree one, its fixed-node
expansion is

    P(X)=q_z(X)+a(z)X,
    Q_z(X,Y)=Y+a(z)X.

Each Q_z has degree one when z merely indexes a fixed node. But substituting
X=z2,Y=0 jointly with the varying parameter gives

    alpha*z2+z1*z2,

of Boolean degree two. This is a counterexample to an unqualified inference
from fixed-node degree preservation; it is not an asserted counterexample
inside the actual BV recursive construction.

For deeper or different source geometries, one must audit the low subspaces,
their vanisher coefficients, any seed-dependent choices of auxiliary
directions, and the joint coordinate maps along the entire normalized row.
The dimension-eight/two-level fixture avoids that gap because q0 and q1 are
fixed and all remaining displayed substitutions are affine. No generic
recursive theorem follows solely from the32 checked monomials.

## 6. Consequence for the current discriminator

In this actual fixture, honest RS auxiliary storage does not itself increase
the maximum raw Boolean degree of a degree-<32 root polynomial. Any degree
growth observed only after Boolean compilation therefore needs to be located
in the compiled computation or in a changed residual/root family. A source
scaling argument must separately address deeper geometric dependence; the
present result removes one possible source of hidden inflation at the first
genuinely recursive geometry.
