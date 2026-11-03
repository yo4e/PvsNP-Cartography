# Orientation — integer modulus amplification and exact block counts

Research lead: 月野テンプレクス. Fresh approval in this conversation on 2026-11-03 JST; one session only. Starting checkpoint 80b32293476eb9b3a3366b3b246c0c44389e749f. This file is not authority for another session.

## Observe / choose

Read the current AGENTS and open Issues 8,15,25, mandatory protocol/barrier/prior-art/bibliography material, research direction and current status. The preceding full log and accepted execution record are available in this conversation at the unchanged starting checkpoint. Older dated README/direction targets do not restart closed issues. Issue25 is the earliest useful unblocked mathematical question; the old independent-review gates retain their scopes.

## Named target and fidelity

Construct F_s(Y)=sum_{j=s}^{2s-1} choose(2s-1,j)Y^j(1-Y)^(2s-1-j), for s>=1. Derive its actual degree and parity congruence for every integer Y, including negative Y. Connect a faithful integer coefficient lift of an actual GF2 polynomial to this amplifier, then recover exact numbers of accepting Boolean tail assignments modulo 2^(ell+1), without wraparound. A correct finite sum is not by itself a faster algorithm.

Preserve genuine polynomial degree, original Boolean evaluation, and the distinction between ordinary integers and the coefficient ring modulo a composite power of two. Do not import a field-only lemma into that ring. Examine squarefree reduction, monomial folding and subset-zeta evaluation as the next concrete connections, rather than creating an unrelated framework.

## Attack plan

Test s=1, negative integers, unreduced powers, signed coefficient lifts, zero/one polynomials, empty and full tail blocks, overlapping monomial supports, degree multiplication and the strict modulus-versus-count bound. The previously known modulus-2^ell wraparound failure remains a control, not a new discovery. Audit every formal endpoint for goal-as-hypothesis, placeholders and accidental input/degree restrictions. Keep written arguments, finite tests, kernel acceptance and independent semantic review separate.

## Source and operating boundary

Primary source: Emanuele Viola, ECCC TR20-015 revision5 (2021-01-12), Section2.2, Theorem12/Lemmas13-14, https://eccc.weizmann.ac.il/report/2020/015/revision/5/download/ . Retrieved and read the relevant parsed text this session. Both requested page screenshots failed with cache-miss errors; no visual inspection is claimed. The source attributes the amplifier to Yao/Beigel-Tarui and the transform to Yates. Known-method reconstruction; novelty is not claimed.

Local Lean/lake are absent and git ls-remote failed DNS. Use the existing connected GitHub/Actions execution path without changing paid resources or credentials. This meaningful orientation write tests write availability. Before reporting any accepted proof or persistence, retrieve actual files/commit and completed execution results. Any failure or partial bridge must remain accurately labeled. No general speedup, E^NP-to-NP substitution, unrestricted circuit lower bound or P-versus-NP conclusion is authorized by this local lemma.
