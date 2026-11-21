# The exact and budgeted minima over free padding are both 17

**Scope.** Fix every used physical bit of the primary cross/cap-21 honest
YES proof: A(x)=1+x, B(x)=x with its honest shared extension, and truthful
private gates, copies, constants and public cells. Only unused padding
values are free. This note proves the completion and error-obstruction
principles; [padding-checks.json](padding-checks.json) supplies the actual
finite values and [padding-notes.md](padding-notes.md) specifies the
constructed completion. No optimization over other physical proofs or
encodings, general-family conclusion, Lean result or novelty is claimed.

## 1. A downset determines exactly the coefficients that matter

Identify cube points and squarefree monomial supports with nonnegative
integer bit masks. Write `T subseteq S` when T is a bitwise submask of S.
A set I is a downset if `S in I` implies every submask of S lies in I.
Let a specify Boolean truth values on a downset I. For each `S in I`, put

    c_S = XOR_{T subseteq S} a(T).                    (1)

These coefficients depend entirely on specified coordinates. Every total
extension f of a has exactly these ANF coefficients at masks in I, because
the coefficient formula (1) uses no truth value outside I. Hence every
extension's degree is at least

    d_I = max{|S| : S in I and c_S=1}.                (2)

This lower bound is attained by the polynomial

    P_I(x) = XOR_{S in I, c_S=1} product_{i in S} x_i. (3)

Indeed, at any x in I, only supports S that are submasks of x can
contribute, and all such supports lie in I. Substituting (1), the value
a(T) appears `2^(|x|-|T|)` times. Over GF(2), every multiplicity is even
except at T=x. Thus `P_I(x)=a(x)`.

Equivalently, start from any extension's ANF and set every coefficient
indexed outside I to zero. This preserves all specified truth values
and gives the canonical minimum-degree completion (3). It need not set
the *padding truth values* to zero. Zero padding in the truth table and
zero free coefficients in ANF are different conventions.

If every coefficient in (1) is zero, the zero polynomial is a completion;
its algebraic degree may be called minus infinity, or the least allowed
nonnegative degree cutoff is zero. The present nonconstant fixture has
`d_I=17`, so this convention does not affect its conclusion.

## 2. Application to the physical prefix

The address is `(physical tag << 7) | seed`. The 21,845 used rows occupy

    I = [0,M),   M=21,845*128=2,796,160.

The full address cube has Q=2^22 points. The remaining 10,923 rows, or
1,398,144 bits, are unused by every physical clause. The prefix I is a
downset because a submask of x is no larger than x as an integer.

The retained zero-padded target had exact degree 18, but all its 202
degree-18 coefficient masks are at least 4,063,119, outside I. Removing
all coefficients outside I therefore immediately gives degree at most
17 and changes no used bit. An unresolved degree-at-most-17 completion
search would have been the wrong next question: the existing data
already determines that completion.

The actual canonical completion has exact degree **17**, with 202
leading coefficients and 833,770 nonzero coefficients in total. Its
reconstructed truth table matches every one of the M used bits and
satisfies the unchanged physical clauses. The lower bound (2) gives
the matching minimum degree over **all choices of padding**. The
computation records the truth-table and ANF hashes; this mathematical
note is not an independent replay of the implementation.

## 3. A fixed subcube blocks further degree reduction by four errors

There is also an obstruction supported wholly on used coordinates.
The subcube

    S = {x : address bit 21 is zero}

has dimension 21, contains `2^21=2,097,152` points, and lies entirely
inside I. The prescribed physical values restricted to S have exact
GF(2) degree **17**, independently of all padding choices.

Any global polynomial p of total degree at most 16 restricts to degree
at most 16 on S: substituting a fixed Boolean coordinate and
multilinearizing cannot increase degree. Its error relative to the
fixed values on S therefore has exact degree 17. By the elementary
[nonzero-weight argument](degree-bound-notes.md), it has at least

    2^(21-17) = 16

nonzero values on S. Those are **16 wrong used bits**, irrespective
of p's values in padding or the chosen target completion.

The argument has a direct parity-certificate form as well. Choose a
nonzero degree-17 coefficient mask L of this restricted function.
Its four complementary coordinates within S partition S into sixteen
disjoint 17-dimensional affine subcubes. Because the restricted target
has degree 17, its parity on each such subcube is the same leading
coefficient `c_L=1`. Every degree-at-most-16 polynomial has parity zero
on each: each of its monomials omits at least one varying coordinate,
so pairing points along that coordinate cancels its evaluations.
Each of the sixteen disjoint subcubes therefore contains at least one
disagreement. Directly checking these target parities makes an
independently inspectable obstruction supported on fixed coordinates.

The actual certificate chooses `L=1,965,967`, whose four complementary
coordinates are 4, 5, 6 and 17. Its sixteen base masks run over every
subset of those four coordinates; address bit 21 is fixed to zero.
The retained checker reads all 2,097,152 target bits directly across
these sixteen disjoint subcubes and obtains parity one in all sixteen.
Thus the lower obstruction can be checked without relying on the
ANF transform's claimed global degree or a search over approximants.

## 4. Exact quantifiers for padding and mixtures

Let f range over all total target functions with `f|_I=a`. Choose one
input-independent probability distribution on global degree-at-most-d
polynomials before the input, as in the original approximation setup.
For d<=16, every sampled polynomial has at least sixteen errors on
the fixed subcube S. Consequently

    E_p |{x : f(x)!=p(x)}| >= 16 > 109/23

for every f and every such distribution. No free padding can repair
these used-coordinate errors. The required strict uniform-average
budget is `E_p |E_p| < 109/23`, so degree at most 16 is excluded.
Conversely, choose the degree-17 canonical completion as f and sample
its exact polynomial with probability one. It has zero error. Hence

    minimum exact completion degree over padding = 17,
    minimum degree meeting the stated mean-error budget over padding = 17.

For a uniform-average objective, a mixture cannot beat the smallest
deterministic total error of its members. If its mean is less than
109/23, some member has at most four total errors. When the target
padding is free, the equivalent existence question is whether some
deterministic polynomial has at most four wrong used bits: matching
the target's padding to that polynomial adds no errors. This equivalence
is specific to existence under a uniform-average error bound; it is
not a claim that mixtures cannot help a pointwise guarantee.

A claim about one fixed distribution and target must not silently
choose a different target padding separately for each sampled
polynomial. The sixteen-used-errors lower bound avoids that ambiguity
because it holds on the same fixed subcube for every possible padding.

## 5. Research consequence and limit

Free padding lowers this fixed physical proof's exact target degree
from 18 to 17. The four-bit sufficient error allowance does not lower
it further: exact completion and budgeted approximation have the same
minimum degree 17. Neither degree-at-most-17 completion nor the
degree-at-most-16 four-error question for this fixed proof remains
open after these certificates.

This excludes the prescribed uniform-average approximation hypothesis
below degree 17. It does **not** prove that every lower-degree global
assignment incurs 109 physical clause failures; the linear sensitivity
bound is a sufficient transfer argument, and special error patterns
might require a different analysis. Changing the used physical proof,
the encoding, or the growing-family parameters is also outside this
fixed-proof completion result.
