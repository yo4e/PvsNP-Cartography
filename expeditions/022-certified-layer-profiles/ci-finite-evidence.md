# Retrieved exact finite profile evidence

Code d65bfec70538c4b53e6ff2ab741c61da131345d3;
tree0eadd81ea9dd458e65900830f5d8b22609d3b061.
Completed SUCCESS run39614264276/job119270959043, CPython3.12.15.
https://github.com/yo4e/PvsNP-Cartography/actions/runs/39614264276

Full actual job log was fetched. Normal and optimized Python outputs match
byte-for-byte. Parsed actual JSON equals committed result.json. Actual excerpt:

2026-10-21T14:08:54.1379542Z   "elementary_integer_cases_n0_to6": 41870,
2026-10-21T14:08:54.1380040Z   "mobius_degree_checks": 1022,
2026-10-21T14:08:54.1380458Z   "n11_canonical_input_comparisons": 4096,
2026-10-21T14:08:54.1385276Z   "n11_minimum": "158/231",
2026-10-21T14:08:54.1402486Z   "q_r_input_evaluations": 174762,
2026-10-21T14:08:54.1402930Z   "single_coefficient_mutation_witnesses": 134,
2026-10-21T14:08:54.1404082Z   "weighted_layer_cases": 4608
2026-10-21T14:08:54.1794932Z Exact profile checks match saved output; generic Lean acceptance is separate.

Re-fetched verifier Git blob65ba8c57284dfd1fb25309e24de85aaca4b05e52 and result
blob1ae9be5ed0f6a248a178cd83d42afe8cea7947c1, then the actual Git commit/tree.
The local6871-byte verifier reproduces the same Git blob exactly. Local normal
and -O result files agree; canonical compact JSON plus newline reproduces the
remote result blob. No local Lean execution is claimed.

Bounded scope: all A and x at n0..8, elementary integer counts at n0..6,
existing n11 seed regression, signed means, impossible layers and134 actual
single-coefficient mutations. This is independent implementation, not an
independent author or a generic proof. The separate naive-lift attack has its
own exact script and CI, not covered by this earlier run.
