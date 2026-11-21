# A positive error radius need not lower the required polynomial degree

**Scope.** This is a written elementary argument for Boolean functions and
polynomials over GF(2), reconstructed from scratch. It audits what the new
uniform-average error budget actually permits. It does not assert an actual
degree for the compiled proof function without its separate measured
algebraic-normal-form result. No mathematical novelty or proof-assistant
verification is claimed.

## Minimum nonzero weight, with proof

Let q be a nonzero multilinear polynomial over GF(2) on m Boolean variables,
with exact degree D, where `0<=D<=m`. Its truth-table Hamming weight obeys

    wt(q) >= 2^(m-D).                                (1)

For D=0, q is the constant one polynomial, with weight `2^m`, including
the case m=0. For D>=1, choose a variable that occurs in a degree-D monomial
and separate it:

    q(x',t) = q_0(x') + t q_1(x').

The coefficient polynomial `q_1` is nonzero and has exact degree D-1.
For every x' with `q_1(x')=1`, the two values q(x',0) and q(x',1) differ,
so exactly one is one. For every other x', the fiber contributes either
zero or two ones. Thus

    wt(q) >= wt(q_1)
          >= 2^((m-1)-(D-1))
          = 2^(m-D),

where the middle step is induction on m. This proves (1) with all
boundary cases. The product of D distinct coordinate variables attains
the bound; when D=0 its empty product is one.

## Error between an exact-degree target and a lower-degree polynomial

Let a nonconstant Boolean function f on the m-cube have exact GF(2)
algebraic degree D in its unique multilinear representation. Let p be
any polynomial over GF(2) of total degree at most d, where d<D.
Multilinearizing p by replacing positive powers of each Boolean variable
by that variable preserves its values on the cube and cannot increase
degree. Consequently the error function

    e = f+p

has exact degree D: none of f's degree-D monomials can be canceled by
the lower-degree representation of p. Since disagreement over GF(2)
is precisely the value e=1, (1) gives

    |{x : f(x)!=p(x)}| >= 2^(m-D),
    Pr_x[f(x)!=p(x)] >= 2^(-D).                       (2)

The argument does not require the presented polynomial p to have already
been multilinear. It does require GF(2), Boolean input coordinates and
the actual exact algebraic degree of f on the entire addressed cube.
If unused addresses are filled differently, that changes f and can change D.

Constant targets have degree zero and are exactly represented by constant
polynomials. For the common convention that allowable degree cutoffs are
nonnegative, there is no lower cutoff to exclude. If the zero polynomial
is assigned degree minus infinity instead, the only lower-degree
competitor to f=1 at D=0 is zero, which disagrees everywhere, consistently
with (2). Do not assign a nonzero-degree argument to the zero target.

## Fixed distributions do not evade this distance

Choose one probability distribution of global degree-at-most-d
polynomials before the input, with d<D. Every sampled p has at least
`2^(m-D)` erroneous bits by (2). Therefore

    E_p |{x : f(x)!=p(x)}| >= 2^(m-D),
    E_p Pr_x[f(x)!=p(x)] >= 2^(-D).                   (3)

Finite, normalized nonnegative mixtures are covered directly; no
independence between errors at different inputs is needed. The same
inequality holds for any well-defined probability distribution supported
on such polynomials. An input-dependent choice of p would be a different
quantifier order and is not allowed. A pointwise error guarantee also
implies the uniform-average guarantee, so (3) remains an obstruction
for that stronger requirement.

## Consequence for the cross compiler

The actual cross layout has `Q=2^22=4,194,304`, exact unrestricted
signed sensitivity 23 and exact NO minimum 109. The sufficient
uniform-average threshold is

    eta < 109/(23Q),
    Q eta < 109/23 = 4 + 17/23.                      (4)

Thus four arbitrary erroneous bits are uniformly tolerated by the
linear transfer bound. The separately supplied
[ANF computation](degree-checks.json) reports
exact D=18, with 202 nonzero degree-18 monomials, for the particular
honest cross-compiler YES proof with **zero at every unused padding
address**, using the [specified convention](degree-notes.md). The
following mathematical implication takes that exact
degree computation as its input; this note does not independently
certify the ANF algorithm or its output.

For that specified function, every lower-degree p has at least

    2^(22-18) = 16 > 109/23

errors. No fixed mixture of lower-degree polynomials can meet (4).
The exact polynomial for f, taken with probability one, does meet (4)
at degree 18. Under this measured-degree condition, the minimum
existential degree needed for the stated approximation budget is
therefore **exactly 18**. The positive four-bit radius still does not
lower that degree. This is a statement about one fully specified proof
function, not the minimum degree over all satisfying proofs, arbitrary
values on free padding, or alternative encodings.

This reasoning differs from the earlier integer-only obstruction:
the old budget was less than one error and forced some exact polynomial
without using its degree. The new budget is larger than one, but the
nonzero error functions of all lower-degree competitors can be separated
from f by a larger, rigorously quantified distance.

The same obstruction applies to any target on this cube of exact degree
D<=19, since its lower-degree error distance is at least eight. The
boundary is substantive. At D=20, (2) guarantees only four errors,
which is below `109/23`; the argument alone then cannot exclude a
qualifying lower-degree approximant. For example, the product of 20
coordinates on a 22-cube has exact degree 20 and differs from the zero
polynomial at exactly four inputs. This is a sharpness example for the
degree argument, **not** an approximant for the compiled truth function.
At D=21 or 22, the corresponding universal bounds are only two or one
errors. Additional structure of the actual function would be needed.

In general, a strict budget `E_p |E_p| < T` excludes every polynomial
mixture with cutoff below D whenever `2^(m-D)>=T`; equality still
excludes because the budget is strict. Here T is `109/23`.

## What must remain separate in the conclusion

1. The actual raw sensitivity improvement and four-bit sufficient radius
   remain valid statements about the implemented verifier.
2. Their consequence for approximation degree depends on the exact
   GF(2) degree of the new, fully padded proof function and on (2).
3. The old and new address encodings are different Boolean functions.
   An equality of approximation and exact degree for each target does
   not by itself compare those two degrees.
4. A symbolic growing ratio `V_NO/sigma` does not establish a useful
   lower-degree approximant for the growing encoded family. Its degree,
   nonzero error distance, padding and Q must be priced together.
