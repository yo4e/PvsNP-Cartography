# Conclusion — public structure, a scoped obstruction, and a costed alternative

Issue 36's scoped milestone is complete. The useful outcome is a sharper
choice of model: a public low-dimensional symbolic dictionary is sufficient;
RS membership alone cannot guarantee every witness is easy; and a guessed
layout is not automatically unsound, although the explicit table is too
expensive in the current growing compiler.

## 1. Public layout without knowing which witness is used

If each row has public coefficients in a dictionary whose functions have seed
degree at most delta, coefficient tags and distinct ranks give an exact
completion of degree at most delta+1. For dictionary dimension L, maximum
coefficient multiplicity mu and N seeds, the actual address count is

    Q' = N * 2^L * 2^ceil(log2 mu).

The public layout is the same for every admissible witness. Its construction
does not compute the witness, while the approximating polynomial may depend
on it. This elementary linear/Hadamard mechanism is useful at polynomial
storage only when L is small enough. A public XOR/AND syntax condition and
its precise limits are given in [the derivation](public-dictionary-notes.md).

The standalone relation w0*w1=0 has exactly three satisfying proofs, twelve
physical rows, and one common layout. Each has minimum exact **and budgeted**
degree three even with arbitrary padding. The raw NO minimum, all-error
sensitivity and degree lower bound have separate written arguments and
executable controls.

| Quantity | Standalone public-layout control |
|---|---:|
| Expanded YES / NO clauses | 116 / 124 |
| Compact / new address cube | 64 / 1,024 |
| Raw NO minimum | 4 |
| Exact signed sensitivity at 00 / at 01 or 10 | 9/2 / 5 |
| Common strict uniform-error threshold | 1/1,280 |
| Exact and budgeted minimum degree | 3 |

These are expanded physical clauses, not the growing compiler's template
census. The raw budget is below one erroneous bit; this example establishes
the structural construction, not a better positive-error regime.

## 2. A real satisfying-witness obstruction with a precise limit

The original growing YES fixture is unique on used bits: its residual forces
A=1+X and B=X. A different, explicitly defined **code-only relaxation** keeps
all shared row/column checks and admits every B of degree less than 2s.
Its first 2s field values give 2sk freely variable systematic bits among
genuine satisfying code-only proofs.

For any fixed m-bit layout, degree-d polynomials have at most
2^(sum_{j<=d} binom(m,j)) restrictions. Multiplying by the radius-e Hamming
ball volume yields an obstruction when that product is below 2^(2sk).
At m=O(k), d=O(log k), e=O(s), this holds eventually. This is a written
counting argument, not extrapolation from the finite runs.

At GF(128), the code-only witness B=X^3 passes the actual shared geometry.
On 112 used cells in the original tag layout, its exact nearest affine
distance is **42**, from all 512 restricted affine tables. The separate
arbitrary-layout dimension bound is also strict at degree one and radius
four. The [full derivation](scoped-rs-obstruction.md) distinguishes the
particular witness/layout from that existence bound.

The code-only relaxation discards the outer residual and inherits no NO gap.
It still has easy witnesses. Therefore the result kills an **all-witness
guarantee from code structure alone**, not existential completeness or all
possible encodings of an unknown witness.

## 3. The false shortcut was a quantifier claim, not just a bad example

A nondeterministic algorithm may guess one row map Lambda and one polynomial
P and decode pi(i,z)=P(Lambda(i),z). Every branch still supplies one global
old proof, so the old universal NO soundness applies. The same map must be
used at every alias. Constant row tags preserve signed projection degree.
Injection preserves arbitrary-proof transport and the error metric; it is
not necessary for NO soundness alone.

All 256 eight-bit constant-row vectors admit a degree-one completion after
an injective value/rank layout. By contrast, at any fixed eight tags in a
four-bit tag cube, at most 32 patterns have exact affine representations.
The changing layout carries information: its explicit table is 32 bits in
this toy. In the growing compiler, R>=k(4s^2+s-1), so R*t descriptor bits
already cost Omega(N*k*t), outside an o(N) target. There is no compression or
hierarchy contradiction hidden in the degree-one observation.

Changing the map by occurrence really is unsound: the conflicting units
(v) and (not v) can both pass if their common cell is detached. Merging
consistent rows does not have that failure, but can increase one-bit error
sensitivity by a factor of eight in the included control. See the
[source/quantifier ledger](sources-and-quantifiers.md) and
[preserved failed shortcut](../../graveyard/2026-11-24-layout-quantifier-shortcuts.md).

## Verification and next decision

Three exact Python suites cover the public layout, shared RS witnesses, and
guessed-map semantics. The independent root checker enumerates all 4,096
proofs of a small inconsistent shared system, 24,576 reindexings, every map
to two tag bits paired with an affine polynomial, and all 12,870 occupied
eight-tag sets in a four-bit cube. These finite enumerations supplement the
written universal arguments; they do not stand in for them. Actual commands,
output hashes, remote readback and any CI status belong in
[execution-evidence.md](execution-evidence.md).

The next frontier is a **succinct layout for the residual-constrained,
fixed-rate recursive source verifier**. Determine which row identities are
constant per query, whether a small public dictionary or a short guessed map
can serve one satisfying witness, and charge descriptor length, global alias
consistency, composed degree, actual templates, NO gap and precision together.
Do not continue scaling the one-level fixture as a substitute for that step.

No new Lean execution, independent external review, novelty clearance,
general lower bound, or P-versus-NP separation is claimed. Issues 8 and 15
retain their separate review scopes. Another nightly session needs fresh
approval.
