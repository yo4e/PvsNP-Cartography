# 2026-10-08 — Formal CI attempt 1

Issue: #3

Workflow run:

https://github.com/yo4e/PvsNP-Cartography/actions/runs/37695424966

Commit:

`26b3e1c032e03ab2d83b7ffdbc50ca530c7f3a55`

## Result

**Failed before compiling Lean source.**

The pinned Lean toolchain installed successfully:

- Lean `v4.35.0-rc4`
- Lake `5.0.0-src+c29b6dd`

The action then stopped during automatic configuration with:

```text
No lake-manifest.json found. Run lake update to generate manifest
```

Therefore this run says nothing about whether the definitions or sanity lemmas compile.

## Repair

The workflow is changed to bootstrap the dependency manifest explicitly:

1. install the pinned Lean toolchain with `auto-config: false`;
2. run `lake update` in `formal/`;
3. print the generated manifest for capture;
4. run a second explicit build + axiom-audit action.

If the next run succeeds, the generated `lake-manifest.json` should be committed so later CI can use the ordinary single-stage path.

## Research lesson

Infrastructure failure is not theorem failure, but it still belongs in the record.

Do not collapse “CI red” into “math false,” and do not collapse “toolchain installed” into “formal proof verified.”
