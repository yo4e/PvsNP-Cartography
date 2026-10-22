import PvsNPCartography.ProfileMixtures
import PvsNPCartography.FiniteDual

open scoped BigOperators

namespace PvsNPCartography.RestrictedCliqueObstruction

open Symmetrization CliqueProfiles ProfileMixtures

noncomputable section
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

/-- Precisely zero/all q9/all r8. NOT the class of all degree-two polynomials. -/
def Allowed (P : BinaryPolynomial 12) : Prop :=
  P = 0 ∨ (∃ A : Finset (Fin 12), A.card = 9 ∧ P = q A) ∨
    (∃ A : Finset (Fin 12), A.card = 8 ∧ P = r A)

theorem allowed_degree {P : BinaryPolynomial 12} (hP : Allowed P) :
    P.totalDegree ≤ 2 := by
  rcases hP with rfl | ⟨A, _, rfl⟩ | ⟨A, _, rfl⟩
  · simp
  · exact q_degree A
  · exact r_degree A

/-- Total layer masses are 5/14 and 9/14, not per-input masses. -/
def dualMass (x : BooleanCube 12) : ℝ :=
  (5 / 14 : ℝ) * layerMass 6 x + (9 / 14 : ℝ) * layerMass 10 x

theorem dualMass_nonneg (x : BooleanCube 12) : 0 ≤ dualMass x := by
  exact add_nonneg (mul_nonneg (by norm_num) (layerMass_nonneg 6 x))
    (mul_nonneg (by norm_num) (layerMass_nonneg 10 x))

theorem dualMass_normalized : (∑ x, dualMass x) = 1 := by
  simp only [dualMass, Finset.sum_add_distrib, ← Finset.mul_sum]
  rw [layerMass_normalized 6 (by decide), layerMass_normalized 10 (by decide)]
  norm_num

theorem dual_expectation (g : BooleanCube 12 → ℝ) :
    (∑ x, dualMass x * g x) =
      (5 / 14 : ℝ) * layerAverage g 6 + (9 / 14 : ℝ) * layerAverage g 10 := by
  simp only [dualMass, add_mul, mul_assoc, Finset.sum_add_distrib,
    ← Finset.mul_sum, layerMass_expectation]

/-- Proved from the actual target and zero polynomial, not a supplied score. -/
theorem zero_layer_mean (w : ℕ) (hw : w ≤ 12) :
    layerAverage (correct SmallSupportMod3.target (0 : BinaryPolynomial 12)) w =
      if w % 3 = 0 then 0 else 1 := by
  classical
  have he (x : Layer 12 w) :
      correct SmallSupportMod3.target (0 : BinaryPolynomial 12) x.1 =
        if w % 3 = 0 then (0 : ℝ) else 1 := by
    have hx : (∑ i, (x.1 i).val) = w := x.2
    by_cases h : w % 3 = 0 <;> simp [correct, SmallSupportMod3.target, hx, h]
  have hc : ((12 : ℕ).choose w : ℝ) ≠ 0 := by
    exact_mod_cast (Nat.choose_ne_zero hw)
  unfold layerAverage
  simp_rw [he]
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, layer_card]
  field_simp <;> ring

theorem q9_layer_six (A : Finset (Fin 12)) (hA : A.card = 9) :
    layerAverage (correct SmallSupportMod3.target (q A)) 6 = (9 / 11 : ℝ) := by
  rw [q_layer_mean, hA]
  norm_num [qGood, Finset.sum_range_succ, Nat.choose]

theorem q9_layer_ten (A : Finset (Fin 12)) (hA : A.card = 9) :
    layerAverage (correct SmallSupportMod3.target (q A)) 10 = (6 / 11 : ℝ) := by
  rw [q_layer_mean, hA]
  norm_num [qGood, Finset.sum_range_succ, Nat.choose]

theorem r8_layer_six (A : Finset (Fin 12)) (hA : A.card = 8) :
    layerAverage (correct SmallSupportMod3.target (r A)) 6 = (23 / 33 : ℝ) := by
  rw [r_layer_mean, hA]
  norm_num [rGood, Finset.sum_range_succ, Nat.choose]

