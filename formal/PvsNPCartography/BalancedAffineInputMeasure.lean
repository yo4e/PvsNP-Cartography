import PvsNPCartography.BalancedAffineObstruction
import PvsNPCartography.BalancedAffineBinomial

open scoped BigOperators

namespace PvsNPCartography.BalancedAffineCounting

open Symmetrization SmallSupportMod3

noncomputable section

/-- Push the sample probability to the actual Boolean cube, adding fiber masses.
No injectivity of sampleInput and no uniform-fiber claim is assumed. -/
def inputMass {n : ℕ} (x : BooleanCube n) : ℝ := by
  classical
  exact ∑ s : Sample n, if sampleInput s = x then sampleMass n s else 0

theorem inputMass_nonneg {n : ℕ} (hn : 3 ≤ n) (x : BooleanCube n) :
    0 ≤ inputMass x := by
  classical
  unfold inputMass
  apply Finset.sum_nonneg
  intro s _
  split_ifs
  · exact sampleMass_nonneg hn s
  · norm_num

/-- Finite change of variables, with duplicate masses added rather than dropped. -/
theorem inputMass_mean {n : ℕ} (g : BooleanCube n → ℝ) :
    (∑ x, inputMass x * g x) = ∑ s : Sample n, sampleMass n s * g (sampleInput s) := by
  classical
  unfold inputMass
  simp_rw [Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro s _
  simp only [ite_mul, zero_mul]
  simp

theorem inputMass_sum {n : ℕ} (hn : 3 ≤ n) :
    (∑ x : BooleanCube n, inputMass x) = 1 := by
  calc
    _ = ∑ s : Sample n, sampleMass n s := by
      simpa using inputMass_mean (fun _ : BooleanCube n => (1 : ℝ))
    _ = 1 := sampleMass_sum hn

theorem inputMass_affine_score {n : ℕ} (p : Affine n) :
    (∑ x, inputMass x * (affineCorrect p x : ℝ)) = sampleScore p :=
  inputMass_mean (fun x => (affineCorrect p x : ℝ))

theorem singleton_success_count {n : ℕ} (b : BooleanCube n) :
    (∑ i : Fin n, (affineCorrect (0,b) (sampleInput (.inl i)) : ℝ)) =
      (n : ℝ) - hammingWeight b := by
  have he (i : Fin n) : (affineCorrect (0,b) (sampleInput (.inl i)) : ℝ) =
      1 - (b i).val := by
    rw [singleton_correct]
    norm_num [bitSign]
    ring
  simp_rw [he]
  simp [Finset.sum_sub_distrib, hammingWeight]

/-- The actual number of successful ordered distinct triples. The factor six
is explicit; this does not count repeated coordinates or discard their weights. -/
theorem ordered_triple_success_count {n : ℕ} (b : BooleanCube n) :
    (∑ i : Fin n, ∑ j : Fin n, ∑ k : Fin n,
      if Distinct i j k then (affineCorrect (0,b) (sampleInput (.inr (i,j,k))) : ℝ) else 0) =
      6 * ((hammingWeight b : ℝ) * ((n - hammingWeight b).choose 2 : ℝ) +
        ((hammingWeight b).choose 3 : ℝ)) := by
  classical
  have he (i j k : Fin n) :
      (if Distinct i j k then (affineCorrect (0,b) (sampleInput (.inr (i,j,k))) : ℝ) else 0) =
      ((if Distinct i j k then (1 : ℝ) else 0) -
        (if Distinct i j k then bitSign (b i) * bitSign (b j) * bitSign (b k) else 0)) / 2 := by
    by_cases hd : Distinct i j k
    · simpa [hd, bitSign] using triple_correct (0,b) i j k hd
    · simp [hd]
  simp_rw [he]
  simp only [← Finset.sum_div, Finset.sum_sub_distrib]
  rw [ordered_triple_count, sign_triple_moment, bitSign_sum]
  simp only [choose_two_cast, choose_three_cast, Nat.cast_sub (hammingWeight_le b)]
  ring

/-- The binomial expression is now connected to actual input correctness,
not merely to another freely defined algebraic function. -/
theorem actual_score_binomial {n : ℕ} (hn : 3 ≤ n) (b : BooleanCube n) :
    (∑ x, inputMass x * (affineCorrect (0,b) x : ℝ)) = countedScore n (hammingWeight b) := by
  rw [inputMass_affine_score, sampleScore_zero hn]
  exact (countedScore_eq hn (hammingWeight_le b)).symm

theorem polynomial_input_bound {n : ℕ} (hn : 7 ≤ n) (P : BinaryPolynomial n)
    (hd : P.totalDegree ≤ 1) :
    (∑ x, inputMass x * (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P =
      target x then (1 : ℝ) else 0)) ≤ envelope n := by
  classical
  have he (x : BooleanCube n) : (affineCorrect (coefficientRow P) x : ℝ) =
      if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P = target x then 1 else 0 := by
    rw [affine_polynomial_correct, ← degree_one_eq_affine P hd]
  simp_rw [← he]
  rw [inputMass_affine_score]
  exact sampleScore_bound hn (coefficientRow P)

/-- The boundary failure is about this particular input measure, not about
existence of some different n=6 dual or the already proved n=6 degree equality. -/
theorem six_balanced_dual_tight :
    sampleScore (0, (![1,0,0,0,0,0] : BooleanCube 6)) = (2 : ℝ) / 3 := by
  rw [sampleScore_zero (by decide)]
  convert BalancedAffineDualAlgebra.six_is_tight using 1
  norm_num [hammingWeight, Fin.sum_univ_succ]

end
end PvsNPCartography.BalancedAffineCounting
