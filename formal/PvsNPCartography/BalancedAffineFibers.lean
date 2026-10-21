import PvsNPCartography.BalancedAffineInputMeasure
import PvsNPCartography.LayerCertificates

open scoped BigOperators

namespace PvsNPCartography.BalancedAffineCounting

open Symmetrization

noncomputable section

private theorem bits_eq_input {n : ℕ} (s : Finset (Fin n)) (x : BooleanCube n) :
    bits s = x ↔ s = ones x := by
  constructor
  · intro h
    simpa only [ones_bits] using congrArg ones h
  · intro h
    rw [h, bits_ones]

private theorem triple_support_card {n : ℕ} {i j k : Fin n}
    (hd : Distinct i j k) : ({i,j,k} : Finset (Fin n)).card = 3 := by
  rcases hd with ⟨hij,hik,hjk⟩
  simp [hij,hik,hjk]

/-- Exact singleton fiber on the actual Boolean encoding, at any arity. -/
theorem singleton_fiber_count {n : ℕ} (x : BooleanCube n) :
    (∑ i : Fin n, if bits {i} = x then (1 : ℝ) else 0) =
      if hammingWeight x = 1 then 1 else 0 := by
  classical
  simp_rw [bits_eq_input]
  by_cases hw : hammingWeight x = 1
  · have hc : (ones x).card = 1 := (ones_card x).trans hw
    obtain ⟨i, hi⟩ := Finset.card_eq_one.mp hc
    rw [if_pos hw]
    simp [hi]
  · rw [if_neg hw]
    apply Finset.sum_eq_zero
    intro i _
    have hn : ({i} : Finset (Fin n)) ≠ ones x := by
      intro h
      apply hw
      rw [← ones_card, ← h]
      simp
    exact if_neg hn

/-- Indicator-moment count of ordered distinct triples inside a finite set.
The full diagonal correction comes from the previously proved moment identity. -/
theorem triples_inside_count {n : ℕ} (s : Finset (Fin n)) :
    (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
      if Distinct i j k ∧ i ∈ s ∧ j ∈ s ∧ k ∈ s then (1 : ℝ) else 0) =
      (s.card : ℝ) * (s.card - 1) * (s.card - 2) := by
  classical
  let f : Fin n → ℝ := fun i => if i ∈ s then 1 else 0
  have hf : (∑ i, f i) = (s.card : ℝ) := by simp [f]
  have hf2 (i : Fin n) : f i ^ 2 = f i := by
    by_cases h : i ∈ s <;> simp [f,h]
  have hf3 (i : Fin n) : f i ^ 3 = f i := by
    by_cases h : i ∈ s <;> simp [f,h]
  have he (i j k : Fin n) :
      (if Distinct i j k ∧ i ∈ s ∧ j ∈ s ∧ k ∈ s then (1 : ℝ) else 0) =
        if Distinct i j k then f i * f j * f k else 0 := by
    by_cases hd : Distinct i j k <;> by_cases hi : i ∈ s <;>
      by_cases hj : j ∈ s <;> by_cases hk : k ∈ s <;> simp [hd,hi,hj,hk,f]
  simp_rw [he]
  rw [ordered_triple_moment]
  simp_rw [hf2,hf3]
  rw [hf]
  ring

/-- There are exactly six positive-mass ordered triple fibers at weight three.
Repeated coordinates are excluded, even when their support is a valid input. -/
theorem triple_fiber_count {n : ℕ} (x : BooleanCube n) :
    (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
      if Distinct i j k ∧ bits {i,j,k} = x then (1 : ℝ) else 0) =
      if hammingWeight x = 3 then 6 else 0 := by
  classical
  by_cases hw : hammingWeight x = 3
  · have hc : (ones x).card = 3 := (ones_card x).trans hw
    have he (i j k : Fin n) :
        (Distinct i j k ∧ bits {i,j,k} = x) ↔
          (Distinct i j k ∧ i ∈ ones x ∧ j ∈ ones x ∧ k ∈ ones x) := by
      rw [bits_eq_input]
      constructor
      · rintro ⟨hd,hs⟩
        refine ⟨hd, ?_⟩
        simp [← hs]
      · rintro ⟨hd,hi,hj,hk⟩
        refine ⟨hd, Finset.eq_of_subset_of_card_le ?_ ?_⟩
        · intro a ha
          simp only [Finset.mem_insert, Finset.mem_singleton] at ha
          rcases ha with rfl | rfl | rfl <;> assumption
        · rw [hc, triple_support_card hd]
    simp_rw [he]
    rw [triples_inside_count, hc, if_pos hw]
    norm_num
  · rw [if_neg hw]
    apply Finset.sum_eq_zero
    intro i _
    apply Finset.sum_eq_zero
    intro j _
    apply Finset.sum_eq_zero
    intro k _
    have hn : ¬ (Distinct i j k ∧ bits {i,j,k} = x) := by
      rintro ⟨hd,hx⟩
      apply hw
      rw [← hx, ← ones_card, ones_bits]
      exact triple_support_card hd
    exact if_neg hn

