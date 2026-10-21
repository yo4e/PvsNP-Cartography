# Actual bounded exact verification, 2026-10-21 JST

Code da8538d3d04ac64d228987c060563602fd609784,
tree8305336c1ae9d8436c205709c2cf0f9b42160808.
Completed SUCCESS run39546665458/job119046262844:
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39546665458
The actual completed status and full job log were fetched and inspected.
CPython3.12.15. Both normal and optimized Python executed. Their output files
agree byte-for-byte; parsed actual output equals committed result.json.

Actual attributed excerpt:
```
2026-10-21T04:55:22.9666976Z   "all_subset_pairs": 1398101,
2026-10-21T04:55:22.9669291Z   "fiber_input_cases": 8191,
2026-10-21T04:55:22.9701522Z   "intersection_histogram_cells": 251902,
2026-10-21T04:55:22.9702426Z     "drop_sixfold_fiber_mass": "7/12",
2026-10-21T04:55:22.9702965Z     "extend_normalization_to_n2": "1/2",
2026-10-21T04:55:22.9708184Z   "ordered_triple_samples": 6084,
2026-10-21T04:55:22.9708637Z   "signed_expectation_tests": 30,
2026-10-21T04:55:24.1846261Z Bounded fiber/intersection audits match saved output; no generic Lean claim.
```

Re-fetched verifier blob50c2a48b7d3a4c4d4e2273be347ed146fbf6673e;
result blobdb03a8d0116068b24ef53fe359149f63e78160d4. The workflow-run record
also identifies the exact code commit and tree above. Local normal/-O runs
agreed independently before the commit. This is replication across execution
environments, not independent human review or a second proof kernel.

Scope: all fibers for n0..12; actual probability normalization/pointwise masses
for n3..12; three signed/nonsymmetric expectation functions at each such n;
all subset pairs for n0..10 with histogram cells w,r up to n+1. Repeated triples
are excluded from positive mass. The total guarded intersection formula is
checked on impossible as well as possible cells. These are bounded tests,
not a generic proof; separate Lean execution is required for formal promotion.
