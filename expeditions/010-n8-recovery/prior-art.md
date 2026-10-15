# Provenance and primary-source check

Date: 2026-10-16 JST. Role: historian. Novelty status: unknown.

## Existing project mathematics

The n=8 numerical value and original four orbit seeds were already established
as finite certificates in ../004-exact-mod3-n8/. Its certificate.json is unchanged,
Git blob45f4c6b63b17ad5f7820512bb01530a93c345885. The generic symmetrization
interface was already verified in Expedition008. Expedition009 contributed the
Hamming-layer/counting and n=8 candidate that this session repaired. Completion
of that chain is a verification advance, not discovery of a new numerical value.

The prior local-only Oct14 compact witness was supplied in:

- PvsNP-Cartography_2026-10-14_report.md
- PvsNP-Cartography_2026-10-14_compact-n8_handoff.zip
- PvsNP-Cartography_2026-10-14_compact-n8.patch

Patch SHA256:
df82d29ef430efa2a09e36397e409c10d3be7c95c1bedba4168a4d158441cf2a.
It contains22 additional files and was NOT applied wholesale. The current
recover_939.py reconstructs its exact939 coefficient rows (canonical SHA256
ffd64b510a09c110fd1843e988e0b0948740319b6a03ea78a487f8223d3da666).
The old direct checker is preserved byte-identically as verify_compact.py
(SHA256 ebe439593567f997943b3897c10a79876e1ea4aeb5540f846d2c14526bb64f02).
No claim is made that every legacy archive file has been copied into main.

## Primary technical documentation consulted

- SciPy linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
- SymPy matrices and exact row reduction: https://docs.sympy.org/latest/modules/matrices/matrices.html
- Lean tactic reference: https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/

The documentation informs implementation, not a mathematical novelty claim.
The locally executed search used numpy2.3.5, scipy1.17.0 and sympy1.14.0;
current online documentation can describe a newer release. Exact validators
use only the Python standard library and do not trust optimizer success.
Lean verification used the repository's pinned Lean4.35.0-rc4 and Mathlib
9e6b3aac99b624d10c84653ab9c5357283b9b3b8, not an assumed latest toolchain.

No targeted literature audit sufficient to claim novelty or support minimality
for the159-row presentation was completed. Same-author rediscovery, a smaller
JSON and a successful CI job do not establish priority or publication readiness.
