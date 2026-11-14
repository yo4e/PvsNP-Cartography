# A two-level signed-clause ACSP with sharp NO rejection

Start at the [Expedition 040](../040-recursive-verifier/soundness.md) translated literal test over the new field F=GF(256). Take the same four-element H and singleton selectors, a direct strict degree-two test on A and the [paired, two-level RS test](paired-soundness.md) on B with strict degree cutoff 32. At public seed x evaluate the ACSP once, pair only the B proximity test at x and x XOR 9, and require all three predicates. The B used in the residual is the actual physical root used by the RS verifier. This is an explicitly chosen field-symbol verifier, including both recursive levels. There is no Boolean gate or per-clause rejection denominator in this calculation.

Let Z(S) denote the monic polynomial with simple roots exactly S. Write T₀=Z({1,2,3}), T₁=Z({0,2,3}), Tᵣ=Z({0,1}), and Z=Z({0,1,2,3}). The NO residual in characteristic two is

    T₀(X)(A(X)+1)³ + T₁(X)A(X+1)³
    + Tᵣ(X)A(X+2)(A(X+2)+1) + Z(X)B(X).

The YES instance instead uses (A(X)+1)²(A(X+1)+1) in the first term and A(X)³ in the second. The constants 0,1,2,3 are polynomial-basis labels and translations are field additions. These selectors use the source vanishing products at every field point. [Ben-Sasson and Viola, Theorem 4.2 and §5.2, equations (2)–(5)](https://eccc.weizmann.ac.il/report/2014/017/download/)

## All global assignments

If A fails its direct RS test at one seed, it fails at all seeds because the test asks for its entire word. Otherwise fix its affine polynomial. Let S be the accepted seed set of the **paired RS test by itself**. The ACSP predicate can destroy invariance under XOR 9, so applying the paired-set parity argument directly to the *joint* acceptance set would be invalid.

If the paired RS sparse case holds (at most one outer-row label or at most two low labels), |S|≤32 and at most 32 seeds can pass the joint predicate. Otherwise the paired proof constructs a degree-≤31 polynomial P over F agreeing with physical B at every seed in S. In particular it agrees on all joint acceptances. This agreement on the **specific sites** is stronger than a distance bound giving agreement at some sites of equal cardinality.

Form the residual polynomial with P in place of B. The four summands have degrees at most 6, 6, 4 and 35. Both 0 and 1 cannot be roots: the nonzero surviving selector at 0 would require A(0)=1, while at 1 the surviving selector requires A(0)=0. Thus it is a nonzero polynomial of degree at most 35 over F. Every joint acceptance is one of its roots. Combining both cases, each global assignment rejects at least **221 of the 256 seeds**.

## Attainment and adversarial control

For NO put A=0. Let U(X) be the product of X+v over the 32 distinct polynomial-basis indices v=4,…,35 and put

    B(X) = (U(X)+U(0))/(X U(0)).

The numerator is divisible by X; B has degree 31 and at every interpolation point v it takes value 1/v. The residual factors as T₀(X)U(X)/U(0), with exactly the 35 distinct roots 1,…,35. Its bivariate extensions at both levels make the paired test pass everywhere, attaining exactly 221 joint rejections. For YES, A(X)=1+X and B(X)=X make the residual vanish identically with both degree tests satisfied. (The first two summands together are (X+1)Z, the third is Z, and the fourth is XZ.)

The extremum does not require the actual B root to be a codeword. Flip the lowest bit at field address 48 of this NO witness while keeping every physical auxiliary value. This word disagrees at just one point with the old polynomial and hence cannot have degree ≤31. A single inner row now fails. Pairing checks both inner parities, so the RS test rejects the entire outer coset 48,…,63. That coset was disjoint from the 35 roots, and the residual still rejects at 48 after the toggle as verified by direct field arithmetic. The joint acceptance set remains exactly 1,…,35.

Run `python check_outer_application.py` in this directory. It reconstructs the residual using independent carryless multiplication and checks agreement of its full base-field multiplication table with the physical verifier. It evaluates the two-level B tests on every physical leaf for each witness, sharing the underlying geometry and interpolation implementation with `two_level_oracle.py`. It confirms the factored NO residual on all 256 seeds, including the constrained endpoints, then obtains the following results.

| Field proof | ACSP accepts | Paired RS accepts | Joint accepts | Joint rejects |
|---|---:|---:|---:|---:|
| Honest YES | 256 | 256 | 256 | 0 |
| Degree-31 extremal NO | 35 | 256 | 35 | 221 |
| NO with a changed root at 48 | 35 | 240 | 35 | 221 |

The all-assignment lower bound is the interpolation argument above. The executable checks the attaining assignments on the fixed physical symbol layout. The 256-seed scan, finite interpolation, and extra direct A test are charged literally here. No uniform verifier generation theorem, bit-level circuit, asymptotic compiler cost, or hierarchy simulation is obtained from this extension.
