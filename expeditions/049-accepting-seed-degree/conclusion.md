# Conclusion — separate witness degree from compiler-created difficulty

Expedition 049 completes a scoped milestone of Issue #38. The main positive
result is a written source-level degree transfer from a genuine satisfying
Boolean assignment to its canonical A, forced B and one public outer
residual circuit. The main negative result is an exact counterexample to
treating satisfying-proof approximation as a necessary condition for a
successful low-degree counting certificate.

These are mathematical deductions with explicit hypotheses, supported by
finite controls. They are not a new complexity separation or a claim of
novelty. The full growing recursive proximity circuit is still open.

## 1. A source-level exact degree transfer

Let `F=GF(2^k)`, let `H0` be the assignment subspace, and let `H` be its
one-dimension extension in the BV outer residual. Put `S=|H|`, assume
`3S<|F|`, and let `c` be the largest clause-selector codimension in H. Let
`w:H0->{0,1}` be any satisfying assignment of Boolean degree r. Choose its
canonical interpolant A, of ordinary degree less than `|H0|=S/2`.

The deductions in [linearized-degree.md](linearized-degree.md) give:

    deg_2 A = r,
    deg_2 B <= D0 = max(c+3r, 1+r),
    maximum honest outer-gate degree <= D0+1.

The zero function can be assigned degree zero in these upper bounds. The
diagnostic ANF files use minus one to distinguish zero rows from nonzero
constants.

Three ingredients do the work. Affine-subspace selectors have exact Boolean
degree equal to their codimension and admit a Frobenius-based circuit with
the same gate-degree bound. Canonical interpolation preserves assignment
degree by an injective restriction and matching filtered dimensions. Finally,
division by a monic affine-linearized polynomial of degree S is controlled by
`chi(e)=floor(e/S)+popcount(e mod S)`: every quotient monomial has chi at most
the numerator's maximum chi minus one. Under `deg Q<3S`, this gives
`deg_2(Q/Z_H)<=deg_2 Q`.

For the source residual, the honest A cutoff makes `deg Q_A<2.5S`, so the
quotient lemma applies. B is uniquely determined once A is fixed. There is
no need to assume B is separately easy. The public circuit uses linear
squaring and constant multiplication, bilinear multiplication, and tests
zero only after the complete residual has been formed. It is independent of
the satisfying witness and preserves the predicate on arbitrary inputs.

For the intended exponential-time source family, `c=O(log k)`. This is an
exact conditional upper bound; it does not establish the existence of a
low-degree satisfying assignment, and it does not cover recursive proximity
gate rows. The standard binary-weight identity is sourced to Carlet; the
source residual and gate encoding are from BV14. Precise distinctions and a
minor selector-normalization discrepancy are in [source-audit.md](source-audit.md).

## 2. The actual two-level field family is fully classified

The new source-shaped designed residual retains the actual GF(256) shared
two-level B oracle and a direct F-affine A test. It has exactly three fully
accepting used field proofs:

| A | Forced B |
| --- | --- |
| `1` | `0` |
| `X` | `X^2` |
| `1+X` | `X^2+X+1` |

Full seed acceptance covers all 832 leaf tests. Shared interpolation gives a
degree-at-most-31 B and uniquely determines every physical auxiliary symbol;
the residual degree bound then forces its polynomial quotient. Thus the
classification is over all accepting used field proofs, not selected
examples. Every one of their 1,024 raw bit rows is affine or constant.

This ease has a reason: the affine A cutoff and this small selector residual
force quadratic B. A nonconstant F-affine A cannot be Boolean on more than
two inputs, so the toy cannot be scaled into the general source assignment
by merely increasing the field. The classification and masked-root and
pointwise-division attacks are in [accepting-family.md](accepting-family.md).
No new NO gap or Boolean compiler census is inferred from it.

