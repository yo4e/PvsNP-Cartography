# The sparse-star compiler and its actual physical cost

The primary implementation is the **cross** schedule

    U = {0,...,7},  V = {0,8,...,120},  D = U union V.

It reads 23 distinct A offsets. The two earlier trials use the Hamming balls
of radii one and two, with 8 and 29 offsets. All three retain the same GF(128)
external A and B words, GF(16384) recursive extension cells, original residual,
shared B row/column tests, signed gate clauses and public seed pins. No new
field-proof table is introduced. The only field-level change is to replace
full A membership by the fixed-star requirements

    A(x+s) + A(x) = s (A(x+1) + A(x))   for s in D minus {0,1}.

The characteristic-two additions on physical addresses are XOR. Multiplication
on values is the inherited GF(128) multiplication. Both 0 and 1, and the
residual's offset 2, lie in every implemented schedule. The implementation is
in `sparse_compiler.py`; predecessors 040 and 044 are imported without edits.
The proof of the field rejection bound is separate from the compiler checks.

## Actual census

These are generated layouts, not counts obtained by scaling a query estimate.

| Schedule and chosen private fanout | Instance | AND | XOR | Private copies | Used rows | Clause templates | Padded Q |
|---|---|---:|---:|---:|---:|---:|---:|
| Radius one, cap 21 | YES | 2,742 | 16,427 | 2,071 | 21,360 | 78,092 | 4,194,304 |
| Radius one, cap 21 | NO | 2,757 | 16,437 | 2,067 | 21,381 | 78,169 | 4,194,304 |
| Radius two, cap 27 | YES | 2,889 | 16,768 | 2,124 | 21,901 | 80,003 | 4,194,304 |
| Radius two, cap 27 | NO | 2,904 | 16,778 | 2,124 | 21,926 | 80,088 | 4,194,304 |
| Cross, cap 21 | YES | 2,847 | 16,699 | 2,179 | 21,845 | 79,711 | 4,194,304 |
| Cross, cap 21 | NO | 2,862 | 16,709 | 2,178 | 21,869 | 79,794 | 4,194,304 |

Each row has 128 seed addresses. Q includes padding to a power of two in the
row tag. Clause-template counts include the constant/output units and fourteen
clamped public-bit templates. The cross YES and NO therefore have respectively
10,203,008 and 10,213,632 clause–seed occurrences. They do not have one common
normalized failure probability; comparisons use raw failed occurrence counts.

For each schedule the checker also costs cap two. The smaller fanout does not
remove the physical read bottleneck and crosses a padding boundary. The chosen
caps are the largest caps whose generic private-gate bound remains no larger
than the physical reader load. This is a comparison within the specified
compiler family, not an optimization theorem over all Boolean encodings.

## A uniform, sharp signed-error bound

An input key `(block,page,bit,delta)` denotes the same physical bit as before,
at seed `x XOR delta`. The new compiler gives every used key a mandatory private
copy root, then splits outgoing private fanout exactly as in Expedition 044.
All uses of one physical key retain their alias, including the shared B
rectangle. Private cells are indexed at the original seed. The assertion of
the final output counts as a driver use.

The maximum distinct physical read counts are:

| Schedule | A bit | B bit | Chosen cap | Uniform signed sensitivity sigma |
|---|---:|---:|---:|---:|
| Radius one | 8 | 23 | 21 | 23 |
| Radius two | 29 | 23 | 27 | 29 |
| Cross | 23 | 23 | 21 | 23 |

The B value is unchanged: a common-rectangle symbol can be read at eight row
offsets and sixteen column offsets, with the zero offset shared, hence
8+16−1=23. No row/column copy has been detached.

Here sigma means the maximum ratio of failed physical clause–seed occurrences
to flipped physical bits, relative to any satisfying global assignment. It
ranges over unrestricted error sets. For the retained signed clauses, the
local error charges are

    AND: e_left + e_right + 2 e_output
    XOR: e_left + e_right + e_output
    COPY: e_input + e_output.

The constant and output units have charge one. A wrong public-bit cell has
exactly two pin failures. Counting every occurrence and using the actual
private fanout cap bounds the total by

    F(E) <= max(mu, cap+2) |E|.

