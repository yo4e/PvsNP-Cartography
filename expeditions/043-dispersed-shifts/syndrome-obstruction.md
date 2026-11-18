# A quantitative obstruction from a binary linear map

Fix the constant rate exponent $a\ge3$, external seed space $\mathbb F_2^k$, $N=2^k$ and strict RS degree bound $D=N/2^a$. A fixed mask set $H$ includes zero. Its bundled tests all read the same canonical physical proof. Let $K$ be the exact base overlap set from Expedition 042, so two augmented views can intersect precisely at differences in $K+H+H$. The single base call already reads its own external root cell. [Physical address derivation](../042-accepted-sites/exact-overlap.md)

Let $B\colon\mathbb F_2^k\to\mathbb F_2^m$ have rank $m$. Assume
$$
\max_{d\in K+H+H}|Bd|\le w,
$$
where the absolute value is binary Hamming weight and $w$ is a nonnegative integer. This criterion uses the actual displacement set. One convenient sufficient estimate is $w=\ell+2b$, where $\ell=\max_{e\in K}|Be|$ and $b=\max_{h\in H}|Bh|$. If every column of $B$ has weight at most $c$, the sharper bound $|e|\le3a$ on $K$ gives $\ell\le3ac$.

The $3a$ displacement bound follows directly from the shape formula. A single leaf retains at most $2a$ original bits. In an internal-node pair the row branch followed by rows reaches its last internal node at dimension $2a+1$ and retains at most its $a$ low original bits. The column branch retains at most $2a$. Their disjoint-block sum therefore has weight at most $3a$.

## The interpolating assignment

Take $n$ to be the largest odd integer at most $\lfloor m/a\rfloor$, assuming $n\ge1$. Divide $an$ output coordinates of $B$ into $a$ disjoint groups of size $n$. Their bits are independent and fair at a uniform seed because $B$ is surjective. In each group take the majority. The resulting $a$ bits partition the root field into $2^a$ regions, each with exactly $D$ sites. Call a seed interior if every group weight differs from $n/2$ by more than $w$.

If the view of an interior seed $z$ intersects the view at $y$, their output bit strings differ in at most $w$ positions. They therefore belong to the same majority region. For any prescribed root word $f$, interpolate its $D$ symbols on each region by a degree-$<D$ polynomial over the external field. Put the honest physical proof of that polynomial on all cells read by interior centers of the region. Views of interior centers in different regions are disjoint. Overlaps within one region receive the same honest value.

Assign the prescribed $f$ at every external root site, including boundary sites. If an interior view reads root$(y)$, it meets the view at $y$ since that view reads its own root. Thus $y$ is in the center's region and the prescribed value agrees with the interpolant already assigned there. Set remaining auxiliary symbols arbitrarily. Every interior center sees one complete honest proof and accepts. All parent and sibling aliases retain one value per canonical address.

Writing
$$
\beta_n(w)=2^{-n}\sum_{j:\,|j-n/2|\le w}\binom nj,
$$
the rejection probability of this assignment is at most
$$
1-(1-\beta_n(w))^a\le a\beta_n(w)\le2aw\,2^{-n}\binom n{\lfloor n/2\rfloor}.
$$
The exact expression includes empty interiors when $2w\ge n$. At fixed $a$, the upper bound tends to zero whenever $w=o(\sqrt m)$. The central mass is $O(n^{-1/2})$ by the elementary product estimate in Expedition 042. This is a written all-parameter construction; bounded integer counts check its probabilities separately. [Earlier binomial argument](../042-accepted-sites/low-rank.md)

For the prescribed word $f(x)=x^D$, the exact relative distance from degree-$<D$ is $1-2^{-a}$. A difference polynomial has at most $D$ roots, and interpolation attains agreement at any $D$ selected sites. The same construction for the designed four-selector NO fixture, with $A=0$, $B(x)=1/x$ for $x\ne0$ and $B(0)=0$, makes the once-evaluated residual vanish except at zero. Its joint rejection is at most the displayed bound plus $1/N$. These are symbol-level probabilities.

## Masks close to a subspace

Suppose every $h\in H$ is within Hamming distance $b$ of one fixed subspace $U$ of dimension at most $r$. Partition original seed coordinates into $m=\lfloor k/(r+1)\rfloor$ disjoint blocks of size $r+1$. In each block choose a nonzero parity annihilating $U$. The resulting disjoint checks are independent, their matrix has column weight at most one, and each mask changes at most $b$ output bits. The criterion applies with $w=3a+2b$. Thus every prescribed root has a shared proof of rejection
$$
O_a\left((a+b)\sqrt{\frac{r+1}{k}}\right).
$$
For a claimed fixed positive soundness gap on every far root, it is necessary that no sequence of such approximating subspaces have $(a+b)^2(r+1)=o(k)$. Equivalently one may minimize the covering radius over every dimension-$r$ subspace. This gives a necessary condition, without a converse. An affine offset can be included by adjoining its direction to $U$, increasing dimension by at most one.

## Attacks and scope

Full row rank of $B$ is needed for the equal region sizes. A dense inverse of the mask matrix alone supplies no bound on $BK$. The Hamming weight bound concerns the actual mask list and geometry, without closing the list under arbitrary linear combinations. The bound uses existence of an exponentially large prover assignment; the number of translated tests and the verifier's polynomial cost are unchanged. Interpolating only interior sites would not justify restoring arbitrary boundary root symbols, which is why each region contains and fits all of its $D$ sites.

The construction has no novelty or Lean claim. It identifies an obstruction to constant soundness and to exact agreement for this recursive model. Relativization, Natural Proofs and algebrization remain constraints on a future complexity separation, and none is escaped by this finite-field interpolation argument.
