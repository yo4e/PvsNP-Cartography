# A shared proof that defeats exact accepted-site agreement

Fix rate exponent $a\ge3$, root field $F=\mathbb F_{2^k}$, $N=2^k$ and strict external degree cutoff $D=N/2^a$. Use the offset enumeration and canonical physical symbol addresses of Expedition 038. Fix any nonempty list of $t=t(k)$ public XOR translations in advance. At seed $z$, AND the complete RS tests for those translates on the same proof. For counting, append the single root cell at $z$ to the list of addresses, even if the program never reads it. Call the resulting set $V_z$; adding that cell changes no predicate. Define $q$ to be an upper bound on the number of slots in this augmented list, before deduplication.

## Why the overlap bound applies to physical symbols

For any fixed branch sequence, fresh words and leaf XOR offset, each original seed bit occurs once in the saved edge labels or live coordinate. A downward row step saves the high part and appends fresh bits to the low part. A downward column step saves the low part and fresh bits, retaining the high part as the live coordinate. A leaf offset flips fixed positions. On a row return only the fresh suffix (possibly flipped) determines whether the point belongs to the parent. A redirect removes that suffix and restores the high part from the saved label. A column-to-sibling redirect stores the live high tuple as the sibling row label and the saved low tuple plus fresh bits and a fixed marker as the sibling coordinate. In both cases the surviving physical path and its point jointly retain each original bit once, up to a known flip. The terminal shape and stop depth depend only on the fixed slot. Decoding the path and point recovers the original seed. Precomposing with a fixed XOR translation is invertible; the appended root-address map is also injective.

Thus one particular physical cell lies in the augmented lists of at most $q$ seeds, even when *different* slots can name that cell. This count already includes all parent/sibling aliases. It does not identify two distinct proof cells merely because their field abscissas happen to coincide. The construction assigns one value to each canonical address. The same fiber conclusion holds after any injective relabeling of the physical symbol storage. [Routing derivation](../038-recursive-query-fibers/attacks.md) · [Physical oracle](../038-recursive-query-fibers/source-compiler.md) · [BV14, §6](https://eccc.weizmann.ac.il/report/2014/017/download/)

One auditable budget counts raw occurrences for a single call recursively. Write $L(d)=2^d$ for $d\le2a$ and otherwise
$$
L(d)=2^a L(\lfloor d/2\rfloor+a)+2^{a-1}L(\lceil d/2\rceil).
$$
The branch multiplicities enumerate distinct fresh words on each edge. Repeating equivalent tapes only duplicates existing slots and may be removed for this count. Take $q=1+tL(k)$. The upper bound $2^{2a}(2^a+2^{a-1})^{1+\lfloor\log_2(k-2a)\rfloor}$ on $L(k)$ holds for $k>2a$. Thus a polynomial number of translations has polynomial query and predicate cost at fixed $a$. The attack does not alter a single query map. Public reconstruction of the predicate and leaf reordering use the original budget. [Previous cost bound](../041-two-level-distance/whole-row-limit.md)

## Construction and exact counting

Let $H(c)=\{z: V_z\cap V_c\ne\varnothing\}$. The overlap relation is symmetric, includes the center, and $|H(c)|\le q^2$. For any $m$ distinct centers $C$, replace the all-zero proof by the all-one proof precisely on $U=\bigcup_{c\in C}V_c$. Each of these two constant proofs passes every RS leaf at every seed. They are valid over the external field and the ambient extension. Each center therefore accepts on the patched single proof and reads an external one. Every seed outside $\bigcup_c H(c)$ accepts, with external symbol zero. No decision is needed on the other seeds. The centers and their neighborhoods may overlap arbitrarily.

For any external polynomial $P$ of degree $<D$, zero disagrees on the $m$ accepted ones; a nonzero $P$ disagrees on at least $N-mq^2-(D-1)$ accepted zeros by the root bound. Thus every polynomial misses at least
$$
\min\{m,\ N-mq^2-D+1\}
$$
actually accepting sites. Taking $m=\lfloor(N-D+1)/(q^2+1)\rfloor$ gives at least $m$ misses, also at least $m/N$ as a fraction of all seeds or of accepting seeds. In the one-center case $N-q^2\ge D$ suffices to rule out exact agreement. Consequently a verifier in this model purporting to have exact agreement on all accepted sites for every proof must have $q^2\ge N-D+1$. A polynomial query budget fails that prerequisite eventually at every fixed rate. Enough accepting zeros exist in the witness to exclude sparse interpolation.

For one center the root also agrees with zero except on at most $q$ positions, while at most $q^2-1$ seeds can reject. Near-code words suffice to refute the exact universal statement. This is neither a lower bound on the rejection count of this particular witness nor a violation of an average-distance soundness bound. Constant losses, and approximation bounds weaker than the displayed scale, remain possible. This argument uses the physical symbol tester; it does not transport the denominator to Boolean clauses. Novelty is unassessed, and no proof kernel has checked the argument.
