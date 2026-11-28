# Targeted source audit for residual and gate degree

Date: 2026-11-28 night. Repository checkpoint `2a546c3781d71cd159b388997bd5312a7ceb78e6`. Read AGENTS and compared the required documents with the previously read checkpoint; only README changed among those required files. Read the completed Expedition 048 conclusion, normalization and conditional cost argument.

This note identifies source statements and boundaries. The mathematical proofs are in `linearized-degree.md`. They are repository derivations, with no novelty claim.

## Verified primary documents

1. Eli Ben-Sasson and Emanuele Viola, *Short PCPs with projection queries*, ECCC TR14-017, February 9, 2014. Official report PDF: <https://eccc.weizmann.ac.il/report/2014/017/download/>.
2. Claude Carlet, *Boolean Functions for Cryptography and Coding Theory*, author's hosted monograph: <https://www.math.univ-paris13.fr/~carlet/book-fcts-Bool-vect-crypt-codes.pdf>.

Both PDFs were reopened and the passages below were read directly. Page numbers are printed page numbers; Carlet's printed p63 is PDF index62.

## What BV14 actually provides

- **Lemma 1.6, pp4–5:** Cook–Levin turns the postprocessing circuit into a 3CNF; added proof cells store its gate-variable values at addresses (z,i). This controls size and query form, not the degree of each honest gate row.
- **Theorem 4.2, p10:** the constructed ACSP has public translated reads, polynomial-size arithmetic postprocessing, and honest A/B ordinary-degree bounds when satisfiable.
- **Definition 5.1/Lemma 5.2, pp13–14:** selectors are vanishing-polynomial quotients and have succinct arithmetic circuits for affine subspaces.
- **Equations (2)–(5), pp14–15; Claims 5.4–5.5, pp15–16:** the residual combines clause and Boolean-range constraints; its formal vanishing is equivalent to divisibility and to a Boolean satisfying assignment on H0.

These statements do not select a canonical evaluation order or promise low-degree Cook–Levin auxiliaries. They also do not say B can be chosen independently after A. Once A is fixed, its formal quotient is unique.

### The selector normalization discrepancy

Definition 5.1 uses the monic quotient Z_H/Z_U without a scaling factor. For U=a+V subset H=a+W, let J=Z_V(W). The quotient's value on U is the coefficient of Y in Z_J(Y), a nonzero constant b0, while it is zero on H\U. Claim 5.5's prose on p16 calls that value one. In general it is not one under the earlier definition.

This does not damage the zero-constraint argument: on the selected affine slice there is one nonzero scalar multiplying the relevant clause/range polynomial. Our proof explicitly uses b0 times the indicator; it does not silently replace the source definition. Scaling by b0^(-1) would normalize the selector if desired.

The range-selector term in equation (4) uses a translate of H0, of codimension one in H. It must not be confused with the clause selectors' translates of H1. The paragraph immediately preceding (4) has a corresponding H1/H0 inconsistency; the displayed equation and range-check proof specify the intended set.

## Binary-degree source

Carlet, Section2.2, printed pp62–63, especially **Proposition6 and its proof on p63**, identifies vectorial Boolean degree with the maximum binary exponent weight in the canonical degree-less-than-|F| univariate representative. The following paragraph characterizes GF(2)-linear and affine maps by linearized polynomials and linearized polynomials plus a constant. These are standard algebraic facts, not a novelty claim for this project.

This is the exact source fact required to turn the root's formal monomial-division filtration into a statement about Boolean degree. If a formal numerator has degree at least |F|, its function may have a lower-degree canonical representative, and the degree argument needs to be redone after reduction. The stated 3S<|F| margin prevents that problem for the honest residual calculation.

## Deductions now available, with their hypotheses

The accompanying note proves:

1. An affine selector for U subset H has exact vectorial Boolean degree dim(H)−dim(U). A Frobenius-based circuit also bounds the intermediate gate rows by that codimension, apart from the degree-one public-input operations.
2. The unique degree-less-than-|U| interpolant of a function on an affine U preserves its exact Boolean vectorial degree. For a Boolean source assignment, this connects the canonical A root to the actual assignment's ANF degree.
3. For monic affine-linearized L of ordinary degree S, the lead's chi filtration bounds long division. When Q=L B and deg_uni Q<3S<|F|, it yields deg_2 B<=deg_2 Q.
4. With the BV honest cutoff deg_uni A<=S/2, c equal to the largest clause-selector codimension, and r_A=deg_2 A, the quotient has degree at most D0=max(c+3r_A,1+r_A). One public Boolean implementation of the outer residual has all honest gate rows of degree at most D0+1.

These are exact statements. They do not prove that a hard source instance has an easy satisfying assignment, or that a near-correct assignment extends to a near-correct full proof. The one-site Lagrange example in the mathematical note shows why approximation stability is a separate obligation.

## Boundaries kept explicit

The three-witness companion fixture has a two-site Boolean assignment relation and an F-affine A cutoff. A nonconstant F-affine map takes Boolean values at at most two field points. The fixture therefore cannot be scaled into the growing BV assignment relation by merely enlarging its field. Its full-acceptance classification and easy raw rows are valid within its stated designed residual.

The constructive gate bound concerns the outer residual. It does not settle the Boolean degree of recursive proximity-test coefficients, seed-dependent bases, interpolation reciprocals, or their gate encodings. A small field circuit may still have high-degree coordinate functions. Fixed-node expansion lemmas require that their relevant linearized q and affine parameterizations remain fixed as the seed varies; that issue is being audited separately.

No 221 field rejection count is used as a Boolean clause gap. No new numerical alpha, hierarchy separation, or low-degree completeness theorem is extracted here.
