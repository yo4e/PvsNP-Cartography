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

Implementation commit:
[7031fd2597f520933ddcfc0e86dd69dfad00fdfb](https://github.com/yo4e/PvsNP-Cartography/commit/7031fd2597f520933ddcfc0e86dd69dfad00fdfb),
tree `fadd7c562d7d946630d0456fb7e4b43e0bf71462`, parent
`ce66bdc08702922138dc77b93c6c2b4054873944`.

The connected GitHub API accepted the tree, commit and non-forced main
advance with the expected parent. The actual immutable commit was then
retrieved: its parent and tree matched. All **18** committed files were
separately re-fetched through GitHub's file API at this commit; every returned
text matched the prepared source exactly.

A fresh Git fetch independently obtained the commit objects. Every changed
file's actual Git object was compared byte for byte with the prepared file,
and its Git blob hash was recomputed. All matched. The files were extracted
into a fresh immutable snapshot, and all three suites were executed normally
and with `-O` from that snapshot. All six runs completed successfully, with
empty stderr and output identical to the re-fetched stored JSON.

[remote-readback.json](remote-readback.json) contains the full path/hash
manifest and actual replay outcomes. These are local executions of retrieved
GitHub source, not GitHub Actions or a different proof kernel. The later
record commit adds this evidence and the project checkpoint; it does not
change the tested programs or mathematical results.

Issue [36](https://github.com/yo4e/PvsNP-Cartography/issues/36) was closed as
completed after the successful readback; the actual completion comment is
[7135567206](https://github.com/yo4e/PvsNP-Cartography/issues/36#issuecomment-7135567206).
Issue [37](https://github.com/yo4e/PvsNP-Cartography/issues/37) was created for
the next source-level cost question. Issues 8 and 15 were not changed.
