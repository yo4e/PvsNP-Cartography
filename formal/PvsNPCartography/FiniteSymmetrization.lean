import PvsNPCartography.PermutationTransport

open scoped BigOperators

namespace PvsNPCartography.Symmetrization

noncomputable section

/-- Uniform average over ALL variable permutations, not all Boolean inputs. -/
def orbitAverage {n : ℕ} (g : BooleanCube n → ℝ) (x : BooleanCube n) : ℝ :=
  (∑ e : Perm n, g (permuteInput e x)) / Fintype.card (Perm n)

theorem permutation_card_pos (n : ℕ) : (0 : ℝ) < Fintype.card (Perm n) := by
  exact_mod_cast (Fintype.card_pos : 0 < Fintype.card (Perm n))

/-- Only finite reindexing is used. No invariant-target premise is needed here. -/
theorem orbitAverage_invariant {n : ℕ} (g : BooleanCube n → ℝ)
    (t : Perm n) (x : BooleanCube n) :
    orbitAverage g (permuteInput t x) = orbitAverage g x := by
  classical
  let E : Perm n ≃ Perm n :=
    { toFun := fun e => e.trans t
      invFun := fun e => e.trans t.symm
      left_inv := by intro e; ext i; simp
      right_inv := by intro e; ext i; simp }
  have h := E.sum_comp (fun e => g (permuteInput e x))
  change (∑ e : Perm n, g (permuteInput e (permuteInput t x))) /
      Fintype.card (Perm n) = _
  exact congrArg (fun z : ℝ => z / Fintype.card (Perm n)) h

theorem orbitAverage_lower_bound {n : ℕ} (g : BooleanCube n → ℝ) (a : ℝ)
    (h : ∀ x, a ≤ g x) (x : BooleanCube n) : a ≤ orbitAverage g x := by
  have hc := ne_of_gt (permutation_card_pos n)
  calc
    a = (∑ _ : Perm n, a) / Fintype.card (Perm n) := by
      simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      field_simp
    _ ≤ orbitAverage g x := div_le_div_of_nonneg_right
      (Finset.sum_le_sum (fun e _ => h (permuteInput e x)))
      (le_of_lt (permutation_card_pos n))

/-- One fixed product-indexed polynomial family. Repeated rows are retained. -/
def symPolynomials {n : ℕ} {I : Type*} (P : I → BinaryPolynomial n)
    (r : I × Perm n) : BinaryPolynomial n := permutePolynomial r.2 (P r.1)

def symWeights {n : ℕ} {I : Type*} (mu : I → ℝ) (r : I × Perm n) : ℝ :=
  mu r.1 / Fintype.card (Perm n)

theorem sym_degree {n : ℕ} {I : Type*} (P : I → BinaryPolynomial n)
    {d : ℕ} (hd : ∀ i, (P i).totalDegree ≤ d) (r : I × Perm n) :
    (symPolynomials P r).totalDegree ≤ d := by
  rw [symPolynomials, permute_degree]
  exact hd r.1

theorem sym_nonneg {n : ℕ} {I : Type*} (mu : I → ℝ)
    (hn : ∀ i, 0 ≤ mu i) (r : I × Perm n) : 0 ≤ symWeights mu r :=
  div_nonneg (hn r.1) (le_of_lt (permutation_card_pos n))

theorem sym_normalized {n : ℕ} {I : Type*} [Fintype I]
    (mu : I → ℝ) (hs : ∑ i, mu i = 1) :
    (∑ r : I × Perm n, symWeights mu r) = 1 := by
  classical
  have hc := ne_of_gt (permutation_card_pos n)
  calc
    (∑ r : I × Perm n, symWeights mu r) =
        ∑ i, ∑ _ : Perm n, mu i / Fintype.card (Perm n) := by
      simp only [symWeights, Fintype.sum_prod_type]
    _ = ∑ i, mu i := by
      apply Finset.sum_congr rfl
      intro i _
      simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      field_simp
    _ = 1 := hs

