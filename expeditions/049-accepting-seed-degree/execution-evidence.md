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

## Immutable implementation readback and replay

The implementation commit is
[`6835b3af0765a72fa0d90e8db0a4288e88221c3a`](https://github.com/yo4e/PvsNP-Cartography/commit/6835b3af0765a72fa0d90e8db0a4288e88221c3a),
with tree `48d4d58658a1914855b1ac98c980776e49adca3c` and parent
`2a546c3781d71cd159b388997bd5312a7ceb78e6`. The branch update used that
expected parent and did not force the ref.

All 21 implementation files were fetched again at that exact commit through
the GitHub file API and compared with their intended UTF-8 content. A Git
fetch then supplied the actual objects: every blob's raw bytes matched the
local file and every computed Git blob SHA matched the API's blob SHA. The
commit parent and tree were also checked.

An archive extracted from that immutable commit was run outside the working
repository. All four suites again passed ordinary and optimized Python,
with empty stderr and byte-for-byte equality to the stored JSON results:

| Program | Immutable ordinary / optimized seconds |
| --- | --- |
| `check_linearized_degree.py` | 0.541388 / 0.623939 |
| `check_accepting_family.py` | 1.768475 / 1.889319 |
| `check_auxiliary_artifacts.py` | 0.201353 / 0.420833 |
| `check_honest_extension_degree.py` | 6.002974 / 6.022229 |

This gives 16 successful recorded executions across the local and immutable
phases. [remote-readback.json](remote-readback.json) records the API checks,
Git blob/byte/SHA-256 checks, exact snapshot path, dependency hashes and all
eight immutable execution records. This documentation commit changes no
program or saved mathematical result from the implementation commit.

[Issue #38](https://github.com/yo4e/PvsNP-Cartography/issues/38) was closed as
a completed scoped milestone, with
[completion comment](https://github.com/yo4e/PvsNP-Cartography/issues/38#issuecomment-7240201619).
[Issue #39](https://github.com/yo4e/PvsNP-Cartography/issues/39) records the
next structural task. Their saved state and the final documentation commit
are re-fetched before the session's completion report.

## Mathematical evidence boundary

The mathematical lemmas have written proofs and internal adversarial review.
Finite results are not used as a replacement for those proofs. There is no
new Lean run, CI result, independent external acceptance or novelty claim.
