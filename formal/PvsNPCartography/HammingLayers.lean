import PvsNPCartography.FiniteSymmetrization
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.Perm

open scoped BigOperators

namespace PvsNPCartography.Symmetrization

noncomputable section

def hammingWeight {n : ℕ} (x : BooleanCube n) : ℕ := ∑ i, (x i).val

abbrev Layer (n w : ℕ) := {x : BooleanCube n // hammingWeight x = w}

def ones {n : ℕ} (x : BooleanCube n) : Finset (Fin n) :=
  Finset.univ.filter (fun i => x i = 1)

def bits {n : ℕ} (s : Finset (Fin n)) : BooleanCube n :=
  fun i => if i ∈ s then 1 else 0

private theorem bit_indicator (a : Fin 2) : (if a = 1 then 1 else 0 : ℕ) = a.val := by
  fin_cases a <;> decide

private theorem bit_reconstruct (a : Fin 2) : (if a = 1 then 1 else 0 : Fin 2) = a := by
  fin_cases a <;> decide

private theorem bit_zero (a : Fin 2) (h : a ≠ 1) : a = 0 := by
  fin_cases a <;> simp_all

theorem ones_card {n : ℕ} (x : BooleanCube n) : (ones x).card = hammingWeight x := by
  classical
  rw [Finset.card_eq_sum_ones, ones, Finset.sum_filter]
  simp only [bit_indicator, hammingWeight]

theorem bits_ones {n : ℕ} (x : BooleanCube n) : bits (ones x) = x := by
  funext i
  simpa [bits, ones] using bit_reconstruct (x i)

theorem ones_bits {n : ℕ} (s : Finset (Fin n)) : ones (bits s) = s := by
  classical
  ext i
  simp [ones, bits]

/-- An explicit bijection with all subsets of cardinality w. -/
def layerEquivSubsets (n w : ℕ) :
    Layer n w ≃ {s : Finset (Fin n) // s ∈ (Finset.univ : Finset (Fin n)).powersetCard w} where
  toFun x := ⟨ones x.1, Finset.mem_powersetCard.mpr
    ⟨Finset.subset_univ _, (ones_card x.1).trans x.2⟩⟩
  invFun s := ⟨bits s.1, by
    rw [← ones_card, ones_bits]
    exact (Finset.mem_powersetCard.mp s.2).2⟩
  left_inv x := Subtype.ext (bits_ones x.1)
  right_inv s := Subtype.ext (ones_bits s.1)

theorem layer_card (n w : ℕ) : Fintype.card (Layer n w) = n.choose w := by
  simpa only [Fintype.card_coe, Finset.card_powersetCard, Finset.card_univ,
    Fintype.card_fin] using Fintype.card_congr (layerEquivSubsets n w)

theorem hammingWeight_le {n : ℕ} (x : BooleanCube n) : hammingWeight x ≤ n := by
  rw [← ones_card]
  exact (Finset.card_le_card (Finset.subset_univ _)).trans_eq (by simp)

theorem ones_type_card {n : ℕ} (x : BooleanCube n) :
    Fintype.card {i : Fin n // x i = 1} = hammingWeight x := by
  rw [Fintype.card_subtype]
  exact ones_card x

/-- Full coverage: equal-weight inputs are related by a genuine bijection. -/
theorem exists_permutation_of_weight_eq {n : ℕ} (x y : BooleanCube n)
    (h : hammingWeight x = hammingWeight y) :
    ∃ e : Perm n, permuteInput e x = y := by
  classical
  have hc : Fintype.card {i : Fin n // y i = 1} =
      Fintype.card {i : Fin n // x i = 1} := by
    rw [ones_type_card, ones_type_card, h]
  let ep : {i : Fin n // y i = 1} ≃ {i : Fin n // x i = 1} :=
    Fintype.equivOfCardEq hc
  let en : {i : Fin n // ¬ y i = 1} ≃ {i : Fin n // ¬ x i = 1} :=
    Fintype.equivOfCardEq (by rw [Fintype.card_subtype_compl, Fintype.card_subtype_compl, hc])
  let e : Perm n := Equiv.subtypeCongr ep en
  refine ⟨e, ?_⟩
  funext i
  change x (e i) = y i
  by_cases hi : y i = 1
  · have he : e i = (ep ⟨i, hi⟩).val := by simp [e, Equiv.subtypeCongr, hi]
    rw [he, (ep ⟨i, hi⟩).property, hi]
  · have he : e i = (en ⟨i, hi⟩).val := by simp [e, Equiv.subtypeCongr, hi]
    rw [he, bit_zero _ (en ⟨i, hi⟩).property, bit_zero _ hi]

/-- A permutation of a Hamming layer, with its inverse proved. -/
def permuteLayer {n w : ℕ} (e : Perm n) : Layer n w ≃ Layer n w where
  toFun x := ⟨permuteInput e x.1, (permute_weight e x.1).trans x.2⟩
  invFun x := ⟨permuteInput e.symm x.1, (permute_weight e.symm x.1).trans x.2⟩
  left_inv x := by apply Subtype.ext; funext i; simp [permuteInput]
  right_inv x := by apply Subtype.ext; funext i; simp [permuteInput]

def layerAverage {n : ℕ} (g : BooleanCube n → ℝ) (w : ℕ) : ℝ :=
  (∑ y : Layer n w, g y.1) / Fintype.card (Layer n w)

/-- Double counting. No positivity or symmetry assumption on g is needed. -/
theorem sum_orbitAverage_layer {n w : ℕ} (g : BooleanCube n → ℝ) :
    (∑ y : Layer n w, orbitAverage g y.1) = ∑ y : Layer n w, g y.1 := by
  classical
  have hc := ne_of_gt (permutation_card_pos n)
  simp only [orbitAverage, ← Finset.sum_div]
  rw [Finset.sum_comm]
  have hreindex (e : Perm n) :
      (∑ y : Layer n w, g (permuteInput e y.1)) = ∑ y : Layer n w, g y.1 :=
    Equiv.sum_comp (permuteLayer e) (fun y => g y.1)
  simp_rw [hreindex]
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  field_simp

/-- Full permutation averaging is exactly the uniform mean on the input's
Hamming layer, at arbitrary arity, including the empty variable set. -/
theorem orbitAverage_eq_layerAverage {n : ℕ} (g : BooleanCube n → ℝ)
    (x : BooleanCube n) : orbitAverage g x = layerAverage g (hammingWeight x) := by
  classical
  let : Nonempty (Layer n (hammingWeight x)) := ⟨⟨x, rfl⟩⟩
  have hc : (Fintype.card (Layer n (hammingWeight x)) : ℝ) ≠ 0 := by
    exact_mod_cast (Fintype.card_ne_zero : Fintype.card (Layer n (hammingWeight x)) ≠ 0)
  have heq (y : Layer n (hammingWeight x)) : orbitAverage g y.1 = orbitAverage g x := by
    obtain ⟨e, he⟩ := exists_permutation_of_weight_eq x y.1 y.2.symm
    rw [← he, orbitAverage_invariant]
  have hs := sum_orbitAverage_layer (w := hammingWeight x) g
  simp_rw [heq] at hs
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at hs
  unfold layerAverage
  apply (eq_div_iff hc).mpr
  simpa [mul_comm] using hs

/-- The same identity with explicit factorial and binomial denominators. -/
theorem permutation_mean_eq_layer_mean {n : ℕ} (g : BooleanCube n → ℝ)
    (x : BooleanCube n) :
    (∑ e : Perm n, g (permuteInput e x)) / (n.factorial : ℝ) =
      (∑ y : Layer n (hammingWeight x), g y.1) / (n.choose (hammingWeight x) : ℝ) := by
  simpa only [orbitAverage, layerAverage, Perm, Fintype.card_perm,
    Fintype.card_fin, layer_card] using orbitAverage_eq_layerAverage g x

end
end PvsNPCartography.Symmetrization
