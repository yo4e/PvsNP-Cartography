# A 23-read affine test crosses the zero-error obstruction

The selected GF(128) verifier keeps the exact NO minimum 109 while reducing
the exact unrestricted signed sensitivity from 128 to 23. Both its YES and
NO Boolean proof cubes still have Q=4,194,304 addresses. The strict sufficient
uniform-error budget becomes

    eta < 109/(23 Q) = 109/96,468,992.

This is an improvement by exactly 128/23 (about5.565) over Expedition044's
109/(128 Q) benchmark. It guarantees separation after **any four erroneous
physical bits** in a satisfying YES proof: at most92 clause–seed failures
occur, whereas every NO assignment has at least109. Five errors are outside
this uniform linear guarantee; no five-error failure is implied.

This is a written mathematical derivation, a generated finite compiler and
executable verification. It is not a new Lean result, external peer review,
a low-degree approximation construction, a general circuit lower bound,
or a P-versus-NP resolution.

## The mathematical change

Let U={0,...,7} and V={0,8,...,120}, viewed as complementary binary subspaces
of GF(128). Set D=U union V, of size23. At each seed x test

    A(x+d)+A(x) = d (A(x+1)+A(x))  for every d in D.

The equations at0 and1 are identities. All reads use the original A page at
fixed XOR offsets; slopes are computed privately, not stored in an unchecked
shared oracle. The existing residual reads offsets0,1,2, all in D.

A passing center defines a single affine polynomial on x+D. For distinct
centers x,y, decompose x+y=u+v with u in U and v in V. The two distinct
sites x+u=y+v and x+v=y+u belong to both stars. Their local affine
polynomials must be equal. Thus all passing centers use one polynomial,
even when the complete A table is not affine.

If more than19 joint centers accept, the inherited shared B test has at
least two passing rows and two passing column groups. The existing
interpolation argument supplies one degree-at-most15 polynomial B_* on
all B-passing sites. On every joint acceptance, the residual now agrees
with a single degree-at-most19 polynomial in x. It is nonzero: vanishing
at0 would force P(0)=1, whereas vanishing at1 would force P(0)=0.
There can therefore be at most19 accepting centers.

This proves at least109 rejecting centers for every field assignment.
The previous A=0 reciprocal-interpolant B witness still attains109.
Private gate definitions and public pins transport this exact minimum to
all Boolean assignments. See [the full derivation](theory-notes.md) and
[the hostile review](attack-notes.md).

## Fully counted finite implementation

| Quantity | Expedition044 cap126 | Selected23-offset cap21 |
|---|---:|---:|
| Distinct A reader maps per physical bit |128|23|
| Maximum B reader maps per physical bit |23|23|
| Exact unrestricted signed sensitivity |128|23|
| Exact NO raw failure minimum |109|109|
| YES used physical rows |24,526|21,845|
| NO used physical rows |24,551|21,869|
| YES clause templates |88,852|79,711|
| NO clause templates |88,937|79,794|
| Padded physical addresses Q |4,194,304|4,194,304|
| Strict guaranteed integer error radius |0|4|

The new YES circuit has 2,179 private copies; NO has 2,178. Gate and copy
definitions give F(E)<=max(mu,f+2)|E|. Here mu=23 and f=21, so sigma<=23
for arbitrary mixed errors, not merely singleton errors. Flipping a
maximal-load physical A or B bit while keeping the private copies honest
violates exactly 23 copy clauses. This proves equality, uniformly over
satisfying references. The code also evaluates an attaining singleton.

Raw failed clause–seed pairs are the decision quantity. YES and NO template
counts differ; their normalized failure probabilities are not silently
compared using one common template denominator.

## Attacks changed the construction

| A schedule | Proven NO lower bound | Executed NO upper witness | Exact sigma in tested layout | Guaranteed integer radius |
|---|---:|---:|---:|---:|
| Eight-point Hamming star |28|106|23|1|
|29-point Hamming ball |98|108|29|3|
|23-point complementary-subspace union |109|109|23|4|

The trial lower bounds use explicit finite connectivity certificates and
the same residual argument. Their upper witnesses are globally consistent
physical A/B assignments, including honest shared B extensions. Neither
trial's true optimum is asserted.

A three-star splice leaves22 NO centers accepting under the eight-read
test; a wider splice leaves20 accepting under the29-read test. These
counterexamples disprove carrying over the old exact109 minimum merely
from the correct zero-error code space. Under the selected23-read test,
the same three-star and wider splices reject128 and124 centers respectively.
The original one-star attack rejects119. The failure and repair are retained
in [graveyard](../../graveyard/2026-11-21-sparse-affine-splices.md).

## What the nonzero error radius does and does not imply

The former mean-error threshold below 1/Q forced any qualifying polynomial
mixture to contain an exact polynomial. The new threshold is above 4/Q,
so that integer/expectation obstruction no longer follows. A distribution
whose every member has between one and four wrong bits is consistent with
the error budget.

This observation does not construct such a distribution in a desired
low-degree class. The new gate/copy encoding is a new Boolean function,
and the approximation hypothesis must be made for that function. No claim
of a strictly larger fixed-degree approximation class for this particular
honest encoding is made without a witness.

More precisely, for uniform-average error of a finite polynomial mixture,
the existence of a mixture with mean wrong-bit count below 109/23 is
equivalent to the existence of one polynomial in the same degree class
with at most four wrong bits: if every member had at least five, its mean
would be at least five; conversely a deterministic four-error polynomial
meets the threshold. This equivalence is for uniform-average error. It
does not turn a four-error deterministic polynomial into a pointwise-error
guarantee at each address.

## The next scientific frontier

The direct approximation audit exposes a remaining obstruction. For the
named honest YES assignment A(X)=1+X, B(X)=X and **zero at every unused
padding address**, the new 22-variable truth function has exact GF(2)
algebraic degree 18. Its exact Mobius transform has 202 degree 18 monomials.
Every polynomial of degree at most 17 differs from it on at least
2^(22-18)=16 addresses. The elementary minimum-weight proof extends the
same lower bound to the mean error of every fixed polynomial mixture.
Since 16 >109/23, the new error budget still requires degree 18 for this
particular padded function. An exact degree 18 representation attains it.
[Computation](degree-notes.md) · [Written distance proof](degree-bound-notes.md).

Thus the immediate next question is whether a different assignment to
the **unused** addresses permits a lower-degree completion while keeping
every queried physical bit fixed. The present calculation does not
optimize padding, choose among all satisfying proofs, or compare the
old and new encodings' exact degrees. It closes the shortcut that a
positive error radius by itself establishes an approximation-degree gain.

For the designed one-level family k=2a+1, s=2^a, the same subspace union
has 3s-1 read offsets. The accepted-site argument gives the written exact
field minimum 2s^2-2s-3. The corresponding canonical read ratio
(2s^2-2s-3)/(3s-1) grows with s. This is a structural reason to continue,
rather than automatically enumerating another arbitrary fixture.

Another remaining task is to generate and fully price that family, including
Q, actual gate/copy layouts and approximation requirements for the encoded
proof functions. The existing full recursive source family is a separate
extension: its accepted-site B recovery cannot be replaced by the one-level
argument. The unpaired GF(256) optimum remains parked.

Verification details and exact commit/run readback are in
[execution-evidence.md](execution-evidence.md). Independent-review Issues 8
and 15 retain their separate scopes. Novelty remains unknown.
