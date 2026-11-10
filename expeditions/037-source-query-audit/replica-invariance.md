# Tagged permutations preserve congestion, not merely soundness

2026-11-10 JST, later session. Author: 月野テンプレクス. Status: author-written general finite derivation with executable finite controls. No independent semantic review, Lean verification or novelty claim. This tests a proposed modification; it is NOT a counterexample to the published PCP.

## Precise experiment

Let X be a finite nonempty address set of size N, with signed OR tests t of normalized nonnegative real weights nu(t). Fix a binary proof pi satisfying every test. Write A_t for the nonempty set of distinct addresses of literals true under pi. Repeated addresses and tautologies are permitted. For an error set E subset X define

    f(S) = sum_{t: A_t subset S} nu(t),
    F(E) = sum_t nu(t) * [test t rejects pi XOR 1_E],
    kappa = N * max_{nonempty S} f(S)/|S|,
    C = N * max_{nonempty E} F(E)/|E|.

These are the capacity-formula and exact signed-error constants of Expedition036. Here we use the formulas directly; the copy-invariance argument does not need another max-flow theorem. F(empty)=0 by the satisfying-proof premise. In general C<=kappa, not equality.

Choose a finite nonempty set B of L copy labels and a permutation sigma_b of X for each label. The new address set is X times B, uniform over all NL addresses. Sample b uniformly, then t with its original weight. Replace every queried address x by (sigma_b(x),b), leaving the literal signs unchanged. The honest proof is

    pi'(y,b) = pi(sigma_b^{-1}(y)).

The SAME b is used for the entire original test. This is not per-occurrence resampling.

## Exact invariance of both loss constants

For any new address subset S', let S_b be the inverse image under sigma_b of its b-section. Then |S'|=sum_b |S_b| and the forced true mass is L^{-1} sum_b f(S_b). Consequently

    NL * forced_mass(S') / |S'|
      = N * sum_b f(S_b) / sum_b |S_b| <= kappa.

The inequality follows term by term from N f(S_b)<=kappa |S_b|; empty sections contribute zero. Equality is attained by placing an original maximizing set in one copy (or the same permuted maximizing set in every copy). Hence kappa'=kappa exactly.

For an error set E', use its inverse-image sections E_b. Actual failure is L^{-1} sum_b F(E_b), while uniform proof error is (NL)^{-1} sum_b |E_b|. The identical argument gives C'<=C, with equality by using a maximizing error set in one copy. Thus

    C' = C,   kappa' = kappa.

No bound on the width is needed for these identities. They apply to arbitrary real test weights, zero-weight tests and repeated queries. They are written finite-sum proofs, not extrapolations from the checker. Uniform copy weights and comparison with the uniform PRODUCT address measure are explicit premises; replacing one of these measures changes the problem.

## Completeness and universal global-proof soundness

The honest pi' satisfies every copied test. Conversely any global submitted proof h on X times B defines, for each b, an ordinary global proof h_b(x)=h(sigma_b(x),b). Its acceptance is the average of the original acceptance of h_b. Therefore a universal original soundness bound holds in the copied verifier as well. In fact the maximum acceptance over ALL submitted proofs is unchanged: the upper bound is immediate and the same maximizing original proof can be placed in every copy. This argument does not require the existence of a satisfying pi; it applies also on no-instances.

Thus the proposed modification is not dismissed for lacking soundness. It preserves soundness but buys NO improvement in the two error-loss constants. Pure relabeling plus disjoint copies cannot solve the congestion problem.

## Explicit low-degree attack despite perfectly uniform first marginal

Let X be the m-bit cube and q(z) have its first k coordinates zero, retaining the remaining coordinates, 1<=k<=m. Set pi=1 and choose full XOR translations sigma_s(x)=x XOR s, with s uniform on the m-bit cube. The new query is

    (y,s) = (q(z) XOR s, s).

The marginal y is uniform; s is also uniform. But their JOINT distribution lies on y_j=s_j for j<k. It has density ratio 2^k relative to the full 2m-bit cube. The actual GF2 polynomial

    p(y,s) = 1 + product_{j<k}(1+y_j+s_j)

has ordinary total degree exactly k, uniform error 2^{-k} against pi'=1, and error ONE on every query. The factors involve disjoint variable pairs, so the displayed degree is not a quotient-ring illusion. The repeated positive OR of this queried bit fails always.

At k=1 this already gives a degree-one example. Taking k logarithmic in m gives inverse-polynomial uniform error but failure one, without appealing to a high-degree arbitrary truth table. This is a family of counterexamples to the smoothing inference, not a statement about the actual source PCP's query ranks.

Affine sigma_s and q preserve the degree of a polynomial under substitution. For XOR translations the new coordinates have degree one, although y=q(z) XOR s is generally 2-local rather than the source's 1-local interface. Degree preservation therefore does not repair the distribution mismatch. Full translations add m proof-address bits and m randomness bits; an asymptotic counting argument must also charge the larger space. Even polynomially many tagged copies do not improve the invariant constants.

## Removing the label is not a free repair

Take X={0,1}, with the two equally weighted repeated-literal tests NOT v_0 and v_1. The proof pi(0)=0, pi(1)=1 satisfies both. Shift their addresses by a uniform s in {0,1} but keep only the address, not s, and leave signs unchanged. The resulting four tests include both signs at both addresses. Every global proof now has acceptance exactly 1/2. The original yes-instance has lost perfect completeness.

This refutes THIS untagged shift construction, not all possible encodings or consistency gadgets. A different transformation must supply its own global-proof semantics, completeness, soundness, degree and cost bounds.

## Source-style seed shifts are a different operation

For any deterministic query q and uniform seed Z, q(Z XOR s) has exactly the same distribution as q(Z), for each fixed s. The substitution is a bijection of the seed cube. Averaging over a list of such shifts also leaves each original query marginal unchanged. For a direct repetition of an already fixed clause family, uniformly choosing one copied clause gives the same mean clause failure; checking the conjunction of all repetitions is a different acceptance event. This does not refute soundness amplification by conjunction. Nor does it analyze new auxiliary clauses introduced by a later circuit encoding.

## Finite scope

verify_smoothing.py checks the constants independently by complete cut/error-set enumeration on small examples; it does not implement a whole PCP. It also checks global-proof soundness by exhausting all submitted bit tables in its small soundness cases, constructs the explicit GF2 counterpolynomial, and separately checks exact affine fibers and input hardwiring. Exact counts, hashes and remote execution are recorded in execution-evidence.md. Different algorithms in the same author's checker are not independent review.
