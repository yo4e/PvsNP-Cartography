import PvsNPCartography.Definitions

namespace PvsNPCartography

universe u v w

theorem reducesVia_id {α : Type u} (A : Language α) :
    ReducesVia A A id := by
  intro x
  rfl

theorem reducesVia_comp
    {α : Type u} {β : Type v} {γ : Type w}
    (A : Language α) (B : Language β) (C : Language γ)
    (f : α → β) (g : β → γ)
    (hAB : ReducesVia A B f) (hBC : ReducesVia B C g) :
    ReducesVia A C (g ∘ f) := by
  intro x
  exact (hAB x).trans (hBC (f x))

theorem disagreementCount_self
    {α : Type u} [Fintype α] (f : α → Bool) :
    disagreementCount f f = 0 := by
  simp [disagreementCount]

theorem disagreementCount_eq_zero_of_pointwise
    {α : Type u} [Fintype α] {f g : α → Bool}
    (h : ∀ x, f x = g x) :
    disagreementCount f g = 0 := by
  simp [disagreementCount, h]

end PvsNPCartography