theorem r8_layer_ten (A : Finset (Fin 12)) (hA : A.card = 8) :
    layerAverage (correct SmallSupportMod3.target (r A)) 10 = (14 / 33 : ℝ) := by
  rw [r_layer_mean, hA]
  norm_num [rGood, Finset.sum_range_succ, Nat.choose]

theorem zero_dual_score :
    (∑ x, dualMass x * correct SmallSupportMod3.target (0 : BinaryPolynomial 12) x) =
      (9 / 14 : ℝ) := by
  rw [dual_expectation, zero_layer_mean 6 (by decide), zero_layer_mean 10 (by decide)]
  norm_num

theorem q9_dual_score (A : Finset (Fin 12)) (hA : A.card = 9) :
    (∑ x, dualMass x * correct SmallSupportMod3.target (q A) x) = (9 / 14 : ℝ) := by
  rw [dual_expectation, q9_layer_six A hA, q9_layer_ten A hA]
  norm_num

theorem r8_dual_score (A : Finset (Fin 12)) (hA : A.card = 8) :
    (∑ x, dualMass x * correct SmallSupportMod3.target (r A) x) = (241 / 462 : ℝ) := by
  rw [dual_expectation, r8_layer_six A hA, r8_layer_ten A hA]
  norm_num

theorem allowed_dual_bound {P : BinaryPolynomial 12} (hP : Allowed P) :
    (∑ x, dualMass x * correct SmallSupportMod3.target P x) ≤ (9 / 14 : ℝ) := by
  rcases hP with rfl | ⟨A, hA, rfl⟩ | ⟨A, hA, rfl⟩
  · exact le_of_eq zero_dual_score
  · exact le_of_eq (q9_dual_score A hA)
  · rw [r8_dual_score A hA]
    norm_num

/-- Any finite REAL distribution in the declared family, allowing arbitrary
nonuniform subset probabilities and repeated rows. No rationality premise.
The family and weights precede the universal input. -/
theorem no_allowed_mixture {I : Type} [Fintype I]
    (P : I → BinaryPolynomial 12) (mu : I → ℝ)
    (hP : ∀ i, Allowed (P i)) (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1) :
    ¬ (∀ x, (2 / 3 : ℝ) ≤ success SmallSupportMod3.target P mu x) := by
  exact finite_dual_obstruction
    (fun i x => correct SmallSupportMod3.target (P i) x) mu dualMass
    (9 / 14) (2 / 3) hn hs dualMass_nonneg dualMass_normalized
    (fun i => allowed_dual_bound (hP i)) (by norm_num)

/-- Explicit existential certificate is refuted with its support in the statement. -/
theorem no_allowed_certificate :
    ¬ ∃ (m : ℕ) (P : Fin m → BinaryPolynomial 12) (mu : Fin m → ℝ),
      (∀ i, Allowed (P i)) ∧ (∀ i, 0 ≤ mu i) ∧ (∑ i, mu i = 1) ∧
      (∀ x, (2 / 3 : ℝ) ≤ success SmallSupportMod3.target P mu x) := by
  rintro ⟨m, P, mu, hP, hn, hs, hp⟩
  exact no_allowed_mixture P mu hP hn hs hp

/-- Attack: changing only the allowed subset size already defeats this dual.
This does NOT assert a pointwise approximant from q8. -/
theorem q8_dual_score (A : Finset (Fin 12)) (hA : A.card = 8) :
    (∑ x, dualMass x * correct SmallSupportMod3.target (q A) x) = (5 / 6 : ℝ) := by
  rw [dual_expectation, q_layer_mean, q_layer_mean, hA]
  norm_num [qGood, Finset.sum_range_succ, Nat.choose]

def firstEight : Finset (Fin 12) := Finset.univ.filter (fun i => i.val < 8)

theorem support_restriction_essential :
    ∃ P : BinaryPolynomial 12, P.totalDegree ≤ 2 ∧
      (9 / 14 : ℝ) < ∑ x, dualMass x * correct SmallSupportMod3.target P x := by
  refine ⟨q firstEight, q_degree firstEight, ?_⟩
  rw [q8_dual_score firstEight (by decide)]
  norm_num

end
end PvsNPCartography.RestrictedCliqueObstruction
