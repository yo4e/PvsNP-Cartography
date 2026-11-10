# True-literal capacity, deterministic loss, and the limit of the certificate

2026-11-10 JST. Research lead: 月野テンプレクス. Evidence class: **author-written finite mathematical derivations with exact finite corroboration**. No Lean verification or independent semantic review of this document is claimed. The capacity argument is a standard max-flow/weighted-Hall application, not a novelty claim.

## 1. Fixed proof and the quantity to optimize

Let X be a nonempty finite address set, N=|X|. Fix a binary global proof pi and a finite family of signed three-occurrence OR tests t. Let nu_t>=0 be REAL weights summing to1. Assume pi satisfies every test. Let A_t be the set of DISTINCT addresses of occurrences true under pi, and B_t the set of addresses of occurrences false under pi. Thus 1<=|A_t|<=3. Repeated equal occurrences are not additional addresses. A_t and B_t may intersect when opposite signs query the same address; that test is tautological.

A fractional allocation consists of REAL w_tx>=0, zero for x outside A_t, with sum_x w_tx=nu_t. Define rho_x=sum_t w_tx. It is a probability measure on addresses. Its congestion is kappa=N*max_x rho_x. The allocation depends on pi and the tests, but is fixed BEFORE sampling an approximating polynomial. It is not a new proof for each occurrence.

The optimization here minimizes congestion among these single-true-address certificates. It does not yet minimize the actual failure of signed clauses. Section5 attacks that distinction.

## 2. Exact capacity characterization, including arbitrary real weights

For U subset T put Gamma(U)=union_{t in U} A_t. For kappa>=0, a fractional allocation with rho_x<=kappa/N exists if and only if

    nu(U) <= (kappa/N)*|Gamma(U)|    for every U subset T.             (1)

Necessity: all mass from U must enter Gamma(U), whose total capacity is the right side.

For sufficiency construct a FINITE DIRECTED network. Source-to-test t has capacity nu_t; test t to address x in A_t has capacity2; address x to sink has capacity kappa/N. Total source capacity is1. Any cut crossing a middle edge has capacity at least2. Every other cut, with source-side tests U and addresses S, satisfies Gamma(U) subset S and has capacity

    1 - nu(U) + (kappa/N)*|S| >= 1

by (1). A maximum flow therefore has value1; it saturates every source edge, and its middle-edge values are the required w_tx.

For completeness, this invocation does not assume rational weights or termination of naive augmenting paths. The feasible flow set is a nonempty closed bounded subset of a finite-dimensional real space, hence the continuous flow value attains a maximum. If a positive-residual source-to-sink path remained at a maximizer, augment by the minimum of its finitely many positive residual capacities to improve the value. There is no such path. The residual-reachable source side then has all outgoing edges saturated and all incoming edges carrying zero flow; conservation identifies the cut capacity with the maximum flow value. The preceding cut lower bound proves value1. This proves the directed real-capacity instance needed here without extrapolating from integer experiments.

An equivalent condition, often better for finding concentration, is

    nu({t : A_t subset S}) <= (kappa/N)*|S|    for every S subset X.    (2)

To get (2) from (1), take U to be the tests entirely contained in S. Conversely, take S=Gamma(U); its forced-test mass is at least nu(U). Empty sets cause no division problem because every A_t is nonempty.

Consequently the attained optimum is

    kappa_frac = N * max_{nonempty S subset X}
                       nu({t : A_t subset S}) / |S|.                 (3)

In particular 1<=kappa_frac<=N. This is a GENERAL finite real-weight argument. The tested rational instances are only controls. The maximum ranges over address sets, not individual overloaded addresses alone; singleton tests are insufficient to characterize feasibility.

## 3. Weighted error transfer still chooses ONE global polynomial

Let mu be any fixed finite normalized nonnegative REAL distribution on binary global functions p (in particular genuine GF2 polynomials of a common degree bound). Set

    err(x)=Pr_mu[p(x)!=pi(x)],  delta=(sum_x err(x))/N.

For every x in A_t, failure of test t implies p(x)!=pi(x): that occurrence was true for pi, so predicting it correctly would already make the OR true. Multiply these inequalities by w_tx and sum over x. Since row mass is nu_t,

    nu_t*1[test t fails under p] <= sum_x w_tx*1[p(x)!=pi(x)].

Sum over tests, then average over the SAME p for all tests. Finite sum interchange and nonnegativity give

    E_mu[test failure] <= sum_x rho_x*err(x) <= kappa*delta.          (4)

A positive-mass member p of the original family therefore has failure at most kappa*delta. Otherwise every positive-mass member had strictly larger failure and their finite normalized average would too. Thus a single polynomial of the original degree attains acceptance at least1-kappa*delta. Zero-mass rows cannot be the selected witness.

Fractional w is only a proof certificate for this inequality. It does NOT independently re-sample p, its queried bits, or its sign at each test. The one-global-proof soundness premise is unchanged. For a verifier with soundness gap g, the useful regime requires kappa*delta<g; a large kappa can make the result vacuous. Nothing here constructs a satisfying pi or an approximating distribution.

## 4. Deterministic selectors have a sharp factor-three loss

A deterministic selector chooses one x(t) in A_t for each t and assigns all nu_t there. Let kappa_det be its best congestion. Trivially kappa_frac<=kappa_det.

