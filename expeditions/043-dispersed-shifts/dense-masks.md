# Dense full-rank masks with large pairwise distance still admit almost all seeds

Fix an even integer $r\ge4$, and let the seed dimension be $k=2^r-1$. Index the $k$ seed coordinates by nonzero vectors $x\in\mathbb F_2^r$. For every nonzero $y$ choose the fixed mask
$$
h_y(x)=x\mathbin{\cdot}y+\mathbf1_{x=y},
$$
and include the zero mask. There are $k+1$ tests. The rate exponent $a\ge3$ is fixed as $r$ grows. This family has full binary rank, dense individual masks, and pairwise distances near $k/2$, while the actual recursive verifier admits almost every seed for every prescribed external word.

## Rank and pairwise distances

Let $A$ be the $r\times k$ matrix whose columns are all nonzero $r$-bit vectors. The nonzero simplex words are the columns of $Q=A^\mathsf T A$, giving $q_y(x)=x\cdot y$. Every such column has weight $2^{r-1}$. The standard binary simplex code has dimension $r$ and length $2^r-1$. [Magma's code construction reference](https://magma.maths.usyd.edu.au/magma/handbook/text/1971)

For $r\ge3$, each diagonal entry of $AA^\mathsf T$ is the even integer $2^{r-1}$ reduced modulo two. Each off-diagonal entry is the even integer $2^{r-2}$ reduced modulo two. Hence $AA^\mathsf T=0$ and $Q^2=0$. The matrix with columns $h_y$ is $M=I+Q$, which satisfies $M^2=I$ in characteristic two. Its rank is exactly $k$. The perturbation from $q_y$ flips just coordinate $y$, giving mask weights $2^{r-1}-1$ or $2^{r-1}+1$. Distinct columns differ by
$$
h_y+h_z=q_{y+z}+e_y+e_z,
$$
so their distance lies between $2^{r-1}-2$ and $2^{r-1}+2$. The masks are fixed in the original physical coordinate basis; the construction rotates neither the field representation nor the recursive address maps.

## Many independent checks see only one flipped bit

On each successive pair of coordinates of an $r$-bit index define the linear map $T(a,b)=(b,a+b)$. Its square sends $(a,b)$ to $(a+b,a)$, so $T^2+T+I=0$ and $T^3=I$. Solving $T(a,b)=(a,b)$ forces both bits to be zero. Applied to all pairs, it has no nonzero fixed vector and partitions the nonzero indices into triples
$$
\{x,Tx,T^2x\},\qquad x+Tx+T^2x=0.
$$
These triples partition all $k$ seed coordinates. Let $B$ have one row per triple, taking the parity of its three positions. Its $m=k/3$ rows have disjoint supports, hence rank $m$, and its columns have weight one. Summing a simplex word over any triple gives zero. Thus $Bq_y=0$ and $Bh_y=Be_y$, which is exactly the one unit bit for the triple containing $y$.

The physical base overlap set satisfies $|e|\le3a$, so $|Be|\le3a$ for every $e\in K$. Each of the two mask contributions changes at most one check bit. The [binary-map criterion](syndrome-obstruction.md) applies with
$$
m=k/3,\qquad w=3a+2.
$$
For the largest odd $n\le\lfloor k/(3a)\rfloor$, every prescribed external root has one shared proof with rejection at most $1-(1-\beta_n(3a+2))^a$, which is $O_a(k^{-1/2})$. In particular the root $x^D$ remains at exact distance $1-2^{-a}$, and the reciprocal NO root has joint rejection bounded by the same quantity plus $2^{-k}$.

## Why this remains outside the small-bias repair

For the uniform distribution on the $k+1$ masks, a given triple parity is one on precisely three masks. Its bias is exactly $1-6/(k+1)$, approaching one. Density and pairwise Hamming distances leave these linear tests highly unbalanced. The small-bias condition controls all nonzero parities, which these masks fail explicitly. This comparison uses the definition of bias and the direct count above. [Naor and Naor, original paper](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/bias.pdf)

The obstruction also holds for every normalized nonnegative weighting on this same support. Every nonzero mask has syndrome weight one, and zero has weight zero. If $p_j$ is the probability that triple parity $j$ equals one, then $\sum_{j=1}^{m}p_j\le1$. Some $p_j\le1/m$, so that nonzero character has signed bias $1-2p_j\ge1-2/m$. Repeating masks or changing their probabilities therefore cannot turn this support into a distribution whose bias is bounded away from one as $k$ grows. The finite checker already verifies the one-unit syndrome of every nonzero mask, which is the counting invariant used here.

Generating the entire mask table needs polynomial work in $k$, for example $O(k^2\log k)$ bit operations by evaluating the dot products. Each precomposition only complements fixed seed bits of the existing query projections. The schedule has $(k+1)L(k)$ raw symbol occurrences and at most $k+1$ times the base predicate work, plus the conjunction. The proof establishes failure for this particular linear-size family, leaving dispersed polynomial schedules available.

## Checks and failed extrapolations

The accompanying checker constructs the actual binary masks, verifies full rank and $M^2=I$, enumerates pairwise distances, and checks every triple syndrome at $r=4,6,8$. It also computes the exact image of the prior physical overlap formula and compares its syndrome support to the stated bound. Large integer calculations evaluate the majority-region masses without materializing their field or proof table. Their outputs are guarantees on the specified interior sets. They do not enumerate every verifier verdict.

The claim that large pairwise distances plus full mask rank suffice for constant soundness is refuted by this family. The diagonal perturbation is essential for its rank claim; the simplex masks alone have rank $r$. The triple construction requires even $r$, while the rank calculation only requires $r\ge3$. Dropping the physical $BK$ estimate would invalidate the interpolation argument. The family and the criterion have written derivations and finite exact checks, with mathematical novelty and kernel verification unassessed.
