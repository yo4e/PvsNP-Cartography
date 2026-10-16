# Nightly research log: 2026-10-16 JST, approved session

Research lead: 月野テンプレクス. Start main a5315840b06d4bad7d016d10ebf8b93a6d775639. Read all mandated docs, open Issues #8/#9, previous code and last conclusion.

1. OBSERVE/ORIENT. n=8 degree interface and Hamming-layer identity were complete; open #9 selects n=9. The previous suggested n=8 coordinate lift fails at n=9 all-one input. Choose a new witness rather than restating the old theorem.
2. ACT. Exploratory 17578 quadratic masks, 8618 distinct layer profiles; ten-constraint LP numerical maximin 0.710377949..., four positive rows. Attack each chosen row rather than trusting the optimizer. A single row (1,127,36505001791) has exact layer success >=85/126, so discard the unnecessary LP mixture.
3. VERIFY. Pure-Python standard-library audit checks all512 Boolean inputs, three representations of the seed, all1024 affine masks, integer Walsh dual and independent hypergeometric formula. Exact upper85/126; exact affine bound322/504=23/36. Normal and -O agree.
4. ATTACK/REPAIR. Raw seed alone fails at one weight-one input. Full coordinate permutations give a valid input-independent distribution. Recognize 4/3/2 block invariance and independently expand1260 partition coefficient rows; all645120 polynomial/input evaluations agree. Literal all362880 permutations at ten layer representatives also match.
5. ATTACK. Exhaust one-orbit coefficients invariant within one, two or three nonempty coordinate blocks: 7432 patterns, only (4,3,2)/mask727 succeeds. Archive 7431 failed patterns with narrow scope, no global impossibility.
6. FORMALIZE. New Mod3NineDegree.lean connects concrete bounds to existing arbitrary-arity layer bridge and degree predicate. Commit480fa2df compiles the n9 module but its full run38908015191 fails an audit syntax rule: import after declarations. Fix **only** the audit import location in commit80712411.
7. VERIFY. Run38908696378/job116998734457 passes --wfail 9041-job build, namespace audit356 and14 printed n9 targets under foundational allowlist. Re-fetch audited source, commit and actual logs. Separate deterministic checker/scan code a529afed passes run38909099839/job117000104346, Python normal and optimized.
8. RECORD. Save expedition orientation/barrier/statement/conclusion, actual axiom evidence, claim status, concrete graveyard countermodels, README/assumption ledger and open-Issue frontier. Update #9's completion only after re-fetching recorded results.
9. CONTINUE. n=10 restricted <=3-block one-orbit scan (14 size partitions,8520 coefficient patterns) finds no qualifying single orbit; best minimum62/105 for (4,3,3). This rules out only the stated restricted one-orbit models. Fresh mixtures, four-block seeds and universal duals remain possible.

No independent human semantic review, second kernel, new general-n bound, P-vs-NP proof or novelty claim. See Expedition011 conclusion and scoped negative evidence.
