# Positive bit tolerance is not an approximation-degree witness

## Claim retired

Once the compiler tolerates a nonzero number of incorrect bits, its
existential low-degree approximation requirement has necessarily weakened.

## Exact counterexample within the current construction

For the selected cross compiler, fix the honest YES assignment
A(X)=1+X and B(X)=X, its honest shared extension and private computation
values, and zero at every unused padding address. The resulting Boolean
truth function has 22 address variables and exact GF(2) algebraic degree 18.
The complete exact transform and independent controls are reproducible in
[check_degree.py](../expeditions/045-sparse-affine-reads/check_degree.py);
the result is in [degree-checks.json](../expeditions/045-sparse-affine-reads/degree-checks.json).

Every polynomial of degree at most 17 differs from this function on at
least 16 points: their difference has exact degree 18, and a nonzero
degree 18 multilinear polynomial on 22 bits has weight at least2^4.
The same bound holds for every fixed mixture of such polynomials.
The new mean-error budget is strictly below 109/23, approximately 4.739,
so no such mixture qualifies. Degree18 does qualify by representing
the target exactly.

Thus the compiler's genuine four-bit guarantee coexists with no decrease
in the existential approximation degree of this specified proof function.

## Scope and salvage

The target includes its padding convention. This is not a lower bound
over all padding choices, all satisfying proofs, other layouts or a
growing verifier family. Free addresses can be changed without changing
the verifier's queried values, and such a completion can alter algebraic
degree. Determining whether that freedom changes this obstruction is a
specific next research question.

The full [minimum-weight argument](../expeditions/045-sparse-affine-reads/degree-bound-notes.md)
is elementary and written out. No Lean, novelty or new general complexity
lower bound is claimed. The sensitivity improvement itself remains valid.
