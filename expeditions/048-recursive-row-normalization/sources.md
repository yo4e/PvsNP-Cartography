# Fixed-rate recursive layouts: sources, quantifiers, and cost

Date: 2026-11-28. Read-only audit against repository main `ba1da266a3e51f4025b7ba4f00d305b94796cbff`. It supplies a written coordinate argument and a bounded source audit; it makes no novelty claim.

## Conclusion

The recursive proof has exponentially many node identities, but this does **not** force an exponentially large table for every useful row layout. In the offset-query variant specified in Expedition 038, a public inverse shuffle of each canonical physical address separates the original root coordinates from the fresh auxiliary coordinates. A row can therefore run across many actual nodes. There are only polynomially many such transverse rows at a fixed rate exponent.

A guessed label table on those rows costs polynomially many bits, and each fixed query remains a constant tag followed by signed seed coordinates. This removes the particular per-node-table cost objection. It does not establish a low-degree approximation to an honest proof. Moreover, this class of label changes has an elementary additive-degree pullback: a degree-d polynomial in the new layout induces an old-address completion of degree at most d + O(log k).

## Primary-source index

All page numbers below are printed page numbers. PDFs were reopened on 2026-11-28.

| Source | Exact locations | Facts used here |
| --- | --- | --- |
| Eli Ben-Sasson and Emanuele Viola, [Short PCPs with projection queries, TR14-017](https://eccc.weizmann.ac.il/report/2014/017/download/) | Theorem 1.1, p. 2; Definition 6.2, pp. 18–19; proof of Theorem 4.6 and §§6.2–6.3, pp. 20–21 | Polynomial-time construction of signed projection queries, polynomially many queries, quasilinear proof length, existential perfect completeness, universal NO soundness. The recursion partitions coordinates between edge labels and a live word; fixing its logarithmically many control bits leaves permutations and flips. |
| Emanuele Viola, [New lower bounds for probabilistic degree and AC0 with parity gates, TR20-015 revision 5](https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/), January 12, 2021 | Lemma 11, pp. 11–12; Theorem 12, p. 12; §2.3, pp. 13–15 | Polynomially many three-literal templates with inverse-polynomial rejection; exact counting of a degree-D GF(2) polynomial on k variables in time 2^(k−Ω(k/D)+O(log k)). The application guesses one shared polynomial and composes it with fixed linear queries. |

These sources do not state the transverse-row normalization lemma below, do not promise low degree for every satisfying proof, and do not supply a generic faster counter for an arbitrary small-circuit address decoder. The lemma below is an elementary derivation for the repository's explicitly stated coordinate variant.

Local definitions and assumptions are in:

- `expeditions/038-recursive-query-fibers/source-compiler.md` and `verify_recursive.py`;
- `expeditions/039-unary-overlap-counting/budget.md`;
- `expeditions/047-witness-layouts/` for the shared-map quantifiers and guessed-label model.

## What the fixed control bits do and do not fix

Fix a rate exponent a ≥ 3 and a root coordinate width k. At dimension d > 2a put l = floor(d/2). The Expedition 038 coordinate rules are

- R: save V as the edge label and replace the live word (U,V) by (U,A), where A has a bits;
- C: save (U,A') as the edge label and replace the live word by V, where A' has a−1 bits.

Here U has l bits and V has d−l bits. A fixed tape fixes branch choices and fresh bits. It does not fix U or V, so it does not fix actual node identities. In particular, a public header describing the sequence R,C,... is different from its seed-dependent edge-label payload.

The depth is at most

    h = 0                                 if k ≤ 2a,
    h = 1 + floor(log2(k−2a))             otherwise.

The native edge-and-live payload has at most k+ah bits; path header, tree identifier and symbol-bit index require O(log k) additional bits for fixed a. The complete native width m0 is k+O(log k).

### A valid but narrowly scoped node-count objection

Along the all-R path, let d0=k and d(j+1)=floor(dj/2)+a. Then d(j)−2a repeatedly halves with floor, and the terminal dimension is 2a after h steps. The number of actual terminal nodes with this one shape is

    product_j 2^(dj−floor(dj/2))
      = 2^(sum_j (dj−d(j+1)+a))
      = 2^(k−2a+ah).

For h ≥ 2 this is at least 2^k. Each final row has private extension points, so a separately guessed arbitrary label for every actual node already costs too much for the Expedition 039 clock. This argument rules out that explicit per-node table. It says nothing adverse about a table whose rows cross many node identities.

## Positive coordinate lemma: canonical transverse rows

Work with the physical storage convention in Expedition 038: column names redirect to the corresponding row sibling; a row point in its parent copy redirects to the parent. Normalize **after this canonicalization**, using only the resulting physical address.

For a fixed canonical path shape S, reverse its frames from the last frame to the first:

1. At an R frame, split the live word as (U,A), extract A, and append the saved label V to recover (U,V).
2. At a C frame, split the saved label as (U,A'), extract A', and prefix U to the live word V to recover (U,V).

Every step is a permutation and separation of coordinate slots. Induction therefore gives a bijection

    edge labels + final live coordinate  <->  (z, A_S),

where z consists of all k original root-coordinate slots, in their original order, and A_S consists of

    g(S) = a * #(R in S) + (a−1) * #(C in S) ≤ ah

fresh-coordinate slots. The construction depends on the canonical shape and public dimensions, not on the originating query, witness, or stored value. Thus aliases cannot acquire distinct normalized names.

For the stated polarity, the independently stored symbols are precisely:

- the root row;
- shapes ending in R whose final a-bit auxiliary chunk is nonzero.

Earlier fresh chunks are unrestricted. A terminal C is an alias, and a final R chunk equal to zero is the parent-copy alias. The set of allowed (S,A_S) tags is independent of z. For every allowed tag, all 2^k root strings give distinct stored symbols. Tree identifiers and permitted symbol-bit indices refine these symbol rows into bit rows.

There are fewer than 2^(h+1) shapes and at most 2^(ah) fresh strings for each shape. Consequently the number R of bit rows is poly(k) at fixed a. Additional gate and public-input rows of the stated Boolean compiler can be included with their existing public tags; their full field/CNF implementation remains a separate obligation.

### Fixed offset queries

For a fixed down tape and fixed leaf XOR offset, the original k tokens are each retained once, possibly complemented. The canonical return rules give a constant final shape and constant fresh coordinates. After the public inverse shuffle, its bit query has the form

    z  ->  (tau, z XOR delta),

for fixed row tag tau and fixed delta. This is the useful positive property: the row tag is constant even though the original edge labels and actual node identities vary with z. Absolute leaf replacement would instead erase some original tokens and needs its own rank accounting. Public-input pins in the Boolean compiler clamp one coordinate and are handled separately.

### Source polarity caveat

This lemma uses the corrected coordinate convention already stated in Expedition 038. Under the row basis with origin beta and last direction c0+beta, a point with all auxiliary coordinates zero is in beta+L0, the parent copy. The last-selector test printed in BV14 §6.3 has the opposite polarity from that displayed origin. This audit does not silently identify the literal printed test with the repository variant. The column redirect uses last selector one and therefore lies in the auxiliary rectangle. The lemma concerns the resulting specified coordinate model, not a fresh verification of the entire published construction.

## Guessed labels, global consistency, and resource accounting

Let lambda:[R]->{0,1}^t be one guessed row-label map, where t=O(log k), and let P be one polynomial of degree d in k+t Boolean variables. Decode a global old physical proof by

    pi_lambda,P(a) = P(lambda(tau(a)), z(a)).

Every occurrence of a uses the same canonical normalization and the same lambda. Hence even a noninjective lambda defines a genuine global proof: collisions impose extra equalities between its bits. Universal NO soundness is preserved without injectivity. Injection is needed to transport an arbitrary honest assignment without imposed equalities and to identify used-cell Hamming errors one for one. An occurrence-specific choice of lambda is not this construction and may break shared-cell consistency.

For the injective version choose ceil(log2 R) ≤ t = O(log k):

| Resource | Bound | Reason |
| --- | --- | --- |
| Label description | Rt = poly(k) bits | R is a transverse-row count, not a node count |
| Injection check | O(Rt log R) bit-comparison work | Sort the labels and check adjacent equality |
| New address width | m=k+t=k+O(log k) | Fixed-rate tag count |
| Polynomial description | B(m,d)=sum_(i≤min(d,m)) binom(m,i) bits | Multilinear coefficient representation |
| Fixed query | Constant label plus signed seed projections | lambda(tau) is fixed once the table is guessed |
| Three-literal clause | Degree at most 3d on k seeds | Each signed substitution preserves degree |
| Number of counter calls | M=poly(k), conditional on the stated compiler | Relabeling does not multiply the template count by R |

At k=n+O(log n), d=O(n/log n), the coefficient description and ordinary expansion are 2^o(n). A signed substitution expands a monomial into at most 2^d terms; multiplying the three substituted polynomials and collecting Boolean monomials remains subexponential under this budget. Polynomially many label operations do not consume the required exponential saving.

This ledger is conditional on the full compiler's polynomial template and construction bounds. The coordinate checker alone does not build those field predicates or their Boolean gate clauses.

## Additive-degree pullback for this particular layout class

There is a sharper fact than treating the whole normalizer as a generic circuit.

Each canonical transverse bit row is an axis-aligned k-dimensional subcube of the native m0-bit address cube: its header, symbol index, all fresh-coordinate slots and omitted-payload padding are constants; exactly k payload positions remain free. Let chi_tau be the product of the literals fixing its m0−k other coordinates. Let z_tau(a) be the permutation of its k free coordinates into root order. The row subcubes are disjoint.

For any shared label table lambda, even one with collisions, define

    F_old(a) = sum_tau chi_tau(a) * P(lambda(tau), z_tau(a))   over GF(2).

This polynomial has degree at most

    d + (m0−k) = d + O(log k).

On each used physical cell exactly one selector is one, so F_old agrees with the decoded proof. Including the old padding literals in the selector makes F_old zero outside the used row union. This is an elementary selector construction, not a new approximation theorem.

With injective labels, the discrepancy count on used cells is preserved by the coordinate bijection. Uniform errors on entire padded cubes require their actual denominators: e wrong used cells gives e/Q_old and e/Q_new respectively, and a new polynomial may additionally err on unused new labels. Consequently a theorem stated in full-cube error must carry these factors or use the appropriate completion convention. It must not silently call the two uniform rates equal.

The pullback shows that arbitrary label rearrangements among these polynomially many rows cannot yield a degree improvement beyond the O(log k) selector cost when the used-cell approximation budget is transported correctly. It does not rule out a different representation with other algebraic properties, nor does it prove that useful approximants exist.

## General succinct recoders and the inherited counting boundary

For comparison, if a single global recoder Phi has coordinate GF(2) degree at most q, then P composed with Phi has degree at most qd. With an original signed query and a three-literal clause, the degree bound is 3qd. The inherited counter therefore has the schematic cost

    poly(n) * 2^(k−c*k/(3qd)+O(log k)),

plus the work needed to construct the explicit polynomial. Under the Expedition 039 clock one needs qd ≤ alpha*n/log n for a sufficiently small fixed alpha paying all polynomial overhead. A polynomial-size circuit description of Phi alone does not establish this condition or bound the expansion cost. No stronger counting theorem for arbitrary small-circuit recoders is supplied by the two primary sources audited here.

The normalized row construction is better behaved because its tag is constant separately on each fixed query. Its counter degree remains 3d. The additive pullback above is a limitation on possible representation gain, not an added 3(d+O(log k)) cost that must be paid in the normalized counting algorithm.

## Evidence checked and remaining obligations

Read the implementing branch of `check_recursive_normalization.py`, now archived beside this note. Its inverse shuffles agree with the written R/C formulas; `canonical_rows` implements the stated alias conditions. Its normalization uses only physical-address fields. No semantic issue was found in those parts.

The module imports Expedition 038's geometry and symbolic candidate generator. Its separate normalization routine and concordance checks are useful independent coordinate checks; they are not an independent implementation of the entire source verifier. No completed execution result is asserted by this source note. The final execution record is in `execution-evidence.md`.

The remaining substantive issue is an existential approximation statement for an actual satisfying global proof, at the required degree and error budget, together with the complete recursive field/CNF resource ledger. A coordinate reindexing, a code-only all-witness lower bound, and a finite symbol-address check do not settle that issue.
