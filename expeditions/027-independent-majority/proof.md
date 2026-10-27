# Independent majority and the original MOD3 obstruction: derivation

Research lead 月野テンプレクス. Freshly approved session executed2026-10-28 JST.
Author reconstruction of a known-method consequence; novelty is unknown.
This derivation is not itself a claim of completed Lean acceptance. Consult the
actual completed execution record and source commit for that separate status.

## 1. Preserve the original contract

For arbitrary n,d and f:{0,1}^n->GF2, assume a FIXED finite family of actual
GF2 polynomials P_i, each of total degree<=d, and REAL mu_i>=0 summing to1.
For every input x, success is at least2/3. Coefficients and probability weights
are not elements of the same field. The source family precedes every input.

Index the new family by all tuples v:Fin15->I and give it mass
nu(v)=product_j mu(v_j). This is nonnegative, and repeated finite distributivity
gives sum_v nu(v)=(sum_i mu_i)^15=1. The source may have zero weights, duplicate
polynomials or irrational weights. No rational-ticket representation is needed.
The empty source cannot satisfy normalization; zero-length tuples remain valid.

## 2. Derive the law rather than assume independent errors

Fix x only after constructing the entire family. Let e_x(i) indicate failure,
and p=sum_i mu_i e_x(i), so0<=p<=1/3. Let T_p(r,k) be the mass of tuples with
at least k failures. Splitting the tuple into its head and tail yields exactly

 T_p(0,k)=[k=0], T_p(r,0)=1,
 T_p(r+1,k+1)=p*T_p(r,k)+(1-p)*T_p(r,k+1).

IndependentTrials.failure_law derives this recurrence from actual product
weights, with no independence or amplified-success premise. The identity even
holds algebraically for signed normalized weights; probability comparisons do not.

Induction gives0<=T<=1 and T_p(r,k+1)<=T_p(r,k). To compare0<=p<=q<=1,
first use the induction hypothesis in both recursive terms. The remaining
change from p to q is

 (q-p)*(T_q(r,k)-T_q(r,k+1)) >= 0.

Thus T_p(r,k)<=T_q(r,k). This elementary argument avoids a calculus dependency.
The familiar binomial expression sum_{j=k}^r choose(r,j)p^j(1-p)^(r-j)
satisfies the same recurrence and initial conditions by Pascal's identity.
The current Lean implementation proves the recurrence directly; it does not
claim a separate general binomial-form equality theorem. The finite checker
cross-checks tuple enumeration, recurrence and binomial formula independently.

## 3. Majority is an actual low-degree polynomial

Over GF2 define Q_v as the eighth elementary symmetric polynomial of the fifteen
P_(v_j): sum over8-element coordinate subsets of the product of their eight
polynomials. Every summand has total degree<=8d; therefore Q_v does as well.
This construction does not rely on multilinearizing source polynomials.

On Boolean evaluations, if w of the fifteen values are1, Q_v evaluates to
choose(w,8) modulo2. For0<=w<=15 this is precisely[w>=8], using the earlier
kernel-checked identity. For either target bit, a majority error occurs exactly
when at least8 of the15 source evaluations are wrong. Hence success+failure=1,
and the exact product law bounds failure by T_(1/3)(15,8).

To compute that one rational endpoint, define natural counts A(r,k) with
A(0,k)=[k=0], A(r,0)=3^r, and A(r+1,k+1)=A(r,k)+2*A(r,k+1).
Induction proves T_(1/3)(r,k)*3^r=A(r,k). Kernel reduction of the finite integer
count gives A(15,8)=1266027, hence delta*=422009/4782969.
This rational calculation does NOT restrict arbitrary source mu to rational values.
We obtain the ORIGINAL approximation predicate at error delta* and degree<=8d.

## 4. Apply the previously constructed MOD3-to-product bridge

For n299 and d2, amplification yields degree<=16 and error delta*. The accepted
Mod3ProductBound.necessary_inequality, with m297, requires

 (1-2delta*)*2^297 <= B(297,16),
 B(m,D)=sum_{j=0}^{min(m,floor((m+D)/2))}choose(m,j).

But B(297,16) is the exact prefix recorded in result.json and MajorityNumerics;
the difference of the left side minus that prefix is strictly positive, with
exact numerator173942218836028022567908624832604370947637296701413596332611277990970693974594993470985749600
and denominator4782969. Lean proves a linear-depth binomial evaluator equals
Nat.choose before reducing this finite sum. There is no imported numerical axiom,
Python-supplied proof, native_decide, rounded float or assumed gap.

## 5. Extend by actual restrictions, NOT numerical monotonicity

The direct gap already fails at n300; graveyard044 preserves that counterexample.
Instead, define the actual polynomial substitution X_0=0 and X_(j+1)=X_j.
Its degree cannot increase. Evaluation at x equals the original at(0,x), and
MOD3's target is unchanged. The SAME original weights retain normalization,
nonnegativity and every-input success. Inductively restrict any n>=299 family
to299. That contradicts step4, yielding the all-n endpoint.

## 6. Scope

The final target is exclusion of total degree<=2 for every n>=299 at error1/3,
not equality to3, a best possible threshold, or a result about unrestricted
circuits. The finite truth tables and small polynomial tests are corroboration,
not the general probability or restriction proofs. A known polynomial-method
reconstruction is not a P-vs-NP separation. Independent semantic review and a
second proof kernel must be tracked separately from the existing Lean execution.

Primary context: Goldreich, ECCC TR23-034 revision1 (2023), Section3.2, and the
source comparisons in Expeditions023-026. The author identifies this as an
exposition of known approximation-method lower bounds. This repository's exact
299 cutoff and explicit real-distribution adapters are not attributed as literal
statements in that paper. Current-session PDF screenshot attempts failed; parsed
text, not visual PDF inspection, is the available source evidence.
