# 2026-11-05 — zeta build recovery and cost shortcuts

Research lead: 月野テンプレクス. These are failures of specific proof scripts or tempting inferences, not counterexamples to the repaired exact-count theorem. No novelty is claimed.

## A. The preceding source was not accepted

Source `4b9aa2bb2ddb64d73b423aca3652fb3fa1e43560`, tree `324af6d794b80c1251d9df047e3b9c14584bb228`, failed run41843984571/job126622587093. Full decoded output was retrieved. FoldedBlockCount built, but SubsetZeta failed; later theorem reports were skipped. Existing successful amplifier-only runs did not validate this newer connection.

At SubsetZeta line43, `rw [he, hd]` attempted to rewrite a proposition underneath a condition with a dependent Decidable argument and produced an invalid rewrite motive. At line102, `Finset.toFinset_toList` was an unknown constant.

Repair `51a86b10cb0f493b0c093aa81dba734400cb0118` changes only those tactics/names to `simp only [he, hd]` and `Finset.toList_toFinset`. No statement, input domain, degree bound, axiom allowlist or warning policy was weakened. Completed run42038613103/job127283180450 accepted the repaired whole project. See Expedition033 execution-evidence.md for immutable source and actual output excerpts.

## B. Dead inference: extensional recursion gives fast tabulation for free

Even assigning unit cost to an original coefficient lookup, a literal unshared recursive evaluator makes2^|S| leaf calls for one output S. Over all S it makes3^a calls. Written induction/binomial reasoning and an executable model at a0..12 agree. At a12 there are531441 leaf calls, versus24576 additions in the shared-table algorithm. Different operations must not be reported as a wall-clock speedup ratio. This does not benchmark Lean's compiler; the source specification is noncomputable.

Repair: use a stored table and the fresh-coordinate stage invariant. Prove/value-test the invariant separately from the production evaluator. Do not call the old exhaustive stage checker the fast implementation.

## C. Dead inference: coordinate duplication and head collisions are harmless

Repeating a coordinate doubles a contribution: input[1,0] becomes[1,1] once and[1,2] twice modulo4. The formal Nodup condition is substantive.

For the actual GF2 source P=x+y with one head and one tail variable, the canonical amplifier modulo4 is x+y+2xy. Proper coefficient aggregation returns exact counts[1,1]. Replacing aggregation with last-write-wins yields[1,3], exceeding a block's size. The source theorem uses a sum and has no such defect. `runtime_audit.py` retains both attacks.

## D. Dead inference: the final butterfly cost is the whole counting cost

For n8, P=sum(x_i), b6, the checked construction visits17608 product pairs and retains254 terms before producing only4 table cells with4 final zeta additions. Omitting construction would manufacture a speedup. Materializing sorted product records also uses space proportional to pair records, not merely surviving supports.

Repair: include input encoding, coefficient construction, sorting, arithmetic bit lengths, folding, table allocation and output aggregation. The written bound in cost-and-fidelity.md chooses a conservative b=floor(n/(100d)) in its nontrivial regime; the large b6 example is not selected there.

## Disposition

These shortcuts are rejected; the known modulus-counting method survives with explicit qualifications. Finite tests are controls, not general proofs. The repaired Lean count identity is accepted at the cited source, whereas the new Python refinement and asymptotic bit-cost argument remain outside its formal scope. No new unrestricted circuit lower bound or P-versus-NP result follows.
