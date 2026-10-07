import Mathlib

namespace PvsNPCartography

universe u v

/-- A language over an arbitrary carrier. This is only membership semantics. -/
abbrev Language (α : Type u) := α → Prop

/--
`ReducesVia A B f` says that `f` preserves and reflects membership.

This deliberately contains no computability or time bound. It is therefore
*not* yet a polynomial-time many-one reduction.
-/
def ReducesVia {α : Type u} {β : Type v}
    (A : Language α) (B : Language β) (f : α → β) : Prop :=
  ∀ x, A x ↔ B (f x)

/-- Boolean inputs of fixed length. -/
abbrev BitVec (n : Nat) := Fin n → Bool

/-- Boolean functions on fixed-length bit vectors. -/
abbrev BoolFn (n : Nat) := BitVec n → Bool

/--
Number of inputs on which two Boolean-valued functions disagree.

This is a finite counting primitive only. It is not an approximation-degree
definition and contains no error threshold.
-/
def disagreementCount {α : Type u} [Fintype α] (f g : α → Bool) : Nat :=
  (Finset.univ.filter fun x => f x ≠ g x).card

end PvsNPCartography
