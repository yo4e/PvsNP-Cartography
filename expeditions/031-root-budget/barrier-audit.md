# Barrier audit: no escape inferred from a connected approximation proof

Author: 月野テンプレクス, freshly approved 2026-10-31 JST night.

The root-budget lemma reconstructs a known algebraic approximation method for a
specified finite AND/OR/NOT/XOR circuit model over GF2. It does not establish a
new lower bound for unrestricted polynomial-size circuits. An arbitrary depth
may make its degree bound too large to combine usefully with the MOD3 obstruction.
Neither adding a Lean proof nor improving a constant changes that limitation.

Relativization: no oracle-robust simulation or separation has been proved. This
algebraic construction must not be labeled a nonrelativizing P-vs-NP argument
merely because it discusses polynomials.

Algebrization: no asymmetric oracle/polynomial-extension statement has been
checked against the Aaronson-Wigderson definition. Use of GF2 is not a barrier
escape criterion. The current result concerns the concrete unrelativized model.

Natural proofs: the current modules do not supply a truth-table property with
all of largeness, appropriate efficient constructivity and usefulness against
unrestricted P/poly. Razborov-Rudich TR94-010 was fetched from the official ECCC
source, https://eccc.weizmann.ac.il/report/1994/010/download/ . Section2's
printed page2 was visually inspected (PDF index2); a second screenshot request
failed. The definition measures efficient recognition in truth-table length2^n,
not the number n of variables. Its general-circuit limitation has a hardness
assumption. A counting argument alone is not that limitation or its escape.

Continuation: next-frontier.md separates a valid necessary Hamming-cover bound
from its FALSE converse and from an unproved efficient recognition algorithm.
The pointwise-versus-average distinction is essential. It identifies missing
implications rather than claiming them solved by finite experiments.

No new independent semantic review, second kernel, publication-level novelty,
optimal constants, unrestricted circuit separation or P-vs-NP conclusion is
claimed. #8 and #15 keep their earlier scopes. A later session needs new approval.
