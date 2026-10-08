# Conclusion: Expedition 003

Status: **sample-restricted optimality verified; universal inference refuted**
Date: 2026-10-08. Novelty: **unknown**.

## What survived

For a precise deterministic pool S of 10,016 n=8 quadratic
polynomials (6,407 different layer profiles), the best mixture of
uniform permutation-orbits has minimum pointwise success exactly
569/902. Exact rational primal and dual certificates prove
this **conditional on membership in S**.

## What died

The proposed dual q is not a lower certificate for **all**
quadratics. A polynomial with coefficient masks c=1, a=255,
b=60548413 attains q-average correctness 27376/41041 > 2/3.
The common inference from “no witness in the pool” to
“no witness anywhere” is invalid and has been archived.

## What is unknown

Neither pdeg_(1/3)(MOD_3^8)=2 nor pdeg_(1/3)(MOD_3^8)>2 was
established. Restriction from the verified n=7 case gives only
the lower bound >=2. There is no asymptotic or P-vs-NP consequence.

## Next exact frontier

1. Find a rational mixture of n=8 degree-2 polynomial orbits with
   each layer at least 2/3, then audit pointwise and negative controls.
2. Otherwise design a truly **universal** n=8 degree-2 lower
   certificate and a verifiable complete-class search method.
3. Explore graph-isomorphism/orbit canonicalization or SAT/SMT/ILP
   only with a proof of coverage. Sample LP duals are hypotheses
   to attack, not obstructions to advertise.
