import PvsNPCartography.HammingLayers
import PvsNPCartography.SmallSupportMod3
import PvsNPCartography.BalancedAffineDualAlgebra

open scoped BigOperators

namespace PvsNPCartography.BalancedAffineCounting

open Symmetrization SmallSupportMod3

noncomputable section

/-- Ordered triples without repeated coordinates. -/
abbrev Distinct {α : Type*} (i j k : α) : Prop := i ≠ j ∧ i ≠ k ∧ j ≠ k

private theorem triple_exclusion {α : Type*} [DecidableEq α]
    (f : α → ℝ) (i j k : α) :
    (if Distinct i j k then f i * f j * f k else 0) =
      f i * f j * f k - (if i = j then f i ^ 2 * f k else 0) -
      (if i = k then f i ^ 2 * f j else 0) -
      (if j = k then f i * f j ^ 2 else 0) +
      2 * (if i = j ∧ j = k then f i ^ 3 else 0) := by
  classical
  by_cases hij : i = j <;> by_cases hik : i = k <;> by_cases hjk : j = k <;>
    simp_all [Distinct] <;> ring

/-- Inclusion-exclusion on ordered triples. No Boolean or bounded-n hypothesis. -/
theorem ordered_triple_moment {α : Type*} [Fintype α] [DecidableEq α] (f : α → ℝ) :
    (∑ i, ∑ j, ∑ k, if Distinct i j k then f i * f j * f k else 0) =
      (∑ i, f i) ^ 3 - 3 * (∑ i, f i ^ 2) * (∑ i, f i) +
        2 * (∑ i, f i ^ 3) := by
  classical
  have hfull : (∑ i, ∑ j, ∑ k, f i * f j * f k) = (∑ i, f i) ^ 3 := by
    simp only [← Finset.mul_sum, ← Finset.sum_mul]
    ring
  have h₁ : (∑ i, ∑ j, ∑ k, if i = j then f i ^ 2 * f k else 0) =
      (∑ i, f i ^ 2) * (∑ i, f i) := by
    calc
      _ = ∑ i, ∑ k, ∑ j, if i = j then f i ^ 2 * f k else 0 := by
        apply Finset.sum_congr rfl
        intro i _
        exact Finset.sum_comm
      _ = _ := by simp [← Finset.mul_sum, ← Finset.sum_mul]
  have h₂ : (∑ i, ∑ j, ∑ k, if i = k then f i ^ 2 * f j else 0) =
      (∑ i, f i ^ 2) * (∑ i, f i) := by
    simp [← Finset.mul_sum, ← Finset.sum_mul]
  have h₃ : (∑ i, ∑ j, ∑ k, if j = k then f i * f j ^ 2 else 0) =
      (∑ i, f i) * (∑ i, f i ^ 2) := by
    simp [← Finset.mul_sum, ← Finset.sum_mul]
  have h₄ : (∑ i, ∑ j, ∑ k, if i = j ∧ j = k then f i ^ 3 else 0) =
      ∑ i, f i ^ 3 := by
    simp [ite_and]
  simp_rw [triple_exclusion]
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib]
  rw [hfull, h₁, h₂, h₃]
  simp only [← Finset.mul_sum]
  rw [h₄]
  ring

/-- Real count, including the empty and other low-arity cases. -/
theorem ordered_triple_count (n : ℕ) :
    (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
      if Distinct i j k then (1 : ℝ) else 0) =
      (n : ℝ) * (n - 1) * (n - 2) := by
  have h := ordered_triple_moment (fun _ : Fin n => (1 : ℝ))
  simp only [one_mul, one_pow, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, mul_one] at h
  rw [h]
  ring

abbrev Sample (n : ℕ) := Fin n ⊕ (Fin n × Fin n × Fin n)

/-- Half uniform on single coordinates; half on ordered distinct triples.
Repeated-coordinate triples carry zero probability. -/
def sampleMass (n : ℕ) : Sample n → ℝ
  | .inl _ => 1 / (2 * n)
  | .inr (i,j,k) =>
      if Distinct i j k then 1 / (2 * (n : ℝ) * (n - 1) * (n - 2)) else 0

