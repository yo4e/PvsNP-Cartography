import PvsNPCartography.HammingLayers

open scoped BigOperators

namespace PvsNPCartography.HammingIntersections

open Symmetrization

noncomputable section

abbrev Slice {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :=
  {X : Finset (Fin n) // X.card = w ∧ (X ∩ A).card = r}

private theorem union_inter {n : ℕ} {A Y Z : Finset (Fin n)}
    (hy : Y ⊆ A) (hz : Z ⊆ Finset.univ \ A) : (Y ∪ Z) ∩ A = Y := by
  ext a
  have hya : a ∈ Y → a ∈ A := fun h => hy h
  have hza : a ∈ Z → a ∉ A := fun h => (Finset.mem_sdiff.mp (hz h)).2
  simp only [Finset.mem_inter, Finset.mem_union]
  tauto

private theorem union_sdiff {n : ℕ} {A Y Z : Finset (Fin n)}
    (hy : Y ⊆ A) (hz : Z ⊆ Finset.univ \ A) : (Y ∪ Z) \ A = Z := by
  ext a
  have hya : a ∈ Y → a ∈ A := fun h => hy h
  have hza : a ∈ Z → a ∉ A := fun h => (Finset.mem_sdiff.mp (hz h)).2
  simp only [Finset.mem_sdiff, Finset.mem_union]
  tauto

/-- Split a subset into its parts inside and outside A; inverse is disjoint union.
The range guard prevents natural subtraction from inventing impossible choices. -/
def splitEquiv {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) (hr : r ≤ w) :
    Slice A w r ≃
      {Y : Finset (Fin n) // Y ∈ A.powersetCard r} ×
      {Z : Finset (Fin n) // Z ∈ (Finset.univ \ A).powersetCard (w-r)} where
  toFun X :=
    (⟨X.1 ∩ A, Finset.mem_powersetCard.mpr ⟨Finset.inter_subset_right, X.2.2⟩⟩,
     ⟨X.1 \ A, Finset.mem_powersetCard.mpr ⟨by
        intro a ha
        exact Finset.mem_sdiff.mpr ⟨Finset.mem_univ a, (Finset.mem_sdiff.mp ha).2⟩,
       by
        have h := Finset.card_sdiff_add_card_inter X.1 A
        have h1 := X.2.1
        have h2 := X.2.2
        omega⟩⟩)
  invFun YZ := by
    have hy := Finset.mem_powersetCard.mp YZ.1.2
    have hz := Finset.mem_powersetCard.mp YZ.2.2
    have hd : Disjoint YZ.1.1 YZ.2.1 := Finset.disjoint_left.mpr (by
      intro a ha hb
      exact (Finset.mem_sdiff.mp (hz.1 hb)).2 (hy.1 ha))
    refine ⟨YZ.1.1 ∪ YZ.2.1, ?_, ?_⟩
    · rw [Finset.card_union_of_disjoint hd,hy.2,hz.2]
      omega
    · rw [union_inter hy.1 hz.1]
      exact hy.2
  left_inv X := by
    apply Subtype.ext
    ext a
    simp only [Finset.mem_union,Finset.mem_inter,Finset.mem_sdiff]
    tauto
  right_inv YZ := by
    have hy := (Finset.mem_powersetCard.mp YZ.1.2).1
    have hz := (Finset.mem_powersetCard.mp YZ.2.2).1
    apply Prod.ext
    · apply Subtype.ext
      exact union_inter hy hz
    · apply Subtype.ext
      exact union_sdiff hy hz

/-- The standard choose-inside/choose-outside count, valid also for empty slices. -/
theorem intersection_card_of_le {n : ℕ} (A : Finset (Fin n)) (w r : ℕ)
    (hr : r ≤ w) :
    Fintype.card (Slice A w r) = A.card.choose r * (n-A.card).choose (w-r) := by
  have hc : (Finset.univ \ A).card = n - A.card := by
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ A)]
    simp
  have h := Fintype.card_congr (splitEquiv A w r hr)
  simpa only [Fintype.card_prod,Fintype.card_coe,Finset.card_powersetCard,hc] using h

/-- Guarded total formula: no assumption that r,w,k are in a feasible range. -/
theorem intersection_card {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :
    Fintype.card (Slice A w r) =
      if r ≤ w then A.card.choose r * (n-A.card).choose (w-r) else 0 := by
  classical
  by_cases hr : r ≤ w
  · rw [ite_eq_left hr]
    exact intersection_card_of_le A w r hr
  · rw [ite_eq_right hr]
    apply Fintype.card_eq_zero_iff.mpr
    refine ⟨fun X => ?_⟩
    have h := Finset.card_le_card (Finset.inter_subset_left : X.1 ∩ A ⊆ X.1)
    exact hr (by simpa only [X.2.1,X.2.2] using h)

/-- Exact correspondence to Boolean inputs, not just a renamed cardinal formula. -/
def booleanSliceEquiv {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :
    {x : BooleanCube n // hammingWeight x = w ∧ (ones x ∩ A).card = r} ≃ Slice A w r where
  toFun x := ⟨ones x.1, (ones_card x.1).trans x.2.1, x.2.2⟩
  invFun X := ⟨bits X.1, by rw [← ones_card,ones_bits]; exact X.2.1,
    by rw [ones_bits]; exact X.2.2⟩
  left_inv x := Subtype.ext (bits_ones x.1)
  right_inv X := Subtype.ext (ones_bits X.1)

theorem boolean_intersection_card {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :
    Fintype.card {x : BooleanCube n // hammingWeight x = w ∧ (ones x ∩ A).card = r} =
      if r ≤ w then A.card.choose r * (n-A.card).choose (w-r) else 0 := by
  rw [Fintype.card_congr (booleanSliceEquiv A w r)]
  exact intersection_card A w r

/-- Dropping r<=w is false: an empty input cannot intersect A in one point. -/
theorem unguarded_subtraction_counterexample :
    Fintype.card (Slice (Finset.univ : Finset (Fin 1)) 0 1) = 0 ∧
      (1 : ℕ).choose 1 * (1-1).choose (0-1) = 1 := by
  constructor
  · rw [intersection_card]
    norm_num
  · decide

end
end PvsNPCartography.HammingIntersections
