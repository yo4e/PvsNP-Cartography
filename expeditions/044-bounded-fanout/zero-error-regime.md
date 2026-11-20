# The improved finite threshold still requires an exact polynomial to exist

The ratio improvement in [actual-instance.md](actual-instance.md) is real,
but its quantifiers impose a further limitation. Both old and new thresholds
are smaller than one physical bit of uniform error:

    109/(288Q) < 109/(128Q) < 1/Q.

For a single deterministic Boolean polynomial p on the Q-point cube, its
uniform disagreement with the intended proof pi is |E_p|/Q, an integer
multiple of 1/Q. Either sufficient threshold therefore forces E_p to be empty.
The worst-case guaranteed integer error radius remains zero. This is not a
claim that every one-bit error fails; many benign locations have lower cost.

The probabilistic formulation does not enlarge the existential approximation
class in this fixture either. For any distribution on global degree-at-most-d
polynomials, the mean number of wrong bits is E_p |E_p| = Q eta. If this is
less than one, then

    Pr[p equals pi on the entire cube] >= 1 - E_p |E_p| > 0,

because every nonexact polynomial has at least one wrong bit. Hence some
degree-at-most-d polynomial represents pi exactly. Conversely an exact
polynomial, sampled with probability one, meets either error threshold.
Thus existence of a distribution satisfying either threshold is equivalent
to exact degree-d representability for its respective encoded truth function.
The two encoded functions can differ; no relation between their exact degrees
is established here. The 9/4 factor relaxes the allowed mean error of a specified
mixture and its sharp linear transfer budget. It does not show a broader
approximable-function class or a useful low-degree approximant.

## Why optimizing private fanout cannot cross this threshold

The full A check at every center demands that the entire A word be an affine
GF(128) polynomial. Flip one physical bit of one symbol in a correct A word.
The resulting word is not affine: a different affine polynomial cannot agree
at the other 127 points. Every one of the N field centers rejects.

For any unweighted private encoding that charges at least one failed clause
to every rejecting field center, keeping all auxiliary bits at the old honest
YES values after this one-bit change still incurs at least N failures. Thus
sigma>=N is intrinsic to that retained full-A predicate and raw input
representation, not just an artifact of the particular copy-tree bound.
Meanwhile truthful gates on any NO field proof fail only the single output
unit at each rejecting center, so V_NO<=N. Consequently

    V_NO/sigma <= 1,    V_NO/(Q sigma) <= 1/Q.

This obstruction assumes the stated unweighted, single-output, private
encoding and the same physical A cells. It does not rule out a changed
predicate, changed input representation, or a separately justified smaller
sensitivity for errors realizable by a restricted polynomial class.

In general the strict linear bound guarantees at most
ceil(V_NO/sigma)-1 arbitrary erroneous bits. A next verifier should aim for
V_NO>sigma, and preferably a ratio growing with the seed dimension, while
also controlling Q and the computational counting cost. Reducing readership
without retaining sufficient NO rejection is not enough. This is the sharper
mathematical target of [Issue 34](https://github.com/yo4e/PvsNP-Cartography/issues/34).

The argument is elementary integer/expectation reasoning and the existing
private-encoding soundness charge. It was challenged independently by a
separate agent; no new finite enumeration or Lean claim is needed or made.