/-- The original pushforward, decomposed by its two actual fibers. -/
theorem inputMass_fiber_formula {n : ℕ} (x : BooleanCube n) :
    inputMass x =
      (if hammingWeight x = 1 then (1 : ℝ) else 0) / (2 * n) +
      (if hammingWeight x = 3 then (6 : ℝ) else 0) /
        (2 * (n : ℝ) * (n - 1) * (n - 2)) := by
  classical
  have ht (i j k : Fin n) :
      (if bits {i,j,k} = x then
        (if Distinct i j k then 1 / (2 * (n : ℝ) * (n-1) * (n-2)) else 0) else 0) =
      (if Distinct i j k ∧ bits {i,j,k} = x then (1 : ℝ) else 0) /
        (2 * (n : ℝ) * (n-1) * (n-2)) := by
    by_cases hd : Distinct i j k <;> by_cases hx : bits {i,j,k} = x <;> simp [hd,hx]
  unfold inputMass
  simp only [Fintype.sum_sum_type, Fintype.sum_prod_type, sampleInput, sampleMass]
  simp_rw [ht]
  have hs (i : Fin n) :
      (if bits {i} = x then 1 / (2 * (n : ℝ)) else 0) =
        (if bits {i} = x then (1 : ℝ) else 0) / (2 * n) := by
    by_cases hx : bits {i} = x <;> simp [hx]
  simp_rw [hs]
  simp only [← Finset.sum_div]
  rw [singleton_fiber_count, triple_fiber_count]

/-- Closed point mass of the EXISTING input distribution. -/
theorem inputMass_closed {n : ℕ} (hn : 3 ≤ n) (x : BooleanCube n) :
    inputMass x = if hammingWeight x = 1 then 1 / (2 * (n : ℝ))
      else if hammingWeight x = 3 then 1 / (2 * (n.choose 3 : ℝ)) else 0 := by
  classical
  have hnr : (3 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (n : ℝ) ≠ 0 := by linarith
  have hn1 : (n : ℝ) - 1 ≠ 0 := by linarith
  have hn2 : (n : ℝ) - 2 ≠ 0 := by linarith
  have hfrac : (6 : ℝ) / (2 * (n : ℝ) * (n-1) * (n-2)) =
      1 / (2 * (n.choose 3 : ℝ)) := by
    rw [choose_three_cast]
    field_simp [hn0,hn1,hn2] <;> ring
  rw [inputMass_fiber_formula]
  by_cases h1 : hammingWeight x = 1
  · have h3 : hammingWeight x ≠ 3 := by omega
    simp [h1,h3]
  · by_cases h3 : hammingWeight x = 3
    · simpa [h1,h3] using hfrac
    · simp [h1,h3]

/-- Arbitrary real expectations are exactly half of each of the two layer means. -/
theorem inputMass_half_layer_mean {n : ℕ} (hn : 3 ≤ n) (g : BooleanCube n → ℝ) :
    (∑ x, inputMass x * g x) =
      (layerAverage g 1 + layerAverage g 3) / 2 := by
  classical
  have he (x : BooleanCube n) : inputMass x * g x =
      (if hammingWeight x = 1 then g x else 0) / (2 * (n : ℝ)) +
      (if hammingWeight x = 3 then g x else 0) / (2 * (n.choose 3 : ℝ)) := by
    rw [inputMass_closed hn]
    by_cases h1 : hammingWeight x = 1
    · have h3 : hammingWeight x ≠ 3 := by omega
      simp [h1,h3,div_eq_mul_inv,mul_comm]
    · by_cases h3 : hammingWeight x = 3 <;> simp [h1,h3,div_eq_mul_inv,mul_comm]
  simp_rw [he]
  rw [Finset.sum_add_distrib]
  simp only [← Finset.sum_div]
  rw [← sum_layer_eq_filter, ← sum_layer_eq_filter]
  unfold layerAverage
  rw [layer_card, layer_card, Nat.choose_one_right]
  ring

end
end PvsNPCartography.BalancedAffineCounting
