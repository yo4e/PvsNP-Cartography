# Execution evidence — Expedition 049

## Local verification completed before the implementation commit

All four archived programs ran in ordinary Python and with `python3 -O`.
All eight processes exited zero, emitted valid JSON, had empty stderr, and
matched their saved result bytes. Checks use explicit `require` functions;
the `-O` execution does not remove them. Exact commands, elapsed times,
source hashes, result hashes and interpreter details are in
[local-execution.json](local-execution.json).

| Program | Ordinary / optimized seconds | Saved result SHA-256 |
| --- | --- | --- |
| `check_linearized_degree.py` | 0.574335 / 0.639525 | `8a5fc028580afddb72aa11b964a3f1a7208a4f5bfe4b5fab8d011c1be3bc7f4b` |
| `check_accepting_family.py` | 1.787546 / 1.904130 | `a887c0c2a5d22129f79bd80e2503d4e775b5dd7572f06a99dd1aeb43d568d742` |
| `check_auxiliary_artifacts.py` | 0.290007 / 0.389038 | `50827e3dab56f52ecf2c03d31d009214b69171e6a51599c30efd5e9b4e22e4dc` |
| `check_honest_extension_degree.py` | 5.723075 / 5.624831 | `9c00734dd161c97b11fc5732039d72e49ea8be878c2e3f04bb50392eaa657b84` |

Run each program without arguments from this directory. The field-family
and extension programs accept an optional `--repo-root`; their default is
the repository containing the script. The linearized program optionally
accepts `--output`, otherwise it prints the same JSON.

The linearized and signed-clause controls implement their own arithmetic or
Boolean objectives. The actual field-family and extension programs explicitly
reuse the predecessor field arithmetic, interpolation, leaf tests and address
normalization. This is not an independent full source-verifier implementation.

## Evidence boundary at this commit

This initial implementation record contains completed local runs. The
immutable GitHub file readback and execution replay require this commit's
identifier and are recorded by the following verification commit. They are
not asserted as already complete in this initial version.

The mathematical lemmas have written proofs and internal adversarial review.
Finite results are not used as a replacement for those proofs. There is no
new Lean run, CI result, independent external acceptance or novelty claim.
