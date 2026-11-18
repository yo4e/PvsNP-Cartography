# Refuted: share decision tables and retain the amplified rejection for free

**Attraction.** All translated checks use one proof, so computing each base decision once and reusing it at many centers appears to reduce gate storage while retaining the stronger AND rejection.

**Failure.** Let E be the actual failed base decisions. A shared copy buffer declares a set Z of failures. Copy constraints cost |E symmetric-difference Z|; private AND/output constraints cost |Z+H|. With zero in H their minimum is exactly |E|, attained by declaring every buffer true. At four seeds a one-point E and all four masks give four rejecting field centers but only one violated copy constraint.

**Precision consequence.** The exact signed sensitivity of the all-one decision-table toy is t+1: one flipped buffer breaks its own copy and t input implications. Thus even the sharp error-transfer constant sees the cost of fanout. Full shared base circuits may have higher sensitivity. The toy is a scoped compiler counterexample, not a standalone NO-sound verifier or a proof that every compiler fails. [Precise semantics and exhaustive gate controls](../expeditions/043-dispersed-shifts/compiled-cost.md)

**A second overreach rejected.** Private replication does not universally worsen precision: large shared overhead may amortize. The valid product test is M_H Q_H≥t M_1 Q_1, with actual costs and padding. Separate-score equality also needs honest/public pins or sufficiently charged duplicated pin checks.

**Salvage.** Price total signed failure sensitivity and address storage. Weighted or redundantly checked consistency can recover some rejection, but its error load must be charged too. The next target is a concrete improvement to gamma N/(Q sigma), preserving fixed projections and a global proof.
