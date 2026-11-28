# Failed shortcuts — accepting degree and the compiler

Session: November 28, 2026, approved night. Expedition 049, Issue #38.

## 1. Enlarge the affine-A field toy to obtain hard satisfying rows

**Attraction:** the actual two-level RS code permits B up to degree31, so
multiple satisfying roots might expose difficult seed dependence.

**Failure:** the designed residual with affine A has numerator degree at most
six. Its degree-four vanisher forces B to be at most quadratic. The new
three-witness family is fully classified and all raw rows remain affine.
Moreover, a nonconstant F-affine A can be Boolean on at most two sites.

**Salvage:** use the genuine Boolean assignment's canonical interpolant. Its
Boolean degree equals the assignment's ANF degree; the source honest cutoff
does not automatically make that assignment simple.

## 2. Linearized division always preserves Boolean degree

**Attraction:** the divisor is an affine-linear function in Boolean field
coordinates.

**Counterexample:** over GF(256), `Q=X^128+X`, `L=X^2+X`, and their formal
quotient has ordinary degree126 and Boolean degree6, although Q has Boolean
degree1. Pointwise inverse reasoning cannot supply a low degree bound.

**Salvage:** the explicit chi filtration proves the required nonincrease
under `deg Q<3S<|F|`. The source honest cutoff satisfies that ratio.

## 3. Exact interpolation degree control transports small errors

**Attraction:** canonical interpolation preserves degree, so perhaps it also
preserves a useful approximation radius.

**Counterexample:** changing one value on a 16-point assignment subspace
changes exactly241 of256 root symbols in its interpolant. A Lagrange basis
polynomial has no zeros outside the other15 assignment sites.

**Salvage:** prove a weighted stability statement separately, or analyze the
actual clause-failure objective of the proposed tuple directly.

## 4. Easy raw fields imply easy gate rows for any equivalent compiler

**Counterexample:** a codimension-one selector has degree1, while a naive
factor circuit for the same GF(16) function creates degree4 gate rows. A
Frobenius circuit keeps all rows at degree1. A public circuit on a live
canceling output cone can also force arbitrary public functions into rows
without changing the exact raw NO minimum.

**Salvage:** name the public implementation. The outer residual now has an
explicit controlled evaluation order; the recursive proximity circuit does
not inherit that result automatically.

## 5. High exact gate degree obstructs the approximation budget

**Counterexample:** the complete live prefix-AND tuple has exact degree k but
exact minimum used error `2^(k-d)` at row degree d, for `1<=d<k`.
Inverse-polynomial error budgets need only logarithmic degree. Counting only
the final sparse row would also have missed the costs of its predecessors.

**Salvage:** use a distance/parity argument at the actual physical weighted
budget, for all satisfying witnesses, and distinguish it from exact degree.

## 6. No close low-degree honest-proof approximation means no counting certificate

**Counterexample:** the live bent control's unique satisfying proof has
minimum affine used error20, signed-charge error54 and literal-weight error
176. Its raw NO minimum is32. Nevertheless the minimum actual failure count
of an affine tuple is8, below the half-gap threshold16.

**Failure point:** the union-bound/sensitivity condition is sufficient, not
necessary. Low-degree tuples can violate a few gate equations while remaining
far from every exact computation trace.

**Salvage:** either construct a genuinely sufficient approximation or work
with the actual violation objective. Do not invert the sufficient condition.

## 7. Fixed-node degree preservation automatically holds across all recursive nodes

**Unjustified step:** the q-adic filtered basis is fixed in the lemma. A
normalized row ranges over many nodes whose basis may depend on the seed.
The actual two-level fixture has the needed fixed low spaces and affine
substitutions, but an arbitrary-depth basis-selection algorithm being
polynomial time does not establish those properties.

**Countercontrol to the unqualified inference:** for alpha outside GF(2),
take `q_z(X)=X^2+(alpha+z1)X` and `P=X^2`. At each fixed node,
`Q_z(X,Y)=Y+(alpha+z1)X` has degree one. The jointly varying substitution
`X=z2,Y=0` gives `alpha*z2+z1*z2`, of degree two. Even affine vanisher
coefficients can matter. This is an abstract varying-node example, not a
claimed counterexample inside the BV recursion.

**Next task:** prove them for a public uniform recursive choice or give an
actual source-family counterexample, then analyze its Boolean predicate.

All controls, derivations and limitations are retained in
[Expedition 049](../expeditions/049-accepting-seed-degree/conclusion.md).
