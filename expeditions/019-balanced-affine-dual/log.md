# Structural research loop, approved2026-10-20 JST

OBSERVE: n7..11 finite affine duals share equal-half weight1/weight3 input mass.
ORIENT: split the research target into combinatorial counting and pure real
algebra, rather than extrapolating finite tables to arbitrary arity.
ACT: derive S(n,k)=1/2+t(n^2-t^2)/(4n(n-1)(n-2)),t=n-2k. Supply a counting
sketch for odd intersections and an explicit sum-of-squares cubic envelope.
VERIFY: symbolic numerator/SOS residuals vanish. Standard-library exact checks
compare33147 formula pairs n3..256, plus full input cubes/all affine rows via
Walsh and direct canonical sums n3..12. Local normal/-O outputs match.
ATTACK: strictness down to n6 fails at k1 with2/3; n5k1 gives7/10. Reject the
specific too-broad dual, not the previously proved n5/n6 degree equalities.
REPAIR: retain real-algebra domain n>=7,0<=k<=n and explicitly leave the generic
Boolean-cube counting bridge unproved. Preserve the boundary in graveyard018.
FORMALIZE: initial source ea1f4e04 adds the algebra module and six axiom targets.
Independent exact CI39381262415/job118490656488 passes normally and with-O,
with saved/actual equality. Its success is not the formal acceptance.
ATTACK: formal39381262500/job118490657553 FAILS on real computability and an
unused-hypothesis warning. Retrieve full failure log; preserve graveyard019.
REPAIR: dde6151a marks the real definition noncomputable and explicitly uses
hhi. No changed statement, domain, threshold, --wfail or axiom allowlist.
VERIFY: actual production39381768668/job118492254315 SUCCESS:9044 jobs,
518 namespace declarations, six algebra and18 n11 printed reports, all within
propext/Classical.choice/Quot.sound. Retrieve full completed log, then entire
repaired source and matching Git commit/tree. Re-fetched source blob
 ef92fdecc80241481d9b4578dce596848733ff33 agrees with local Git-blob hashing.
Re-fetch bounded result720dc3ff2ecc5109f1091720946748609b975033 and compareactualCI.
RECORD: save attributed evidence, formal algebra claim, exact remaining scope,
and open #12 for generic counting/normalization/actual evaluation/duality.
Update #8's unfulfilled independent human-review gate, not close it.

No second kernel, independent human review or novelty claim. The real theorem
is genuinely general in its stated variables, but the Boolean-cube connection
is not thereby proved. No all-n degree2 upper bound or P-vs-NP conclusion.
