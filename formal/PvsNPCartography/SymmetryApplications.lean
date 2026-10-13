import PvsNPCartography.FiniteSymmetrization
import PvsNPCartography.SmallSupportMod3

open scoped BigOperators

namespace PvsNPCartography.Symmetrization

noncomputable section

/-- The actual MOD3 target is symmetric at every arity. This is not a statement
about its probabilistic degree at every arity. -/
theorem mod3_symmetric (n : ℕ) : IsSymmetric (@SmallSupportMod3.target n) := by
  intro e x
  unfold SmallSupportMod3.target
  rw [permute_weight]

/-- A closed application to the previously verified n=6/n=7 witnesses.
No feasibility hypothesis is requested from the caller. The constructed
product-indexed family retains genuine polynomials and real probabilities. -/
theorem mod3_symmetric_witness (n : ℕ) (hn : n = 6 ∨ n = 7) :
    ∃ (m : ℕ) (P : Fin m → BinaryPolynomial n) (mu : Fin m → ℝ),
      (∀ r : Fin m × Perm n, (symPolynomials P r).totalDegree ≤ 2) ∧
      (∀ r : Fin m × Perm n, 0 ≤ symWeights mu r) ∧
      (∑ r : Fin m × Perm n, symWeights mu r = 1) ∧
      (∀ x, 1 - (1 / 3 : ℝ) ≤
        success (@SmallSupportMod3.target n) (symPolynomials P) (symWeights mu) x) ∧
      (∀ t x, success (@SmallSupportMod3.target n) (symPolynomials P) (symWeights mu)
          (permuteInput t x) =
        success (@SmallSupportMod3.target n) (symPolynomials P) (symWeights mu) x) := by
  have h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) (1 / 3 : ℝ) 2 :=
    (SmallSupportMod3.feasible_degree_iff n hn 2).mpr (by decide)
  obtain ⟨m, P, mu, hd, hp, hs, hx⟩ := h
  exact ⟨m, P, mu, symmetrization_preserves (mod3_symmetric n) P mu hd hp hs hx⟩

def firstCoordinate (x : BooleanCube 2) : ZMod 2 := ((x 0).val : ZMod 2)

def swapTwo : Perm 2 := Equiv.swap 0 1

def oneZero : BooleanCube 2 := ![1, 0]

/-- An actual polynomial counterexample to omitting target symmetry from the
correctness-transport identity. The renaming/evaluation identity stays valid. -/
theorem target_symmetry_is_needed :
    correct firstCoordinate
      (permutePolynomial swapTwo (MvPolynomial.X 0)) oneZero = 0 ∧
    correct firstCoordinate (MvPolynomial.X 0) (permuteInput swapTwo oneZero) = 1 := by
  norm_num [correct, firstCoordinate, permutePolynomial, permuteInput, swapTwo, oneZero]

/-- Three of four inputs agree with zero, but the all-one orbit still fails.
This is a countermodel to substituting a whole-cube average for orbit bounds. -/
def andTwo (x : BooleanCube 2) : ℕ := if x 0 = 1 ∧ x 1 = 1 then 1 else 0

theorem whole_cube_average_is_insufficient :
    (∑ x : BooleanCube 2, if andTwo x = 0 then (1 : ℕ) else 0) = 3 ∧
    andTwo (![1, 1] : BooleanCube 2) = 1 := by
  decide +kernel

/-- Probability weights live in R, not the characteristic-two coefficient field. -/
theorem field_average_is_not_probability_average :
    (2 : ZMod 2) = 0 ∧ (1 / 2 : ZMod 2) = 0 ∧ (0 : ℝ) < 1 / 2 := by
  have htwo : (2 : ZMod 2) = 0 := by decide +kernel
  refine ⟨htwo, ?_, by norm_num⟩
  rw [htwo, div_zero]

end
end PvsNPCartography.Symmetrization