This argument covers mixed field, gate, copy, constant, public and padding
errors; it does not require their independence. Padding is unused and has
zero charge. The generated layouts are checked for the relevant fanouts,
physical aliases, fixed offsets and clamped public addresses.

The bounds are sharp. Keep every private cell at its satisfying reference
value and flip one physical A bit in the cross or radius-two layout. Exactly
23 or 29 distinct copy definitions each lose one equivalence clause. Nothing
else changes. For the radius-one layout use a common-rectangle B bit, which
has 23 readers. This attains the upper bound independently of the particular
satisfying reference's values. A complete singleton scan on the named honest
YES reference supplies explicit executable witnesses:

- Cross: physical tag 0, seed 0, 23 failed occurrences; role maxima A23,
  B23, constant1, public19 and private-gate22.
- Radius two: tag 0, seed 0, 29 failures; role maxima A29, B23, constant1,
  public23 and private-gate28.
- Radius one: tag 56, seed 0, 23 failures; role maxima A8, B23, constant1,
  public19 and private-gate22.

The written charge argument supplies the all-error upper bound. Finite
singleton scans by themselves would supply only a lower bound.

## Soundness transport and its limits

With correct public bits and every ordinary definition satisfied at a seed,
the Boolean output equals that seed's field predicate. A rejected field seed
thus forces an ordinary failure or a wrong public-bit cell there. The two
clamped pins charge each wrong public cell twice. As in Expedition 044,

    field rejected seeds <= ordinary failures + pin failures / 2.

Therefore an independently proved field NO lower bound transports to every
global Boolean assignment, including dishonest gates and copies. Truthfully
filled private cells attain one output-unit failure per rejected field seed.
The old affine A=0 reciprocal-interpolant witness still gives 109 failures in
each schedule, but that witness alone is only an upper bound on each NO
minimum.

The distinction matters: the sparse ball schedules admit explicit noncode A
splices with only 106 or 108 rejections. The checker includes their exact global A
and B tables. With the cross schedule, the radius-one and radius-two splices
instead cause 119 and 124 rejections respectively; the three-star radius-one
splice causes 128 cross rejections. These are executed finite
witness counts; the separate cross-star overlap argument is what can retain
the universal NO minimum 109.

Given that 109 field minimum, the cross compiler's strict sufficient threshold
is

    eta < 109 / (23 * 4,194,304) = 109 / 96,468,992.

It is 128/23 times Expedition 044's threshold at the same Q. The strict raw-bit
budget is 109/23, so four arbitrary wrong bits are guaranteed tolerable.
This calculation concerns the **new** encoded Boolean proof. It does not
transport an approximating polynomial for an old layout, construct a useful
low-degree approximant, or turn unrestricted error sensitivity into a
degree-restricted sensitivity claim.

## Reproducible verification

Run `python check_compiler.py` from this directory and compare its complete
JSON with `compiler-checks.json`. Run again under `python -O` to verify that
acceptance is not supplied by removable Python assertions. Checks use explicit
exceptions.

Both commands completed with exit code zero in this session. Their complete
22,370-byte outputs are identical, with SHA256
`ebf02aa785ea0b1755350ae55997297286536b436aa6654d4fb2ae35e8856e3a`.

For each of the three schedules and both public instances, the scalar
reference uses separate finite-field convolution/reduction, absolute-point
Lagrange interpolation, and direct residual evaluation. Its B interpolation
cache is keyed by the complete immutable physical B table. It is compared
against the generated Boolean circuit on all 142 inherited field assignments
and 23 additional assignments, each at all 128 seeds. Every chosen-cap
private-copy circuit is then compared against those results. Full physical
clauses are evaluated for the new noncode assignments and canonical witnesses.

Additional controls enumerate every one-bit A perturbation (128 locations
times seven symbol bits), verify its exact translated star of membership
failures, scan every used physical singleton at the honest reference, directly
replay selected mutations through scalar DIMACS addresses, and exercise mixed
error sets of sizes 1, 2, 7, 31, 128 and 1,024. The JSON preserves exact counts,
deterministic verdict-stream SHA256 digests and the full compiler census.

These are finite executions plus the explicit inherited gate-charge proof.
They are not Lean verification, a second proof kernel, an external review,
or a novelty claim. No universal NO bound is inferred solely from the fixture
suite.
