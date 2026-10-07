# Graveyard

This directory is intentionally first-class.

Every seductive but failed route should leave a readable post-mortem.

## The Lean cemetery

Some ideas do not die in prose.

They die when a proof assistant quietly refuses to accept the step that everyone wanted to call “obvious.”

Those belong here too.

A failed Lean formalization is not wasted work. It can expose:

- a hidden assumption
- a quantifier error
- a weakened theorem statement
- an accidental circularity
- an imported axiom doing the real work
- a claim that is true only in a smaller form

So this repository keeps a **Lean cemetery** for proof attempts that fail under formalization.

The point is not to collect corpses for decoration. The point is to remember exactly where and why an argument stopped being mathematics.

A grave marker should answer:

1. What was the claim?
2. Why did it look promising?
3. What killed it?
4. Was the failure logical, computational, literature-based, barrier-based, or formalization-based?
5. Is any smaller lemma salvageable?
6. How do we stop a future agent from rediscovering the same mistake?

A good grave is reusable knowledge.
