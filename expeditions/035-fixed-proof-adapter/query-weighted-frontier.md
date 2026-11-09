# Query-weighted error: a precise next question, not free average-case transfer

2026-11-09 JST. Research lead: 月野テンプレクス. Status: author-written elementary argument and explicit counterfamily, with finite corroboration. Not independently reviewed, not Lean-checked, and not a novelty claim. This extends Expedition034's query-concentration control into a rank-sensitive family; it does not refute the original pointwise PCP argument.

## 1. What the one-true-literal proof actually needs

Let X be a finite nonempty address set, N=|X|, with a fixed proof pi. Let t range over a finite test distribution nu, with nu>=0 and sum nu=1. Every signed OR test is satisfied by pi. Fix a true occurrence j(t) in each test BEFORE sampling the approximating polynomial. The choice can depend on pi and t, but not on the sampled polynomial or its errors.

Write a(t) for that occurrence's queried address and let

    rho(x) = sum_{t: a(t)=x} nu(t).

Then rho is nonnegative and normalized, even if addresses repeat or some tests have zero mass. For a fixed finite nonnegative normalized polynomial distribution mu, define err(x)=Pr_mu[P(x)!=pi(x)]. An OR test can fail only when the selected true literal is predicted incorrectly. Finite summation therefore gives

    E_mu[clause failure] <= sum_x rho(x)*err(x).

If rho(x)<=kappa/N for every x, then err(x)>=0 yields

    E_mu[clause failure] <= kappa * (sum_x err(x)/N).

The same weighted-average argument used by FixedProofTransfer selects one positive-mass polynomial with test acceptance at least one minus this bound. This is a written argument for arbitrary real weights, not an extrapolation from rational examples. The existing Lean module currently proves the pointwise-epsilon version, NOT this density refinement.

The useful comparison is kappa*average_error versus the verifier's actual soundness gap. A large kappa can erase all apparent savings. Choosing a balanced selector is a separate mathematical/existence problem. Nothing here supplies an efficient algorithm for finding it from a succinct verifier or for finding the approximating distribution.

## 2. Allowed coordinate projections can concentrate perfectly on a small error set

For integers 1<=k<=n, take pi(x)=1 on the n-bit cube and the actual GF2 polynomial

    p(x) = 1 + product_{j<k}(1+x_j).

Expanding over GF2 cancels the constant term and leaves precisely all nonempty subsets of the first k variables. Thus its ordinary multilinear degree is exactly k. Its error set is the codimension-k subcube x_0=...=x_(k-1)=0, and its uniform error is exactly2^-k.

Use the allowed coordinate projection

    q(z)=(0,...,0,z_k,...,z_(n-1)).

It has image rank n-k and exactly2^k preimages for each image point. Use the repeated-address positive clause p(q(z)) OR p(q(z)) OR p(q(z)). The original proof pi satisfies every test, but p fails every one. All three possible true-literal choices query the same address, so no selector can avoid the concentration.

For uniform z, rho is uniform on this image subcube, with density ratio kappa=2^k relative to the full address cube. Hence the loss bound is tight here:

    kappa * average_error = 2^k * 2^-k = 1 = clause failure.

For n>=2, choosing k=ceil(log2 n) gives degree O(log n), O(n) monomials, and uniform error at most1/n, yet test failure1. This is a general explicit construction; the finite code only corroborates small parameters. It does not construct a full PCP, claim that the published PCP must have these queries, or show an impossibility of useful smooth-query variants. It kills only the unconditional replacement of pointwise approximation by uniform-average agreement for the presently allowed query interface.

## 3. What would change the research decision

The next bounded problem is to characterize how much query congestion can be avoided by selecting among the true occurrences of a satisfied clause family, and then inspect whether the ACTUAL source construction has the needed property. Constant/literal query locality by itself is insufficient, as the family above shows.

A useful route is to formulate selection as a finite weighted allocation to allowed true addresses, distinguish fractional and deterministic selectors, and derive a necessary-and-sufficient cut or capacity criterion. Before using such a criterion in a complexity argument, charge access to the succinct query description, dependence on the unknown proof, and preservation of completeness, global-proof soundness and polynomial degree. An existential selector in an averaging proof is not automatically a uniform sampler.

A natural next milestone is a proved weighted transfer/capacity characterization or a concrete obstruction in the actual PCP query family—not a claim that a new lower bound already follows. Keep the original E^NP/infinitely-often scope, external hierarchy assumptions and runtime gaps separate.

## 4. Reproducible bounded evidence

query_pressure.py checks all45 pairs1<=k<=n<=9, verifies the actual GF2 expansion and exact degree, counts every projection fiber and the source/query errors, and checks16 weighted pushforward inequalities for all four targets and four candidate rows on two addresses. Its full stdout is query-pressure.json. Normal/-O outputs and py_compile agree locally. These are same-author controls, not an independent semantic review or a universal formal proof.
