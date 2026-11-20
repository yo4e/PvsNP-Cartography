# Weighted consistency recovers field rejection and pays for it in sensitivity

This analysis fixes the physical decision row $f$ of the shared-buffer compiler from Expedition 043. Put $E=\{z:f(z)=0\}$, $e=|E|$, and take a set $H$ of $t\ge1$ distinct XOR masks containing zero. The auxiliary row $b$ is compared with $f$ by its two copy-equivalence clauses. Each center has its own binary AND tree for the $t$ values $b(x+h)$ and its own output-true unit. Every private gate row is distinct across centers. The YES reference has $f=b=1$ and every private AND gate equal to one. Errors in the sensitivity calculation may flip any physical input, buffer or private gate cell. [Original interface and precision](../043-dispersed-shifts/compiled-cost.md)

Give both clauses of each copy the weight $\alpha\ge0$, and give every private gate and output clause weight $\beta\ge0$. Weights are rational if literal duplication is wanted. Multiplying all weights by a common denominator implements their integer multiples without adding proof variables. Clause-selection costs still belong in an implementation, while the address cube $Q$ is unchanged by duplicating existing clauses alone.

## Exact auxiliary optimum and exact signed sensitivity

If $Z=\{z:b(z)=0\}$, the copy cost is $\alpha|E\triangle Z|$. At a center touching $Z$, correct evaluation violates one output unit, and every alternative gate assignment must violate at least one equivalence clause or the output unit. All those clauses have weight $\beta$. Other centers admit zero cost. Therefore
$$
V(E)=\min_Z\{\alpha|E\triangle Z|+\beta|Z+H|\}
     =\min_{Z\subseteq E}\{\alpha(e-|Z|)+\beta|Z+H|\}.
$$
The restriction follows by removing points of $Z\setminus E$, which never increases either term. It remains valid when some weights vanish.

At the all-one YES reference, assign the true literal of each AND input-implication clause to that input and its positive-output clause to its output. Charge the two copy clauses respectively to $f$ and $b$, and each output unit to its output. Every physical input has load $\alpha$, each shared buffer $\alpha+t\beta$, and each private AND gate $2\beta$. A violated clause needs an error at its charged literal, including for mixed error sets. For $t\ge2$ the buffer load dominates the other two. A single buffer flip attains it. At $t=1$ there are no AND gates and the direct output unit gives the same expression. Thus, for $(\alpha,\beta)\ne(0,0)$,
$$
\sigma=\alpha+t\beta.
$$
If either weight is zero, $V=0$. If both are zero the encoding has no positive soundness budget and no positive precision threshold is assigned to the undefined ratio $0/0$.

## The exact price of recovering the expanded numerator

If $e=0$, then $V=0$. In the following ratios assume $e>0$ and let $s=|E+H|$. Because $0\in H$, $e\le s\le te$. The assignments $Z=\varnothing$ and $Z=E$ give $V\le\min(\alpha e,\beta s)$. Hence
$$
\sup_{\alpha,\beta\ge0}\frac{V}{\sigma}
\ \le\ \frac{es}{s+te}\ \le\ \frac e2.
$$
For $e>0$ the first envelope is optimized at $\alpha/\beta=s/e$. It need not equal the actual optimum because a proper nonempty subset $Z$ can be cheaper. For $E=\{0,1,2\}$ and $H=\{0,1\}$ on four seeds,
$$
V=\min(3\alpha,\alpha+2\beta,4\beta),\qquad
\sup V/(\alpha+2\beta)=1.
$$
The endpoint envelope is $6/5$, and the optimal unshifted symmetric-copy value is $3/2$.

The repair $\alpha=t\beta$ exactly restores $V=\beta s$ for every $E$. Indeed
$$
|E+H|\le |Z+H|+t|E\setminus Z|
$$
for $Z\subseteq E$, so every candidate costs at least $\beta s$ and $Z=E$ attains it. All $\alpha\ge t\beta$ also work. A singleton $E$ shows that $t\beta$ is universally necessary. At the cheapest universal repair,
$$
\frac{V}{Q_t\sigma}=\frac{s}{2tQ_t}\le\frac{e}{2Q_t}.
$$
The unshifted symmetric encoding has $V=e\min(\alpha,\beta)$ and $\sigma=\alpha+\beta$, with optimum $e/(2Q_1)$. Whenever $Q_t\ge Q_1$, no symmetric weighting of this translated shared-buffer compiler improves that optimum. This comparison is conditional on the same fixed decision row, with the stated all-one YES reference. Taking the same old NO minimizer gives the corresponding family upper bound when those references and address conventions are shared.

