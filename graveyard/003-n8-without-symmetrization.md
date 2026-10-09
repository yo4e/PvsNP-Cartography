# Graveyard 003: omitting symmetrization from the n=8 witness

Date: 2026-10-09. Status: refuted semantic mutation / negative control.
This was deliberately generated to test the certificate, not a claim
previously believed or published by the research lead.

## Invalid claim

Choosing the four raw polynomials with probabilities 1/12,1/4,1/3,1/3,
WITHOUT also uniformly permuting their variables, already gives
pointwise success at least 2/3.

## Attraction

The four layer-success vectors combine to values >=2/3. Reading that
layer average as a per-input guarantee silently drops the randomization.

## Exact counterexample

x=14 means (x0,...,x7)=(0,1,1,1,0,0,0,0). Its weight is 3, so MOD3(x)=1.
Under the raw mixture only the first polynomial agrees, giving success
1/12, far below 2/3. The checker computes this on the whole cube.

## Failure point and salvage

A representative's correctness fraction inside a layer is not its
correctness at each member of that layer. Uniformly randomize variable
permutations after selecting the row. This restores the exact pointwise
probabilities by equal orbit multiplicities. The repaired four-orbit
certificate survives both evaluators and the complete permutation audit.
