# Primary-source comparison and novelty boundary

Sources were retrieved during the November 21 JST session. The following
comparison motivates and bounds the construction; it is not a priority claim.

## Projection-query PCP structure

Eli Ben-Sasson and Emanuele Viola, *Short PCPs with projection queries*,
ECCC TR14-017, February 9, 2014:
https://eccc.weizmann.ac.il/report/2014/017/download/

The relevant source locations are equations(8)–(9), Proposition6.1 and
Section6.2. They describe the polynomial decomposition and the physically
shared parent/row/column structure used by the existing Expedition040
fixture. This session retains that B structure. Its A replacement and
the109/23 cost calculation are explicit fixture arguments in this repository,
not numerical constants attributed to that paper. The broad source theorem
does not by itself certify a modified local predicate.

## Local testing is established prior art

Eli Ben-Sasson, Noga Ron-Zewi and Madhu Sudan,
*Sparse affine-invariant linear codes are locally testable*, April 27, 2012
manuscript:
https://people.csail.mit.edu/madhu/papers/2012/sparse-affine-full.pdf

Theorem1.1 gives a constant-query local tester for each fixed field and
sparsity parameter, for the stated linear affine-invariant properties.
The surrounding definitions concern maps from an extension field to a fixed
base field and distance to the property. This does not directly give our
chosen fixed-XOR query schedule, the actual Boolean address cost, or the
joint NO residual bound. In particular, this session does not claim to have
invented local testing from affine overlap.

The elementary fact that two affine field polynomials agreeing at two
distinct points are equal, and the complementary-subspace identity
(U union V)+(U union V)=U+V, supply the selected proof. We claim a checked
construction and a cost comparison in the named repository model.
The targeted source check is incomplete as an equivalence/priority search;
novelty remains unknown. No exact hypercube connectivity theorem is imported:
the intermediate Hamming-ball calculations retain explicit finite path
certificates, and the final cross construction does not require them.