The companion [honest extension audit](honest-extension-degree.md) proves a
stronger scoped fact: for every allowed degree-less-than-32 root polynomial
in this actual two-level geometry, honest normalized raw rows have degree
at most the root's Boolean degree. A fixed-node expansion in `X^i q(X)^j`
preserves the binary-weight filtration. The two-level implementation has
fixed low subspaces and affine actual coordinates, allowing the argument
to be applied twice. All 32 monomials were replayed through the actual
extension, with 26,624 leaf checks and 32,512 raw bit rows. This does not
establish those hypotheses for the full growing recursion.

## 3. Gate degree is a property of an implementation

The selector control computes the same codimension-one GF(16) selector in
two ways. A product-of-factors circuit creates gate rows of degree four,
although its output is affine. A public Frobenius circuit keeps every gate
at degree at most one. No witness-dependent simplification is used.

More generally, replace one output unit `(v)` by a circuit computing public
`c(z)`, followed by `u=v XOR c`, `t=u XOR c`, and `(t)`. Both occurrences use
the same physical c row. Minimizing over new rows gives exactly the old
output-unit failure, even when the old public pins are wrong. Satisfying
proofs correspond bijectively and the raw NO minimum is unchanged. Yet c
may have higher degree. The number of templates, normalized gap and
sensitivity change and must be recomputed.

The [signed-clause controls](auxiliary-artifacts.md) price both a live bent
function and an entire prefix-AND chain:

| Four-seed live bent control | Exact value |
| --- | ---: |
| Raw NO minimum | 32 |
| All-error signed sensitivity | 3 |
| Minimum used-cell distance to any affine tuple | 20 |
| Minimum signed-charge distance | 54 |
| Minimum literal/fiber weighted distance | 176 |
| **Minimum actual affine clause failures** | **8** |
| Half-NO acceptance threshold | 16 |

The unique satisfying proof is too far from every affine tuple for any of
the stated sufficient approximation budgets, yet an affine tuple has only
eight failures and passes the counting threshold. This refutes the reverse
implication from failed approximation to failed counting. The actual
low-degree failure objective can be strictly easier than closeness to an
honest proof.

For the live `AND_k` chain, the exact minimum total used error at row degree
`1<=d<k` is `2^(k-d)`, and the displayed tuple causes only
`2^(k-d-1)` actual failures. Disjoint odd-parity cubes prove the error minimum
for the whole tuple. Thus inverse-polynomial error budgets need only
`O(log k)` degree for this high-exact-degree artifact; it cannot explain an
`alpha*k/log k` obstruction.

## 4. Exact control does not imply stable approximation

The interpolation and quotient deductions concern exact functions. One
changed assignment value on a 16-point affine domain changes 241 of 256
field symbols in its canonical interpolant. No weighted approximation
guarantee can be transported through interpolation without a separate
argument. Likewise, the quotient ratio matters: over GF(256), dividing
`X^128+X` by `X^2+X` raises Boolean degree from one to six.

The independent small-field checker covers 3,753 nested affine selectors,
2,944 monomial columns of division maps, and 10,432 Boolean interpolation
instances. These are finite controls for the written proofs, not a substitute
for them. [Execution evidence](execution-evidence.md) records the local and
immutable-commit replay; predecessor field arithmetic is reused only where
explicitly identified.

## 5. Research decision

Park further affine-toy enlargement and compiler-independent auxiliary
degree claims. The source assignment's degree is now the exact canonical A
degree, while the honest B quotient and outer residual gates have controlled
overhead. The next structural task is to prove or falsify an analogous
uniform statement for the **growing recursive RS geometry and its actual
Boolean predicate**, with the seed dependence of every low basis, coordinate
map and interpolation coefficient explicit.

Any approximation application must then price either a sufficient shared
proof approximation or the actual low-degree clause-failure objective. The
two objectives must not be treated as equivalent. The remaining question is
mathematical, not another generic compiler or tag-enumeration exercise.

All general deductions remain written and internally attacked, with novelty
unknown. No new Lean or CI run, independent external acceptance, universal
low-degree completeness, or P-versus-NP separation is claimed. Issues #8/#15
remain separate, and completion does not authorize a later research session.
