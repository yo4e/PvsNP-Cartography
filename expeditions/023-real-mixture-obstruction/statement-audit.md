# Statement audit, approved2026-10-22 JST night

Audit is by the research author, not an independent reviewer. Lean acceptance
and a separate exact computational implementation are distinct evidence.

1. Target is the ORIGINAL SmallSupportMod3.target on BooleanCube12, value1
   exactly when Hamming weight is divisible by3. Evaluations are in ZMod2;
   correctness indicators and probabilities are real, not field averages.
2. Allowed explicitly says zero OR actual q_A with card9 OR actual r_B with
   card8. All such subsets are quantified, not just canonical representatives.
   allowed_degree derives actual MvPolynomial.totalDegree<=2. This is not a
   purported normal form for every quadratic polynomial.
3. no_allowed_mixture quantifies a finite index type, family P and real mu,
   assumes each row Allowed, nonnegative weights and total mass1, THEN rejects
   forall inputs success>=2/3. No rationality, uniform-subset or distinct-row
   restriction is introduced. Repeated rows aggregate harmlessly.
4. The input dual is ACTUAL per-input mass. The layer probabilities5/14,9/14
   are divided by choose(12,6),choose(12,10). Full-cube normalization is proved.
   Empty-layer behavior of the generic interface does not enter this dual.
5. Score identities are consequences of q_layer_mean/r_layer_mean, themselves
   derived from actual polynomials. No score bound is assumed as a premise of
   no_allowed_certificate. Existing finite_dual_obstruction supplies duality.
6. Generic feasible_of_profiles genuinely bridges short profiles to the
   original probabilistic-degree predicate by existing full symmetrization.
   It does not confuse a raw seed-layer average with pointwise success of
   that same seed family. Symmetry of the target is an explicit premise.
7. q8_dual_score=5/6 and support_restriction_essential are Lean-checked attacks.
   They kill this dual as a universal quadratic bound, not the possibility
   of other unrestricted lower bounds or approximation constructions.
8. The matching9/14 primal is exhaustively checked finite data plus elementary
   weak duality. It is NOT a compiled Lean minimax-equality theorem. Arbitrary
   real mixture impossibility at2/3 IS compiled. These scopes are separated.
9. Source amplification/restriction arguments concern arbitrary n and real
   distributions for mathematical reasons stated in source-bridge.md. The
   majority/padding tests do not establish that generality by extrapolation.
   The hard Omega(sqrt(n)) theorem is explicitly imported from the literature.
10. Relativization, natural proofs and algebrization are not overcome here.
    This fixed-size support restriction is far from unrestricted circuit
    lower bounds; a known restricted-model asymptotic result is not P!=NP.

Hostile controls, precise saved output and failed-build provenance are in
verify.py/result.json, bridge-check.py/bridge-result.json, graveyard033..035.
New-code independent semantic review and a second kernel remain absent.