From an optimal fractional allocation, choose an address with largest w_tx in each row. Since |A_t|<=3, the chosen share is at least nu_t/3. At each address, the total deterministic load is therefore at most three times its fractional load. This proves

    kappa_frac <= kappa_det <= 3*kappa_frac.                          (5)

The factor is sharp WITHIN THE THREE-QUERY INTERFACE. Take the four addresses of a two-bit cube, pi=1, and one positive clause querying three distinct addresses0,1,2 with weight1. Fractional loads1/3 at each give kappa_frac=4/3. Every deterministic choice has one load1 and kappa_det=4. All queries can be constant coordinate projections. No conjectured asymptotic instance is needed. Thus the fractional cut criterion cannot silently be used as a deterministic-selector criterion.

## 5. Attack: optimal congestion is not optimal signed-clause transfer

For a fixed binary p, let E={x:p(x)!=pi(x)}. A signed clause fails EXACTLY when

    A_t subset E  AND  B_t intersect E is empty.                       (6)

All previously true literals must flip to false, and all previously false literals must stay false. This also handles repeated addresses and tautologies: if A_t intersects B_t, the conjunction is impossible.

For the fixed tests/proof, the optimal nonnegative constant in a uniform-error bound over ALL binary p is therefore

    C_OR = N * max_{nonempty E subset X}
        nu({t:A_t subset E and B_t intersect E is empty}) / |E|.       (7)

There are only finitely many error sets, each realized by p=pi XOR 1_E, so this is both necessary and sufficient. The empty E has failure0 and is harmless. Averaging the deterministic inequality proves the same constant for finite mixtures. Formula (7) is a structural characterization, NOT an efficient method on succinct or exponentially large address spaces, and not a low-degree-restricted optimum.

Dropping the B_t condition proves C_OR<=kappa_frac. Equality holds when B_t is empty for every test, but can fail even WITHOUT tautological clauses.

Concrete countermodel: X={0,1,2,3}, pi=1, and three equiprobable clauses

    (v0 OR v1 OR not v2),
    (v1 OR v2 OR not v0),
    (v2 OR v0 OR not v1).

Their A_t are the three pairs of{0,1,2}. The full three-address set forces all mass, so (3) gives kappa_frac=4/3; one can also rotate deterministic selections to attain it. For actual failures, exactly two errors among0,1,2 cause exactly one failed clause; zero, one, or three such errors cause no failure. An additional error at unused address3 only increases the uniform error. Thus C_OR= (1/3)/(2/4)=2/3, strictly below4/3.

This example is compatible with low degree: on the two-bit address cube, p(y0,y1)=y1 disagrees with pi at addresses0 and1, has uniform error1/2, and fails1/3 of the clauses. It attains the ratio2/3. Therefore the failed inference is not rescued by requiring actual polynomials. The upper bound (4) survives; only its purported global optimality was false. See the preserved post-mortem in ../../graveyard/2026-11-10-capacity-optimality.md.

## 6. What this changes, and what it leaves open

We can now test the proposed average-error replacement against a precise obstruction: every set S must have forced true-query mass bounded by kappa*|S|/N. A balanced fractional allocation is enough for the single-global-sample averaging argument; insisting on deterministic selection loses up to a sharp factor3. However, the full signed structure can give a better error bound than any such certificate. The capacity optimum is not a complete account of actual failures.

The prior rank-deficient projection family still has kappa=2^k and delta=2^-k with failure1; no unrestricted average-case transfer is recovered. To use the new criterion, inspect the ACTUAL projection-PCP query construction or a justified variant and account for dependence of A_t on the satisfying proof. Enumerating its tests/addresses or error sets may cost exponentially much. An existential allocation is not a uniform sampler. Average error also does not automatically amplify pointwise by majority when errors concentrate at a few addresses.

The next substantive decision is whether the source construction has a provable, degree-compatible query-distribution/signed-error bound that preserves perfect completeness and global-proof soundness. If not, park this average-error route rather than accumulating generic flow infrastructure. Existing E^NP/infinitely-often scope and external hierarchy/runtime assumptions remain separate. No unrestricted lower bound or P-versus-NP conclusion follows.

## Sources and evidence classification

- L.R. Ford Jr. and D.R. Fulkerson, Maximal Flow Through a Network, Canadian Journal of Mathematics8(1956),399-404, DOI10.4153/CJM-1956-045-5. Retrieved primary scan https://www.cs.yale.edu/homes/lans/readings/routing/ford-max_flow-1956.pdf ; Theorem1 page400 visually inspected. It supplies standard flow context; the exact directed weighted characterization above is derived here, not quoted as their literal statement.
- Emanuele Viola, New lower bounds for probabilistic degree and AC0 with parity gates, ECCC TR20-015 revision5(2021-01-12), Section2.3, https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . The single-global-polynomial OR step was visually inspected at PDF page index14. That fixed-proof route is the context, not refuted by our altered-interface counterexamples.
- verify_capacity.py compares two cut enumerations with exact integer max-flow/cut certificates, exhausts tiny deterministic selectors, verifies signed failure semantics, and retains both explicit countermodels. Complete scope/counts and source digest are in checks.json. Normal/-O outputs agree locally. Remote execution is recorded separately only after it is observed.

These standard reductions and elementary countermodels are not announced as novel research results. All new general arguments here are author-written and unreviewed; no finite computation or unrelated Lean build promotes them to formal theorems.