/-- Exact bridge: averaging polynomials in the distribution equals averaging
success on the input orbit. The target-symmetry premise is essential. -/
theorem sym_success_eq_average {n : ℕ} {I : Type*} [Fintype I]
    {f : BooleanCube n → ZMod 2} (hf : IsSymmetric f)
    (P : I → BinaryPolynomial n) (mu : I → ℝ) (x : BooleanCube n) :
    success f (symPolynomials P) (symWeights mu) x =
      orbitAverage (success f P mu) x := by
  classical
  unfold success
  simp only [Fintype.sum_prod_type, symPolynomials, symWeights, correct_permute hf]
  rw [Finset.sum_comm]
  simp only [orbitAverage, Finset.sum_div, div_mul_eq_mul_div]

theorem sym_success_invariant {n : ℕ} {I : Type*} [Fintype I]
    {f : BooleanCube n → ZMod 2} (hf : IsSymmetric f)
    (P : I → BinaryPolynomial n) (mu : I → ℝ) (t : Perm n) (x : BooleanCube n) :
    success f (symPolynomials P) (symWeights mu) (permuteInput t x) =
      success f (symPolynomials P) (symWeights mu) x := by
  rw [sym_success_eq_average hf, sym_success_eq_average hf, orbitAverage_invariant]

/-- A full orbit-average certificate suffices for the original pointwise
predicate. It is NOT enough to give one average over the whole Boolean cube. -/
theorem feasible_of_orbit_bounds {n : ℕ} {I : Type} [Fintype I]
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d : ℕ}
    (hf : IsSymmetric f) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1)
    (ha : ∀ x, 1 - epsilon ≤ orbitAverage (success f P mu) x) :
    HasProbabilisticDegreeAtMost f epsilon d := by
  apply feasible_of_fintype (symPolynomials P) (symWeights mu)
    (sym_degree P hd) (sym_nonneg mu hn) (sym_normalized mu hs)
  intro x
  rw [sym_success_eq_average hf]
  exact ha x

/-- Symmetrization preserves all semantic obligations, and additionally makes
success invariant. The witness family is fixed before any input is chosen. -/
theorem symmetrization_preserves {n : ℕ} {I : Type} [Fintype I]
    {f : BooleanCube n → ZMod 2} {epsilon : ℝ} {d : ℕ}
    (hf : IsSymmetric f) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ d) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) (hp : ∀ x, 1 - epsilon ≤ success f P mu x) :
    (∀ r : I × Perm n, (symPolynomials P r).totalDegree ≤ d) ∧
    (∀ r : I × Perm n, 0 ≤ symWeights mu r) ∧
    (∑ r : I × Perm n, symWeights mu r = 1) ∧
    (∀ x, 1 - epsilon ≤ success f (symPolynomials P) (symWeights mu) x) ∧
    (∀ t x, success f (symPolynomials P) (symWeights mu) (permuteInput t x) =
      success f (symPolynomials P) (symWeights mu) x) := by
  refine ⟨sym_degree P hd, sym_nonneg mu hn, sym_normalized mu hs, ?_,
    sym_success_invariant hf P mu⟩
  intro x
  rw [sym_success_eq_average hf]
  exact orbitAverage_lower_bound (success f P mu) (1 - epsilon) hp x

/-- Equivalent certificates with the original field, actual degree, real
probabilities and quantifier order. No finite experiment is generalized here. -/
theorem feasible_iff_orbit_average {n : ℕ} {f : BooleanCube n → ZMod 2}
    {epsilon : ℝ} {d : ℕ} (hf : IsSymmetric f) :
    HasProbabilisticDegreeAtMost f epsilon d ↔
      ∃ (m : ℕ) (P : Fin m → BinaryPolynomial n) (mu : Fin m → ℝ),
        (∀ i, (P i).totalDegree ≤ d) ∧ (∀ i, 0 ≤ mu i) ∧
        (∑ i, mu i = 1) ∧
        (∀ x, 1 - epsilon ≤ orbitAverage (success f P mu) x) := by
  constructor
  · rintro ⟨m, P, mu, hd, hn, hs, hp⟩
    exact ⟨m, P, mu, hd, hn, hs,
      orbitAverage_lower_bound (success f P mu) (1 - epsilon) hp⟩
  · rintro ⟨m, P, mu, hd, hn, hs, ha⟩
    exact feasible_of_orbit_bounds hf P mu hd hn hs ha

end
end PvsNPCartography.Symmetrization
