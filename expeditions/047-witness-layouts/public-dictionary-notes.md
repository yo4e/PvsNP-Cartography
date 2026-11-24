# Public symbolic dictionaries: a sufficient structural condition

Status: a written elementary derivation with a standalone finite control.
This is a new constrained witness relation, not a modification of Expedition046.
No novelty, Lean acceptance, hard language, or general PCP result is asserted.

## Statement and quantifiers

Let the public instance specify R distinct physical rows and seed space
{0,1}^k, N=2^k. Let W_I be its admissible witnesses. Suppose public syntax
supplies an L-element dictionary phi_1,...,phi_L and public coefficient
vectors c_i in GF(2)^L such that, for every w in W_I and every seed z,

    f_i(w,z) = sum_l c_i,l phi_l(w,z).

Require that z -> phi_l(w,z) has degree at most delta for every fixed w.
The dictionary identities and this degree bound require a derivation;
observing them at one known witness is insufficient. The compiler must compute
the dictionary representation from public syntax without finding w.

For each repeated coefficient vector, give its rows distinct ranks. Let
M=max_c |{i:c_i=c}| and r=ceil(log2 M). Assign the public row tag (c_i,rank_i)
and define, for each fixed but unknown satisfying witness,

    P_w(c,rank,z) = sum_l c_l phi_l(w,z).

The tag map is independent of w. Every used bit agrees, the whole completed
truth table has degree at most delta+1, and the padding cube is exactly

    Q' = N 2^(L+r).

The rank bits are ignored by P_w, but never by the address map: rows of equal
value or equal symbolic signature remain physically distinct. In particular,
Q' <= 2 N 2^L M <= 2 N 2^L R. The expansion is polynomial in N R if
L=O(log(NR)). This condition is sufficient, not necessary.

All original tests retain their signs and their seed-coordinate projections;
only constant tag coordinates change. Injectivity gives a bijection between
assignments on the old and new *used* physical cells. Thus raw failure counts,
NO minima and signed sensitivity about each reference are identical. Unused
padding is unconstrained. Normalized approximation thresholds pay the actual
Q' denominator.

The theorem is `for every I, public layout(I), for every admissible w, exists
P_w`. The compiler never has to construct P_w or compute a satisfying witness.
The assumed polynomial-approximation theorem, if any, is a separate hypothesis.

## A syntax check that supplies the dictionary

For a straight-line XOR/AND computation on m witness inputs and k seed inputs,
introduce the dictionary

    1, w_1,...,w_m, z_1,...,z_k, outputs of each of A AND gates.

Every wire has a public coefficient vector: XOR adds vectors, NOT adds the
constant, a copy preserves the vector, and each AND output receives its own
new basis coordinate. This uses L=1+m+k+A and does not evaluate the witness.
The AND outputs themselves are functions phi_l defined by the public circuit.
If the maximum number of AND gates on an input-to-wire path is h, induction
gives seed degree at most min(k,2^h) after fixing the witness. Thus the completed
proof has degree at most 1+min(k,2^h). Affine circuits (A=0) give degree at most
two with potentially many unknown witnesses.

This condition is useful only when the dimension and seed degree are small
enough. A polynomially long XOR network with few AND gates qualifies; a generic
large private Boolean compiler need not. More economical public dictionaries
may exist, but witness-specific constant folding cannot be used to justify
their public dimension. This construction does not claim that every efficient
proof computation has a small dictionary.

## Exact standalone control

The relation is w0*w1=0 on two unknown bits; it has the three witnesses 00,01,10.
There are two seed bits and twelve physical rows:

    1, w0, w1, z0, z1, u=w0+z0, v=w1+z1,
    uv, p=w0*w1, u+v, copy(u), copy(uv).

The public symbolic dictionary is (1,w0,w1,z0,z1,uv,p), L=7.
There are two duplicate signatures, each of multiplicity two, so r=1.
The fixed public tags, in the displayed row order, are

    1,2,4,8,16,10,20,32,64,30,138,160.

The compact seed-times-row cube has Q=64. The public symbolic cube has
Q'=1024, a factor sixteen. All three satisfying witnesses have the same tags.
This is polynomial overhead in this finite example, not an asymptotic claim
that the factor sixteen is universal.

The executable constructs the actual signed CNF: one-row and seed pins,
three XOR definitions, two AND definitions, two private copies, the unit p=0,
and copies enforcing each witness row to equal its seed-zero value. It has
116 expanded YES clauses. The NO variant adds w0=w1=1 at every seed and has
124 expanded clauses. These counts are **expanded physical clauses**, not
numbers of common randomized templates. Every query address is fixed or a
constant row tag followed by the seed or zero coordinates; the finite code
expands the public seed pin signs rather than claiming a new source-PCP
template compiler.

These are exactly the three satisfying proofs, not merely three exhibited
ones: the unit clauses fix one and the seed rows; witness-copy clauses make
each witness row constant; gate clauses and private copies determine every
remaining row; and p=0 excludes precisely w=11.

For every assignment on the NO proof, each seed's local AND(p,w0,w1), p=0,
w0=1,w1=1 subsystem has at least one failure. These four subsystems have
disjoint physical row cells. Hence the raw NO minimum is at least four.
The honest circuit evaluation at w=11 attains exactly four failures, so the
minimum is exactly four. This is not the predecessor's 109 or 477.

The public completion has degree three at every witness. This is optimal
over all padding choices: the all-seed slices of rows one and uv together
form an affine 3-cube whose parity is one. The former slice has parity zero;
the latter is (z0+w0)(z1+w1) and has parity one. Every polynomial of degree at
most two has even parity on every affine 3-cube. Thus no degree-two
completion matches all used cells under the public layout.

The exact signed mixed-error coefficient is 9/2 about w=00 and 5 about each
of w=01,10. For an AND definition, failed clauses are bounded by
e_a+e_b+2e_c; XOR uses e_a+e_b+e_c and a copy uses e_a+e_c. At the reference
AND inputs 00 the sharper half(e_a+e_b)+2e_c is valid. Applying that sharper
bound to p at w=00 gives maximal global load 9/2. Flipping both witness cells
at seed zero produces nine failures (six constancy, two XOR, one AND),
attaining 9/2. At 01 or 10, flipping the zero witness cell at seed zero
produces five failures (three constancy, one XOR, one AND), attaining five.
All other row loads are at most four. These are all-error charge arguments;
the executable checks their local truth tables and the attaining sets.

The common strict uniform-error threshold is therefore

    eta < 4/(5*1024) = 1/1280.

It is below one erroneous bit. Exact degree-three completion makes the
example feasible anyway; this is not an improved positive-error regime.
The example is easy and supplies no complexity-class lower bound.

The budgeted minimum degree over padding is also three for each satisfying
proof. The odd affine cube forces every degree-at-most-two polynomial to
make at least one used-cell error. Each reference's strict raw error budget
is below one: 4/(9/2)=8/9 at 00 and 4/5 at 01 or 10. Therefore every fixed
mixture consisting of such lower-degree polynomials has mean error at least
one and also fails the threshold. The degree-three exact completion attains
zero error.

## Execution and limits

`check_public_dictionary.py` verifies the actual census, all four witness
evaluations, every used tag, exact completed ANFs, the padding-independent
odd parities, 72 local charge truth tables, and 4552 changed or independently
sampled global assignments. All size-one and size-two error sets are included
about each satisfying proof; the randomized controls use seed 20261124.
The finite controls supplement the separate injection/charge arguments;
they do not replace their universal quantifiers.

Source-lineage limitation: this is one additional same-model exploratory
branch, not an independent external review or a proof-assistant kernel.
