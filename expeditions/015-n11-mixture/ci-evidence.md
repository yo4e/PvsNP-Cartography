# Retrieved n11 finite CI evidence, 2026-10-17 JST

Code:81ca743a43b232b055de7849fa9a8782f913696c.
Tree:6929ca098bbb77b2a9cff2acbed9077929861686.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/39037985386
Job:117411565884, completed SUCCESS. Python:CPython3.12.15.

Retrieved the completed job status and full job log, then the actual certificate,
finite result and Git commit/tree. Normal and optimized `verify.py --full` outputs
agree byte-for-byte. Parsed actual JSON equals the committed result.

Actual attributed output excerpt:

```
2026-10-17T13:47:10.9976014Z     "affine_maximum": "69/110",
2026-10-17T13:47:10.9976505Z     "affine_rows": 4096,
2026-10-17T13:47:10.9997017Z     "expanded_denominator": 277200000,
2026-10-17T13:47:10.9997624Z     "expanded_indexed_polynomials": 4785,
2026-10-17T13:47:10.9998211Z     "expanded_minimum": "24044/34375",
2026-10-17T13:47:10.9998740Z     "inputs": 2048,
2026-10-17T13:47:11.0000309Z     "state": "exact finite evidence; n11 Lean not run",
2026-10-17T13:47:13.7678791Z Saved n11 finite result matches actual execution; no Lean n11 claim.
```

Seven mutated certificates were rejected:coefficient, layer, normalization,
field, target, quantifier and dual. Independent coefficient encodings, explicit
full pointwise expansion, Mobius degree tests, direct/Walsh/hypergeometric dual
checks are all in the committed standard-library verifier.

Re-fetched certificate Git blob683736b7d84c1b7dc38fce3eeefd65b2b04baa66.
Re-fetched finite-result Git bloba07a6db2d63ddffda09e1f36fe53f926dab8e7a2.

No Lean n11 execution occurred. The next formal interface is tracked in #11;
any unfinished earlier n10 gate in #10 retains priority. Human semantic review
is independently pending in #8. No novelty or all-n extrapolation is established.
