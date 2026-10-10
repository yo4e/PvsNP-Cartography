import PvsNPCartography.Mod3Five

open scoped BigOperators

namespace PvsNPCartography.Mod3Five

set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

/-- All 30 distinct coefficient pairs in the n=5 orbit, sorted lexicographically.
The proof below checks each input directly and does not assume orbit coverage. -/
def upperMasks : Fin 30 → ℕ × ℕ :=
  ![(15,254), (15,445), (15,487), (15,699), (15,727), (15,823),
    (23,382), (23,477), (23,491), (23,731), (23,827), (23,855),
    (27,493), (27,638), (27,733), (27,747), (27,829), (27,871),
    (29,494), (29,734), (29,830), (29,925), (29,939), (29,967),
    (30,508), (30,762), (30,886), (30,953), (30,981), (30,995)]

def pairs : Fin 10 → Fin 5 × Fin 5 :=
  ![(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

def linCoeff (r : Fin 30) (i : Fin 5) : ℕ := (upperMasks r).1 / 2^i.val % 2

def quadCoeff (r : Fin 30) (k : Fin 10) : ℕ := (upperMasks r).2 / 2^k.val % 2

def upperValue (r : Fin 30) (x : Cube) : ℕ :=
  (1 + (∑ i, linCoeff r i * (x i).val) +
    ∑ k, quadCoeff r k * (x (pairs k).1).val * (x (pairs k).2).val) % 2

def upperCorrect (r : Fin 30) (x : Cube) : ℕ :=
  if upperValue r x = target x then 1 else 0

/-- Pointwise over all 32 inputs, not an average over each Hamming layer. -/
theorem upper_integer_bound :
    ∀ x : Cube, 21 ≤ ∑ r : Fin 30, upperCorrect r x := by
  decide +kernel

def upperFieldValue (r : Fin 30) (x : Cube) : ZMod 2 :=
  1 + (∑ i, (linCoeff r i : ZMod 2) * (x i).val) +
    ∑ k, (quadCoeff r k : ZMod 2) * (x (pairs k).1).val * (x (pairs k).2).val

theorem upper_field_correct :
    ∀ (r : Fin 30) (x : Cube), upperCorrect r x =
      if upperFieldValue r x = (target x : ZMod 2) then 1 else 0 := by
  decide +kernel

noncomputable def upperPolynomial (r : Fin 30) : MvPolynomial (Fin 5) (ZMod 2) :=
  1 + (∑ i, MvPolynomial.C (linCoeff r i : ZMod 2) * MvPolynomial.X i) +
    ∑ k, MvPolynomial.C (quadCoeff r k : ZMod 2) *
      MvPolynomial.X (pairs k).1 * MvPolynomial.X (pairs k).2

theorem upper_polynomial_eval (r : Fin 30) (x : Cube) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (upperPolynomial r) =
      upperFieldValue r x := by
  simp [upperPolynomial, upperFieldValue]

/-- The witnesses are actual Mathlib multivariate polynomials of degree <=2. -/
theorem upper_degree (r : Fin 30) : (upperPolynomial r).totalDegree ≤ 2 := by
  have hlin (c : ZMod 2) (i : Fin 5) :
      (MvPolynomial.C c * MvPolynomial.X i).totalDegree ≤ 1 := by
    simpa using MvPolynomial.totalDegree_mul (MvPolynomial.C c)
      (MvPolynomial.X i : MvPolynomial (Fin 5) (ZMod 2))
  have hquad (c : ZMod 2) (i j : Fin 5) :
      (MvPolynomial.C c * MvPolynomial.X i * MvPolynomial.X j).totalDegree ≤ 2 := by
    calc
      _ ≤ (MvPolynomial.C c * MvPolynomial.X i).totalDegree +
          (MvPolynomial.X j : MvPolynomial (Fin 5) (ZMod 2)).totalDegree :=
        MvPolynomial.totalDegree_mul _ _
      _ ≤ 1 + 1 := Nat.add_le_add (hlin c i) (by simp)
  unfold upperPolynomial
  apply (MvPolynomial.totalDegree_add _ _).trans
  apply max_le
  · apply (MvPolynomial.totalDegree_add _ _).trans
    apply max_le
    · simp
    · exact (MvPolynomial.totalDegree_finsetSum_le fun i _ => hlin _ i).trans (by decide)
  · exact MvPolynomial.totalDegree_finsetSum_le fun k _ => hquad _ _ _

theorem upper_pointwise (x : Cube) :
    (7 : ℝ) / 10 ≤ ∑ r : Fin 30, (1 / 30 : ℝ) * (upperCorrect r x : ℝ) := by
  have h : (21 : ℝ) ≤ ∑ r : Fin 30, (upperCorrect r x : ℝ) := by
    exact_mod_cast upper_integer_bound x
  calc
    (7 : ℝ) / 10 ≤ (∑ r : Fin 30, (upperCorrect r x : ℝ)) / 30 := by linarith
    _ = ∑ r : Fin 30, (1 / 30 : ℝ) * (upperCorrect r x : ℝ) := by
      rw [Finset.sum_div]
      apply Finset.sum_congr rfl
      intro r _
      ring

/-- A finite-support real probability distribution on genuine quadratic
GF(2) polynomials, chosen independently of the input. -/
theorem exists_quadratic_approximation :
    ∃ (P : Fin 30 → MvPolynomial (Fin 5) (ZMod 2)) (mu : Fin 30 → ℝ),
      (∀ r, (P r).totalDegree ≤ 2) ∧
      (∀ r, 0 ≤ mu r) ∧ (∑ r, mu r = 1) ∧
      (∀ x : Cube, (2 : ℝ) / 3 ≤ ∑ r, mu r *
        (if MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (P r) =
          (target x : ZMod 2) then 1 else 0)) := by
  refine ⟨upperPolynomial, (fun _ => 1 / 30), upper_degree, ?_, ?_, ?_⟩
  · intro r; norm_num
  · simp
  · intro x
    have h := upper_pointwise x
    have heq : ∀ r : Fin 30, (upperCorrect r x : ℝ) =
        if MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (upperPolynomial r) =
          (target x : ZMod 2) then 1 else 0 := by
      intro r
      rw [upper_polynomial_eval, upper_field_correct]
      split_ifs <;> norm_num
    simp_rw [heq] at h
    linarith

end PvsNPCartography.Mod3Five
