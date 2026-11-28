# Linearized degree: selectors, interpolation, quotients, and the outer circuit

Date: 2026-11-28 night. Source checkpoint: `2a546c3781d71cd159b388997bd5312a7ceb78e6`.

Status: targeted primary-source reading and elementary written derivations. No novelty, complete source-compiler verification, or new complexity separation is claimed. The division filtration in Section 5 was proposed by the research lead and independently attacked here. The source theorems and the repository deductions are separated below.

## 1. Primary references and exact scope

| Source | Locations verified | What is used |
| --- | --- | --- |
| Ben-Sasson and Viola, [Short PCPs with projection queries, ECCC TR14-017](https://eccc.weizmann.ac.il/report/2014/017/download/), February 9, 2014 | Lemma 1.6, pp. 4–5; Theorem 4.2, p. 10; Definition 5.1 and Lemma 5.2, pp. 13–14; equations (2)–(5), pp. 14–15; Claims 5.4–5.5, pp. 15–16 | Polynomial-size gate encodings use cells indexed by seed and gate. The ACSP uses translated reads, affine-subspace selectors, a Boolean-range constraint, and a quotient identity. Honest bounded-degree A exists; for fixed A, the identity determines B. No low Boolean degree for gate rows or canonical gate evaluation order is promised. |
| Claude Carlet, [Boolean Functions for Cryptography and Coding Theory, author's monograph](https://www.math.univ-paris13.fr/~carlet/book-fcts-Bool-vect-crypt-codes.pdf) | Section 2.2, printed pp. 62–63; Proposition 6 and its proof, p. 63; linearized-polynomial characterization immediately afterward | For the canonical univariate representation over GF(2^k), vectorial Boolean degree equals the maximum binary weight of a nonzero exponent. Frobenius maps and linearized polynomials are GF(2)-linear. The monograph supplies a direct dimension proof. |

The following selector, interpolation and quotient lemmas are explicit mathematical deductions. They are not attributed as new theorems of either source. The relevant local compiler is the specified variant in Expedition 038; Expedition 048 supplies its coordinate normalization and its conditional time/error ledger. This audit compared the required repository documents with the previous checkpoint before reusing unchanged readings.

## 2. Three degrees that must remain distinct

Write F=GF(2^k), and identify its elements with k Boolean coordinates using any fixed basis. For a field-valued function f:F->F, its Boolean degree is the maximum ANF degree of its coordinate functions. This definition is invariant under invertible linear changes of input or output basis.

If the unique representative is

    f(X)=sum_{0<=e<2^k} a_e X^e,

then Proposition 6 gives

    deg_2(f)=max_{a_e!=0} wt_2(e).

The representation must first have degree below |F|. A formal polynomial of larger degree can represent a much simpler function after reduction modulo X^|F|−X. On a proper affine input subspace, the same exponent calculation gives an upper bound; equality there requires a separate argument.

Consequences include:

- X^(2^j) has Boolean degree one, although its ordinary univariate degree is 2^j.
- X^(2^j−1) has Boolean degree j when the exponent is below |F|.
- A degree-D ordinary polynomial has Boolean degree at most floor(log2(D+1)); a fixed-rate RS cutoff still permits Boolean degree of order k.
- An arithmetic circuit's size does not bound the Boolean degrees of its intermediate values. The values, and the order/identities used to compute them, must be examined.

The field quotient, the Boolean degree of the quotient function, and the gate rows used to verify a quotient identity are different objects.

## 3. Affine selectors have exactly codimension degree

Let U subset H subset F be affine GF(2)-subspaces, of dimensions u and h. Put c=h−u. This h is an affine-space dimension, not the recursion-depth parameter from Expedition 048.

Choose a in U and write U=a+V and H=a+W, where V subset W are linear subspaces. For a finite set S, let

    Z_S(X)=product_{s in S}(X−s).

For linear V, Z_V is a monic linearized polynomial. For affine U,

    T(X)=Z_U(X)=Z_V(X−a)

is linearized plus a constant, hence an affine GF(2)-linear function on F. Its kernel after translating by a is V. Its image on H is the c-dimensional **linear** space

    J=Z_V(W).

It is linear even when H and U are affine: a belongs to both, and T(a+w)=Z_V(w).

### Exact polynomial identity

Both sides of

    Z_H(X)=Z_J(T(X))

are monic of degree 2^h and have exactly the roots H. Equivalently, T(x) belongs to J precisely when x belongs to a+W. Thus this is an identity of formal polynomials, with no missing scalar.

Write the linearized polynomial of J as

    Z_J(Y)=sum_{j=0}^c b_j Y^(2^j),

where b_c=1 and b_0!=0. Since J contains zero, Y divides Z_J(Y). Therefore

    Sel_{U subset H}(X)=Z_H(X)/Z_U(X)
                       =sum_{j=0}^c b_j T(X)^(2^j−1).

The j=0 term is the constant b_0; no pointwise division at T=0 is performed.

Every term has Boolean degree at most j, because T is affine and Frobenius powers are linear. Hence the vectorial degree is at most c. On H, the selector is b_0 on U and zero on H\U. Choose an output linear functional taking b_0 to one. Its restriction to H is the indicator of an affine subspace of codimension c, whose ANF degree is exactly c. Affine restriction cannot increase degree, proving

    deg_2(Sel_{U subset H})=c.

For c=0 the selector is one and has degree zero. In general its value on U is a nonzero constant, not necessarily one. The zero/nonzero property is what the residual argument needs; a constant normalization can be applied if desired. This also avoids overreading the informal “equals one” language after BV14's unnormalized selector definition.

### A circuit that controls intermediate degrees

Compute T using Frobenius maps, constant field multiplications and additions. These are all affine or linear Boolean operations and have polynomial-size XOR implementations in k. To obtain the selector terms, compute

    P_0=1,
    P_(j+1)=P_j^2 * T.

Then P_j=T^(2^j−1). If P_j has Boolean degree at most j, its field square has the same bound and multiplication by T raises the bound to at most j+1. Implement squaring by its linear map, and field multiplication by bilinear bit products followed by XORs. Every AND intermediate in the multiplication has degree at most j+1; subsequent XOR partial sums do not increase it. Therefore every selector gate row has degree at most max(1,c), including the input-coordinate operations. The selector output itself has degree exactly c.

This is a public implementation choice, independent of the proof or of a known satisfying witness. It computes the same selector on arbitrary proof branches. A long sequential product over all elements of H is neither required nor the intended succinct size bound.

The coefficient construction is also polynomial time. Given a basis of V, build its vanishing polynomial one basis vector at a time using Z_(V+<v>)(X)=Z_V(X)^2+Z_V(v)Z_V(X); only its linearized coefficients are stored. Applying Z_V to a complementary basis of W produces a basis of J, and the same recurrence constructs Z_J. No enumeration of the 2^u or 2^h field points is required.

## 4. Canonical interpolation preserves the assignment's Boolean degree

Let U be an h-dimensional affine subspace of F and w:U->F any function of Boolean vectorial degree r in affine coordinates on U. Let A be its unique univariate interpolant of degree less than 2^h. Then

    deg_2(A:F->F)=r.

Proof: consider the F-vector space

    V_r=span_F {X^e: 0<=e<2^h, wt_2(e)<=r}.

Its dimension is B(h,r)=sum_{j<=r} binom(h,j). Restriction to U is injective by the root bound. Every restricted monomial has Boolean degree at most wt_2(e), since the affine input parameterization and Frobenius maps have degree one. The F-vector space of F-valued functions of Boolean degree at most r on h Boolean coordinates also has dimension B(h,r), by its ANF coefficients. Thus the injective restriction map is onto that space. The unique interpolant of w belongs to V_r, so its global degree is at most r. Restriction supplies the matching lower bound.

For the BV assignment domain H0, this identifies the exact Boolean degree of the canonical A root with the ANF degree of the genuine Boolean satisfying assignment indexed by H0. A low RS degree bound alone does not make that assignment easy. Conversely, a low-degree Boolean assignment has a canonical low-Boolean-degree extension; it need not be an F-affine polynomial.

An F-affine nonconstant A(X)=aX+b is injective and can take Boolean values on at most two input points. Thus the designed two-site affine families are useful finite models but cannot be substituted for an arbitrary growing BV Boolean assignment domain.

## 5. The quotient filtration under the honest cutoff

This section records the research lead's elementary division argument, independently audited here. Let L be a monic affine-linearized polynomial of ordinary degree S=2^h:

    L(X)=X^S + sum_{j<h} l_j X^(2^j) + l_const.

For an exponent e>=0 define

    chi_h(e)=floor(e/S)+wt_2(e mod S).

Let Chi(P) be the maximum chi_h of its nonzero monomials. Handle the zero polynomial separately. In mathematical upper bounds we may assign it degree zero; the algebraic diagnostics use the sentinel minus one. No positive degree cutoff depends on this convention.

### Division claim

Polynomial long division of Q by L produces a quotient B satisfying

    Chi(B)<=Chi(Q)−1,

provided B is nonzero. This holds whether or not the remainder is zero.

Indeed, canceling a leading term X^e with e>=S inserts X^(e−S) into the quotient; its chi is exactly chi_h(e)−1. Each new lower dividend exponent is either e−S or e−S+2^j with j<h. Adding 2^j increases chi by at most one. If the low h-bit block overflows, the quotient part increases by one but the carry removes at least one low one; the same inequality still holds. Thus newly introduced dividend terms never exceed the current maximum chi. Descending long division proves the claim. Coefficient cancellation can only remove monomials and cannot harm the bound.

### Boolean-degree consequence used here

Suppose Q=L B and

    deg_uni Q<3S<|F|.

Then deg_uni B<2S. For e<3S, floor(e/S) is 0, 1 or 2, giving

    chi_h(e)<=wt_2(e)+1.

For e<2S, chi_h(e)=wt_2(e). Both Q and B are canonical full-field representatives because their degrees are below |F|. The binary-weight identity and division claim give

    deg_2 B <= Chi(Q)−1 <= deg_2 Q.

There is no quotient computation by a guessed circuit in this statement. It is a structural bound on the uniquely determined formal quotient. The zero numerator gives B=0 and is immediate.

The ordinary degree restriction is essential to this deduction. In general, division by a linearized polynomial can increase Boolean degree. For example Q=L^4 is Frobenius-linear in L, while B=L^3 can be quadratic as a function when L has sufficiently large image. The source's honest ordinary-degree cutoff is doing work.

## 6. Application to the actual BV outer residual

Use source dimensions ell=ell1+ell2, dim H0=ell, dim H=ell+1. Set

    S=|H|=2^(ell+1),
    c=ell2+1,
    k=log2 |F|.

The source clause selectors have codimension c in H. The range selector, for a translate of H0 inside H, has codimension one. Thus c is not the ambient codimension k−dim H. For T=2^n, the source construction has c=O(log n) and k=n+O(log n). The external field margin is chosen large enough here that 3S<|F|, as in the repository's slack convention.

In the unambiguous form of equations (4)–(5), write

    Q_A(X)=sum_beta Sel_(beta+H1 subset H)(X)
                    * product_(i=1..3)(A(X+s_i,beta)−b_i,beta)
            + Sel_(zeta+H0 subset H)(X)
                    * (A(X+zeta)^2−A(X+zeta)),

    residual(X)=Q_A(X)−Z_H(X)B(X).

The signs, shifts and subspaces are public. The translated reads preserve Boolean seed degree. If r_A=deg_2 A, the selector lemma and GF(2)-linearity of squaring give

    deg_2 Q_A <= D0 := max(c+3r_A, 1+r_A).

For the honest cutoff deg_uni A<=|H0|=S/2, every clause term has ordinary degree less than S+3S/2=2.5S, and the range term has degree at most 1.5S. Consequently

    deg_uni Q_A<3S<|F|.

When the assignment is satisfying, Claims 5.4–5.5 give the formal identity Q_A=Z_H B. The quotient lemma therefore proves

    r_B=deg_2 B<=D0.

In particular, B is not an independently free or independently harder exact-degree choice under these assumptions. For fixed A the polynomial quotient is unique. Different satisfying assignments may give different A, and looser A cutoffs may permit off-domain extensions; neither fact permits independently choosing B.

### Public Boolean implementation bound

With A/B read values supplied as inputs, choose the selector circuits above, linear squaring/constant multiplication, and bilinear field multiplication. Every honest gate row evaluating Q_A has degree at most D0 (or degree one for a public input when that is larger). The B*Z_H multiplication has bit intermediates of degree at most r_B+1<=D0+1. Additions do not increase degree. On a satisfying proof the completed residual is zero at every seed, so a final equality-to-zero test has constant-valued honest internal rows when it is performed after residual formation. Thus one public polynomial-size outer circuit has all honest auxiliary rows of degree at most

    D0+1=max(c+3r_A,1+r_A)+1.

The circuit is chosen from the instance, not from a witness. It preserves the outer predicate on arbitrary input proof values. This controls the **outer residual computation only**. It does not construct all Boolean clauses of the recursive proximity verifier or prove a degree bound for every possible equivalent circuit.

With r_A=O(1), the bound is O(log k). With r_A on the n/log n scale, it incurs a constant-factor degree cost and an additive O(log n); the hierarchy ledger must pay that factor by choosing the original degree coefficient smaller. No numerical constant is extracted from the external counting theorem.

## 7. What these exact lemmas do not say about approximation

Exact-degree control does not supply a weighted-error stability theorem. If two assignments on H0 differ at just one point p, their canonical interpolants differ by a nonzero scalar times the Lagrange polynomial for p. That polynomial has roots exactly H0\{p}, so the extended field words differ on

    |F|−|H0|+1

points. A small change on the assignment domain may therefore become a constant-density field-symbol change outside it. Restricting an existing approximation to H0 has the ordinary domain-size loss; extending an approximately correct assignment cannot be assumed to preserve its error budget.

Likewise, a high exact-degree auxiliary row need not obstruct the weighted approximation target. An r-variable conjunction is nonzero on only a 2^(−r) fraction of seeds and is well approximated by zero at that fraction. For gates of this kind with total occurrence/fiber weight W, zeroing only those with support fraction at most 2^(−d) costs at most W*2^k*2^(−d). It fits a raw gap budget gamma*2^k/2 when W*2^(−d)<gamma/2. Polynomial W and inverse-polynomial gamma need only d=O(log k).

This is a sufficient condition for sparse artifacts, not invariance under arbitrary gate encodings. Public computations with nontrivial distance from the permitted polynomial class can be forced into gate rows while their values cancel later. The companion compiler-artifact work addresses that distinction. The constructive outer rewrite above avoids a particular artifact exactly and uniformly; it does not rely on deleting rarely wrong gates.

## 8. Remaining scope: recursive geometry and interpolation gates

BV14's recursive basis/abscissa computation is polynomial time, but polynomial time alone is not a Boolean degree bound. A fixed field inverse map, extended by zero at zero, has representative X^(2^k−2) and vectorial degree k−1. This illustrates why an unexamined reciprocal gate is insufficient evidence of low degree. It does not prove that the actual denominators in a restricted interpolation computation realize that degree; their seed image and cancellations must be analyzed.

A separate fixed-node algebraic fact is sound: for a fixed monic linearized q of degree 2^l, the polynomials X^i q(X)^j with i<2^l and j<2^(k−l) form a triangular F-basis, and the subset wt_2(i)+wt_2(j)<=r spans exactly the degree-at-most-r Boolean functions. Their leading exponents concatenate i and j, their binary-degree upper bounds follow from Frobenius linearity, and the filtered dimensions match. Fixed-node row/column restrictions or jointly affine substitutions preserve that bound.

It does not follow that q, its coefficients, and the relevant affine parameterizations remain fixed when a normalized transverse row varies over many recursively selected nodes. That is the next hypothesis to check. The actual two-level fixture has fixed low subspaces and can be audited directly; the complete growing recursion and its Boolean gate rows remain outside the present result.

## 9. Finite-family scope check

Read the companion [accepting-family.md](accepting-family.md) and the actual Expedition 041 auxiliary-direction definitions. The three-witness field classification is properly scoped: full leaf coverage, shared-cell interpolation and the ordinary degree/root bound force a unique quotient and unique physical extension for each of its three allowed affine A roots. Its two-site Boolean range test is compatible with the stated small designed residual. It explicitly does not instantiate the entire growing BV assignment relation.

The omitted selector term at its other clause site is a designed arithmetization choice. An arbitrary Boolean tautology does not necessarily yield an identically zero polynomial off the Boolean assignment domain; keeping the exact displayed residual matters for its quotient. No inherited 221 count or finite affine raw-row census is used here as a Boolean gap or a general witness-degree theorem.

No new experiment results are asserted by this source note. The lead's monomial-division tests and the family agent's exact field runs should be cited from their own recorded artifacts. The arguments above are the substantive evidence for the general algebraic claims.
