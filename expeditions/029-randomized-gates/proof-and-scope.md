# Actual gates, shared randomness, and the remaining circuit bridge

Author: 月野テンプレクス. Approved2026-10-29 JST night. Known-method reconstruction; novelty unknown. Kernel acceptance is recorded separately in ci-evidence.md when an actual successful run has been retrieved. This derivation is not itself execution evidence or independent review.

## 1. The primary construction and our quantifiers

Primary source: Oded Goldreich, On teaching the approximation method for circuit lower bounds, ECCC TR23-034 revision1 (25 March2023), Section2.2.1, Claim2.1 and Lemma2:
https://eccc.weizmann.ac.il/report/2023/034/revision/1/download/

The actual parsed PDF text was retrieved and inspected. Screenshot requests for the relevant pages timed out; no visual PDF inspection or local PDF archive is claimed. Claim2.1 supplies uniformity of a random linear form at a fixed nonzero field vector. The discussion leading to equation(3) retains random approximation at each fixed input; equation(4) then averages to one polynomial. We retain the earlier randomized object to match the repository's ORIGINAL pointwise predicate, rather than importing the averaged conclusion as if it had stronger quantifiers. The detailed lemma states a multiplicative-in-depth degree bound. The paper's MODq convention outputs1 for a nonzero residue, whereas SmallSupportMod3.target outputs1 for residue zero; complementing is necessary in comparisons. No external approximation theorem is an axiom of our Lean development.

## 2. Genuine GF2 gate polynomials

For k,r natural, let Mask(k)=GF2^k and Matrix(k,r)=Mask(k)^r. Every mask has real weight1/|Mask(k)|, and matrix weight is the product of its row weights. This is one finite normalized nonnegative distribution BEFORE any input is chosen. Mask(0) has one member, not zero members. Sampling zero rows is also a singleton distribution.

For arbitrary actual source polynomials P_0,...,P_(k-1), define

 L_a(P)=sum_j a_j P_j,
 Q_A(P)=1+product_(t<r)(1+L_(A_t)(P)).

All arithmetic here is in GF2; plus equals minus, but no Boolean multilinear reduction is performed. If every P_j has totalDegree<=D, each L_a has degree<=D, each complemented factor has degree<=D, and the product has degree<=rD. Adding1 does not increase this bound. This proves an ACTUAL polynomial substitution bound, including repeated source polynomials and powers of variables. Evaluation commutes with sums, products and constants, connecting Q_A(P)(x) to the direct linear-hash evaluator at z_j=P_j(x).

The target OR(z) is0 iff z is the zero vector. If z=0, every row vanishes and Q_A(z)=0, including r0. Otherwise pick a coordinate j with z_j=1. Translation a->a+e_j is a bijection on ALL masks and changes L_a(z) by1. Therefore its zero and one weighted fibers each have mass1/2. Splitting a row tuple into head and tail proves that all r hashes vanish with mass(1/2)^r. Since Q_A(z)=0 exactly when all rows vanish, the exact error is0 on zero input and2^-r otherwise. Reindexing matrices by Fin(card Matrix) supplies HasProbabilisticDegreeAtMost at epsilon2^-r and degree r with its original ordering of quantifiers.

AND_A(P)=1+Q_A(1+P) has the same actual-degree bound. Its target is1 iff all input bits are1; complement cancellation gives error0 on all-one input and2^-r otherwise. NOT, XOR and constants have exact polynomial evaluations; NOT/XOR do not increase the maximum input degree, and constants have degree0.

## 3. Why one shared matrix is sufficient

For deterministic vectors z_i, i<S, define E_i(A) to be the OR gate's local error on z_i. Pointwise, the indicator of their union is at most the sum of the indicators. Multiply by nonnegative matrix weights, sum over A, interchange the finite sums, and use the exact gate law. The result is

 Pr_A[exists i<S, E_i(A)] <= S*2^-r.

No inter-gate independence is used or asserted. All nodes may reuse one r-by-K matrix. OR nodes with smaller arity pad their arguments with0; AND nodes pad with1 before complementing. Thus every gate can use the same finite sample space. Matrix coordinates correspond to argument POSITIONS, not source-wire identities. The four false strengthenings in graveyard049 explain why this detail and the deterministic-input restriction are essential.

## 4. Full DAG continuation: derivation, NOT yet a Lean endpoint

Specify a finite topological list of gates referencing original inputs, constants or earlier gate IDs. Allowed gates: NOT, finite XOR, finite OR and finite AND; repeated references and sharing are allowed. Choose an output wire. Let S count OR/AND nodes once each, and h count the maximum number of OR/AND nodes on a dependency path to the output. Empty fan-in uses the conventional OR0=0, AND0=1, XOR0=0. Each node's depth is the maximum child depth (empty maximum0), plus1 exactly at OR/AND.

Sample one independent-row matrix A before x. Recursively construct ACTUAL polynomials in a table, reusing references rather than expanding the DAG into a formula. Input variables have degree1, constants degree0; XOR/NOT preserve maximum degree, OR/AND multiply it by at most r. For r>=1, induction gives degree<=r^(node depth), in particular<=r^h at the output. The monotonicity of r^depth for r>=1 is needed for shallower children and skip wires; graveyard049 refutes the r0 version.

Fix original x. Compute all TRUE deterministic original wire values. At each OR/AND node define its local bad event using those true inputs, with complements for AND. If none of these S events occurs, topological induction shows every approximated node equals its true value: at the first possibly wrong node all predecessor approximations are already correct, and the node's own true-input local event excludes its being wrong. Thus output error is contained in the union of S local events, yielding<=S2^-r under the SAME shared matrix. This proof does not feed sample-dependent corrupted vectors into the pointwise hash lemma.

Converting the resulting finite real distribution to the original predicate, and assuming3S<=2^r, should yield probabilistic degree<=r^h at error1/3. If the circuit computes the original residue-zero MOD3, the accepted growing-degree obstruction would imply n<(16*r^h+2)^2+2. The remaining formal obligations are the actual DAG datatype/evaluator, recursive polynomial table, actual depth induction, first-error inclusion, padding/family reindexing and the original-predicate/end-theorem composition. The gate theorem or finite checker must not be described as already completing these obligations.

## 5. Attack and barrier scope

Graveyard048 retains implementation failures;049 retains repeated-wire, inter-gate independence, adaptive-input and r0 counterexamples. check_dag.py separately implements sparse unreduced polynomials and direct Boolean evaluation, checks genuine degrees, all fixed-input errors and the true-input union implication on a bounded exhaustively specified class. Normal and -O output equality guards against disabled Python asserts. This is same-author replication, not independent semantic review and not a general proof.

This is a reconstruction of a known restricted-model polynomial method. It does not supply a property useful against general P/poly, a cryptographic counterexample, a nonrelativizing/nonalgebrizing escape, optimal constants, new unrestricted circuit lower bounds or P versus NP. Relativization and algebrization are not escaped merely because we use GF2 or a Lean proof. The method's dependence on degree growing exponentially with nonlinear path-depth is part of its quantitative scope, not an unrestricted-circuit solution. Existing n5..11 exact results, n>=7 affine exclusion, n>=299 quadratic exclusion and the growing-degree theorem remain unchanged. Independent review scopes #8/#15 are not silently extended.
