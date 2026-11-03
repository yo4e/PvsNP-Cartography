import PvsNPCartography.IntegerPolynomialLift

open scoped BigOperators

namespace PvsNPCartography.BooleanIntegerReduction
noncomputable section
attribute [local instance] Classical.propDecidable

/-- The squarefree monomial supported at the original nonzero exponents. -/
def squarefreeMonomial {σ R : Type*} [CommRing R] (e : σ →₀ ℕ) : MvPolynomial σ R :=
  ∏ i ∈ e.support, MvPolynomial.X i

/-- Ring-generic reduction; no field or characteristic-two premise. -/
def reduce {σ R : Type*} [CommRing R] (P : MvPolynomial σ R) : MvPolynomial σ R :=
  ∑ e ∈ P.support, MvPolynomial.C (P.coeff e) * squarefreeMonomial e

theorem support_card_le_sum {σ : Type*} (e : σ →₀ ℕ) :
    e.support.card ≤ e.sum (fun _ k => k) := by
  calc
    e.support.card = ∑ _i ∈ e.support, 1 := by simp
    _ ≤ ∑ i ∈ e.support, e i := by
      apply Finset.sum_le_sum
      intro i hi
      have h := Finsupp.mem_support_iff.mp hi
      omega
    _ = e.sum (fun _ k => k) := rfl

theorem squarefree_degree {σ R : Type*} [CommRing R] [Nontrivial R] (e : σ →₀ ℕ) :
    (squarefreeMonomial e : MvPolynomial σ R).totalDegree ≤ e.support.card := by
  calc
    _ ≤ ∑ i ∈ e.support, (MvPolynomial.X i : MvPolynomial σ R).totalDegree :=
      MvPolynomial.totalDegree_finsetProd _ _
    _ = e.support.card := by simp

theorem reduce_degree {σ R : Type*} [CommRing R] [Nontrivial R] (P : MvPolynomial σ R) :
    (reduce P).totalDegree ≤ P.totalDegree := by
  apply MvPolynomial.totalDegree_finsetSum_le
  intro e he
  calc
    _ ≤ (MvPolynomial.C (P.coeff e)).totalDegree +
        (squarefreeMonomial e : MvPolynomial σ R).totalDegree := MvPolynomial.totalDegree_mul _ _
    _ ≤ e.support.card := by simpa using (squarefree_degree (R := R) e)
    _ ≤ e.sum (fun _ k => k) := support_card_le_sum e
    _ ≤ P.totalDegree := MvPolynomial.le_totalDegree he

/-- Equality only at Boolean points, not equality of formal polynomials. -/
theorem reduce_eval {σ R : Type*} [CommRing R] (P : MvPolynomial σ R)
    (x : σ → R) (hx : ∀ i, x i = 0 ∨ x i = 1) :
    MvPolynomial.eval x (reduce P) = MvPolynomial.eval x P := by
  calc
    _ = ∑ e ∈ P.support, P.coeff e * ∏ i ∈ e.support, x i := by
      simp [reduce, squarefreeMonomial, map_sum, map_prod]
    _ = ∑ e ∈ P.support, P.coeff e * ∏ i ∈ e.support, x i ^ e i := by
      apply Finset.sum_congr rfl
      intro e _
      congr 1
      apply Finset.prod_congr rfl
      intro i hi
      have hn : e i ≠ 0 := Finsupp.mem_support_iff.mp hi
      rcases hx i with h | h <;> simp [h, hn]
    _ = MvPolynomial.eval x P := by
      simpa only [MvPolynomial.eval₂_id, RingHom.id_apply] using
        (MvPolynomial.eval₂_eq (RingHom.id R) x P).symm

/-- The explicit composed-and-reduced integer polynomial used by the prototype. -/
def blockPolynomial {σ : Type*} (ell : ℕ) (P : MvPolynomial σ (ZMod 2)) :
    MvPolynomial σ ℤ := reduce (IntegerPolynomialLift.amplified ell P)

theorem blockPolynomial_degree {σ : Type*} (ell d : ℕ) (P : MvPolynomial σ (ZMod 2))
    (hd : P.totalDegree ≤ d) : (blockPolynomial ell P).totalDegree ≤ (2*ell+1)*d :=
  (reduce_degree _).trans (IntegerPolynomialLift.amplified_degree ell d P hd)

theorem blockPolynomial_count {a b : ℕ} (P : BinaryPolynomial (a+b)) (x : BooleanCube a) :
    (∑ y : BooleanCube b, MvPolynomial.eval (IntegerPolynomialLift.joined x y)
      (blockPolynomial b P)) % (2 : ℤ)^(b+1) =
      (IntegerPolynomialLift.acceptingCount P x : ℤ) := by
  have hbits (y : BooleanCube b) (i : Fin (a+b)) :
      IntegerPolynomialLift.joined x y i = 0 ∨ IntegerPolynomialLift.joined x y i = 1 := by
    unfold IntegerPolynomialLift.joined
    have h := (Fin.addCases (motive := fun _ => Fin 2) x y i).isLt
    have hh : (Fin.addCases (motive := fun _ => Fin 2) x y i).val = 0 ∨ (Fin.addCases (motive := fun _ => Fin 2) x y i).val = 1 := by omega
    rcases hh with h | h <;> simp [h]
  have he (y : BooleanCube b) :
      MvPolynomial.eval (IntegerPolynomialLift.joined x y) (blockPolynomial b P) =
      MvPolynomial.eval (IntegerPolynomialLift.joined x y) (IntegerPolynomialLift.amplified b P) :=
    reduce_eval _ _ (hbits y)
  simp_rw [he]
  exact IntegerPolynomialLift.exact_block_count P x

end
end PvsNPCartography.BooleanIntegerReduction
