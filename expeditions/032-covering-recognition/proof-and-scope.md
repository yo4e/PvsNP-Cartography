# Pointwise approximation to a finite Hamming cover

Research lead: 月野テンプレクス. Freshly approved 2026-11-02 JST session.
Mathematical source16de2eb187960c770e63114b3dadbb1690f08b3f passed completed formal run41396234158/job125118052432. This document is an author statement/dependency audit, not independent semantic review. See ci-evidence.md for the separately attributed execution evidence.

## Exact endpoint

Let N=2^n, M=sum(j=0..min(n,d), choose(n,j)), and V(N,R)=sum(j=0..R, choose(N,j)). Let L(n,d) consist of all GF2-valued Boolean targets satisfying the unchanged HasProbabilisticDegreeAtMost at error1/3 and actual MvPolynomial totalDegree<=d. Then

 |L(n,d)| <= 2^M V(N,floor(N/3)).

PointwiseCover.feasible_count proves this for ALL natural n,d, including n0,d0 and d>n. Its final signature has no hypothesis assuming covering, a rank bound, a successful approximation family, or the desired count. Feasibility is used only to define the set being counted. Finite REAL distributions remain arbitrary, nonnegative, normalized and fixed before every input. No restriction to rational weights, sampled coefficient rows, affine polynomials or symmetric targets occurs.

## Positive-support averaging

positive_support_le proves a general finite real-weight lemma. Normalization and nonnegativity first imply a positive-mass index. If all such rows exceeded a threshold, their weighted sum would strictly exceed it; zero-mass rows contribute zero. The empty index type cannot satisfy normalization. The lemma neither assumes every weight is positive nor selects a zero-weight witness.

mean_error obtains the failure complement from each original pointwise success inequality and interchanges two finite sums. positive_support_third then finds a positive-mass polynomial whose integer disagreement count is at most floor(N/3). feasible_has_close_row unpacks the original predicate, retaining its actual polynomial degree bound. This is a ONE-WAY implication. It does not turn average-case approximation into pointwise feasibility; graveyard055/056 preserve the false converse.

## Counting genuine evaluation rows without changing the degree predicate

fieldCube is the full finite cube over ZMod2. codebook is the image on BooleanCube of the entire finite vector space spanned by squarefree monomials of support size<=d. The previously accepted AgreementDimension.eval_mem_low, specialized to0 and1, proves that every actual degree<=d polynomial evaluation belongs to this span. Its derivation reduces each variable power on the two-point grid and does not increase support degree. No truth-table degree replaces totalDegree in the original definition.

lowSpace_finrank bounds the dimension of that span by the number of generating supports over an abstract Field. Specializing after elaboration avoids the failed concrete-field typeclass reduction. Module.card_eq_pow_finrank and the accepted supports_card give codebook.card<=2^M. An upper bound suffices: this module does not claim a separately implemented normalizer, an explicit coefficient normal form, or an independent codebook bijection theorem.

## Hamming balls and the union

For a fixed binary row, its error set determines the other binary row. errors_injective proves that statement by kernel-reduced finite facts over ZMod2, not native_decide. The binary restriction matters: outputs1 and2 over a larger alphabet can have the same error positions against0.

smallSets_card partitions finite subsets by their size and counts each fiber with powersetCard. ball_card_le injects a Hamming ball into those subsets. covered_card applies the finite union cardinality inequality. feasible_subset_covered is then the original-predicate-to-covering bridge, and feasible_count follows.

far_not_feasible is a sound sufficient test, not a characterization. large_of_bound proves more-than-half density conditional on the explicit arithmetic inequality2^M V<2^(N-1). The unconditional n>=7,d<=1 estimate is a separate WRITTEN proof in recognition-and-scope.md; it is not silently included in the Lean endpoint.

## Adversarial and trust boundaries

The author inspected the definitions, derivations, final explicit signatures and axiom dependencies. All16 new reported theorems use only the unchanged [propext, Classical.choice, Quot.sound]. The new module contains no sorry, admit, new axiom, native_decide or warning waiver. All previous reports passed again. Repeated execution with the same kernel is not a second kernel or independent semantics.

The finite program tests actual powers versus squarefree evaluation, exact integer error counts, restricted denominator-three mixtures, direct affine enumeration versus a Walsh transform, residue recurrences and explicit easy-circuit counterexamples. These corroborate particular definitions and attacks; they do not prove the universal statement or classify arbitrary-real feasible targets.

Two implementation candidates failed before the accepted source; graveyard057 preserves both. New written counterfamilies and all-n largeness/recognition arguments have their own evidence class and are not Lean-accepted by association. This is a reconstruction of standard averaging, finite-dimensional counting and Hamming covering. No mathematical priority or unrestricted circuit lower bound is claimed.
