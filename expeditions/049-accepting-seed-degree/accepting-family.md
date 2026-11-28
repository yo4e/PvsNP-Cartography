# A residual-constrained three-witness family, and why its raw rows stay easy

Status: written classification plus exact finite evidence; novelty-unknown.
This is a **source-shaped designed residual**, not the full Ben-Sasson--Viola
ACSP family on a growing Boolean assignment domain. The actual GF(256)
two-level B geometry, physical sharing and field tests are reused from
Expedition041, with the public normalization from Expedition048. No complete
Boolean compiler, new NO gap, Lean acceptance or complexity-class result is
claimed.

## 1. The new public constraint

Let F=GF(256), in the same polynomial basis as Expedition041, and let

    T0(X)=(X+1)(X+2)(X+3),
    Z(X)=X(X+1)(X+2)(X+3).

The stored A word must pass its direct affine test, so A(X)=c+sX over F.
The stored B word and its 16,128 extension symbols use the actual two-level
paired RS test with strict root degree cutoff32. The A/B values read by the
residual are exactly their stored roots, not detached copies.

Define

    N_A(X) = T0(X)(A(X)+1)^2(A(X+1)+1)
             + X(X+1)A(X+2)(A(X+2)+1),

and test H_A,B(X)=N_A(X)+Z(X)B(X)=0 at each field seed. All arithmetic is in
characteristic two. The first term is the falsification product for the
Boolean clause A(0) OR A(1), repeating its first literal to have width three.
Positions2 and3 carry Boolean-range conditions. Position1 imposes no clause;
its selector term is identically zero. This choice is explicitly part of the
new designed instance.

At H={0,1,2,3}, write a0=A(0) and a1=A(1). The four residual values, regardless
of B, are

    6(a0+1)^2(a1+1),   0,   6a0(a0+1),   6a1(a1+1).

The coefficient6 is a nonzero field element. Consequently, full acceptance
forces a0,a1 in{0,1} and a0 OR a1=1. Since two values determine an F-affine
polynomial, the only possible A polynomials are1, X and1+X.

## 2. Full acceptance covers every leaf and determines the auxiliary proof

This part concerns **all global assignments** to the used field cells, not
only the three subsequently generated witnesses.

For z=u+16v, the original bundled proximity test selects:

- outer columns c=u+16h, for h=0,...,3;
- inner rows j=2f+floor(u/8), for f=0,...,7, within outer row v;
- inner columns c=(u mod8)+8h, for h=0,...,3, within outer row v.

Varying z covers all64 outer columns, all16*16=256 inner rows and all16*32=512
inner columns, totaling832 leaves. Full acceptance of the paired test
V(z) AND V(z XOR9) implies full acceptance of V(z), hence every leaf passes.

Within each outer row, all inner rows have degree at most7 and all common
inner columns are affine in their actual ordinates. Interpolate two inner
row polynomials in the ordinate. Agreement on at least eight common abscissas
extends to every point of each inner row. This recovers the entire outer
word as a polynomial of degree at most15. The physical parent/row/column
aliases are essential: all compared values are the same stored cells.

Repeat at the outer level. Its row polynomials have degree at most15, its
common columns are affine, and there are64 common abscissas. Interpolating two
outer rows and using sixteen common points yields a root polynomial of
degree at most31. Projecting extension-field coefficients to F preserves its
agreement with the F-valued root. This is the complete-acceptance case of the
existing Expedition041 interpolation argument, not a newly proved proximity
theorem.

Every outer-row polynomial is uniquely determined by its16 distinct parent
points; every inner-row polynomial is uniquely determined by its8 parent
points. Therefore fixing a fully accepting B root fixes **every used B
extension symbol**. Columns have no independent copies. No alternative
auxiliary field proof remains hidden behind the displayed roots.

## 3. The quotient is forced, and there are exactly three field proofs

Since A is affine, deg N_A<=6. Since the recovered B polynomial has degree at
most31, deg H_A,B<=35<256. Full acceptance on all256 seeds therefore makes
H_A,B the zero polynomial. It follows that Z divides N_A and B=N_A/Z as
polynomials. This is a polynomial identity; pointwise division away from H
would be insufficient.

The resulting classification is:

| A(0),A(1) | A(X) | N_A(X)/Z(X)=B(X) |
|---|---|---|
| 1,1 | 1 | 0 |
| 0,1 | X | X^2 |
| 1,0 | 1+X | X^2+X+1 |

For A=X, the first term is Z(X)(X+1)^2 and the second term is Z(X), giving
N_A=ZX^2. For A=1+X, the first term is ZX(X+1) and the second is Z, giving
N_A=Z(X^2+X+1). For A=1 both terms vanish.

Each listed B has degree below32 and has its unique honest two-level
extension. It passes every leaf, and the residual vanishes identically.
Conversely, Sections1--2 and the degree argument exclude every other used
field proof. There are thus **exactly three fully accepting used field
assignments**, comprising the256 A root symbols and16,384 physical B symbols.
Arbitrary bits in unused ambient padding are outside this count. No Boolean
gate or copy rows have been added to this field-level object.

