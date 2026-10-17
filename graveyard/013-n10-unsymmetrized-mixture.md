# Failed shortcut: use the eight n10 seeds without coordinate randomization

Claim: the canonical eight polynomial rows with weights
[10,2,39,22,15,6,4,2]/100 already satisfy every input with probability >=2/3.

Attraction: their averaged Hamming-layer counts all exceed2/3, so it is easy to
mistake a layer-averaged certificate for the raw pointwise distribution.

Counterexample: little-endian input [0,0,0,0,0,0,1,0,1,1], integer mask832,
Hamming weight3 and target1. The raw mixture wins with probability2/100=1/50.
The independent checker scans all1024 inputs and finds this minimum. The Lean
candidate also states an exact six-out-of-300 ticket counterexample; its formal
status must be read from the expedition's completed CI evidence, not this text.

Failure point: interchanging average-over-layer with for-every-input. This is
not repaired by renaming the layer mean a pointwise probability.

Salvage: first choose the seed with the stated fixed probability, independently
choose a uniform coordinate permutation, then evaluate the renamed polynomial.
The general layer/permutation identity is exactly the missing bridge.

Scope: this kills only the unsymmetrized shortcut, not the eight-orbit witness,
not arbitrary quadratic distributions and not any general complexity claim.
