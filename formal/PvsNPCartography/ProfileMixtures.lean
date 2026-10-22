import PvsNPCartography.CliqueProfiles
import PvsNPCartography.LayerCertificates

open scoped BigOperators

namespace PvsNPCartography.ProfileMixtures

open Symmetrization CliqueProfiles

noncomputable section

/-- Linearity for arbitrary REAL coefficients, including signed coefficients.
Probability hypotheses belong at the certificate-conversion boundary. -/
theorem layerAverage_mixture {n : ℕ} {I : Type*} [Fintype I]
    (f : BooleanCube n → ZMod 2) (P : I → BinaryPolynomial n)
    (mu : I → ℝ) (w : ℕ) :
    layerAverage (success f P mu) w =
      ∑ i, mu i * layerAverage (correct f (P i)) w := by
  classical
  unfold layerAverage success
  rw [Finset.sum_comm]
  simp only [← Finset.mul_sum, Finset.sum_div, mul_div_assoc]

/-- Actual clique-polynomial profiles, not assumed truth-table rows. -/
theorem q_mixture_profile {n : ℕ} {I : Type*} [Fintype I]
    (A : I → Finset (Fin n)) (mu : I → ℝ) (w : ℕ) :
    layerAverage (success SmallSupportMod3.target (fun i => q (A i)) mu) w =
      ∑ i, mu i * ((∑ k ∈ Finset.range (w+1),
        ((A i).card.choose k : ℝ) * ((n-(A i).card).choose (w-k) : ℝ) * qGood w k) /
        (n.choose w : ℝ)) := by
  rw [layerAverage_mixture]
  simp_rw [q_layer_mean]

theorem r_mixture_profile {n : ℕ} {I : Type*} [Fintype I]
    (A : I → Finset (Fin n)) (mu : I → ℝ) (w : ℕ) :
    layerAverage (success SmallSupportMod3.target (fun i => r (A i)) mu) w =
      ∑ i, mu i * ((∑ k ∈ Finset.range (w+1),
        ((A i).card.choose k : ℝ) * ((n-(A i).card).choose (w-k) : ℝ) * rGood w k) /
        (n.choose w : ℝ)) := by
  rw [layerAverage_mixture]
  simp_rw [r_layer_mean]

/-- A short profile certificate enters the EXISTING full-symmetrization bridge.
The distribution is fixed before the input. Empty layers need no lower bound. -/
theorem feasible_of_profiles {n : ℕ} {I : Type} [Fintype I]
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d : ℕ}
    (hf : IsSymmetric f) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (profile : I → ℕ → ℝ)
    (hprofile : ∀ i w, layerAverage (correct f (P i)) w = profile i w)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (hl : ∀ w : ℕ, w ≤ n → 1 - epsilon ≤ ∑ i, mu i * profile i w) :
    HasProbabilisticDegreeAtMost f epsilon d := by
  apply feasible_of_layer_bounds hf P mu hd hn hs
  intro w hw
  rw [layerAverage_mixture]
  simp_rw [hprofile]
  exact hl w hw

/-- Actual input masses for a uniform layer. When w>n this is zero, not a
probability distribution. The expectation identity still totalizes correctly. -/
def layerMass {n : ℕ} (w : ℕ) (x : BooleanCube n) : ℝ :=
  if hammingWeight x = w then 1 / (n.choose w : ℝ) else 0

theorem layerMass_nonneg {n : ℕ} (w : ℕ) (x : BooleanCube n) :
    0 ≤ layerMass w x := by
  unfold layerMass
  split_ifs <;> positivity

/-- Exact transport for any real score; no positivity or symmetry premise. -/
theorem layerMass_expectation {n : ℕ} (w : ℕ) (g : BooleanCube n → ℝ) :
    (∑ x, layerMass w x * g x) = layerAverage g w := by
  classical
  unfold layerAverage
  rw [layer_card, sum_layer_eq_filter]
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hx : hammingWeight x = w <;>
    simp [layerMass, hx, div_eq_mul_inv, mul_comm]

theorem layerMass_normalized {n : ℕ} (w : ℕ) (hw : w ≤ n) :
    (∑ x : BooleanCube n, layerMass w x) = 1 := by
  have h := layerMass_expectation w (fun _ : BooleanCube n => (1 : ℝ))
  have hc : (n.choose w : ℝ) ≠ 0 := by
    exact_mod_cast (Nat.choose_ne_zero hw)
  simpa only [mul_one, layerAverage, Finset.sum_const, Finset.card_univ,
    nsmul_eq_mul, layer_card, div_self hc] using h

end
end PvsNPCartography.ProfileMixtures
