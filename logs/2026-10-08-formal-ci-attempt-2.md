# 2026-10-08 — Formal CI attempt 2

Issue: #3

Workflow run:

https://github.com/yo4e/PvsNP-Cartography/actions/runs/37696114311

Commit:

`3d7179f6af65c5e9be48f88e336f5b02bea37432`

## Result

**Failed before the intended `lake update` step.**

The pinned toolchain again installed successfully, but the first `leanprover/lean-action@v1` invocation failed during its own configuration phase with:

```text
No lake-manifest.json found. Run lake update to generate manifest
```

This happened even with:

```yaml
auto-config: false
build: false
test: false
lint: false
```

So `lean-action` cannot be used as the manifest-bootstrap installer in this configuration.

No Lean project source was compiled and no axiom audit ran.

## Repair

Attempt 3 removes `lean-action` from the bootstrap phase.

The workflow now:

1. installs Elan directly from the official Lean Elan installer;
2. lets the checked-in `formal/lean-toolchain` select/download the pinned Lean release;
3. runs `lake update` to create the dependency manifest;
4. only then invokes `lean-action` for build/cache/axiom auditing.

If this reaches the build, any next failure will finally be evidence about Lake configuration, source elaboration, or the axiom-audit layer rather than the missing-manifest bootstrap cycle.
