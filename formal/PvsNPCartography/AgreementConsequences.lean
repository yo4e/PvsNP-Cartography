import PvsNPCartography.AgreementDimension

open scoped BigOperators

namespace PvsNPCartography.AgreementConsequences

open AgreementDimension
noncomputable section
variable {K : Type*} [Field K] {n : ℕ}
attribute [local instance] Classical.propDecidable

def bound (n d : ℕ) : ℕ :=
  ∑ j ∈ Finset.range (min n ((n+d)/2) + 1), n.choose j

theorem bound_pos (n d : ℕ) : 0 < bound n d := by
  have h : 0 < (supports n ((n+d)/2)).card := by
    apply Finset.card_pos.mpr
    exact ⟨∅, by simp [supports]⟩
  simpa [supports_card, bound] using h

theorem grid_card (a b : K) (hab : a ≠ b) (n : ℕ) :
    (grid a b n).card = 2 ^ n := by
  classical
  simp [grid, hab]

theorem grid_same_card (a : K) (n : ℕ) : (grid a a n).card = 1 := by
  classical
  simp [grid]

/-- Distinctness is NOT necessary for the cardinality bound itself. A collapsed
actual grid is a singleton; it cannot still be counted as 2^n distinct inputs. -/
theorem agreement_bound_allow_equal (a b : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (R : MvPolynomial (Fin n) K) (d : ℕ) (hd : R.totalDegree ≤ d) :
    (agreementSet a b R).card ≤ bound n d := by
  classical
  by_cases hab : a = b
  · subst b
    have hc : (agreementSet a a R).card ≤ 1 := by
      calc
        _ ≤ (grid a a n).card := Finset.card_le_card (Finset.filter_subset _ _)
        _ = 1 := grid_same_card a n
    have hp := bound_pos n d
    omega
  · exact agreement_bound a b ha hb hab R d hd

/-- A real-valued correctness indicator of an actual K-polynomial. -/
def correct (P : MvPolynomial (Fin n) K) (y : Fin n → K) : ℝ :=
  if MvPolynomial.eval y P = ∏ i, y i then 1 else 0

/-- Exact counting identity; the coefficient field is not the probability field. -/
theorem sum_correct (a b : K) (P : MvPolynomial (Fin n) K) :
    (∑ y ∈ grid a b n, correct P y) = ((agreementSet a b P).card : ℝ) := by
  classical
  simp [correct, agreementSet]

def success {I : Type*} [Fintype I] (P : I → MvPolynomial (Fin n) K)
    (mu : I → ℝ) (y : Fin n → K) : ℝ := ∑ i, mu i * correct (P i) y

/-- Derived from the actual agreement theorem, not from a supplied row-score
hypothesis. Arbitrary finite REAL nonnegative mass1 distributions are covered. -/
theorem total_success_le {I : Type*} [Fintype I]
    (a b : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (P : I → MvPolynomial (Fin n) K) (mu : I → ℝ) (d : ℕ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) :
    (∑ y ∈ grid a b n, success P mu y) ≤ (bound n d : ℝ) := by
  classical
  have hrow (i : I) : (∑ y ∈ grid a b n, correct (P i) y) ≤ (bound n d : ℝ) := by
    rw [sum_correct]
    exact_mod_cast agreement_bound_allow_equal a b ha hb (P i) d (hd i)
  have he : (∑ y ∈ grid a b n, success P mu y) =
      ∑ i, mu i * (∑ y ∈ grid a b n, correct (P i) y) := by
    unfold success
    rw [Finset.sum_comm]
    simp only [Finset.mul_sum]
  rw [he]
  calc
    _ ≤ ∑ i, mu i * (bound n d : ℝ) := by
      apply Finset.sum_le_sum
      intro i _
      exact mul_le_mul_of_nonneg_left (hrow i) (hn i)
    _ = (bound n d : ℝ) := by rw [← Finset.sum_mul, hs, one_mul]

/-- Quantitative bridge from pointwise randomized success to deterministic
agreement. The same family and normalized weights precede EVERY input. -/
theorem pointwise_bound {I : Type*} [Fintype I]
    (a b : K) (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    (P : I → MvPolynomial (Fin n) K) (mu : I → ℝ) (d : ℕ) (eta : ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (hp : ∀ y ∈ grid a b n, eta ≤ success P mu y) :
    eta * (2 ^ n : ℝ) ≤ (bound n d : ℝ) := by
  classical
  have hlow : eta * (2 ^ n : ℝ) ≤ ∑ y ∈ grid a b n, success P mu y := by
    calc
      eta * (2 ^ n : ℝ) = ∑ y ∈ grid a b n, eta := by
        simp [grid_card a b hab n, mul_comm]
      _ ≤ _ := Finset.sum_le_sum (fun y hy => hp y hy)
  exact hlow.trans (total_success_le a b ha hb P mu d hd hn hs)

theorem no_pointwise_mixture {I : Type*} [Fintype I]
    (a b : K) (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    (P : I → MvPolynomial (Fin n) K) (mu : I → ℝ) (d : ℕ) (eta : ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) (hgap : (bound n d : ℝ) < eta * (2 ^ n : ℝ)) :
    ¬ (∀ y ∈ grid a b n, eta ≤ success P mu y) := by
  intro hp
  exact (not_le_of_gt hgap) (pointwise_bound a b ha hb hab P mu d eta hd hn hs hp)

end
end PvsNPCartography.AgreementConsequences
