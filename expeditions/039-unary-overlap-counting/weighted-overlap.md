# Paying for inconsistent copies of a proof bit

**Evidence class.** Author derivation for the published signed-projection interface. The finite programs check image geometry and scores by different enumerations. Novelty unknown.

## Table and score

Fix one input to Viola's Lemma 11. There are M equally weighted clauses over a uniform k-bit seed z, each an OR of three signed reads of one global proof. Give each literal occurrence its own index j, including repeats; J=3M. Write its physical address as q_j(z). Its image A_j has 2^{r_j} points, where r_j counts distinct seed bits used. Unused seed bits have uniform fibers, so each address in A_j has slot mass w_j=2^{-r_j}. A_j can impose repeated-coordinate and complemented-coordinate equations as well as constants. It need not be an axis-parallel subcube.

Guess a Boolean function H_j on each A_j, represented as a polynomial on r_j native bits (the distinct used seed bits, in a fixed order). F(H) is the **sum** over clauses of their failure probabilities under one shared z per clause, with each literal evaluated by its corresponding H_j. Define

    D(H) = sum_{j<l} min(w_j,w_l)
                 · #{a in A_j ∩ A_l : H_j(a) differs from H_l(a)}.

Here H_j(a) means evaluation in the unique native coordinates of a. D is an unnormalized price, not a probability. No new proof bits are sampled during a test.

**NO bound.** At each reached address a choose an incident slot of greatest mass w_j, breaking ties by index. Use its answer as the global proof π*(a); fill unused addresses freely. If another slot differs at a, its entire incidence mass equals the smaller mass of its pair with the chosen slot. Those charges use distinct pair/address terms. Therefore the sum over all occurrences of the probability of a change on replacing local bits by π* is at most D. A clause newly failing after replacement has at least one changed occurrence, hence F(π*) ≤ F(H)+D(H). In particular, if every global proof has failure probability at least δ on a uniform clause and seed, every collection of guesses has score at least Mδ. The rounding is an existence argument. The simulator never computes a winning slot at every address.

**YES bound.** Relative to a satisfying proof π let e_j be the disagreement of H_j with π under uniform mass on A_j. Failure of an originally true clause costs at least one wrong literal, so F ≤ Σ e_j. At a disagreement, one of the endpoints is wrong relative to π. The minimum weight permits charging the error to that endpoint. Each slot has J−1 partners, so D ≤ (J−1)Σ e_j. Thus F+D ≤ JΣ e_j. The use of the absolute proof bit before its literal sign is essential.

## From one uniform approximation to these guesses

At the occupied input length encode (tag,z,dummy), with s=ceil(log₂ J) tag bits. The canonical Boolean target on tag j<J returns π(q_j(z)) for the lexicographically first complete proof. It ignores the dummy bits. Invalid tags return zero. For any degree-d approximant with full uniform error η, let η_j be the conditional error at tag j. Then Σ η_j ≤ 2^s η. For each j, fix both the dummy bits and the seed bits unused by q_j to one setting with error ≤η_j on the remaining r_j bits. Averaging ensures its existence; a preassigned all-zero section can have error one. Restriction yields a polynomial H_j of degree ≤d on A_j, so F+D ≤ J 2^s η. The simulator can guess such native polynomials without knowing π, its lexicographic ordering, or the good sections. NO soundness above allows arbitrary, mutually inconsistent guesses.

The sufficient precision is J 2^s η < Mδ. More concretely, Viola establishes Lemma 11 by splitting the 3CNF in Lemma 10. Before clause selection, every NO proof fails some clause with probability at least 1−n^{-10}. Consequently Mδ can be taken to be 1−n^{-10} for that family. For n≥2 use η ≤ 1/(4J 2^s) on YES and accept if F+D < 1/2. An arbitrary inverse-polynomial gap supplied without this construction can instead use a computable smaller inverse-polynomial threshold. Uniform constant error alone does not meet this estimate.

## Computing the score

An image is given by equalities a_p=b or a_p=a_q XOR b. Combine two lists of equations. In the graph of xor constraints, ground constants at one vertex. An odd-parity contradiction gives an empty intersection. Otherwise each ungrounded component supplies one free bit; its other vertices are copies or complements. This is a bijection on the physical intersection. Its b free bits satisfy b≤min(r_j,r_l)≤k. Recover each native coordinate by reading and, if necessary, complementing any representative physical bit. The XOR of the two restricted polynomials therefore has degree ≤d. Count the nonzeros on this b-cube, multiply by min(w_j,w_l), and sum. Singleton and empty intersections cost constant evaluations or zero. There is no 2k-bit independent collision search.

For each clause count its rejection polynomial of degree ≤3d on the original k-cube. A clause uses one shared seed, including when it queries the same cell more than once. In units of 2^{-k}, a pair term contributes an integer count shifted left by k−max(r_j,r_l); a clause contributes its integer number of rejecting seeds. Scores need O(k+log J) bits. These instructions also specify an exact rational threshold comparison.

[Viola, revision 5, Lemmas 10–11 and Theorem 12](https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/) · [Ben-Sasson and Viola, Theorem 1.1 and §3](https://eccc.weizmann.ac.il/report/2014/017/download/) · [Time and length ledger](budget.md) · [Counterexamples](../../graveyard/039-padding-and-collisions.md)
