# Public layouts, existential completeness, and a possible guessed-layout branch

Session: approved November 24 JST night; completed November 25 JST. Source checkpoint: `ce66bdc08702922138dc77b93c6c2b4054873944`.
Role: historian / quantifier skeptic. This is a targeted source reading and elementary written argument, not a new proof-kernel execution, external review, or novelty claim.

## 1. Source facts

**Ben-Sasson–Viola, _Short PCPs with projection queries_, ECCC TR14-017, February 9, 2014, Theorem 1.1 (printed p. 2).**

<https://eccc.weizmann.ac.il/report/2014/017/download/>

Given the public instance x, the theorem constructs Query and Dec in poly(n, log T) time. Completeness requires existence of one globally shared proof for a YES instance; soundness quantifies over every proof for a NO instance. Each Query output coordinate is a constant, one seed bit, or its negation. Dec is a 3CNF. The source does not require low degree for every valid proof. It does not provide a witness-dependent layout procedure. Definition 1.3 and Theorem 1.4 additionally expose the relevance of efficient short descriptions and closure under projections.

**Viola, _New lower bounds for probabilistic degree and AC0 with parity gates_, ECCC TR20-015 revision 5, January 12, 2021, §2.3 (printed pp. 13–15).**

<https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/>

The proof defines a canonical proof-bit function in E^NP by finding the first satisfying assignment bit by bit. After fixing the language input, pointwise probabilistic approximation and averaging yield one polynomial with sufficient test acceptance. The final nondeterministic procedure guesses that polynomial, not its approximation certificate; NO soundness applies to every guessed polynomial. Its description length and the degree after composing fixed queries are explicitly charged. The theorem does not require approximation of all satisfying proofs.

**Moshkovitz–Raz, _Two Query PCP with Sub-Constant Error_, July 28, 2008, §5.3.1 (printed pp. 31–32).**

<https://www.cs.utexas.edu/~danama/papers/two-prover/two-prover-full.pdf>

This primary paper describes Hadamard encoding as evaluating a linear function with a given coefficient vector at all field vectors. The block length is exponential in the coefficient dimension; §3.10 explicitly treats that cost as tolerable only because the inner dimension is small. The public coefficient-tag formula below is an elementary use of the same linear evaluation mechanism, not a new code construction or an instantiation of this paper's PCP theorem.

**Abbe–Shpilka–Ye, _Reed-Muller Codes: Theory and Algorithms_, arXiv:2002.03317v2, June 10, 2020, §II-A/B (printed pp. 5–6).**

<https://arxiv.org/pdf/2002.03317>

The source defines binary degree-d Reed–Muller words by multilinear polynomial evaluations, gives dimension D=sum_{j=0}^d binom(t,j), and proves minimum distance 2^(t-d). For a fixed punctured set of R coordinates, there are at most 2^D distinct restrictions. The covering inequality used in Expedition 046 then follows by multiplying that count by the size of a radius-e Hamming ball. This is standard code counting, not a novelty claim.

## 2. Correct quantifiers for the public compiler model

Let I be the public instance and W(I) its satisfying-witness set. The model chosen by Issue 36 asks for an efficiently computed public injective layout Lambda_I. The useful completeness condition has the form

    for every YES I, there exists w in W(I), a padding completion,
    and an approximating polynomial/distribution meeting the budget
    for the fixed layout Lambda_I.

A construction valid for every w in W(I) is a stronger sufficient condition. A counterexample showing one bad satisfying witness only defeats that stronger condition. To refute existential completeness for a given I, all satisfying witnesses must fail the target property for its fixed layout.

The existing Expedition 046 fixture has a publicly specified honest reference. The repository's arbitrary-independent-constant-row counting obstruction must therefore not be silently promoted to an obstruction for the fixture's actual satisfying set.

## 3. A public dictionary sufficient condition

This section is our elementary derivation, not a theorem attributed to a source above.

Suppose public syntax supplies coefficient vectors c_i in F2^b for R physical rows and guarantees, for each permitted witness w,

    f_{i,w}(z) = sum_{j=1}^b c_{i,j} g_{j,w}(z).

Assume each g_{j,w} has seed degree at most delta. The basis values may depend on w; the vectors c_i and the row assignment may not. Let m be the maximum multiplicity of a coefficient vector, and assign each repeated row a distinct rank in ceil(log2(max(1,m))) bits. Use tag (c_i,rank_i), keeping rows physically distinct.

The exact completion

    F_w(c,rank,z) = sum_j c_j g_{j,w}(z)

has degree at most delta+1 and ignores ranks. It uses

    Q = 2^k * 2^b * 2^ceil(log2(max(1,m)))

addresses. A constant basis element handles affine offsets. If b=O(log R), storage is polynomial in R and seed-domain size. If b is linear in R, this construction is exponentially wasteful. Uniformity additionally requires computing c_i, ranks, and modified queries within the intended public preprocessing bound. Merely asserting the existence of a low-rank representation is insufficient.

For constant rows, this is the familiar linear/Hadamard evaluation viewpoint. A globally fixed public coefficient dictionary is the mathematical condition; small per-row witness dependence alone does not imply it. For example, rows that each equal one unrelated witness bit already have R independent degrees of freedom.

