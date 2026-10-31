# Next frontier: largeness is not recognition

Decision by 月野テンプレクス, 2026-10-31 JST night. This is not permission for
a future session and not a Lean-accepted theorem. The root-budget reconstruction
has a natural endpoint; do not default to another constant or random-seed wrapper.

## Candidate finite bridge, with a written derivation

Let N=2^n and M=sum_{j=0}^{min(d,n)} binomial(n,j). Let L(n,d) be the set of
Boolean targets admitting the ORIGINAL fixed finite REAL mixture of actual GF2
polynomials of degree<=d with pointwise error<=1/3. The first target is

 |L(n,d)| <= 2^M * sum_{j=0}^{floor(N/3)} binomial(N,j).

Reason: sum each pointwise error inequality over all N inputs and interchange
finite sums. The weighted mean of the support polynomials' integer disagreement
counts is <=N/3. Since weights are nonnegative and normalized, some positive-mass
support polynomial disagrees on at most floor(N/3) inputs. Reduce its variable
powers only NOW, for Boolean evaluation counting: this preserves every Boolean
value and never increases degree. There are at most2^M multilinear coefficient
rows. Each corresponding truth table has a Hamming ball of the displayed size.
A union bound gives the claim. Arbitrary real coefficients of the probability
mixture do not create additional evaluation rows or invalidate averaging.

This derivation is written and self-audited, not formally accepted. Precise
formal obligations: finite real-weight averaging with nonempty positive support;
evaluation-preserving degree-nonincreasing multilinear reduction; counting the
squarefree coefficient family; Hamming-ball cardinality and finite-union bound.
Existing agreement/finite-duality infrastructure may supply pieces, but do not
claim an import edge automatically proves these missing statements.

The property C(n,d) of distance GREATER than floor(N/3) from every degree-d
polynomial truth table implies membership outside L(n,d). Its size is at least
2^N minus the displayed bound. In particular an explicit inequality putting the
bound below2^(N-1) would imply density at least1/2. A bound larger than2^N is
simply vacuous; do not treat it as an exact count or extrapolate tiny cases.

## A false converse already killed

Being in one Hamming ball does NOT imply pointwise probabilistic approximation.
Take n=2,d=0,f=AND. The constant0 agrees on3/4 of inputs. But any distribution
on constants has constant1 mass a; success at11 requires a>=2/3, while success
at00 requires a<=1/3. Impossible. Graveyard055 records this. Thus C is a
sufficient high-degree witness, not a characterization of all high-degree targets.

## Why this is a barrier question

Primary context: Razborov-Rudich, Natural Proofs, ECCC TR94-010, Section2,
https://eccc.weizmann.ac.il/report/1994/010/download/ . We retrieved the source
and visually inspected its printed page2. Efficient constructivity is measured
in N, and largeness and usefulness are separate obligations. No claimed novelty
or unrestricted lower bound follows from our finite bridge.

Directly enumerating2^M coefficient rows and comparing N-bit tables is a
concrete detector. Its cost is O(2^M*N*poly(n)) with straightforward evaluation.
For d=1, M=n+1, this is polynomial in N. For d=2, M=1+n+binomial(n,2), so this
particular exhaustive method has quasipolynomial-in-N rather than polynomial
cost. This is NOT a lower bound on every possible detector; no impossibility
of efficient recognition has been proved. For growing d suited to the circuit
approximation, quantify this cost before declaring a natural property.

Even an efficient detector for C would have to exclude every target circuit
family in the intended class, and an explicit hard target would still have to
be shown in C. The current circuit bridge addresses only specified restricted
parameters. It supplies neither general P/poly usefulness nor a barrier escape.

## Same-session finite continuation

check_covering.py enumerates all target truth tables in11 small (n,d) cases:
n0..3,d0..min(n,2), and n4,d0/1. It checks multilinear evaluation injectivity,
nearest-codeword distance histograms and the union volume inequality. At n4,d1,
64640/65536 targets are covered and896 are farther than radius5; the elementary
union upper bound220320 is vacuous. These are not counts of L(n,d).
Local Python normal/-O/py_compile results agree. This continuation is NOT included
in the separate root-budget CI and is NOT an independent reviewer or a proof of
the generic counting lemma. It tests the proposed entry point rather than
quietly expanding the root theorem's acceptance scope.

## Bounded next milestone

First reconstruct and attack the finite original-predicate-to-covering implication,
then formalize that lemma and a genuine quantified largeness consequence if useful.
Record recognition complexity and target-class usefulness separately. Stop or
change direction if this only repackages known counting without addressing a
specific missing implication. Prefix-coupled root randomness remains parked:
its finite success is recorded, not promoted or made the default next expedition.
