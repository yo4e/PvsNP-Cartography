# Fixed-target degree audit: four tolerated errors do not lower this degree

The new cross compiler has a nonzero guaranteed error radius. That fact alone
does not show a weaker polynomial-degree assumption. On the specific honest
YES proof used for the compiler comparisons, with every unused address padded
by zero, the exact GF(2) algebraic degree is **18**. Every polynomial of total
degree at most 17 disagrees with it in at least **16** of its 4,194,304 bits.
The new strict mean-error budget is only 109/23 bits. Consequently the least
degree meeting that budget remains **18 for this fixed target**.

This does not optimize over free padding, other satisfying A/B proofs,
alternative gate assignments or encodings. In particular, padding is not
silently treated as forced by the verifier.

## The actual Boolean function audited

The executable constructs the primary cross layout with private fanout cap21,
sets A(x)=1+x and B(x)=x, fills the physically shared recursive extension using
the inherited honest construction, and fills every private gate, copy and
public cell truthfully. The physical clause failure count is zero.

There are 21,845 used tag rows. They are extended to 32,768 rows by explicitly
setting every bit of the remaining 10,923 rows to zero. Every row has 128
seed positions, so the Boolean function f has 22 address variables and
Q=2^22 positions. Address ordering is

    integer address = (physical tag << 7) | seed.

Variables 0 through6 are the little-endian seed bits. Variables 7 through21
are the tag bits. The truth table has 778,684 ones. Its packed, little-endian
bit-stream SHA256 is

`4a2e3c5b80334ccadd7bef946c6afea95c94e9bf422b6da22bd305326a816761`.

The function changes if free padding is changed. The result below must not be
quoted as the smallest degree among all valid proof encodings.

## Exact algebraic normal form

For a mask S, the coefficient of the squarefree monomial consisting of the
variables in S is

    c_S = XOR_{T subseteq S} f(T).

`check_degree.py` computes all coefficients exactly over GF(2). It packs 64
consecutive truth values into each Python integer. The first six Mobius
butterfly stages use masks and shifts within those words. The remaining
sixteen stages XOR entire words. All arithmetic is exact and the script has
no external runtime dependency.

The result is:

- 1,261,076 nonzero coefficients;
- exact maximum monomial degree18;
- 202 nonzero coefficients of degree18;
- zero coefficients of degrees19 through22.

All 202 leading monomial indices and the complete degree histogram are in
`degree-checks.json`. A mask denotes a monomial by its set bits; it is not a
truth-table location at which the target is necessarily one. For example,
leading indices 4,063,119, 4,190,155 and 4,194,288 were additionally checked by
direct subset parity on the original truth table.

The packed coefficient stream has SHA256

`0449533df4d40c2abd932acb6e931ae6447668764aa9052451db8e08fbc0009e`.

The complete coefficient table is regeneratable from the source and specified
target. The repository stores the summary, all leading indices and hashes,
not a separate binary coefficient file.

## Why degree17 cannot exploit the new budget

Here is the needed elementary minimum-weight argument, stated independently
of the computation. A nonzero multilinear GF(2) polynomial h on m Boolean
variables, of degree d, has at least 2^(m−d) nonzero evaluations. For d=0 it
is the constant one function. For d>0, choose a variable from a degree-d
monomial and write h=g+x_i q. Then q is nonzero of degree d−1 on m−1 variables.
Whenever q evaluates to one, exactly one of g and g+q is one. Induction gives

    weight(h) >= weight(q) >= 2^((m−1)−(d−1)) = 2^(m−d).

For any approximating polynomial p of total degree at most17, Boolean
multilinearization cannot increase its degree. The error function f+p still
has degree18, since p cannot cancel any of f's degree18 coefficients. Hence

    number of wrong bits >= 2^(22−18) = 16.

This is larger than 109/23, so no such polynomial meets the strict sufficient
threshold eta<109/(23Q). The conclusion also covers any input-independent
probability distribution supported on degree-at-most17 polynomials: every
member has at least16 wrong bits, so its mean has at least16 wrong bits.
Conversely, f's exact degree18 algebraic normal form gives zero error. Thus
the least degree for this fixed-target uniform-average approximation
requirement is exactly18, just as its exact degree is18.

The computation supplies the actual degree of f; the written argument supplies
the exclusion of every lower-degree polynomial. Finite sampling of candidate
approximants is not used for that universal exclusion. This is not a new
Lean proof or a novelty claim.

## Verification and reproducibility

Both `python check_degree.py` and `python -O check_degree.py` completed with
exit code zero under Python3.12.14. They produced identical 5,476-byte JSON,
SHA256

`852ae8afaf6764d4da250017adec8552d530686efb40f0f8f9e4cbea07e4ac91`.

The standalone checker verifies:

- The chosen reference satisfies every physical clause.
- The packed transform agrees with the direct subset formula on 378 small
  truth tables, including all 278 tables in dimensions0 through3, and
  additional random/monomial controls through dimension8. These cross the
  within-word and between-word boundary.
- Applying the transform twice restores the entire Q-bit target exactly.
- Three leading coefficients agree with direct parity on their original
  truth-table subcubes.
- Direct evaluation of the recovered algebraic normal form agrees with the
  actual target at 91 selected addresses, including address and padding
  boundaries. The full inversion check already covers all Q truth values.

A separate local NumPy2.3.5 byte-array butterfly calculation gave the same
complete packed coefficient SHA256. It was a cross-check of the custom packed
algorithm; NumPy is not required by the retained checker or its replay.

## Research consequence

The compiler change improves the sharp linear transfer bound and moves the
worst-case guaranteed error radius from zero to four. On this named,
zero-padded satisfying proof, those four bits still cannot buy a reduction in
polynomial degree. A useful next question must therefore address the actual
degree/error tradeoff of valid encoded proof functions, possibly including
their free padding and proof choices. The present audit does not establish
that changing those choices helps or that the entire route is blocked.