theorem sampleMass_nonneg {n : ℕ} (hn : 3 ≤ n) (s : Sample n) :
    0 ≤ sampleMass n s := by
  have hnr : (3 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (0 : ℝ) < n := by linarith
  have hn1 : (0 : ℝ) < (n : ℝ) - 1 := by linarith
  have hn2 : (0 : ℝ) < (n : ℝ) - 2 := by linarith
  rcases s with i | ⟨i,j,k⟩
  · dsimp [sampleMass]; positivity
  · dsimp [sampleMass]; split_ifs <;> positivity

theorem sampleMass_sum {n : ℕ} (hn : 3 ≤ n) :
    (∑ s : Sample n, sampleMass n s) = 1 := by
  classical
  have hnr : (3 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (n : ℝ) ≠ 0 := by linarith
  have hn1 : (n : ℝ) - 1 ≠ 0 := by linarith
  have hn2 : (n : ℝ) - 2 ≠ 0 := by linarith
  have ht : (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
        if Distinct i j k then 1 / (2 * (n : ℝ) * (n-1) * (n-2)) else 0) =
      ((n : ℝ) * (n-1) * (n-2)) / (2 * (n : ℝ) * (n-1) * (n-2)) := by
    rw [← ordered_triple_count n]
    simp only [Finset.sum_div, ite_div, zero_div]
  simp only [Fintype.sum_sum_type, Fintype.sum_prod_type, sampleMass]
  rw [ht]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  field_simp [hn0, hn1, hn2]
  ring

def sampleInput {n : ℕ} : Sample n → BooleanCube n
  | .inl i => bits {i}
  | .inr (i,j,k) => bits {i,j,k}

/-- This is a real sign, not a GF(2) probability. -/
def bitSign (a : Fin 2) : ℝ := 1 - 2 * a.val

theorem bitSign_sq (a : Fin 2) : bitSign a ^ 2 = 1 := by
  fin_cases a <;> norm_num [bitSign]

theorem bitSign_cube (a : Fin 2) : bitSign a ^ 3 = bitSign a := by
  fin_cases a <;> norm_num [bitSign]

theorem bitSign_sum {n : ℕ} (b : BooleanCube n) :
    (∑ i, bitSign (b i)) = (n : ℝ) - 2 * hammingWeight b := by
  simp [bitSign, hammingWeight, Finset.sum_sub_distrib, Finset.mul_sum]

private theorem target_bits {n : ℕ} (s : Finset (Fin n)) :
    target (bits s) = (if s.card % 3 = 0 then 1 else 0 : ZMod 2) := by
  change (if hammingWeight (bits s) % 3 = 0 then 1 else 0 : ZMod 2) = _
  rw [← ones_card, ones_bits]

private theorem affineValue_bits {n : ℕ} (p : Affine n) (s : Finset (Fin n)) :
    affineValue p (bits s) = (p.1.val : ZMod 2) + ∑ i ∈ s, ((p.2 i).val : ZMod 2) := by
  classical
  have hb (i : Fin n) : ((bits s i).val : ZMod 2) =
      if i ∈ s then 1 else 0 := by
    by_cases hi : i ∈ s <;> simp [bits, hi]
  simp only [affineValue, Nat.cast_sum, Nat.cast_mul]
  simp_rw [hb, mul_ite]
  simp

private theorem singleton_sign (c a : Fin 2) :
    ((if (c.val : ZMod 2) + (a.val : ZMod 2) = 0 then 1 else 0 : ℕ) : ℝ) =
      (1 + bitSign c * bitSign a) / 2 := by
  fin_cases c <;> fin_cases a <;> norm_num [bitSign]
  all_goals decide

private theorem triple_sign (c a b d : Fin 2) :
    ((if (c.val : ZMod 2) + ((a.val : ZMod 2) + ((b.val : ZMod 2) + (d.val : ZMod 2))) = 1
      then 1 else 0 : ℕ) : ℝ) =
      (1 - bitSign c * bitSign a * bitSign b * bitSign d) / 2 := by
  fin_cases c <;> fin_cases a <;> fin_cases b <;> fin_cases d <;> norm_num [bitSign]
  all_goals decide

theorem singleton_correct {n : ℕ} (p : Affine n) (i : Fin n) :
    (affineCorrect p (sampleInput (.inl i)) : ℝ) =
      (1 + bitSign p.1 * bitSign (p.2 i)) / 2 := by
  change (affineCorrect p (bits {i}) : ℝ) = _
  unfold affineCorrect
  rw [affineValue_bits, target_bits]
  simpa using singleton_sign p.1 (p.2 i)

theorem triple_correct {n : ℕ} (p : Affine n) (i j k : Fin n)
    (hd : Distinct i j k) :
    (affineCorrect p (sampleInput (.inr (i,j,k))) : ℝ) =
      (1 - bitSign p.1 * bitSign (p.2 i) * bitSign (p.2 j) * bitSign (p.2 k)) / 2 := by
  rcases hd with ⟨hij,hik,hjk⟩
  change (affineCorrect p (bits {i,j,k}) : ℝ) = _
  unfold affineCorrect
  rw [affineValue_bits, target_bits]
  simpa [hij, hik, hjk] using triple_sign p.1 (p.2 i) (p.2 j) (p.2 k)

end
end PvsNPCartography.BalancedAffineCounting
