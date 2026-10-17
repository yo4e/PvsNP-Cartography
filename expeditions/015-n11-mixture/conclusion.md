# n11 conclusion: two exact finite witnesses, preferred three-orbit refinement

Final checkpoint of the approved 2026-10-17 JST session. NO n11 Lean theorem
has been executed. Both finite certificates are preserved and were actually
reproduced by completed normal/-O GitHub CI, with saved/actual JSON equality.

## Preferred compact witness

Three degree<=2 GF(2) polynomial seed orbits with fixed weights[1,4,2]/7:
zero polynomial, (8,2,1) block code31, (7,3,1) block code29. Seeds and coordinate
permutations are selected independently of the input. Full expansion yields
1925 indexed polynomial entries (duplicates allowed), denominator27720. Exact
pointwise success at all2048 inputs is at least158/231>2/3, margin4/231.

Code402b13398af15add64961d4894b2a371beec3711; successful run39038647497,
job117413471238. Completed full logs and actual certificate/result/commit were
re-fetched. See compact-ci-evidence.md, compact-certificate.json,
compact-result.json and compact-verify.py. Triple tickets[3,12,6]/21 and
threshold14 are ready for a faithful later Lean encoding, NOT yet accepted there.

## Preserved larger-margin witness

Original nine-orbit weights/10000 and certificate.json remain unchanged.
Its4785-indexed-polynomial expansion has denominator277200000 and minimum
24044/34375>2/3, margin3382/103125. Code81ca743a43b232b055de7849fa9a8782f913696c;
successful run39037985386/job117411565884. See ci-evidence.md and finite-result.json.
The refinement trades some success margin for fewer seed orbits and simpler
probabilities. It is not a universal improvement or proof of minimality.

## Verification and lower obstruction

Both use two coefficient reconstructions, full canonical truth-table and Mobius
degree checks, independent full pointwise partition expansion and exact layer
scores. Seven altered certificates are rejected. Normal and optimized Python
agree locally and in their respective completed CIs. No optimizer is imported
by the standard-library verifier.

The same lower distribution assigns mass15 to each weight-one input and mass1
to each weight-three input, total330. All4096 affine rows score<=207, namely
69/110<2/3, gap13/330. Direct, Walsh and hypergeometric methods agree. By linearity,
that finite dual excludes any input-independent convex mixture of affine rows.
The n11 formal instantiation linking arbitrary degree-one polynomial objects
through the existing structural normal form has NOT been compiled.

Uniformly omitting one coordinate and reusing the n10 witness fails at n11
weight10 with success61/220. graveyard014 preserves that scoped post-mortem;
it does not refute either fresh n11 distribution.

## Frontier and limits

Issue #11 now prefers the three-orbit witness, with full actual-degree, REAL
normalization, pointwise quantifier and axiom-audit acceptance criteria. The
unfinished n10 build gate in #10 has precedence. Human semantic review remains
independently open in #8. Both n10 build attempts were cancelled, so complete
formal numerical coverage is still n5..9.

Initial search examined10240 raw patterns/4376 distinct profiles; refinement
examined129 numerical subset problems. Those figures do not prove exact LP
optimality, one/two-orbit infeasibility, global support/denominator minimality or
novelty. No all-n MOD3 theorem, circuit lower bound, barrier escape or P-vs-NP
solution follows. The finite upper/lower claims are explicitly bounded to n11.
