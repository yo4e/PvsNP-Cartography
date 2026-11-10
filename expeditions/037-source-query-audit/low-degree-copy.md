# Stronger no-go: full XOR copies also preserve the fixed-degree problem

2026-11-10 JST, later session. Author: 月野テンプレクス. Status: author-written general algebraic derivation plus exact finite corroboration. No independent review, Lean acceptance, or novelty claim. This strengthens replica-invariance.md for a PARTICULAR degree-compatible permutation family; arbitrary nonlinear permutations are not covered by this strengthening.

## Definitions

Let X=F2^m, with any binary target pi. Let Poly_D(X) be the Boolean evaluations of genuine GF2 polynomials of total degree at most D. Replacing powers x_j^e by x_j on Boolean inputs does not increase degree, so this is a finite set of actual functions, not an unbounded symbolic search space. D>=0 is fixed, including constants and m=0.

Define the uniform approximation distance

    dist_D(pi) = min_{p in Poly_D(X)} Pr_x[p(x)!=pi(x)].

For a normalized nonnegative real weighted family of signed OR tests all satisfied by pi, also define

    C_D = max_{p in Poly_D(X), error(p)>0} failure(p)/error(p),

with the harmless convention zero for an empty maximum. An exact row has error zero AND failure zero, so failure(p)<=C_D*error(p) holds for every eligible p. This is a degree-restricted constant, unlike the unrestricted C in Expedition036.

Make a copy for every s in X, and use addresses (y,s), with honest target

    pi'(y,s)=pi(y+s).

Every test uses a SINGLE uniform s for all occurrences and maps an original address x to (x+s,s). Uniform error is over all 2m address bits. Let dist'_D and C'_D denote the same quantities using degree<=D polynomials on those 2m bits.

## Both exact identities

For any candidate P(y,s) of degree<=D and fixed s, define p_s(x)=P(x+s,s). Each substitution is affine, so p_s has degree<=D. Under the product uniform measure,

    error(P)=E_s error(p_s),
    failure(P)=E_s failure(p_s).

The first equality immediately gives error(P)>=dist_D(pi). The second and the defining inequalities for C_D give failure(P)<=C_D*error(P). Thus dist'_D>=dist_D and C'_D<=C_D.

For the opposite inequalities, take an original candidate p and define the JOINT polynomial

    P(y,s)=p(y+s).

This is one actual polynomial on 2m variables of degree<=D: substitute the degree-one forms y_j+s_j in its formal polynomial. Every section p_s equals p because (x+s)+s=x in characteristic two. Consequently BOTH its uniform error and its test failure equal those of p. Apply this lift to a distance minimizer and, where nonzero, a ratio maximizer. The finite sets guarantee attainment. If C_D=0 the upper inequality and nonnegativity suffice. We obtain

    dist'_D(pi') = dist_D(pi),
    C'_D = C_D.

This is a general derivation, not an assertion inferred from enumeration. The degree-preserving slice gives one inequality; the simultaneously degree-preserving lift gives the other. Arbitrary per-copy lookup polynomials would not justify the reverse direction. No independence among literals or resampling of p is used.

## Interpretation and limits

Full XOR-copy smoothing cannot improve either the best uniform approximation at a fixed degree or the fixed-degree worst test-error ratio. Thus the unrestricted no-go is not merely caused by allowing high-degree adversaries. This does not say that every smooth encoding is impossible, or that a PCP with an intrinsically good query distribution is impossible. It concerns disjoint translated copies with the stated full product measure and unchanged tests.

The larger address space can still worsen the cost of exact counting. Existential algebraic identities do not supply a faster way to write a large lifted representation. A source-dependent rank/fiber proof and a fixed-input error premise remain different obligations.

## Finite attack and evidence boundary

verify_low_degree.py constructs all ANF evaluation tables of degree<=D rather than filtering a guessed family. It checks every target on one- and two-bit original address cubes, with one fixed-seed satisfied three-clause family per target and weights1,2,3. It covers D=0..1 and D=0..2 respectively, including all eligible polynomials on the doubled cubes. It checks both inequalities through actual affine-slice membership and joint-lift membership, then compares the exact optima computed from the literal tests.

There are56 family/degree cases,33792 polynomial score evaluations,133328 slice-membership checks and440 lift-membership checks. Counts include repeated work across targets/degrees, not unique polynomial counts. The test-family choice is sampled, NOT exhaustive over all clause families. Normal/-O stdout and compilation succeeded locally; remote evidence is recorded separately after observation. No finite count is a new general proof or an independent reviewer.
