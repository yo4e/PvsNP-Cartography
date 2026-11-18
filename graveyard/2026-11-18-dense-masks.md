# Refuted: dense separated full-rank masks suffice for constant rejection

**Attraction.** The old low-rank and unit-vector counterexamples looked sparse in some obvious sense. A polynomial-size family that spans every coordinate, changes roughly half the bits, and has large pairwise distances might seem to force coherent root agreement.

**Failure.** At k=2^r−1, even r≥4, use h_y(x)=x·y+1[x=y] and zero. Its matrix I+A^T A is self-inverse, every column has weight2^(r−1)±1, and pairwise distances are2^(r−1)±2. Yet a partition into triples {x,Tx,T²x} supplies k/3 disjoint parities. Each mask changes exactly one such parity. Physical overlaps change at most3a additional original positions.

**Counterexample.** Majority regions of these parities each contain exactly D root sites. Fit any prescribed root on every region and splice the honest transcripts on their interiors. All aliases retain one value. Rejection is O_a(k^(−1/2)), although x^D has exact relative code distance1−2^(−a). The designed reciprocal NO root also accepts almost everywhere. [Complete derivation and finite scope](../expeditions/043-dispersed-shifts/dense-masks.md)

**Lesson.** Neither span dimension nor pairwise distance controls all linear statistics relevant to the geometry. Repetition or probability reweighting cannot rescue this support: some triple character has bias at least1−2/m under every such distribution.

**Salvage.** Use an actual all-parities guarantee, such as the packed known small-bias construction, or prove a weaker property specifically sufficient for this physical verifier. Cost that property through the final Boolean encoding.
