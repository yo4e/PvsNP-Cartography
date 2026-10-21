# False shortcut: count both orientations of each quadratic edge over GF(2)

Attraction: ordered pairs are easy to enumerate. Claim: sum over i!=j in A of
X_i X_j equals the unordered clique polynomial.
Counterexample: n=2, A={0,1}, x=(1,1). The unordered quadratic term is1; the
ordered term is1+1=0 in GF(2). For q=1+sum_all X_i+clique, the correct value is0
and the wrong ordered-edge value is1. Division by2 in GF(2) is not a repair.
Salvage: sum each two-element subset exactly once. Integer binomial counting
happens BEFORE its cast to GF(2). The new elementary polynomial uses powersetCard.

Other exact guards in Expedition022: omit the layer denominator at n2,w1,h=1
and the purported mean is2 rather than1; empty n0,w1 has totalized mean0 and
cannot be a normalized distribution; omit the constant at n0 and q changes
from1 to0. The known n11 raw-seed failure at mask63 remains a regression: its
success is0 unless the full symmetrization bridge is used.

These refute only the specified shortcuts, not the intended polynomial or
weighted-layer identities. No all-n degree-two success or complexity separation.
