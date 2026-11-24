# Execution evidence

Session: fresh November 24 JST nightly approval, continued after midnight
November 25. Base: ce66bdc08702922138dc77b93c6c2b4054873944.

## Completed local execution

Python 3.12.14, Clang 22.1.3, in the current Linux runtime. The full runtime
string, exact commands, source SHA-256, elapsed times and output SHA-256 are
in [local-execution.json](local-execution.json). All checks use explicit
exceptions, so optimization does not disable them.

Each of these was executed once normally and once with `python3 -O` by the
integrating research lead. Exit codes were zero, stderr empty, and output
byte-for-byte equal to the corresponding stored JSON:

| Script | Result | Output SHA-256 |
|---|---|---|
| check_public_dictionary.py | public-dictionary-results.json | b752eae1161d32c92b5af233b07031c806221e68f65cad8b74fbaa27a3664deb |
| check_scoped_rs.py | scoped-rs-results.json | f93a8858a73513641e83194fb88c71b55598ddfbc3bcb6438bf9c7d9d75b7c12 |
| check_guessed_layout.py | guessed-layout-results.json | 2aeecae66d28f97ad11d3bcd34d149c3af38a1c6e57f14ae6d1d8166b9adbdac |

The standalone programs use only the Python standard library. The preceding
expedition's implementation is unchanged. No new GitHub Actions or Lean run
is asserted; these records report actual local execution.

## Review scope

Three bounded same-model branches supplied mathematics, exact controls and
source reading. The lead inspected their files and supplied a separate
guessed-layout enumeration. A subsequent bounded semantic attack found no
substantive defect in the finite public-layout degree and sensitivity
arguments or the shared-map decoder. This is not the independent human or
AI gate of Issues 8 and 15, not a second proof kernel, and not novelty review.

## Remote persistence

At the implementation commit this section contains only the completed local
facts above. The following record commit will name the actual accepted
implementation commit and archive the immutable GitHub file/hash comparison.
No remote persistence or replay is claimed before that comparison succeeds.
