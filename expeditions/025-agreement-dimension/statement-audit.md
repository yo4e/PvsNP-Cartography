# Statement audit, author acting as skeptic

This is a same-author adversarial audit, NOT an independent semantic review.
Formal acceptance and exact source/run provenance belong in ci-evidence.md.

The coefficient field K is arbitrary. The finite input grid is built with
Fintype.piFinset and then filtered by actual MvPolynomial evaluation. No Fintype
K is required; infinite fields are covered. Total degree is MvPolynomial.totalDegree,
not monomial count or a truth-table label. Probabilities in the consequence are
REAL, not elements of K. A finite index type and normalized nonnegative weights
are fixed before every input. There is no rational-ticket assumption.

lowSpace is DEFINED as a span of explicit squarefree evaluations. It is not
defined to be the whole function space. eval_mem_low constructs the required
reduction via explicit power interpolation and product expansion. The imported
compression has its actual degree and pointwise proof. Lagrange delta indicators
then reconstruct arbitrary functions on H. Only after these steps does the proof
derive lowSpace=top and use the finite spanning-set dimension inequality.
The binomial count is derived from the cardinality fibers of finite subsets.

The final deterministic endpoint has only field, endpoints, actual polynomial
and degree inputs. It does not assume surjectivity, any row agreement bound,
any cardinality inequality, or a lower bound equivalent to its conclusion.
The mixture endpoint derives every row bound from that actual theorem.
The gap in no_pointwise_mixture is the EXPLICIT numerical inequality
B(n,d)<eta*2^n, not an assumed claim about polynomial approximation.

Attacks: zero endpoints give7>4; after-input polynomial choice gives8>4;
nonnegative-normalization omission admits artificial success1; signed mass1
constants [1,2,0] with weights [1,1,-1] also give success1 against bound1/2.
Equal endpoints DO NOT falsify the cardinality conclusion: the actual grid
collapses to one point. That correction is recorded without silently editing
the previous dated proof. Uniform-grid normalization still needs a!=b.

The generic proof covers empty agreement sets, n=0, both parities of n+d and
d>=n. Finite controls additionally cover several characteristics, zero-inclusive
interpolation grids, non-multilinear monomials and explicit delta functions.
They are corroboration, not the source of the universal quantifiers.

No Python rank value, solver output, native_decide, sorry, admit, new axiom,
weakened warning policy or assumed desired rank theorem is intentionally used.
The build/axiom transcript, not this sentence, determines actual acceptance.
Old Gemini review #15 has no automatic coverage of these new modules.
The n299 conclusion still requires the missing amplification and GF4 transport.
