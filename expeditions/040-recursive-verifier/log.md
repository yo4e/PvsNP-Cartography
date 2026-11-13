# Session record • November 13 JST

The live default branch began at a64135df. Issues 8 and 15 concern separate external reviews. Issue 28 carried the first recursive verifier check after Issue 29 closed. The sources were Ben-Sasson–Viola §§5–6 and Ben-Sasson–Sudan §6, together with the previous source-layout and compiler records.

- **Build.** Implement the rate-1/8 root on θ+GF(128), the shared bivariate domain, the two families of leaf tests and honest extension by division by the subspace polynomial. Generate signed physical clauses for an instance checking affine A and recursively checked B. The expanded CNFs and the extremal assignments can be exported without storing the large streams in Git.
- **Verify.** A second field implementation reconstructs every row by direct interpolation. It agrees with the quotient/remainder construction on all 1,024 cells of 18 polynomials. Compare field-level and compiled decisions on 36,352 (instance, proof, seed) cases. The bit evaluator, packed CNF and a separate DIMACS reader serve different verification stages.
- **Attack and repair.** Exercise detached parent and sibling reads on a reciprocal table, then join the actual addresses. Blind reuse of row weights predicts 392 for an honest 384; normalize row coordinates with the public label. An altered noncode root attains the same 19 accepting seeds as the extremal codeword.
- **Continue.** Interpolate between two passing rows using at least eight passing common abscissae. This forces a low-degree representative on the relevant seeds and prices arbitrary auxiliary assignments. Locate the next obstruction where a child is checked only locally rather than over its whole row.

Internal work on source geometry, independent-by-implementation arithmetic, the extremal calculation and the signed compiler was integrated by 月野テンプレクス. The checks share the mathematical specification. No independent external review occurred.
