# Conditional bridge: one fixed proof, explicit oracle queries, and a charged time budget

2026-11-08 JST. Research lead: 月野テンプレクス. Status: **author-written reconstruction of a known method**, conditional on the explicitly imported PCP and time-hierarchy theorems and the written counting-runtime analysis. This is not a new lower bound, independent semantic review, or a Lean theorem. Finite controls in this expedition do not prove the asymptotic statements below.

## 1. Exact imports and the question being answered

Use the projection-PCP statement of Ben-Sasson–Viola, ECCC TR14-017, February9,2014, Theorem1.1: for a time-T witness verifier, a uniform poly(n,log T)-time construction supplies proof/randomness length r with 2^r<=T polylog T, projection queries, a polynomial-size 3CNF decision predicate, perfect completeness and soundness at most n^-10. The construction, not just existence of query circuits, matters. Source: https://eccc.weizmann.ac.il/report/2014/017/download/ . The relevant theorem page was visually inspected.

Use the binary-language nondeterministic time hierarchy in Seiferas–Fischer–Meyer, JACM25(1),1978, Corollary4.1: for a running time T2, some binary language in NTIME(T2) lies outside the union of NTIME(T1) with T1(n+1)=o(T2(n)). The retrieved primary scan's parsed statement was inspected; visual retrieval failed. In particular take T2(n)=2^n and T1(n)=ceil(2^n/n), changing finitely many small values as needed. The ratio T1(n+1)/2^n tends to0. This imports the hierarchy theorem, not a repository proof of it.

The target comparison is Viola, ECCC TR20-015 revision5, January12,2021, Sections2.1–2.3: https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . Our reconstruction below supplies an explicit encoding, canonical-proof search, parameter ledger and countermodels for that known route; it is not a claim about the latest strongest bound.

Counting ingredient: Expedition033's actual-polynomial count identity has a previously accepted Lean endpoint. Its **separate written** algorithmic bound, after the validation repair described in cost-correction-2026-11-08.md, gives a deterministic counter for canonical squarefree GF2 ANF of degree e>=1 on r variables in time

    r^A0 * 2^(r-r/(200e))

up to a constant. Degree0 is handled directly. The exponent A0 is a fixed constant, not assumed zero. Input normalization, coefficient construction, modular bit arithmetic, sorting, table allocation and accumulation are charged. The Python-to-Lean refinement and this time bound are NOT kernel checked.

**Conditional target.** These ingredients rule out sufficiently small eventually-valid degree alpha*m/log2(m)^2 pointwise1/3 approximations for a particular language F in E^NP. Equivalently, the known route gives a positive-constant lower obstruction on infinitely many lengths. It does not put F in NP, prove an unrestricted circuit lower bound, or settle P versus NP.

## 2. Fix the language and convert whole-verifier soundness to a clause gap

Fix a binary hierarchy language L in NTIME(2^n) outside NTIME(ceil(2^n/n)). Its machine is fixed before all constants below. Apply the imported PCP to its witness verifier. Pad randomness and proof addresses to a uniform, explicitly computable length

    n <= r(n) <= n + C*ceil(log2 n) + C0.

Unused random bits are ignored; old addresses are extended by constant bits. This preserves projection queries and the same acceptance fraction. One may pad the decision predicate to have a nonempty list of k clauses; repeating literals handles shorter nonempty clauses. A tautological extra clause handles an empty list without changing the whole verifier. For large n, k<=n^B, enlarging a fixed integer B if necessary.

For each x of length n, clause i has three address maps q_i,j:{0,1}^r->{0,1}^r. Every coordinate is0,1,z_l or1+z_l. Its predicate R_i is an OR of three possibly negated queried bits. For x in L a single proof pi satisfies every clause at every random string. For x not in L, every single global proof pi makes the whole CNF true on at most n^-10 of the random strings. On each remaining string at least one clause fails. Therefore, averaging uniformly over clauses and random strings,

    failure(pi) >= (1-n^-10)/k >= 1/(2k) >= n^-(B+1),  n>=2.

Set b=B+1 and delta=n^-b. This exposes the gap dilution by the number of clauses; whole-CNF soundness and average-clause soundness are not interchangeable without this step. Constants and sufficiently-large-length guards can absorb harmless finite padding.

## 3. The canonical proof-bit language is in E^NP, not silently in NP

For each x, explicitly form a CNF Phi_x with one variable for every r-bit proof address and all k*2^r three-literal constraints. Its encoding length is

    S=O(k*2^r*r)=2^n*poly(n),

and it can be generated in that time by enumerating the random strings and the uniformly constructed query maps. The address space has N=2^r variables, polynomial in the explicit formula length.

