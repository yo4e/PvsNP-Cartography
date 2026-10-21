import PvsNPCartography.HammingIntersections

open scoped BigOperators

namespace PvsNPCartography.HammingProfiles

open Symmetrization HammingIntersections

noncomputable section

def overlap {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) : ℕ :=
  (ones x ∩ A).card

theorem overlap_le_weight {n : ℕ} (A : Finset (Fin n)) (x : BooleanCube n) :
    overlap A x ≤ hammingWeight x := by
  unfold overlap
  exact (Finset.card_le_card Finset.inter_subset_left).trans_eq (ones_card x)

/-- The overlap fiber in an actual layer is the already counted Boolean slice. -/
def layerFiberEquiv {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :
    {x : Layer n w // overlap A x.1 = r} ≃
      {x : BooleanCube n // hammingWeight x = w ∧ (ones x ∩ A).card = r} where
  toFun x := ⟨x.1.1, x.1.2, x.2⟩
  invFun x := ⟨⟨x.1, x.2.1⟩, x.2.2⟩
  left_inv x := by apply Subtype.ext; apply Subtype.ext; rfl
  right_inv x := by apply Subtype.ext; rfl

theorem layer_overlap_card {n : ℕ} (A : Finset (Fin n)) (w r : ℕ) :
    Fintype.card {x : Layer n w // overlap A x.1 = r} =
      if r ≤ w then A.card.choose r * (n-A.card).choose (w-r) else 0 := by
  rw [Fintype.card_congr (layerFiberEquiv A w r)]
  exact boolean_intersection_card A w r

/-- A legitimate finite partition, for arbitrary signed real h and all arities.
There is no nonempty-layer assumption and no probability claim here. -/
theorem weighted_layer_sum {n : ℕ} (A : Finset (Fin n)) (w : ℕ) (h : ℕ → ℝ) :
    (∑ x : Layer n w, h (overlap A x.1)) =
      ∑ r ∈ Finset.range (w+1),
        (A.card.choose r : ℝ) * ((n-A.card).choose (w-r) : ℝ) * h r := by
  classical
  have hm : ∀ x ∈ (Finset.univ : Finset (Layer n w)),
      overlap A x.1 ∈ Finset.range (w+1) := by
    intro x _
    apply Finset.mem_range.mpr
    have hx := overlap_le_weight A x.1
    rw [x.2] at hx
    omega
  rw [← Finset.sum_fiberwise_of_maps_to' hm h]
  apply Finset.sum_congr rfl
  intro r hr
  have hrw : r ≤ w := by have hh := Finset.mem_range.mp hr; omega
  have hc : (Finset.univ.filter (fun x : Layer n w => overlap A x.1 = r)).card =
      A.card.choose r * (n-A.card).choose (w-r) := by
    simpa only [Fintype.card_subtype, ite_eq_left hrw] using layer_overlap_card A w r
  simp only [Finset.sum_const, nsmul_eq_mul, hc, Nat.cast_mul]
  ring

/-- Totalized real mean; empty layers evaluate to zero, not to a probability. -/
theorem weighted_layer_mean {n : ℕ} (A : Finset (Fin n)) (w : ℕ) (h : ℕ → ℝ) :
    layerAverage (fun x => h (overlap A x)) w =
      (∑ r ∈ Finset.range (w+1),
        (A.card.choose r : ℝ) * ((n-A.card).choose (w-r) : ℝ) * h r) /
      (n.choose w : ℝ) := by
  unfold layerAverage
  rw [weighted_layer_sum, layer_card]

/-- Normalization numerator, proved from the actual layer partition. -/
theorem profile_coefficients_sum {n : ℕ} (A : Finset (Fin n)) (w : ℕ) :
    (∑ r ∈ Finset.range (w+1),
      (A.card.choose r : ℝ) * ((n-A.card).choose (w-r) : ℝ)) = (n.choose w : ℝ) := by
  have hh := weighted_layer_sum A w (fun _ => (1 : ℝ))
  simpa only [mul_one, Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
    layer_card] using hh.symm

theorem layer_denominator_pos {n w : ℕ} (hw : w ≤ n) :
    (0 : ℝ) < n.choose w := by exact_mod_cast Nat.choose_pos hw

/-- Only nonempty layers give normalized overlap probabilities. -/
theorem profile_probabilities_sum {n : ℕ} (A : Finset (Fin n)) (w : ℕ) (hw : w ≤ n) :
    (∑ r ∈ Finset.range (w+1),
      ((A.card.choose r : ℝ) * ((n-A.card).choose (w-r) : ℝ)) / (n.choose w : ℝ)) = 1 := by
  rw [← Finset.sum_div, profile_coefficients_sum]
  exact div_self (ne_of_gt (layer_denominator_pos hw))

theorem empty_layer_mean {n w : ℕ} (hw : n < w) (g : BooleanCube n → ℝ) :
    layerAverage g w = 0 := by
  unfold layerAverage
  rw [layer_card, Nat.choose_eq_zero_of_lt hw]
  simp

/-- A concrete guardrail: empty-layer division-by-zero totalization is not normalization. -/
theorem empty_layer_not_probability :
    layerAverage (fun _ : BooleanCube 0 => (1 : ℝ)) 1 = 0 :=
  empty_layer_mean (by decide) _

end
end PvsNPCartography.HammingProfiles
