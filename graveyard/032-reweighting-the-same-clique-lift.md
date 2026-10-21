# Refuted repair: change only probabilities within the same n12 clique family

After graveyard031, a natural repair is to change the probabilities or abandon
uniform permutations, but keep only zero, q_A with |A|=9 and r_B with |B|=8
on12 inputs. This repair also fails, for ANY nonnegative normalized REAL
mixture over these716 declared deterministic polynomials.

Exact input dual: mass5 on each of the924 weight-six inputs and126 on each of
the66 weight-ten inputs, total12936. Thus the layer probabilities are5/14 and9/14.
The zero polynomial and every q_A have score8316/12936=9/14. Every r_B has
score6748/12936=241/462. The common bound9/14 is below2/3 by1/42.
A convex mixture cannot exceed that same dual average; a pointwise guarantee
of2/3 would have average at least2/3. This is the finite weak-duality argument.

The standalone checker enumerates all220 nine-subsets and495 eight-subsets,
plus zero, and evaluates their actual unordered GF(2) monomials on all990
positive-mass inputs:708840 polynomial/input checks. It independently compares
the scores with binomial profile counts. Normal/-O checks match. Completed
remote CI must be read from the expedition record, not assumed from this file.

Evidence class: exact finite certificate plus explicit mathematical argument.
A dedicated Lean corollary connecting this716-element family to the generic
real duality lemma has NOT been compiled in this expedition. Do not relabel
this restricted certificate as a universal degree-two lower bound.

Scope: other subset sizes, other polynomial shapes, complements and all
remaining degree-two polynomials are NOT covered. No n12 degree determination,
minimum support, optimal dual, new asymptotic theorem or P-vs-NP result follows.
Salvage must change the candidate family, not merely these probabilities.
