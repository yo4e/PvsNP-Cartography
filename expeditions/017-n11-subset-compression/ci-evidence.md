# Actual n11 quotient replication, approved2026-10-18 session

Code8ff6df0ba8362966f2df76d90e5fbe3a84d8f2a5; treef2f8d384c101afb643d90cec781bb1a17efa5cc5.
Completed SUCCESS run39137936272/job117706176557. Full completed log fetched and
inspected. CPython3.12.15, normal and optimized(-O) executions identical;
parsed actual JSON equals the checked-in result. Four negative controls pass.

Actual attributed output:
2026-10-18T14:52:30.0226421Z   "distinct_support": 496,
2026-10-18T14:52:30.0250394Z   "independent_formula_evaluations": 1013760,
2026-10-18T14:52:30.0256166Z   "uniformized_minimum": "281/496",
2026-10-18T14:52:30.0260036Z   "upper_minimum": "158/231"
2026-10-18T14:52:32.3837836Z Exact 496-row measure, full pointwise checks and negative controls PASS.

Actual source, result and commit/tree re-fetched after completion:
verifier Git blob90bb099e9e28f4ee1f86f59e53c19754b4e27b80;
result Git blob4837ef2252c90e973a0056bca543c5e01000eb85.
Source three-orbit certificate is unchanged, blob2fed5a9a274f358deedf59879f4ba1160eb3214f.

The generated496-row table is an Actions artifact, not a checked-in support file:
artifact12140137583 (n11-support496),4130-byte zip, SHA256
7ae26fa3bc6ef4d1f07289290f03d266ddf4828aae163f0c4bd780bcb1f37ec8.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39137936272/artifacts/12140137583
It can be regenerated from the committed verifier. The canonical uncompressed
support hash isaa05128f4d4005cd4911bbed1d2aa833989a4b09e136662f7684b86d1a1b0c64,
excluding the terminal newline. All2048 point-score hashesc61fa759df7e946f9720b91acf76a9c941b88dd76b428f9fb4c07881151e2ce2.

This verifies exact finite equality of probability measures and pointwise
scores. It does not supply n11 Lean acceptance, independent human semantic
review, mathematical novelty or global support minimality. Issue#11 updated
with this evidence and the unchanged remaining formal gate.