## 4. A general degree collapse in this affine-A toy regime

The easy roots are structural. Suppose a similar residual has a numerator
which is a sum of products of degree-at-most-three selector polynomials and
at most three shifted copies of an affine A, with optional signs/constants.
Its degree is at most6. If the same degree-four Z divides that numerator,
then any polynomial quotient has degree at most2. If complete acceptance
and the RS cutoff justify the polynomial identity, no high-degree B can
survive merely because the ambient RS code permits degree31.

This statement needs the degree budget: for a field of size q and a B cutoff
D, require max(6,D+4)<q before inferring identity from q zero evaluations.
It is a bound on the polynomial quotient, not an assertion that every
arbitrary truth table satisfying the pointwise residual is low degree.

Nor is the direct affine-A condition a plausible model of a growing Boolean
assignment domain. If s!=0, the F-affine map c+sX is injective and can take
values in{0,1} on at most two input points. Requiring Boolean values on a
larger domain forces A to be constant. The present two-site OR relation is
therefore deliberately small. A source-like scaling experiment must enlarge
the allowed A polynomial/witness class and reprice its verifier, rather than
repeat this affine fixture at larger fields.

## 5. Actual normalized raw rows

There are64 normalized symbol rows for B, with256 seed positions per row.
The root row has8 physical bits and each other row16 bits, so B has1,016 raw
bit rows. A has8 additional raw bit rows.

For the actual k=8,a=3 geometry, every fixed normalized row has an extension
field abscissa affine in the seed. One can see this without extrapolating from
the truth table. Write z=u+16v. For fixed outer fresh bits p0,p1,p2,

    beta=theta+16v,
    x_outer=(1+p2)beta+u+p0*C1+p1*C2+p2*C0.

For an inner row, write z's low nibble as z0..z3. Its intermediate origin is

    delta=(1+p2)beta+8*z3+p0*C1+p1*C2+p2*C0,

and, for fixed inner fresh bits q0,q1,q2,

    x_inner=(1+q2)delta+(z mod8)+q0*D1+q1*D2+q2*D0.

All C and D values are the fixed auxiliary directions from the actual field
implementation. Thus these are affine functions of the root seed bits.

For a quadratic B=b0+b1X+b2X^2, the globally translated polynomial
B(X+theta) already has degree less than both16 and8. By row interpolation
uniqueness it equals the actual honest value at every physical row point.
Squaring is GF(2)-linear in characteristic two, so each component bit of its
composition with the displayed affine abscissa is affine in the seed.
This proves the raw-row degree bound for all three classified proofs in the
actual two-level geometry. It does not bound gates introduced by a Boolean
evaluation circuit.

Exact measured B rows:

| Accepting root pair | Zero rows | Nonzero constant rows | Degree-one rows | Distinct ANFs | GF(2) span dimension |
|---|---:|---:|---:|---:|---:|
| A=1,B=0 | 1,016 | 0 | 0 | 1 | 0 |
| A=X,B=X^2 | 328 | 400 | 288 | 26 | 9 |
| A=1+X,B=X^2+X+1 | 352 | 360 | 304 | 24 | 8 |

A=1 has seven zero bit rows and one constant-one row; the two nonconstant A
words each have eight degree-one bit rows. Every complete field proof is
therefore easy in seed degree. This answers an existential-versus-universal
ambiguity for this fixture: it does not merely exhibit one easy witness
while leaving other accepting witnesses unclassified.

## 6. Attacks and actual checks

The executable enumerates all65,536 possible affine endpoint pairs and gets
exactly the three stated solutions. Independent polynomial operations derive
their quotient coefficients and compare the symbolic numerator with scalar
field evaluation on every seed. It generates their actual shared physical
extensions, checks all832 leaf tests and all256 residual values for each,
and transports every symbol through Expedition048's canonical normalization.
The field arithmetic and leaf implementation are reused, explicitly.

Two negative controls prevent easy but false shortcuts:

1. Change B's lowest root bit at0 in the A=X proof, keeping every extension
   cell fixed. Z(0)=0 makes the new residual blind to the error: all256 seeds
   still satisfy it. The unpaired RS test accepts248, the paired test240,
   and the joint verifier rejects16. Thus residual equality alone does not
   determine the four masked root sites; the shared low-degree proof matters.
2. Take A=0 and the pointwise B(0)=0, B(x)=1/x for x!=0, extending its rows by
   the same interpolation algorithm. The residual accepts255 seeds, but all
   outer columns fail and the paired RS predicate accepts none. A pointwise
   quotient cannot replace the polynomial quotient or its degree premise.

The figure221 from the predecessor's different NO instance is not used or
transferred. This new object has three accepting field proofs and no newly
claimed NO gap. Its measured degrees do not constitute a weighted Boolean
error obstruction. They locate the next substantive question: how source
constraints and their compiled gate rows acquire seed dependence after the
affine-A toy restriction is removed, and how much of that dependence is
intrinsic rather than an artifact of a chosen implementation.
