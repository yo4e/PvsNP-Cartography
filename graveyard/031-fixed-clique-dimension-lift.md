# Refuted: keep the n11 clique recipe unchanged as the dimension grows

Claim: for all n>=11, use zero, q_A with |A|=n-3, and r_B with |B|=n-4,
weights [1,4,2]/7, followed by full uniform coordinate permutation. This
straightforward extension of the successful n11 recipe still succeeds >=2/3
at every input.

Counterexample: n=12, Hamming weight10. There are choose(12,10)=66 inputs.
The fixed q_A with |A|=9 is correct on36 of them; r_B with |B|=8 on28;
the zero polynomial is correct on all66. The weighted success is
(66+4*36+2*28)/(7*66)=266/462=19/33<2/3, a gap of1/11.
Full coordinate symmetrization makes this layer average the pointwise success
for every input of that weight. Symmetrization does NOT fix a bad layer mean.
The raw unsymmetrized mixture also cannot have a pointwise lower bound2/3
when its layer mean is smaller. A second failing layer is weight7:437/693.

Independent representations: naive-lift-attack.py directly evaluates every
one of4096 Boolean inputs using explicit unordered monomials and independently
checks binomial overlap profiles for all13 layers. Integer/Fraction comparisons,
normal/-O outputs and saved actual result are available. CI status must be
read from the expedition evidence, not inferred from this file's presence.

Scope: this kills only the stated fixed-family, fixed-probability dimension
lift. It does NOT exclude another n12 quadratic mixture, classify all clique
mixtures, change previous n11 results, establish n12 degree, or settle P vs NP.
Salvage: use certified profiles to test/derive genuine parameter-dependent
mixtures or dual obstructions for a precisely declared restricted family.
Do not extrapolate one feasible dimension or one failure to an all-n claim.
