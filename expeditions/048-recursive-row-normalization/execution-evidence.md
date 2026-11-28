# Execution evidence — Expedition 048

Source base: `ba1da266a3e51f4025b7ba4f00d305b94796cbff`.
Session: November 28, 2026 JST. All new programs use only the Python standard
library. The local runtime reports Python 3.12.14. Checks use explicit runtime
conditions and remain active under `python -O`.

## Local acceptance

Run from this directory:

```sh
python check_recursive_normalization.py
python -O check_recursive_normalization.py
python check_recursive_field_bridge.py
python -O check_recursive_field_bridge.py
python check_row_sandwich.py
python -O check_row_sandwich.py
python check_layout_degree.py
python -O check_layout_degree.py
```

All eight executions exited zero, produced valid JSON and no stderr, and
matched their corresponding stored result file byte for byte. The full
machine-readable record is [local-execution.json](local-execution.json),
including exact imported dependency hashes and actual timing. The field
bridge deliberately reuses the field arithmetic/interpolation implementation
from Expedition 041; this reuse is not independent theorem reconstruction.

| Program | Source SHA-256 | Stored result SHA-256 |
|---|---|---|
| `check_recursive_normalization.py` | `d17010deb64c9674f0cbb39b929d7d14e39dbde05beaa2282fe55cb310d4bd70` | `ff9c20e044be97f12a90d43f1e4e45cc54ea98d0f00cfed7709eeb1de0f21fc8` |
| `check_recursive_field_bridge.py` | `51f35db2936b2ebf7ac980de71f5c2600fb6161316609db9c6d1b35b197bdc12` | `d5d0d53548934fc53040b1be2a22c7babfaecf5bdd2dfb3bb1742f68f35e175b` |
| `check_row_sandwich.py` | `66540be5ddebc393b6a70f809591d653f71db5fa6680572468fdcf446c6a4cea` | `ccd5d36fea8ffadc0b360e298aece949ac56362d0d243b3fe2a4e1fa72618cd9` |
| `check_layout_degree.py` | `4322e950a91a92b8f9858ea460e2d6584289e30790ba6eedd97d1a6f78a0e3fc` | `195cad5f54970cf6a75ac527fdf599a507b2474f74dd7784fb7e7021d5a50f76` |

## Acceptance scope

The programs check address identities, exact finite-field fixtures, exact
Boolean normal forms, finite polynomial spaces and explicit parity controls.
The written arbitrary-size coordinate and selector arguments are separate
from these finite scans. The conditional hierarchy statement still depends
on the full source compiler and external hierarchy/counting theorems.

The lead inspected every new source and the branch notes. The same-model
branches exchanged findings and performed targeted adversarial reads. This
does not constitute independent external review or close Issues #8/#15.
No Lean executable is present in this runtime; no new Lean, GitHub Actions,
second-kernel or mathematical novelty acceptance is reported.

## Immutable GitHub persistence and replay

Implementation commit:
[`bbbc7cf9f7d1b3ce389a9af276b72f1e27be4183`](https://github.com/yo4e/PvsNP-Cartography/commit/bbbc7cf9f7d1b3ce389a9af276b72f1e27be4183).
Tree: `1170137659bb8819613d1fa1308e785b77cadc66`.
Parent: `ba1da266a3e51f4025b7ba4f00d305b94796cbff`.

The main ref update succeeded without force. The commit, tree and parent were
then fetched from GitHub. All **20 implementation files** were fetched again
at the immutable commit and matched their local contents. A separate
`git fetch origin main` retrieved the Git objects; every changed blob's bytes
and Git object hash matched the API comparison.

An archive of that fetched commit was extracted to a separate directory.
All four programs ran there, in normal Python and `-O`: **eight additional
completed executions**, all exit zero, no stderr, valid JSON, and exact
byte equality with the committed result files. Their actual imported source
hashes matched the local acceptance inputs. The full readback and execution
records are in [remote-readback.json](remote-readback.json).

These are executions from remotely retrieved immutable source in the same
runtime, not a second machine or proof kernel. No new program changes were
made after that replay; the following documentation checkpoint records it.

## Issue disposition

[Issue #37](https://github.com/yo4e/PvsNP-Cartography/issues/37) was closed as
completed after the immutable replay, with
[comment 7235089254](https://github.com/yo4e/PvsNP-Cartography/issues/37#issuecomment-7235089254).
[Issue #38](https://github.com/yo4e/PvsNP-Cartography/issues/38) records the
accepting seed-function frontier. Issues #8 and #15 are unchanged. No write
blocker or unapplied patch remains. Future research still needs fresh approval.
