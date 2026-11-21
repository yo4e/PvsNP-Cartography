# Free padding lowers the exact degree to17; four errors do not lower it further

The degree18 result in `degree-notes.md` explicitly fixed every unused address
to zero. Those bits are not constrained by the verifier. Holding every used
bit of the same honest YES proof fixed, a different free-suffix completion has
exact degree **17**, which is the minimum over all such completions.

The strict error budget109/23 still gives no further degree reduction: every
degree-at-most16 polynomial makes at least **16 errors on used addresses**,
regardless of how the free suffix is filled. This also excludes probability
distributions supported on those lower-degree polynomials. The minimum degree
over the allowed padding choices, both exactly and at the new approximation
threshold, is therefore17.

This is a finite clarification about the named honest proof, not a minimum
over other A/B witnesses, compiler layouts or changes to used proof values.

## Actual address support

The primary cross compiler with cap21 uses21,845 physical tag rows, each with
128 seed positions. Thus its used addresses are precisely

    D = [0,M),  M = 21,845 * 128 = 2,796,160,

within the Q=2^22=4,194,304 address cube. The address is `(tag<<7)|seed`.
`check_padding.py` checks the tags actually appearing in ordinary clause
literals and public pins: all21,845 tags occur, with no internal unused rows.
Every ordinary query's seed map is XOR with a fixed offset and hence covers
its whole row. The two clamped pin maps together cover their whole row as
well. No query reaches a tag outside this prefix.

The fixed used bits come from A(x)=1+x, B(x)=x, the honest shared extension,
and truthful private/public cells. Only the1,398,144 suffix bits at addresses
M through Q−1 may change in this audit.

## Why ANF truncation gives the minimum exact completion

Regard address integers as masks of22 Boolean variables. D is downward closed:
if T is a submask of S, then T<=S, so S<M implies T<M.

For any completion g of the fixed values, every coefficient indexed by S in
D is already determined:

    c_S = XOR_{T subseteq S} g(T).

All values in this expression lie in D. Changing suffix values therefore
cannot change any of these coefficients. Let d be the maximum degree of a
nonzero forced coefficient. Every exact completion has degree at least d.

Conversely, keep these forced coefficients and set every coefficient whose
mask lies outside D to zero. At any used input x in D, evaluating the resulting
polynomial uses only coefficients indexed by submasks of x, all of which lie
in D. It therefore reproduces the original value at x. This constructs a
degree-d completion, proving that d is the exact minimum.

The executable applies this rule to the original zero-padded function's full
ANF. All202 degree18 coefficients lie outside D and are removed. The retained
coefficients have maximum degree17, with202 leading terms and833,770 nonzero
terms in total. Its inverse transform supplies the actual completed truth
table. The checker compares every one of the2,796,160 used truth values,
reconstructs the physical rows and executes the full clause evaluator. No used
bit changes and the physical clause failure count remains zero.

The new completion changes702,064 previously zero padding bits to one. Its
total truth-table weight is1,480,748. This is a choice of the target proof's
unused bits; these changes are not charged as approximation errors relative
to the newly chosen target.

| Target or optimization scope | Exact degree | Least degree at strict mean wrong-bit budget109/23 |
|---|---:|---:|
| Named honest proof, suffix fixed to zero | 18 | 18 |
| Same used proof bits, canonical suffix completion | 17 | 17 |
| Minimum over all suffix completions with those used bits fixed | 17 | 17 |

The18-to17 improvement comes from selecting the free padding. It is not an
improvement bought by tolerating four errors.

## A lower bound that is independent of the suffix

The whole subcube with address variable21 fixed to zero lies inside D. Its
dimension is21 and it contains2,097,152 fixed truth values. Its exact algebraic
degree is17, again with202 leading coefficients. Any global polynomial of
degree at most16 restricts to degree at most16 on this subcube. The elementary
minimum-weight argument from `degree-notes.md` therefore gives at least
2^(21−17)=16 wrong used bits.

There is also a directly executed parity certificate for this same lower
bound. Choose the degree17 monomial mask

    S = 1,965,967,

whose variables are

    {0,1,2,3,7,8,9,10,11,12,13,14,15,16,18,19,20}.

Its complement within the first21 variables is {4,5,6,17}. Fixing these four
coordinates in each of their16 possible ways, and keeping variable21 zero,
partitions the fixed half into16 disjoint17-dimensional subcubes. The program
directly XORs the original used truth values on each subcube. All16 parities
are one. The JSON records every base mask and parity.

Every polynomial of degree at most16 has even parity on each17-dimensional
subcube. Each monomial omits at least one free variable; summing over that
variable pairs identical contributions and cancels them over GF(2). The
target's odd parity thus forces at least one discrepancy in each of the16
disjoint subcubes. This proves the16-used-error lower bound without relying
only on a full-transform degree summary.

Every allowed suffix completion agrees on these subcubes. Every distribution
supported on degree-at-most16 polynomials consequently has expected total
error count at least16. Since16>109/23, none meets the new transfer threshold.
The degree17 canonical completion supplies the matching upper bound by exact
representation. No search over candidate approximants replaces this argument.

## Reproducible evidence

`check_padding.py` uses only the standard library and imports the packed
transform plus independent small-cube controls from `check_degree.py`.
Both normal and `-O` runs completed with exit code zero under Python3.12.14.
Their complete7,559-byte JSON outputs match, SHA256

`d58e287c466914f3913ba2e3b531ce9ca49abe41eb9fc8d49dd27a68ff73c5ef`.

The output includes all202 forced leading indices, coefficient histograms,
the16-subcube certificate and these packed-stream hashes:

| Object | SHA256 |
|---|---|
| Canonical completed truth table | `fb0c0944144b09e888b6cb64585bd3c66e7186902aa7b01493fe81c73a5732f0` |
| Canonical completed ANF | `ee6f848fb95f7701f03242e687dd491151a48e97b082ad271fad7c2b680e8fb4` |
| Fixed21-dimensional subcube truth table | `707c2158fe5a483f257a3e71cf90dc87b208e031f334c035009e10fdae50281d` |
| Fixed subcube ANF | `5dcf7af03a0e61eb89aa8dcebf340aee340d9f95a39c2a035a22982bd7ce08c3` |

Verification includes all used-bit comparisons, complete transform inversion
on the completion and fixed half, direct parities from used truth values, the
actual clause evaluation, and378 independent scalar small-cube controls. A
separate same-lineage agent's NumPy byte-array calculation independently
matched the completed truth and coefficient hashes. This is computational
cross-checking and written finite mathematics, not external mathematical
review, a second proof kernel, Lean verification or a novelty claim.

The boundary is now explicit: suffix padding can remove one unnecessary
degree, while four tolerated errors cannot remove the next degree for these
fixed used bits. Other satisfying proofs and other physical layouts remain
outside this completed calculation.