## 4. Witness dependence is not intrinsically a soundness violation

This is a separate conditional algorithmic branch; it is not the public compiler requested by Issue 36 and is not supplied by the cited PCP theorem.

Assume an explicit verifier has M fixed signed clauses whose queries have the form (i,rho(z)), with row identity i constant within each template and each coordinate of rho a constant, one seed bit, or its negation. This includes XOR offsets and public-bit clamping. A nondeterministic tester can:

1. Guess an injection Lambda:[R] -> {0,1}^t and verify injection.
2. Guess a degree-d polynomial P on t+k address bits.
3. Count the actual failures of the relabeled signed clauses, using (Lambda(i),rho(z)).

Every guessed injection and polynomial induces one original global proof pi(i,z)=P(Lambda(i),z). Thus every NO soundness bound for arbitrary original proofs still applies. A YES instance needs one witness and one layout that permit a qualifying P. Since each Lambda(i) is a constant within a clause, projection substitution preserves degree d, and a three-literal clause has degree at most 3d.

**Injection is sufficient but not necessary for NO soundness alone.** Even a colliding Lambda defines the displayed global pi provided the SAME row map is reused at every occurrence. Collisions merely impose extra equalities on original rows. Injection is needed for transporting every original proof without value restrictions and for exact preservation of minima, individual physical bit errors, and the old signed sensitivity. If equal rows are merged, the Hamming metric and reader multiplicity need a separate analysis.

Let m=t+k and B(m,d)=sum_{j=0}^{min(d,m)} binom(m,j). The real charge is substantial:

- Explicit row-table guess: R*t bits.
- Injectivity check: deterministic sorting of R labels, costing O(R*t*log R) bit comparisons under a standard comparison sort, with ordinary sequential-record implementation overhead charged separately.
- Polynomial guess: B(m,d) bits in a fixed squarefree monomial order.
- Signed substitution: at most 2^d B(m,d) pre-cancellation records per literal. A naive product of three substituted lists uses at most O((2^d B(m,d))^3) records per clause, followed by sort/XOR cancellation on k-bit masks. This is a deliberately loose valid bound.
- Counting: M calls, each on k seed variables at degree at most 3d. Viola Theorem 12 gives time 2^(k-c*k/(3d)+O(log k)) for an absolute c>0 when d>0; constants are handled directly. M, bit-cost and machine-model factors must be paid. Compare raw integer failure totals to the selected threshold exactly.

This says nothing about arbitrary whole-address permutations, whose composition need not have low degree; nor does it cover tag coordinates that vary with z without a separate proof.

For Expedition 046, mandatory raw-map buffers already force R >= k(4s^2+s-1), with N=2s^2. Hence writing such a table costs at least Omega(N*k*t), which cannot fit an o(N) target. The actual M is also enormous. Polynomial-in-proof-size storage is not enough for a sub-proof-size decision procedure. A future compiler with few constant-tag templates would need a fresh exact cost assessment.

The downstream clock in Expedition 039 is 2^n/n up to fixed polynomial factors, with k=n+O(log n), M=poly(n) and degree d=O(n/log n). Its canonical target width W=n+O(log n) is a sufficient convenient choice. A new width m=O(n) would still make B(m,d)=2^o(n) at d=O(n/log n); signed expansion is also subexponential. Thus t=O(log n) is not logically necessary for the coefficient/counting ledger alone. Constant-factor growth in m requires smaller degree constants, a new monotone occupied-length encoding, canonical E^NP construction, and fresh approximation-error accounting. None of those adjustments can erase the explicit Omega(N*k*t) label-table cost or the large M of Expedition 046.

## 5. Tiny control separating quantifiers from cost

Every vector of R constant row values w_i has a witness-dependent degree-one layout at polynomial storage: label row i by (w_i,rank_i), with ranks unique among equal values, and complete by F(value,rank,z)=value. At most 1+ceil(log2 R) tag bits are needed. This does not contradict a fixed-layout covering obstruction because the layout changes with w.

It also supplies no compression miracle: its explicit label table carries the R independent witness bits. Therefore a useful graveyard entry should reject the overbroad inference “witness-dependent layouts always invalidate soundness,” while retaining the narrower conclusions “not a public compiler” and “explicit guessing fails the relevant cost bound here.”

An actual soundness failure arises from changing the row map by occurrence. The original clauses (v) and (not v) have one failed clause on every proof. Map their occurrences to two unrelated new cells and choose their values 1 and 0 respectively; both clauses accept. There is then no single old proof pi decoded from the occurrence-dependent answers. Constancy of one map across every alias, rather than injectivity by itself, is the essential NO-soundness condition.

## 6. Evidence and limits

The four linked primary papers were retrieved and the cited statements read. Source notation was checked against repository expeditions 034, 039 and 046. No complete external PCP proof was reconstructed, no Lean was run, and no novelty clearance is asserted. The dictionary and guessed-layout statements are elementary written deductions with stated hypotheses; they still require integration with the actual verifier/compiler and the intended language-time parameters. The next useful branch is a succinct witness-dependent row map whose uniformly available or guessed description preserves the query-composition class and the complete time ledger, or a low-dimensional public dictionary. Neither branch is ruled out just by witness dependence.