An ordinary SAT oracle first tests Phi_x. If unsatisfiable, define pi_x to be the all-zero proof. Otherwise obtain its lexicographically first satisfying assignment by at most N further SAT queries: with the previously fixed prefix, ask whether extending it with bit0 remains satisfiable, then select0 or1 accordingly. Every query is an **explicit** CNF plus at most N unit constraints, of length O(S). Its witness is an N-bit assignment, polynomial in its explicit input size. Thus these are legitimate ordinary-NP queries, not a succinct-SAT oracle disguised as NP.

Constructing and writing all queries takes O(N*S*poly(n))=2^(2n)*poly(n). This is acceptable for the definition of an E^NP language. It is deliberately NOT placed inside the final faster tester for L.

Encode (x,y), with y an r(n)-bit address, by a self-delimiting encoding of n followed by x and y. For example, if ell is the binary length of n, use 1^ell 0 bin(n) x y. Its length is

    m(n)=n+r(n)+2*ell+1=2n+O(log n).

Reject malformed encodings. Define F on valid encodings to be pi_x(y). Parsing is uniform and the explicit SAT-prefix procedure costs2^O(m), so F belongs to E^NP. No advice sequence or efficiently computable approximator has been assumed. The polynomial-approximation hypothesis must be applied at total length m, not merely the address length r or original length n.

## 4. Amplification with an integer-computable degree budget

Assume for contradiction that, for this fixed F and all sufficiently large m, there is a fixed finite distribution of GF2 polynomials of degree at most alpha*m/log2(m)^2 with pointwise failure at most1/3. Choose alpha to be a positive rational constant after the fixed cost constants have been determined.

Take t independent samples and compute their odd majority. The exact GF2 multilinear representation of a Boolean function of t bits has degree at most t; composing therefore multiplies the source degree by at most t. For a fixed input let S_bad be the number of erroneous samples. Independence gives

    E[2^S_bad] <= (4/3)^t,
    Pr[S_bad>=t/2] <= (sqrt(8/9))^t.

The elementary integer inequality 2*8^6<9^6 implies that for integer c=b+2 and

    t(n)=12*c*ceil(log2 n)+1,

the failure is at most epsilon=n^-c. This is a written moment/Markov argument; the378 exact binomial checks are only bounded corroboration. Dependence between different query evaluations of the SAME sample is not assumed away.

For an entirely computable descriptor budget, set

    d0(n)=floor(alpha*m(n)/floor(log2 m(n))^2),
    D(n)=min(r(n), t(n)*d0(n)).

For n>=2, m>=2n ensures floor(log2 m)>=log2 n; eventually m<=3n. Since ceil(log2 n)<=2log2 n and log2 n>=1,

    D <= K*alpha*n/log2 n,  K=3*(24c+1).

The budget uses only integer lengths, rational arithmetic and binary logarithm floors/ceilings. It is not a real-valued advice oracle. Squarefree Boolean reduction justifies capping at r. For fixed positive alpha, eventually the uncapped bound is below r. Constants and degree0 cases can be handled separately.

Hardwire the encoded x and header into the amplified distribution. This gives a distribution over actual polynomials on the r address variables with the same pointwise error and degree at most D. No uniform procedure for finding or sampling this distribution is needed by the argument.

## 5. One sample for all tests: the precise averaging adapter

Fix x in L. For any test (i,z), choose one position j whose signed literal under pi_x is true, choosing it before sampling a polynomial P. Because R_i is an OR, if that chosen bit is correctly predicted, R_i accepts. Hence

    Pr_P[R_i(P(q_i,1(z)),P(q_i,2(z)),P(q_i,3(z)))=0] <= epsilon.

This uses only one true literal. Repeated addresses, negations and correlations between the three evaluations are allowed. A generic predicate would instead need a separate error argument, such as the3*epsilon union bound.

Average over (i,z) and interchange the finite sums with the polynomial mixture. Its expected acceptance is at least1-epsilon, so at least one polynomial in its positive-mass support has acceptance at least1-epsilon. Crucially, this is ONE polynomial p_x for every test, not a separate p_i,z for each test and not independent answers for each occurrence. Choosing a different p_x for different original inputs x is legitimate: it is the nondeterministic witness.

For x not in L, every global Boolean proof, including every guessed polynomial, has acceptance at most1-delta<1-epsilon. This quantifier covers bad guesses as well as any hypothetical approximators. The final tester need not certify that its guessed polynomial approximates F; it only computes its actual test acceptance.

## 6. Uniformly construct the tested polynomials and their descriptions

A nondeterministic branch guesses the M=M(r,D)=sum_{j<=D}choose(r,j) coefficient bits in a fixed squarefree monomial order. Such an order can be enumerated in O(M*poly(r)) time without scanning all2^r masks. This avoids duplicate or overlong sparse encodings. It guesses M bits, not all2^M possible polynomials. Every branch has the same bounded description length.

