# Conclusion: the same n11 measure on496 distinct polynomials

Approved2026-10-18 night. Exact finite result; NOT a compiled n11 Lean theorem.
Both local normal/-O execution and completed remote CI now reproduce this
construction. See ci-evidence.md for attributed actual output and re-fetched
source, result, commit and generated support artifact.

Let V={0,...,10}, w=sum_i x_i and E_A=sum_{i<j in A}x_i*x_j over GF(2).
The old block-code31 polynomial is q_A=1+sum_all x+E_A with |A|=8.
The old code29 polynomial is r_A=1+sum_{i notin A}x_i+E_A with |A|=7.
The other seed is zero. In both nonzero seeds the second and third labelled
blocks are indistinguishable as polynomial objects.

For each8-subset there are3 old labelled partitions; for each7-subset there
are4. The zero orbit lists110 copies of the same polynomial. Aggregate exact
rational mass by coefficient row, rather than discarding duplicates. The old
1925-entry indexed distribution is exactly this496-distinct-row measure:
zero has integer mass165, each of165 q_A rows mass4, each of330 r_A rows mass1,
all divided by1155. The total is165+660+330=1155. Exact old/new mass dictionaries
agree, so every input probability is unchanged, not merely the minimum score.

## Independent verification

For k=|A intersect support(x)|, q_A(x)=(1+w+choose(k,2)) mod2 and
r_A(x)=(1+w+choose(k+1,2)) mod2, using choose(k+1,2)=choose(k,2)+k.
These formulas and explicit monomial evaluation agree in1,013,760 comparisons.
Independent layer counts use choose(a,k)*choose(11-a,w-k), a=8 or7.
All2048 pointwise scores and12 layers agree with the old probability measure;
minimum158/231, margin4/231 above2/3. Re-exhausting4096 affine rows confirms the
unchanged dual207/330=69/110<2/3.

Code8ff6df0ba8362966f2df76d90e5fbe3a84d8f2a5; completed SUCCESS run39137936272,
job117706176557. Full log, normal/-O equality and saved/actual JSON equality
were inspected, then verifier/result and commit/tree re-fetched. The generated
support is artifact12140137583, not a checked-in full table. Regenerate it with
`python verify.py --write-support support.json`. Rows are sorted
[constant,linear_mask,quadratic_mask,integer_mass], using55 lexicographic edges.
Canonical compact-JSON SHA256 excluding newline:
aa05128f4d4005cd4911bbed1d2aa833989a4b09e136662f7684b86d1a1b0c64.
The checked-in result also hashes all2048 point scores.

## Refuted shortcuts

Uniformizing496 distinct rows gives281/496<2/3 at mask15, weight4. Deleting
duplicates without accumulating masses leaves304/1155 rather than1. Omitting
symmetrization entirely gives success0 at mask63, weight6. A flipped coefficient
changes actual point scores. These four controls are in the normal/-O verifier
and graveyard016. They refute only those shortcuts, not the valid quotient.

## Frontier and limits

n10 has now separately passed production Lean verification (Expedition016,
closed #10). #11 is next: encode the faithful n11 degree interface, choosing
between the original three-seed/full-permutation proof and a formally justified
496-row quotient. The finite quotient is not itself a Lean transport theorem.
No support/denominator minimality, independent human review, mathematical novelty,
all-n MOD3 result or P-vs-NP conclusion follows. The earlier nine-orbit and
three-orbit certificate files remain unchanged, with all provenance preserved.
