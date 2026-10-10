# Barrier audit: finite n=5 formal reconstruction

Date: 2026-10-10 (JST). Issue #8.

## Relativization

No separation of oracle complexity classes, running-time lower bound, or
unrestricted circuit lower bound is asserted. The n=5 cube has exactly
32 inputs. This finite approximation game does not identify a non-relativizing
step capable of resolving P versus NP. A later transfer must face the
Baker-Gill-Solovay oracle constructions separately.

## Natural Proofs

No property of arbitrary truth tables with proved largeness, constructivity
and usefulness against a circuit class is supplied. Counts for one fixed
Boolean function do not supply such a property. The conditional
Razborov-Rudich barrier is neither evaded nor a reason to stop this work.

## Algebrization

Using GF(2) and a formal proof assistant is not a non-algebrizing technique.
No algebraic-oracle relation or asymmetric oracle-access claim is present.
A future asymptotic transfer would need its own precise audit.

Primary statements, parameters and sources remain in ../../map/BARRIERS.md.
This expedition adds no new barrier theorem and claims no barrier escape.

## Immediate semantic hazards

1. Averaging across inputs is not a per-input guarantee. The upper Lean
   statement quantifies over every member of Cube, not six layer labels.
2. A sampled polynomial type does not cover the complete class. Affine
   includes all binary constant/linear coefficients, but its interface to
   arbitrary MvPolynomial objects of degree <=1 still needs a formal bridge.
3. Real mixture probabilities are not restricted to rational numbers.
   Integer checking is followed by a proof for arbitrary real distributions.
4. Normalization is essential. A zero-mass input measure would make every
   deterministic row appear harmless without constraining pointwise success.
   The countermodel is retained in ../../graveyard/004-zero-mass-dual.md.
