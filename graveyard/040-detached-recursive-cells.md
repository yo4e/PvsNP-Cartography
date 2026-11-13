# Broken copies can turn a NO proof into 127 accepting seeds

**Failed idea.** Store a separate table per child so a leaf has a simple local address. If the cell is also queried by the outer ACSP or another child, private copies can silently change the decision. The failure occurs even in a single recursive step.

**Parent split.** In the GF(128) NO fixture take A=0 and B(x)=1/x off zero, B(0)=0. The residual vanishes everywhere except zero. Feed an independent zero table to the recursive reader, and 127 seeds accept. With actual parent reads and the same zero extension, every row has 56 zero values and a nonzero parent value. No degree-<8 row passes; all 128 seeds reject.

**Sibling split.** Keep the actual root. Interpolate each row independently from its eight genuine parent cells, and offer separate zero columns. All local rows and private columns pass, again giving 127 accepting seeds. Once the columns read their actual row-sibling cells all 32 columns fail and zero seeds accept. The nonzero rows' values at a fixed common abscissa are proportional to the reciprocal of the row ordinate after translation. A degree-one column cannot fit them all.

**Related implementation failure.** Precomputing one set of full-row interpolation weights for all 16 rows appears to save public-input arithmetic. For B(X)=X, row 1 at slot 32 has value 384. Using row 0 weights gives 392. The implementation preserves the common low-coordinate interpolation and translates the evaluation polynomial by the actual public row shift as needed.

The repair is a single physical address for every shared bit, with the root high extension coordinates hardwired to zero, and arithmetic in each row's actual coordinate system. These examples refute detached layouts and the wrong interpolation implementation. The published geometric verifier already specifies shared reads.

[Computed counterexamples](../expeditions/040-recursive-verifier/verifier-checks.json) · [Geometry](../expeditions/040-recursive-verifier/geometry.md) · [Scalar derivation](../expeditions/040-recursive-verifier/soundness.md)
