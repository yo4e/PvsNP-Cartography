# 010: naively lifting n=8 to n=9 fails (restricted construction)

Date: 2026-10-16 JST. State: refuted for THIS lift, not all n=9 quadratics.

## Temptation
Reuse the successful n=8 full-permutation witness, choose one coordinate of n=9 to ignore, evaluate its polynomial on the remaining eight coordinates, and average which coordinate is ignored. This is an appealing shortcut because restriction preserves polynomial degree.

## Exact counterexample
At x=(1,1,1,1,1,1,1,1,1), n=9 MOD3 is **1** (9 divisible by3). Every omitted-coordinate projection has all eight remaining bits one, with Hamming weight8, for which the n=8 MOD3 target is **0**. The existing full-symmetric n=8 witness agrees with its own target at weight8 with probability **2/3**. The lifted distribution therefore agrees with the n=9 target1 at the all-one input with probability **1/3**, strictly below the required 2/3. Randomizing the ignored coordinate cannot repair this input because all nine choices produce the same eight-bit vector.

This refutes only the above direct projection/lifting distribution. It does NOT prove the n=9 degree-two class impossible; Expedition011 supplies a verified n=9 degree-two witness.

## Other quantifier attack
The single source polynomial (1,127,36505001791) is not itself pointwise valid. For x having only coordinate7 set, its field value is1 while the target is0; its success is zero. `Mod3Nine.raw_seed_mixture_is_not_pointwise` formally checks a concrete counterexample. Full random permutation of its variables is necessary to obtain the tested pointwise lower bound.

## Salvage
Use projections as candidate generators only after rechecking each n=9 input, or use the fully symmetrized 4/3/2-block witness of Expedition011. An averaged over-input success statistic cannot stand in for success at each input.
