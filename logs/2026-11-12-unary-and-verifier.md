# November 12 JST night • a sharp GF(32) instance and unary counting

The November 12 session was approved and carried out after midnight on November 13 JST. The initial head was 9f101228. The open work was the end-to-end verifier in #28 and the unary time/accuracy budget in #29; older review issues 8 and 15 have independent scopes.

The two generated GF(32) base instances have exact minimum failed clause–seed counts 0 and 25 out of 469,056. Their witnesses are explicit polynomials, including a cubic for the sharp NO case. For the counting route, both a shared-address consistency score and a separate line-interpolation derivation give a costed inverse-polynomial-error implication for an encoded E^NP family. The unrestricted local-plus-disagreement score has exactly the global optimum, and two opposite units require the smaller endpoint mass. The research decision is to leave constant-error extrapolation aside and resume the recursive verifier conformance target in #28. [Conclusion and scope](../expeditions/039-unary-overlap-counting/conclusion.md) · [Claim and sharpness](../claims/039-common-address-penalty.md)

[Research commit dc8634ed](https://github.com/yo4e/PvsNP-Cartography/commit/dc8634edb2727787a51be200982261243b9bdbbb), tree 501833ccb6fe74d9dd5fe6b080a61da1bcfcbcf4. GitHub returned the exact contents and blob IDs of all 20 changed paths at that commit. [Actions run 43250231497](https://github.com/yo4e/PvsNP-Cartography/actions/runs/43250231497) and [job 131293717936](https://github.com/yo4e/PvsNP-Cartography/actions/runs/43250231497/job/131293717936) completed successfully. The downloaded job output contained the expected commit and all ten SHA-256 digests for the five programs and their five JSON outputs. Normal and optimized Python both reproduced the stored outputs. The checks are finite and do not run Lean.

In a separate checkout of the fetched commit, the generator exported both complete DIMACS streams. A second parser counted clauses and evaluated each signed literal against the physical assignment from the generator layout. For the NO witness it formed B directly from the product U(X) over the four interpolation points. This cross-check shares the original field arithmetic and physical wire layout.

| DIMACS stream | Clauses read | Failed for the stated assignment | SHA-256 of the complete export |
|---|---:|---:|---|
| yes | 469,056 | 0 | f2bce67a6cc7dd4a2f64d81dcbfbd1843171189257337130c0b45dc28b7f46da |
| no | 469,056 | 25 | 1caed15aba2186e2dc32232394575191a9dc3d699c8611aa7490d54906747eb4 |

Recreate either stream with `python expeditions/039-unary-overlap-counting/verify_base_acsp.py --dimacs yes` or `--dimacs no`. The generator, witness descriptions and small JSON results are stored; the expanded DIMACS texts are reproducible exports. [Issue 28 update](https://github.com/yo4e/PvsNP-Cartography/issues/28#issuecomment-6828211809) · [Issue 29 completion](https://github.com/yo4e/PvsNP-Cartography/issues/29#issuecomment-6828212368)

The next named target is one genuine recursive RS child with physical parent and sibling aliases exercised by a satisfying assignment and adversarial global tables. The current base-case rates terminate before that step. No write blocker or pending patch remains. Separate human review and independent formal verification of the new derivations are outstanding.
