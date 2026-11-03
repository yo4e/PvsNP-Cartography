import PvsNPCartography.ModulusAmplification

open scoped BigOperators

namespace PvsNPCartography.IntegerPolynomialLift
open ModulusAmplification
noncomputable section
attribute [local instance] Classical.propDecidable

/-- Coefficientwise canonical lift. It is deliberately NOT declared a ring homomorphism. -/
def lift {σ : Type*} (P : MvPolynomial σ (ZMod 2)) : MvPolynomial σ ℤ :=
  ∑ e ∈ P.support, MvPolynomial.monomial e ((P.coeff e).val : ℤ)

theorem lift_degree {σ : Type*} (P : MvPolynomial σ (ZMod 2)) :
    (lift P).totalDegree ≤ P.totalDegree := by
  apply MvPolynomial.totalDegree_finsetSum_le
  intro e he
  exact (MvPolynomial.totalDegree_monomial_le e _).trans (MvPolynomial.le_totalDegree he)

/-- Reduction modulo two, not exact integer arithmetic, recovers the source. -/
theorem map_lift {σ : Type*} (P : MvPolynomial σ (ZMod 2)) :
    MvPolynomial.map (Int.castRingHom (ZMod 2)) (lift P) = P := by
  calc
    _ = ∑ e ∈ P.support, MvPolynomial.monomial e (P.coeff e) := by
      simp [lift, map_sum]
    _ = P := P.as_sum.symm

theorem eval_lift_cast {σ : Type*} (P : MvPolynomial σ (ZMod 2)) (x : σ → ℤ) :
    ((MvPolynomial.eval x (lift P) : ℤ) : ZMod 2) =
      MvPolynomial.eval (fun i => (x i : ZMod 2)) P := by
  have h := MvPolynomial.map_eval (Int.castRingHom (ZMod 2)) x (lift P)
  rw [map_lift] at h
  exact h

theorem eval_lift_parity {σ : Type*} (P : MvPolynomial σ (ZMod 2)) (x : σ → ℤ) :
    MvPolynomial.eval x (lift P) % 2 =
      ((MvPolynomial.eval (fun i => (x i : ZMod 2)) P).val : ℤ) := by
  have h := ZMod.val_intCast (n := 2) (MvPolynomial.eval x (lift P))
  rw [eval_lift_cast] at h
  exact h.symm

/-- The composed polynomial retains its genuine, unreduced total degree. -/
def amplified {σ : Type*} (ell : ℕ) (P : MvPolynomial σ (ZMod 2)) :
    MvPolynomial σ ℤ := amplify (ell+1) (lift P)

theorem amplified_degree {σ : Type*} (ell d : ℕ) (P : MvPolynomial σ (ZMod 2))
    (hd : P.totalDegree ≤ d) : (amplified ell P).totalDegree ≤ (2*ell+1)*d := by
  have h := polynomial_degree (lift P) (ell+1) d (by omega) ((lift_degree P).trans hd)
  have he : 2*(ell+1)-1 = 2*ell+1 := by omega
  simpa only [amplified, he] using h

theorem amplified_eval {σ : Type*} (ell : ℕ) (P : MvPolynomial σ (ZMod 2))
    (x : σ → ℤ) : MvPolynomial.eval x (amplified ell P) ≡
      ((MvPolynomial.eval (fun i => (x i : ZMod 2)) P).val : ℤ)
      [ZMOD (2 : ℤ)^(ell+1)] := by
  rw [amplified, map_amplify]
  simpa only [eval_lift_parity] using
    parity_congruence (ell+1) (by omega) (MvPolynomial.eval x (lift P))

def joined {a b : ℕ} (x : BooleanCube a) (y : BooleanCube b) : Fin (a+b) → ℤ :=
  fun i => ((Fin.addCases (motive := fun _ => Fin 2) x y i).val : ℤ)

def acceptingCount {a b : ℕ} (P : BinaryPolynomial (a+b)) (x : BooleanCube a) : ℕ :=
  (Finset.univ.filter (fun y : BooleanCube b =>
    MvPolynomial.eval (fun i => (joined x y i : ZMod 2)) P = 1)).card

theorem parity_one_iff (v : ℤ) : v % 2 = 1 ↔ (v : ZMod 2) = 1 := by
  simpa using (ZMod.intCast_eq_intCast_iff' v 1 2).symm

/-- Actual source polynomial, actual accepting inputs, actual composed polynomial.
This identity alone does not certify an efficient way of forming the tail sum. -/
theorem exact_block_count {a b : ℕ} (P : BinaryPolynomial (a+b)) (x : BooleanCube a) :
    (∑ y : BooleanCube b, MvPolynomial.eval (joined x y) (amplified b P)) %
      (2 : ℤ)^(b+1) = (acceptingCount P x : ℤ) := by
  let v : BooleanCube b → ℤ := fun y => MvPolynomial.eval (joined x y) (lift P)
  have he (y : BooleanCube b) :
      MvPolynomial.eval (joined x y) (amplified b P) = amplify (b+1) (v y) :=
    map_amplify (MvPolynomial.eval (joined x y)) (b+1) (lift P)
  have hc : oddCount v = acceptingCount P x := by
    unfold oddCount acceptingCount
    congr 1
    ext y
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    change MvPolynomial.eval (joined x y) (lift P) % 2 = 1 ↔
      MvPolynomial.eval (fun i => (joined x y i : ZMod 2)) P = 1
    rw [parity_one_iff, eval_lift_cast]
  simp_rw [he]
  rw [boolean_block_no_wrap, hc]

end
end PvsNPCartography.IntegerPolynomialLift
