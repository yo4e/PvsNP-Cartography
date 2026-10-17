# Retrieved compact n11 CI evidence, 2026-10-17 JST

Code:402b13398af15add64961d4894b2a371beec3711.
Tree:cf2cceecd9926e393575c73b1d53ac7ab5e101da.
Run:https://github.com/yo4e/PvsNP-Cartography/actions/runs/39038647497
Job:117413471238, completed SUCCESS. Python:CPython3.12.15.

The actual completed job status and FULL log were fetched, not inferred from
an upload or queued run. Both `python compact-verify.py` and `python -O
compact-verify.py` completed; output files match byte-for-byte and parsed actual
JSON equals the committed compact-result.json.

Actual attributed output excerpt:

```
2026-10-17T13:56:52.4932481Z     "affine_maximum": "69/110",
2026-10-17T13:56:52.4932737Z     "affine_rows": 4096,
2026-10-17T13:56:52.4936850Z     "expanded_denominator": 27720,
2026-10-17T13:56:52.4937139Z     "expanded_indexed_polynomials": 1925,
2026-10-17T13:56:52.4937431Z     "expanded_minimum": "158/231",
2026-10-17T13:56:52.4937686Z     "inputs": 2048,
2026-10-17T13:56:52.4938428Z     "seed_orbits": 3,
2026-10-17T13:56:52.4938724Z     "state": "exact finite evidence; n11 Lean not run",
2026-10-17T13:56:52.4946881Z     "upper_margin": "4/231",
2026-10-17T13:56:53.7869170Z Three-orbit certificate matches actual exact execution; n11 Lean not run.
```

Seven altered certificates were rejected: coefficient, layer, normalization,
field, target, quantifier and dual. Canonical ANF/block evaluations, full
partition expansion at all2048 inputs, Mobius degree and exhaustive direct/
Walsh/hypergeometric affine dual checks run in the committed verifier.

After the actual log was inspected, the files and commit/tree were re-fetched:
compact-certificate.json Git blob2fed5a9a274f358deedf59879f4ba1160eb3214f;
compact-result.json Git blobad1f34fd3f814d11ad47a0052619f09db6dfc6d9.
The saved weights are [1,4,2]/7, not a numerical LP approximation.

This is exact finite reproducibility, not n11 Lean acceptance or independent
human review. Three seed orbits do not mean three unsymmetrized polynomials
suffice; full coordinate symmetrization is part of the fixed distribution.
