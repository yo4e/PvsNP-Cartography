# Retrieved n10 exact semantic CI evidence

Code: baa1d976a45c4f74d10dcbb55f7195e7c0ae0744.
Run: https://github.com/yo4e/PvsNP-Cartography/actions/runs/39037298636
Job: 117409604280, completed SUCCESS.
Python: CPython3.12.15. Retrieved the completed job status and full job log.

Normal and `python -O` executions agree byte-for-byte; parsed actual JSON equals
expeditions/014-n10-formal/finite-result.json. Actual log excerpt:

```
2026-10-17T13:37:10.9895058Z   "lean_source_sha256": "bd998f8ad908a1622cac393dd3b68e62505f2bc01dd2ef9010b9cb7e5c948e93",
2026-10-17T13:37:10.9935317Z   "single_coefficient_mutations_detected": 448,
2026-10-17T13:37:10.9951822Z   "upper_minimum": "2123/3000"
2026-10-17T13:37:12.5942548Z Saved result matches actual execution; formal proof is audited separately.
```

All1024 canonical input evaluations and2048 affine rows were checked by the
committed independent methods. All11 layer sums match the actual Lean literals.
The n10 Lean source was separately re-fetched at d25c6cd777c7585d2765682baf34a94e38a9d6bc,
Git blob6840ecfdd7786b583a7cc089e17da8c2f34e30e0. This is a successful finite
semantic audit, not evidence that the formal compilation completed.
