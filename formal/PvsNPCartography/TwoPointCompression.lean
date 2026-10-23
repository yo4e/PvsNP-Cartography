import Mathlib

open scoped BigOperators

namespace PvsNPCartography.TwoPointCompression

noncomputable section
variable {K : Type*} [Field K] {n : ℕ}

/-- Actual squarefree polynomial, not a truth-table encoding. -/
def squarefree (S : Finset (Fin n)) : MvPolynomial (Fin n) K :=
  ∏ i ∈ S, MvPolynomial.X i

/-- On the nonzero two-point grid, this affine polynomial is the inverse of X_i. -/
def inverseFactor (a b : K) (i : Fin n) : MvPolynomial (Fin n) K :=
  (MvPolynomial.C (a + b) - MvPolynomial.X i) * MvPolynomial.C ((a * b)⁻¹)

def inverseProduct (a b : K) (S : Finset (Fin n)) : MvPolynomial (Fin n) K :=
  ∏ i ∈ S, inverseFactor a b i

theorem squarefree_degree (S : Finset (Fin n)) :
    (squarefree S : MvPolynomial (Fin n) K).totalDegree ≤ S.card := by
  classical
  induction S using Finset.induction_on with
  | empty => simp [squarefree]
  | @insert i S hi ih =>
    simp only [squarefree, Finset.prod_insert hi] at *
    calc
      _ ≤ (MvPolynomial.X i : MvPolynomial (Fin n) K).totalDegree +
          (∏ j ∈ S, MvPolynomial.X j : MvPolynomial (Fin n) K).totalDegree :=
        MvPolynomial.totalDegree_mul _ _
      _ ≤ (insert i S).card := by
        rw [MvPolynomial.totalDegree_X, Finset.card_insert_of_notMem hi]
        omega

theorem inverseFactor_degree (a b : K) (i : Fin n) :
    (inverseFactor a b i).totalDegree ≤ 1 := by
  apply (MvPolynomial.totalDegree_mul _ _).trans
  simp only [MvPolynomial.totalDegree_C, add_zero]
  apply (MvPolynomial.totalDegree_sub _ _).trans
  norm_num only [MvPolynomial.totalDegree_C, MvPolynomial.totalDegree_X]

theorem inverseProduct_degree (a b : K) (S : Finset (Fin n)) :
    (inverseProduct a b S).totalDegree ≤ S.card := by
  classical
  induction S using Finset.induction_on with
  | empty => simp [inverseProduct]
  | @insert i S hi ih =>
    have he : inverseProduct a b (insert i S) =
        inverseFactor a b i * inverseProduct a b S := by
      simp only [inverseProduct, Finset.prod_insert hi]
    rw [he, Finset.card_insert_of_notMem hi]
    exact (MvPolynomial.totalDegree_mul _ _).trans
      (by have h := inverseFactor_degree a b i; omega)

/-- Nonzeroness is essential. No root-of-unity premise is needed for this step. -/
theorem inverseFactor_mul (a b : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (y : Fin n → K) (hy : ∀ i, y i = a ∨ y i = b) (i : Fin n) :
    y i * MvPolynomial.eval y (inverseFactor a b i) = 1 := by
  simp only [inverseFactor, map_mul, map_sub, MvPolynomial.eval_C, MvPolynomial.eval_X]
  rcases hy i with h | h
  · rw [h]
    have he : a * ((a + b - a) * (a * b)⁻¹) = (a * b) * (a * b)⁻¹ := by ring
    rw [he, mul_inv_cancel₀ (mul_ne_zero ha hb)]
  · rw [h]
    have he : b * ((a + b - b) * (a * b)⁻¹) = (a * b) * (a * b)⁻¹ := by ring
    rw [he, mul_inv_cancel₀ (mul_ne_zero ha hb)]

/-- Replace a high-support monomial by R times affine inverses of its complement.
The equality is ONLY asserted where R equals the full coordinate product. -/
theorem complement_reduction_eval (a b : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (R : MvPolynomial (Fin n) K) (S : Finset (Fin n))
    (y : Fin n → K) (hy : ∀ i, y i = a ∨ y i = b)
    (hR : MvPolynomial.eval y R = ∏ i, y i) :
    MvPolynomial.eval y (R * inverseProduct a b Sᶜ) = ∏ i ∈ S, y i := by
  classical
  simp only [map_mul, inverseProduct, map_prod]
  rw [hR, ← Finset.prod_mul_prod_compl S (fun i => y i), mul_assoc,
    ← Finset.prod_mul_distrib]
  have hc : (∏ i ∈ Sᶜ, y i * MvPolynomial.eval y (inverseFactor a b i)) = 1 := by
    apply Finset.prod_eq_one
    intro i _
    exact inverseFactor_mul a b ha hb y hy i
  rw [hc, mul_one]

theorem complement_reduction_degree (a b : K)
    (R : MvPolynomial (Fin n) K) (S : Finset (Fin n)) :
    (R * inverseProduct a b Sᶜ).totalDegree ≤ R.totalDegree + (n - S.card) := by
  have hc : (Sᶜ).card = n - S.card := by
    rw [Finset.card_compl, Fintype.card_fin]
  exact (MvPolynomial.totalDegree_mul _ _).trans
    (Nat.add_le_add_left ((inverseProduct_degree a b Sᶜ).trans_eq hc) _)

/-- The substantive compression lemma, with actual polynomials and actual degree.
For t=floor((n+d)/2), n+d<=2*t+1 holds. No agreement count is assumed. -/
theorem compress_monomial (a b : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (R : MvPolynomial (Fin n) K) (d t : ℕ) (hdegree : R.totalDegree ≤ d)
    (hthreshold : n + d ≤ 2 * t + 1) (S : Finset (Fin n)) :
    ∃ Q : MvPolynomial (Fin n) K, Q.totalDegree ≤ t ∧
      ∀ y : Fin n → K, (∀ i, y i = a ∨ y i = b) →
        MvPolynomial.eval y R = (∏ i, y i) →
        MvPolynomial.eval y Q = ∏ i ∈ S, y i := by
  classical
  by_cases hsmall : S.card ≤ t
  · refine ⟨squarefree S, (squarefree_degree S).trans hsmall, ?_⟩
    intro y _ _
    simp [squarefree]
  · refine ⟨R * inverseProduct a b Sᶜ, ?_, ?_⟩
    · have hcard : S.card ≤ n := (Finset.card_le_univ S).trans_eq (Fintype.card_fin n)
      exact (complement_reduction_degree a b R S).trans (by omega)
    · intro y hy hR
      exact complement_reduction_eval a b ha hb R S y hy hR

/-- A concrete attack on dropping the nonzero-grid hypothesis. -/
theorem zero_grid_breaks_inverse :
    (0 : ℚ) * ((0 + 1 - 0) * (0 * 1)⁻¹) ≠ 1 := by norm_num

/-- A kernel-checked finite identity used in the separate majority15 bridge.
It is not a probabilistic error-reduction theorem. -/
theorem majority15_binomial (w : ℕ) (hw : w ≤ 15) :
    w.choose 8 % 2 = if 8 ≤ w then 1 else 0 := by
  interval_cases w <;> norm_num [Nat.choose]

end
end PvsNPCartography.TwoPointCompression