## Nonuniform weights and a minimum cut

Allow a common copy-pair weight $a_z$ at each physical seed and a common private-clause weight $b_x$ at each center. The exact formula becomes
$$
V(E)=\min_{Z\subseteq E}\left(\sum_{z\in E\setminus Z}a_z+
                  \sum_{x\in Z+H}b_x\right).
$$
It is the minimum cut of a bipartite network. A source has an arc of capacity $a_z$ to each $z\in E$. Each such vertex has an infinite-capacity arc to every center $z+h$. Every center has capacity $b_x$ to the sink. A finite cut that keeps $Z$ on the source side must keep its neighborhood there too. The cut cost is the displayed objective, and every subset produces that cut. For computation, any capacity larger than the sum of all finite capacities suffices in place of infinity.

The one-buffer error at $z$ has weight
$$
L_z=a_z+\sum_{h\in H}b_{z+h}.
$$
For $t\ge2$ the exact sensitivity is $\max(\max_zL_z,2\max_xb_x)$. At $t=1$ it is $\max_zL_z$. The same true-literal loads prove the upper bound and single buffer or private output-gate errors attain it.

In fact the no-gain inequality allows arbitrary separate nonnegative weights on all private AND and output clauses. Let $d_z$ be the total weight of the input-implication clauses that consume $b(z)$, including a direct output unit when $t=1$. A single buffer flip gives $\sigma\ge a_z+d_z$. With the fixed NO row, storing all buffers and gates as one costs $A=\sum_{E}a_z$. Storing $b=f$ but all private gates as one costs $D=\sum_Ed_z$. Only the input-implication clauses fail in that second assignment, even when several buffers are zero. Thus
$$
V\le\min(A,D)\le(A+D)/2\le e\sigma/2.
$$
This includes arbitrary multiplicities of private clauses. Nonuniform seed weights are granted as a relaxation here. A proposed implementation would still need to generate its actual weighted query distribution.

## A boundary that changes the baseline

The symmetry of the two copy-clause weights is substantive. Let the clause $\neg b\vee f$ have weight $u$ and $\neg f\vee b$ weight $v$. Only $u$ penalizes the false-acceptance assignment on $E$. For uniform private weight $\beta$,
$$
V=\min_{Z\subseteq E}\{u(e-|Z|)+\beta|Z+H|\},
\qquad
\sigma=\max(u,v+t\beta,2\beta)
$$
when $t\ge2$, with the $2\beta$ term omitted at $t=1$. Taking $v=0,u=t\beta$ gives $V=\beta s$ and $V/\sigma=s/t$, reaching $e$ for disjoint translated copies of $E$. Positive weights can approach that value. For example, on four seeds with singleton $E$ and all four masks, $(u,v,\beta)=(5,1,1)$ gives $V/\sigma=4/5$, exceeding the symmetric upper bound $1/2$.

The unshifted asymmetric family also has supremum $e$, so this observation gives no translation gain over its own optimized baseline. More generally, retain the all-one YES auxiliary assignment and flip only the $e$ physical $f$ cells of the NO row. By the definition of $\sigma$, that assignment costs at most $e\sigma$. It bounds $V/\sigma\le e$ for any compiler using this unchanged physical decision-row interface. This argument cannot be transferred to unrelated YES and NO physical field proofs whose Hamming distance has not been identified.

## Public pins and a computed base predicate

The exact min-cut formulas assume that the physical decision row is fixed and that the private aggregation has no additional untrusted public inputs. If $f$ is computed, retaining its correct base gates and truthful pins still realizes the two upper-bound cheating assignments. Extra base or pin errors can increase YES sensitivity and can create cheaper NO assignments. They cannot invalidate this upper obstruction, but equality for $V$ or $\sigma$ then needs the whole circuit. Direction-asymmetric weights, private copies, or a changed proof layout must be compared with the baseline that uses those same options.

Clause normalization cancels from $V/(Q\sigma)$ because both numerator and signed-error cost use the same weighted failure units. This does not remove $Q$, pin multiplicities, output uses or shared-cell sensitivity. The current result is a written finite derivation with exact Boolean and min-cut checks. No Lean, novelty or unrestricted complexity claim is attached.
