# Night session — 2026-10-08 (JST)

Research lead: 月野テンプレクス. Approval: explicitly granted for this
one nightly session. No continuing authorization assumed.

## Observe

Open issues: #6 (MOD3 exact certificates), #3 (Lean scaffold).
Read AGENTS.md, all five mandatory documents, recent commits, expedition 002,
and the failing formal workflow logs.

## Act, verify, and attack

- Independently implemented the standard-library rational checker at
  `expeditions/002-exact-probabilistic-degree-mod3/verify_certificates.py`.
  It exhausts 64, 128, 256 affine polynomials respectively for n=5,6,7,
  verifies all per-layer quadratic good counts against the published tables,
  checks exact probability arithmetic, and optionally enumerates all n!
  permutations at every Boolean input.
- The full `--permutation-audit` passed locally and in GitHub Actions
  [run 37789085813](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789085813)
  (Python 3.12.3; conclusion: success). A deliberately flipped n=5 constant
  bit is rejected (pointwise minimum zero).
- The on-GitHub checker blob matched the locally executed file bit-for-bit
  (Git blob SHA `d7c9d234d9c5a00d223a005fc33c1aa313c9ddaa`).
- Formal CI [run 37696584897](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37696584897)
  exposed a **module-style warning** under `--wfail`, not a false theorem
  or a kernel failure. Added explicit Lake legacy-module compatibility
  `allowNonModules = true` without relaxing `--wfail`.
- Pinned Lean build, namespace assumption audit, and explicit target axiom
  printing then passed in [run 37789136586](https://github.com/yo4e/PvsNP-Cartography/actions/runs/37789136586).
  Four target lemmas had either no axioms or only
  `propext`, `Classical.choice`, `Quot.sound`. See formal/ASSUMPTIONS.md.

## Commit evidence

- `04f74d699863df1777a9895b3dd78820c8f9e1e5` — checker
- `39631715c994de31f1698608a70e352dff1897a4` — exact-certificate CI
- `146ea42f862a8c5539faa5f5fb5e429a81ece78e` — Lean compatibility repair

The paired CI successes are independent of the repository's prior claimed
local execution. No general complexity lower bound or novelty claim follows.

## Boundary and next frontier

Expedition 002 is a **verified finite certificate workflow**, not a Lean
formalization. The four Lean sanity lemmas are compiled and axiom-audited,
but they do not express the MOD3 result. Later work should faithfully
formalize the finite certificate statement or study n=8 with explicit
distinction between optimizer discovery, exhaustive verification, and
general proof barriers.
