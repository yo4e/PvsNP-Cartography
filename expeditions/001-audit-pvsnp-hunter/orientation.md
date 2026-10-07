# Expedition 001 — Audit p-vs-np-hunter finite-degree findings

Status: **active / preliminary discrepancy found**

Source project:

https://github.com/GISMO-1/p-vs-np-hunter

Target public findings:

https://github.com/GISMO-1/p-vs-np-hunter/blob/main/docs/FINDINGS.md

## Research question

What mathematical quantity is actually computed behind the repository's reported GF(2)/GF(3) “approximate polynomial degree” tables, and how closely does it match the natural-language interpretation in the findings?

## Why start here?

This project is one of the closest public precedents to PvsNP-Cartography:

- multi-agent
- circuit-lower-bound focus
- finite experiments
- Lean artifacts
- explicit barrier awareness

Auditing a serious-looking neighboring system gives us a calibration target for our own standards.

## Initial hypotheses

H1. The reported values are exact minimum 1/3-approximate degrees over GF(p).

H2. The reported values are heuristic/proxy values but are consistently labeled as such.

H3. Different function families are measured using different mathematical quantities under one common output label.

Current preliminary evidence favors **H3**.

## Success criteria

- identify exact code path
- reproduce selected outputs
- state each computed quantity precisely
- compare code semantics with public prose
- independently check small cases where feasible
- distinguish labeling problem from mathematical error
- propose a minimal reproducible correction
