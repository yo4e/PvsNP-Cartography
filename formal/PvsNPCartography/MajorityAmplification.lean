import PvsNPCartography.IndependentTrials
import PvsNPCartography.CliqueProfiles
import PvsNPCartography.TwoPointCompression

open scoped BigOperators

namespace PvsNPCartography.MajorityAmplification
open IndependentTrials Symmetrization
noncomputable section
attribute [local instance] Classical.propDecidable

/-- The eighth elementary symmetric polynomial of fifteen ACTUAL polynomials. -/
def majority15 {n : ℕ} (P : Fin 15 → BinaryPolynomial n) : BinaryPolynomial n :=
  ∑ S ∈ (Finset.univ : Finset (Fin 15)).powersetCard 8, ∏ j ∈ S, P j

theorem majority15_degree {n d : ℕ} (P : Fin 15 → BinaryPolynomial n)
    (hd : ∀ j, (P j).totalDegree ≤ d) : (majority15 P).totalDegree ≤ 8*d := by
  apply MvPolynomial.totalDegree_finsetSum_le
  intro S hS
  calc
    _ ≤ ∑ j ∈ S, (P j).totalDegree := MvPolynomial.totalDegree_finsetProd _ _
    _ ≤ ∑ _j ∈ S, d := Finset.sum_le_sum (fun j _ => hd j)
    _ = 8*d := by simp [(Finset.mem_powersetCard.mp hS).2]

/-- GF2 evaluations are actual bits, not rounded or probabilistically interpreted. -/
def answers {n : ℕ} (P : Fin 15 → BinaryPolynomial n) (x : BooleanCube n) :
    BooleanCube 15 := fun j => MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (P j)

theorem majority15_eval {n : ℕ} (P : Fin 15 → BinaryPolynomial n)
    (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (majority15 P) =
      if 8 ≤ ∑ j, (answers P x j).val then 1 else 0 := by
  have he : MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (majority15 P) =
      MvPolynomial.eval (fun j => ((answers P x j).val : ZMod 2))
        (CliqueProfiles.elementary Finset.univ 8) := by
    simp [majority15, CliqueProfiles.elementary, CliqueProfiles.subsetMonomial, answers]
  rw [he, CliqueProfiles.elementary_eval, CliqueProfiles.overlap_univ]
  have hw := hammingWeight_le (answers P x)
  have hb := TwoPointCompression.majority15_binomial
    (hammingWeight (answers P x)) hw
  change ((hammingWeight (answers P x)).choose 8 : ZMod 2) =
    if 8 ≤ hammingWeight (answers P x) then 1 else 0
  by_cases h : 8 ≤ hammingWeight (answers P x)
  · simp only [ite_eq_left h] at hb ⊢
    apply Fin.ext
    simpa using hb
  · simp only [ite_eq_right h] at hb ⊢
    apply Fin.ext
    simpa using hb

theorem bit_cases (a : ZMod 2) : a = 0 ∨ a = 1 := by
  fin_cases a <;> simp

/-- Exact majority success/failure complement, including the strict threshold. -/
theorem majority_indicator (z : Fin 15 → ZMod 2) (b : ZMod 2) :
    (if (if 8 ≤ ∑ j, (z j).val then (1 : ZMod 2) else 0) = b then (1 : ℝ) else 0) +
      (if 8 ≤ ∑ j, if z j ≠ b then (1 : ℕ) else 0 then 1 else 0) = 1 := by
  rcases bit_cases b with rfl | rfl
  · have hc : (∑ j, if z j ≠ 0 then (1 : ℕ) else 0) = ∑ j, (z j).val := by
      apply Finset.sum_congr rfl
      intro j _
      rcases bit_cases (z j) with h | h <;> simp [h]
    rw [hc]
    by_cases h : 8 ≤ ∑ j, (z j).val <;> simp [h]
  · have hc : (∑ j, if z j ≠ 1 then (1 : ℕ) else 0) + (∑ j, (z j).val) = 15 := by
      rw [← Finset.sum_add_distrib]
      have hterm (j : Fin 15) : (if z j ≠ 1 then (1 : ℕ) else 0) + (z j).val = 1 := by
        rcases bit_cases (z j) with h | h <;> simp [h]
      simp_rw [hterm]
      simp
    by_cases h : 8 ≤ ∑ j, (z j).val
    · have hn : ¬ 8 ≤ ∑ j, if z j ≠ 1 then (1 : ℕ) else 0 := by omega
      simp [h, hn]
    · have ht : 8 ≤ ∑ j, if z j ≠ 1 then (1 : ℕ) else 0 := by omega
      simp [h, ht]

def errorFlag {n : ℕ} {I : Type*} (f : BooleanCube n → ZMod 2)
    (P : I → BinaryPolynomial n) (x : BooleanCube n) (i : I) : Bool :=
  decide (MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) ≠ f x)

