# Failed shortcuts in the private-copy precision change

A first natural design capped every internal driver at fanout two. The actual copy census made the padded Boolean address cube double. Physical A cells still incurred 128 consistency failures per singleton because the direct A test reads the entire 128-symbol table. This design improves the measured precision by 9/8, but misses the larger gain available without crossing the padding boundary. Choosing cap 126 keeps every private charge at most 128 and gives the same exact sigma with 2,603 copies instead of 18,042 on YES. Its measured threshold gain is 9/4. The cap 2 implementation and output remain as a control.

Leaving the original physical input map directly connected to many uses defeats the intended single-read boundary. Removing the mandatory zero-offset A copy root from the cap 126 graph retains the honest verdict yet allows one physical A-bit error to cause 250 clause failures, exceeding 128. Copy roots must remain private per map and seed, with the actual physical aliases retained.

Removing the private split for original wire 5264 likewise preserves honest evaluation but restores a one-bit 199-failure example. A physical-input copy alone does not bound the entire circuit's signed sensitivity.

Charging an erroneous AND output only once is false. On the ordinary three-clause AND encoding, the valid 000 reference changes to 001 when only the output is flipped, and both input-implication clauses fail. The corrected local charge is two for an AND output, one for each input occurrence. The checker preserves this exact truth-table counterexample alongside signed and aliased controls.

A successful field or clause sensitivity calculation concerns the newly encoded global proof. It does not by itself transfer an existing approximating polynomial from old addresses to new copy rows. Such a claim would require a separate approximation and degree analysis of the address transformation.