For a fixed clause, substitute each query's constants and literals into p. Substitution of a degree-one coordinate polynomial cannot increase degree; multiplication of repeated variables followed by Boolean reduction cannot increase it either. Let L_j denote the signed substituted polynomial. Then

    Q_i(z)=1 + product_{j=1}^3 (1+L_j(z))

is exactly the clause acceptance bit over GF2 and has actual Boolean polynomial degree at most3D. Its value is not an independently resampled answer.

The construction cost is explicit. A degree-D source monomial expands into at most2^D records under a projection with negations. Since2^D<=M for D<=r, each projected polynomial emits at most M^2 records before sort/XOR aggregation. Including a constant changes this by at most a constant factor. A naive product of three such lists emits O(M^6) records; it is sufficient here. All masks have r bits. Deterministic sorting and coefficient cancellation cost M^6*poly(n), not an uncharged symbolic operation. This is a deliberately loose bound, not an optimal implementation claim.

For D>=1, an injection from subsets of size<=D to sorted padded D-tuples gives M<= (r+1)^D. Eventually r+1<=n^2, so log2 M<=2Dlog2 n<=2Kalpha n. Thus all k polynomial constructions and the descriptor can be bounded by

    2^(12Kalpha n)*poly(n).

Taking alpha<=1/(48K) makes this at most2^(n/2) for sufficiently large n, after absorbing fixed polynomial factors. This charge covers every guessed coefficient string, not just a specially sparse successful witness.

## 7. Exact threshold comparison and the hierarchy budget

Apply the degree-e counter to each Q_i, with e<=3D. Constant Q_i are counted directly. Let C_sum be the sum of its k integer accepting counts. The tester accepts precisely when

    n^c*C_sum >= (n^c-1)*k*2^r.

This uses O(r+log k+c log n) bit integers. There is no floating-point comparison, random estimator or multiplication of separately counted literal probabilities.

Because r>=n and D<=Kalpha*n/log2 n, the count saving for every nonconstant Q_i is at least

    r/(200e) >= log2 n/(600Kalpha).

Let A be a fixed integer absorbing counting overhead, exact arithmetic and the explicit sequential sorting/record implementation. Increase C to absorb the ceiling and constant in r-n; take B to cover k. The total counting work is at most a constant times

    2^n * n^(A+B+C-1/(600Kalpha)).

Select a positive rational alpha satisfying BOTH

    alpha <= 1/(48K),
    alpha <= 1/(600K*(A+B+C+4)).

All these constants depend on the previously fixed machines, not on n, x or the guessed polynomial. The construction plus verification time is then O(2^n/n^4). Even allowing an extra O(n) factor for an explicit binary clock leaves O(2^n/n^3), eventually below ceil(2^n/n). Finitely many small inputs can be hardwired. The final machine is nondeterministic, uniform, and oracle-free. It contradicts the imported hierarchy choice of L.

For tape-model accounting, the prescribed operations are sequential scans and sort/merge passes on polynomial-bit records, rather than an appeal to a generic random-access simulation with an uncharged quadratic penalty. Product-record generation, aggregation and each table-butterfly stage can be performed by these passes with polynomial(n) overhead. This remains a written algorithm/model argument, not a verified compiler or Turing-machine formalization.

The resulting negation is that F cannot have the proposed pointwise approximation at every sufficiently large input length. Therefore there are infinitely many lengths with a positive-constant degree obstruction of the stated scale. This is the scope of the reconstructed known route. It neither yields such a lower bound for every length nor changes E^NP to NP.

## 8. Attacks and evidence limits

The actual implementation defect found here was in the previous worst-case validation cost: hashing all source masks can require quadratic collision work. It does not change polynomial values, but the quadratic charge cannot be hidden in the large-degree b=0 shortcut. The repair uses deterministic sorting and adjacent duplicate checks; the original output and record remain historical artifacts.

A concrete consistency attack uses clauses(v,v,v) and(not v,not v,not v). Every global proof accepts exactly1/2; resampling independently at each occurrence accepts7/8; choosing the proof after seeing the test accepts1. This refutes those altered interfaces, not the source's fixed-proof argument. Uniform-average agreement also cannot replace pointwise approximation: x+y+xy agrees with the constant-one target on3/4 of two-bit addresses but fails on a query concentrated at00.

Finite code tests substitute actual polynomials, construct signed clauses, compare all their head-block counts against brute truth values, and check bounded averaging/prefix-search models. They do not implement an arbitrary PCP, prove the hierarchy theorem, verify all asymptotic constants, or supply independent review. No Lean source changed in this session. The remaining formal gap is the single-proof signed-query adapter and its connection to the existing exact-count endpoint; formal runtime refinement remains separate.