theorem source_error_complement {n : ℕ} {I : Type*} [Fintype I]
    (f : BooleanCube n → ZMod 2) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hs : ∑ i, mu i = 1) (x : BooleanCube n) :
    errorMass mu (errorFlag f P x) + success f P mu x = 1 := by
  unfold errorMass success
  rw [← Finset.sum_add_distrib]
  convert hs using 1
  apply Finset.sum_congr rfl
  intro i _
  by_cases h : MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) = f x
  · simp [errorFlag, correct, h]
  · simp [errorFlag, correct, h]

theorem actual_majority_complement {n : ℕ} {I : Type*}
    (f : BooleanCube n → ZMod 2) (P : I → BinaryPolynomial n)
    (v : Fin 15 → I) (x : BooleanCube n) :
    correct f (majority15 (fun j => P (v j))) x +
      (if 8 ≤ failures (errorFlag f P x) v then (1 : ℝ) else 0) = 1 := by
  unfold correct
  rw [majority15_eval]
  simpa [answers, failures, errorFlag] using
    majority_indicator (fun j => MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (P (v j))) (f x)

/-- Independent sampling is constructed, not assumed. The same distribution
is selected before every input, and arbitrary real weights remain real. -/
theorem amplified_success {n : ℕ} {I : Type*} [Fintype I]
    (f : BooleanCube n → ZMod 2) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1 - (1/3 : ℝ) ≤ success f P mu x) (x : BooleanCube n) :
    1 - tail (1/3) 15 8 ≤
      success f (fun v : Fin 15 → I => majority15 (fun j => P (v j))) (mass mu) x := by
  have hcomp := source_error_complement f P mu hs x
  have he : errorMass mu (errorFlag f P x) ≤ 1/3 := by linarith [hp x]
  have hb := failure_bound mu (errorFlag f P x) hn hs (1/3) (by norm_num) he 15 8
  have hsum : success f (fun v : Fin 15 → I => majority15 (fun j => P (v j))) (mass mu) x +
      (∑ v : Fin 15 → I, mass mu v *
        (if 8 ≤ failures (errorFlag f P x) v then 1 else 0)) = 1 := by
    unfold success
    rw [← Finset.sum_add_distrib]
    simp_rw [← mul_add, actual_majority_complement, mul_one]
    exact mass_sum mu hs 15
  linarith

/-- Generic original-predicate amplification, with total degree8*d. -/
theorem amplify {n d : ℕ} (f : BooleanCube n → ZMod 2)
    (h : HasProbabilisticDegreeAtMost f (1/3 : ℝ) d) :
    HasProbabilisticDegreeAtMost f (tail (1/3) 15 8) (8*d) := by
  obtain ⟨k, P, mu, hd, hn, hs, hp⟩ := h
  apply feasible_of_fintype
    (fun v : Fin 15 → Fin k => majority15 (fun j => P (v j))) (mass mu)
  · intro v
    exact majority15_degree _ (fun j => hd (v j))
  · exact mass_nonneg mu hn
  · exact mass_sum mu hs 15
  · exact amplified_success f P mu hn hs hp

end
end PvsNPCartography.MajorityAmplification
