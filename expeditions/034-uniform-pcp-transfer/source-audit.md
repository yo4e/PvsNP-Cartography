# Primary-source and scope audit

2026-11-08 JST. Author: 月野テンプレクス. Sources are imported mathematical dependencies, not independently re-proved results. This audit is not a claim that the entire external papers were formally verified.

## Target route

Emanuele Viola, *New lower bounds for probabilistic degree and AC0 with parity gates*, ECCC TR20-015 revision5, January12,2021. https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . Read Definition1, Theorem3 and Sections2.1–2.3. Relevant PDF images at zero-indexed pages12–15 were inspected; the initial page11 screenshot failed. The pinned revision, not an unread journal revision, supplies the comparison. Do not describe its historical bound as a latest result.

Its proof uses a canonical proof-bit function in E^NP, a bounded polynomial guessed nondeterministically, and deterministic counting. The oracle is not part of the final faster nondeterministic decision procedure. There is a local notation inconsistency on printed page14: the averaging sentence labels a polynomial with d, while amplification immediately before and the subsequent guess use d-prime. Our reconstruction consistently uses the amplified degree D. This is a source-reading qualification, NOT evidence that the known result is false.

The same page's comment about using the same sample concerns the completeness calculation. It is not a license to replace a globally fixed proof by inconsistent per-occurrence answers in the soundness test. Our concrete1/2 versus7/8 example attacks that false extrapolation.

## Projection PCP dependency

Eli Ben-Sasson and Emanuele Viola, *Short PCPs with projection queries*, ECCC TR14-017, February9,2014, Theorem1.1, printed page2. https://eccc.weizmann.ac.il/report/2014/017/download/ . Both parsed theorem text and page image were inspected. The author-hosted April22,2014 version was also retrieved in text, but this reconstruction pins the February ECCC statement.

The required parts are uniform poly(n,log T) construction, quasilinear proof length, perfect completeness, bounded whole-verifier soundness, projection coordinates allowing negation/constants, and a polynomial-size3CNF decision predicate. Our clause-averaging gap is derived separately; it is not copied from the whole-verifier soundness number. The PCP's construction/proof is an external dependency, not a newly checked Lean module.

## Hierarchy dependency and access limit

J. I. Seiferas, M. J. Fischer, A. R. Meyer, *Separating Nondeterministic Time Complexity Classes*, JACM25(1),146–167,1978. Primary-paper scan retrieved at https://citeseerx.ist.psu.edu/document?doi=5a5339f901785db63330bc653ea76ea02b51d3fd&repid=rep1&type=pdf . Inspected the parsed time-model definitions, Theorem4 context and Corollary4.1 at printed page155. Screenshot retrieval failed; a later fresh request also returned403, while the cached parsed document remained readable. No visual verification of the scan or independent reconstruction of its proof is claimed.

Corollary4.1's binary language is sufficient. We use T2=2^n and the specific smaller clock ceil(2^n/n), with its shifted little-o condition made explicit. We do not need to claim a unary hierarchy witness. The cited Zak primary page was inaccessible. Williams' author PDF *Improving Exhaustive Search Implies Superpolynomial Lower Bounds*, https://www.cs.cmu.edu/~ryanw/improved-algs-lbs2.pdf , was consulted as a methodological cross-check, not a replacement for a newly proved hierarchy theorem.

## Local contribution and dependency boundary

The repository contribution here is an explicit conditional dependency map, encoding/description/search/cost accounting, elementary amplification calculation, exact implementation countercontrols, and a repaired validation path. `source-bridge.md` states the imported hypotheses before deriving the transfer. Formal exactness from Expedition033 is retained at its original source; the algorithmic runtime, PCP, hierarchy, single-proof transfer and Python refinement are not thereby Lean verified. There is no new independent semantic reviewer or second proof kernel.
