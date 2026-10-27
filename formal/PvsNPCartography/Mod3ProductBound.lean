import PvsNPCartography.GF4Transport

open scoped BigOperators

namespace PvsNPCartography.Mod3ProductBound

open GF4Transport
noncomputable section
attribute [local instance] Classical.propDecidable

def binaryCorrect {n : ℕ} (P : BinaryPolynomial n) (x : BooleanCube n) : ℝ :=
  if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P =
    SmallSupportMod3.target x then 1 else 0

/-- Pointwise union bound on one shared index. No independence premise. -/
theorem same_index_correctness {m : ℕ} (P : BinaryPolynomial (m + 2))
    (y : Fin m → K) (hy : ∀ j, y j = 1 ∨ y j = GF4Transport.omega) :
    binaryCorrect P (pad 0 (decode y)) + binaryCorrect P (pad 1 (decode y)) - 1 ≤
      AgreementConsequences.correct (transported P) y := by
  have hn : 0 ≤ AgreementConsequences.correct (transported P) y := by
    unfold AgreementConsequences.correct
    split_ifs <;> norm_num
  by_cases h0 : MvPolynomial.eval (fun j => ((pad 0 (decode y) j).val : ZMod 2)) P =
      SmallSupportMod3.target (pad 0 (decode y))
  · by_cases h1 : MvPolynomial.eval (fun j => ((pad 1 (decode y) j).val : ZMod 2)) P =
        SmallSupportMod3.target (pad 1 (decode y))
    · have ht := transported_correct P y hy h0 h1
      simp [binaryCorrect, AgreementConsequences.correct, h0, h1, ht]
    · simpa [binaryCorrect, h0, h1] using hn
  · by_cases h1 : MvPolynomial.eval (fun j => ((pad 1 (decode y) j).val : ZMod 2)) P =
        SmallSupportMod3.target (pad 1 (decode y))
    · simpa [binaryCorrect, h0, h1] using hn
    · simp only [binaryCorrect, ite_eq_right h0, ite_eq_right h1]
      linarith

/-- Actual transported family and original real weights: no supplied product-success
hypothesis, no rational-ticket assumption and no input-dependent resampling. -/
theorem transport_success {m : ℕ} {I : Type*} [Fintype I]
    (P : I → BinaryPolynomial (m + 2)) (mu : I → ℝ) (delta : ℝ)
    (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1 - delta ≤ ∑ i, mu i * binaryCorrect (P i) x)
    (y : Fin m → K) (hy : ∀ j, y j = 1 ∨ y j = GF4Transport.omega) :
    1 - 2 * delta ≤ AgreementConsequences.success (fun i => transported (P i)) mu y := by
  have h0 := hp (pad 0 (decode y))
  have h1 := hp (pad 1 (decode y))
  have hsum := Finset.sum_le_sum (s := Finset.univ)
    (fun i _ => mul_le_mul_of_nonneg_left (same_index_correctness (P i) y hy) (hn i))
  simp only [mul_sub, mul_add, mul_one, Finset.sum_sub_distrib,
    Finset.sum_add_distrib, hs] at hsum
  unfold AgreementConsequences.success
  linarith

/-- Complete necessary inequality for the original MOD3 target at arbitrary
error delta. The coefficient extension is an actual four-element field. -/
theorem mod3_product_bound {m : ℕ} {I : Type*} [Fintype I]
    (P : I → BinaryPolynomial (m + 2)) (mu : I → ℝ) (D : ℕ) (delta : ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ D) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1 - delta ≤ ∑ i, mu i * binaryCorrect (P i) x) :
    (1 - 2 * delta) * (2 ^ m : ℝ) ≤ (AgreementConsequences.bound m D : ℝ) := by
  apply AgreementConsequences.pointwise_bound (1 : K) GF4Transport.omega
    one_ne_zero omega_ne_zero omega_ne_one.symm
    (fun i => transported (P i)) mu D (1 - 2 * delta)
    (fun i => (transported_degree (P i)).trans (hd i)) hn hs
  intro y hy
  have hg : ∀ j, y j = 1 ∨ y j = GF4Transport.omega := by
    intro j
    simpa [AgreementDimension.grid, Fintype.mem_piFinset] using
      (Fintype.mem_piFinset.mp hy j)
  exact transport_success P mu delta hn hs hp y hg

/-- Endpoint uses the repository's original probabilistic-degree predicate. -/
theorem necessary_inequality (m D : ℕ) (delta : ℝ)
    (h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target (m + 2)) delta D) :
    (1 - 2 * delta) * (2 ^ m : ℝ) ≤ (AgreementConsequences.bound m D : ℝ) := by
  obtain ⟨k, P, mu, hd, hn, hs, hp⟩ := h
  exact mod3_product_bound P mu D delta hd hn hs hp

theorem no_mod3_approximation (m D : ℕ) (delta : ℝ)
    (hgap : (AgreementConsequences.bound m D : ℝ) < (1 - 2 * delta) * (2 ^ m : ℝ)) :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target (m + 2)) delta D := by
  intro h
  exact (not_le_of_gt hgap) (necessary_inequality m D delta h)

end
end PvsNPCartography.Mod3ProductBound
