import PvsNPCartography.GF4Transport

open scoped BigOperators

namespace PvsNPCartography.Mod3Restrictions
noncomputable section
attribute [local instance] Classical.propDecidable

def zeroVariables {n : ℕ} : Fin (n+1) → BinaryPolynomial n :=
  Fin.cons (MvPolynomial.C 0) MvPolynomial.X

def padZero {n : ℕ} (x : BooleanCube n) : BooleanCube (n+1) := Fin.cons 0 x

/-- Actual zero restriction, preserving the source coefficients and all weights. -/
def restrictZero {n : ℕ} (P : BinaryPolynomial (n+1)) : BinaryPolynomial n :=
  MvPolynomial.eval₂ (MvPolynomial.C.comp (RingHom.id (ZMod 2))) zeroVariables P

theorem restrictZero_degree {n : ℕ} (P : BinaryPolynomial (n+1)) :
    (restrictZero P).totalDegree ≤ P.totalDegree := by
  apply GF4Transport.affine_substitution_degree
  intro j
  refine Fin.cases ?_ (fun k => ?_) j <;> simp [zeroVariables]

theorem restrictZero_eval {n : ℕ} (P : BinaryPolynomial (n+1)) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (restrictZero P) =
      MvPolynomial.eval (fun i => ((padZero x i).val : ZMod 2)) P := by
  have hc : (MvPolynomial.eval (fun i => ((x i).val : ZMod 2))).comp
      (MvPolynomial.C.comp (RingHom.id (ZMod 2))) = RingHom.id (ZMod 2) := by
    ext c
    simp
  have hv : (fun i => MvPolynomial.eval (fun j => ((x j).val : ZMod 2))
      (zeroVariables i)) = (fun i => ((padZero x i).val : ZMod 2)) := by
    funext i
    refine Fin.cases ?_ (fun k => ?_) i <;> simp [zeroVariables, padZero]
  rw [restrictZero, MvPolynomial.eval_eval₂, hc, hv, MvPolynomial.eval₂_id]

theorem target_zero {n : ℕ} (x : BooleanCube n) :
    SmallSupportMod3.target (padZero x) = SmallSupportMod3.target x := by
  simp [SmallSupportMod3.target, padZero, Fin.sum_univ_succ]

theorem restrict_one {n d : ℕ} {epsilon : ℝ}
    (h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target (n+1)) epsilon d) :
    HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) epsilon d := by
  obtain ⟨k, P, mu, hd, hn, hs, hp⟩ := h
  refine ⟨k, (fun i => restrictZero (P i)), mu,
    (fun i => (restrictZero_degree (P i)).trans (hd i)), hn, hs, ?_⟩
  intro x
  simpa only [restrictZero_eval, target_zero] using hp (padZero x)

theorem restrict_add (m k : ℕ) {d : ℕ} {epsilon : ℝ}
    (h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target (m+k)) epsilon d) :
    HasProbabilisticDegreeAtMost (@SmallSupportMod3.target m) epsilon d := by
  revert h
  induction k with
  | zero => intro h; exact h
  | succ k ih => intro h; exact ih (restrict_one h)

theorem restrict_le (m n : ℕ) (hmn : m ≤ n) {d : ℕ} {epsilon : ℝ}
    (h : HasProbabilisticDegreeAtMost (@SmallSupportMod3.target n) epsilon d) :
    HasProbabilisticDegreeAtMost (@SmallSupportMod3.target m) epsilon d := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hmn
  exact restrict_add m k h

end
end PvsNPCartography.Mod3Restrictions
