import PvsNPCartography.CircuitMod3

open scoped BigOperators

namespace PvsNPCartography.RootBudget
open SharedDAG RandomizedGates Symmetrization
noncomputable section
attribute [local instance] Classical.propDecidable
set_option maxHeartbeats 2400000

/-- false selects OR, true selects AND. No arbitrary output gate is admitted. -/
def root {n m K : ℕ} (b : Bool) (ws : Slots n m K) : Gate n m K :=
  match b with
  | false => .disj ws
  | true => .conj ws

theorem root_cost {n m K : ℕ} (b : Bool) (ws : Slots n m K) :
    (root b ws).cost = 1 := by cases b <;> rfl

abbrev Sample (K r t : ℕ) := Matrix K r × Matrix K t

/-- An explicit product distribution, fixed before every input. -/
def weight (K r t : ℕ) (z : Sample K r t) : ℝ :=
  matrixWeight K z.1 * matrixWeight K z.2

theorem weight_nonneg (K r t : ℕ) (z : Sample K r t) : 0 ≤ weight K r t z :=
  mul_nonneg (matrixWeight_nonneg K r z.1) (matrixWeight_nonneg K t z.2)

theorem fst_marginal (K r t : ℕ) (F : Matrix K r → ℝ) :
    (∑ z : Sample K r t, weight K r t z * F z.1) =
      ∑ A : Matrix K r, matrixWeight K A * F A := by
  rw [Fintype.sum_prod_type]
  change (∑ A : Matrix K r, ∑ B : Matrix K t,
    (matrixWeight K A * matrixWeight K B) * F A) = _
  calc
    _ = ∑ A : Matrix K r, (matrixWeight K A * F A) *
        (∑ B : Matrix K t, matrixWeight K B) := by
      apply Finset.sum_congr rfl
      intro A _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro B _
      ring
    _ = _ := by simp only [matrixWeight_sum, mul_one]

theorem snd_marginal (K r t : ℕ) (F : Matrix K t → ℝ) :
    (∑ z : Sample K r t, weight K r t z * F z.2) =
      ∑ B : Matrix K t, matrixWeight K B * F B := by
  rw [Fintype.sum_prod_type]
  change (∑ A : Matrix K r, ∑ B : Matrix K t,
    (matrixWeight K A * matrixWeight K B) * F B) = _
  simp_rw [mul_assoc, ← Finset.mul_sum]
  rw [← Finset.sum_mul, matrixWeight_sum, one_mul]

theorem weight_sum (K r t : ℕ) : (∑ z : Sample K r t, weight K r t z) = 1 := by
  have h := fst_marginal K r t (fun _ => 1)
  simp only [mul_one] at h
  rw [h, matrixWeight_sum]

/-- Actual polynomial substitution; repeated references are not multilinearized. -/
def poly {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (z : Sample K r t) : BinaryPolynomial n :=
  (root b ws).poly z.2 (polynomials z.1 p)

def value {n m K : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (x : Fin n → ZMod 2) : ZMod 2 :=
  (root b ws).eval x (values x p)

def target {n m K : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (x : BooleanCube n) : ZMod 2 :=
  value b p ws (fun j => ((x j).val : ZMod 2))

/-- This is the original circuit semantics after appending the selected gate. -/
theorem target_is_circuit {n m K : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) :
    target b p ws = SharedDAG.target (p.step (root b ws)) (.inr 0) := rfl

theorem poly_degree {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (z : Sample K r t) (hr : 1 ≤ r) :
    (poly b p ws z).totalDegree ≤ t * r^(height (depths p) ws) := by
  have h0 := args_degree (K := K) 0 hr (polynomials z.1 p) (depths p)
    (polynomial_degree z.1 hr p) ws
  have h1 := args_degree (K := K) 1 hr (polynomials z.1 p) (depths p)
    (polynomial_degree z.1 hr p) ws
  simp only [map_zero, map_one] at h0 h1
  cases b with
  | false => exact orPoly_degree z.2 _ h0
  | true => exact andPoly_degree z.2 _ h1

/-- Outside the inner TRUE-input bad-event union, the root sees true children. -/
theorem poly_eval_true {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (z : Sample K r t) (x : Fin n → ZMod 2)
    (h : ¬ bad z.1 x p) :
    MvPolynomial.eval x (poly b p ws z) = (root b ws).approx z.2 x (values x p) := by
  unfold poly
  rw [Gate.poly_eval, funext (polynomial_eval z.1 x p), good_values z.1 x p h]

theorem root_local_error {n m K t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (x : Fin n → ZMod 2) :
    (∑ B : Matrix K t, matrixWeight K B *
      (if (root b ws).approx B x (values x p) ≠ value b p ws x then 1 else 0)) ≤
      (1/2 : ℝ)^t := by
  have h := (root b ws).local_error (r := t) x (values x p)
  rw [root_cost, Nat.cast_one, one_mul] at h
  exact h

/-- A pointwise inclusion, not an independence assertion about child errors. -/
theorem error_indicator {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (z : Sample K r t) (x : Fin n → ZMod 2) :
    (if MvPolynomial.eval x (poly b p ws z) ≠ value b p ws x then (1 : ℝ) else 0) ≤
      (if bad z.1 x p then 1 else 0) +
      (if (root b ws).approx z.2 x (values x p) ≠ value b p ws x then 1 else 0) := by
  by_cases h : bad z.1 x p
  · simp only [ite_eq_left h]
    split_ifs <;> norm_num
  · rw [poly_eval_true b p ws z x h]
    simp [h]

theorem error_bound {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (x : Fin n → ZMod 2) :
    (∑ z : Sample K r t, weight K r t z *
      (if MvPolynomial.eval x (poly b p ws z) ≠ value b p ws x then 1 else 0)) ≤
      (cost p : ℝ)*(1/2 : ℝ)^r + (1/2 : ℝ)^t := by
  calc
    _ ≤ ∑ z : Sample K r t, weight K r t z *
        ((if bad z.1 x p then 1 else 0) +
        (if (root b ws).approx z.2 x (values x p) ≠ value b p ws x then 1 else 0)) :=
      Finset.sum_le_sum (fun z _ => mul_le_mul_of_nonneg_left
        (error_indicator b p ws z x) (weight_nonneg K r t z))
    _ = (∑ A : Matrix K r, matrixWeight K A * (if bad A x p then 1 else 0)) +
        (∑ B : Matrix K t, matrixWeight K B *
        (if (root b ws).approx B x (values x p) ≠ value b p ws x then 1 else 0)) := by
      simp only [mul_add, Finset.sum_add_distrib]
      rw [fst_marginal, snd_marginal]
    _ ≤ _ := add_le_add (bad_mass x p) (root_local_error b p ws x)

theorem success_bound {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (x : BooleanCube n) :
    1 - ((cost p : ℝ)*(1/2 : ℝ)^r + (1/2 : ℝ)^t) ≤
      success (target b p ws) (poly (r := r) (t := t) b p ws) (weight K r t) x := by
  have he := error_bound (r := r) (t := t) b p ws (fun j => ((x j).val : ZMod 2))
  have hc :
      (∑ z : Sample K r t, weight K r t z *
        (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (poly b p ws z) ≠
          target b p ws x then 1 else 0)) +
      success (target b p ws) (poly (r := r) (t := t) b p ws) (weight K r t) x = 1 := by
    unfold success correct
    rw [← Finset.sum_add_distrib]
    convert weight_sum K r t using 1
    apply Finset.sum_congr rfl
    intro z _
    by_cases h : MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (poly b p ws z) =
      target b p ws x <;> simp [h]
  change (∑ z : Sample K r t, weight K r t z *
    (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (poly b p ws z) ≠
      target b p ws x then 1 else 0)) ≤ _ at he
  linarith

/-- Closed original-predicate endpoint. The final row count may even be zero. -/
theorem feasible {n m K r t : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (hr : 1 ≤ r) :
    HasProbabilisticDegreeAtMost (target b p ws)
      ((cost p : ℝ)*(1/2 : ℝ)^r + (1/2 : ℝ)^t)
      (t * r^(height (depths p) ws)) := by
  apply feasible_of_fintype (poly (r := r) (t := t) b p ws) (weight K r t)
  · intro z; exact poly_degree b p ws z hr
  · exact weight_nonneg K r t
  · exact weight_sum K r t
  · exact success_bound b p ws

theorem third_budget (S r : ℕ) (hb : 12*S ≤ 2^r) :
    (S : ℝ)*(1/2 : ℝ)^r + (1/2 : ℝ)^2 ≤ 1/3 := by
  have hh : 12*(S : ℝ) ≤ (2 : ℝ)^r := by exact_mod_cast hb
  have hi : (2 : ℝ)^r * (1/2 : ℝ)^r = 1 := by
    rw [← mul_pow]
    norm_num
  have hm := mul_le_mul_of_nonneg_right hh
    (by positivity : (0 : ℝ) ≤ (1/2 : ℝ)^r)
  have he : (S : ℝ)*(1/2 : ℝ)^r ≤ 1/12 := by nlinarith
  calc
    _ ≤ 1/12 + (1/2 : ℝ)^2 := add_le_add_right he _
    _ = 1/3 := by norm_num

/-- No logarithms, so zero inner cost and empty arity are retained. -/
theorem feasible_third {n m K r : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (S H : ℕ) (hr : 1 ≤ r) (hs : cost p ≤ S)
    (hd : height (depths p) ws ≤ H) (hb : 12*S ≤ 2^r) :
    HasProbabilisticDegreeAtMost (target b p ws) (1/3 : ℝ) (2*r^H) := by
  apply feasible_of_fintype (poly (r := r) (t := 2) b p ws) (weight K r 2)
  · intro z
    exact (poly_degree b p ws z hr).trans (Nat.mul_le_mul_left 2 (pow_mono hr hd))
  · exact weight_nonneg K r 2
  · exact weight_sum K r 2
  · intro x
    have hp := success_bound (r := r) (t := 2) b p ws x
    have hsr : (cost p : ℝ) ≤ (S : ℝ) := by exact_mod_cast hs
    have he : (cost p : ℝ)*(1/2 : ℝ)^r + (1/2 : ℝ)^2 ≤ 1/3 :=
      (add_le_add_right (mul_le_mul_of_nonneg_right hsr (by positivity)) _).trans
        (third_budget S r hb)
    linarith

/-- The only target premise is correctness of the original appended-root circuit. -/
theorem mod3_size_bound {n m K r : ℕ} (b : Bool) (p : Program n K m)
    (ws : Slots n m K) (S H : ℕ) (hr : 1 ≤ r) (hs : cost p ≤ S)
    (hd : height (depths p) ws ≤ H) (hb : 12*S ≤ 2^r)
    (hc : ∀ x, target b p ws x = SmallSupportMod3.target x) :
    n < (32*r^H+2)^2+2 := by
  have hf := feasible_third b p ws S H hr hs hd hb
  have he : target b p ws = @SmallSupportMod3.target n := funext hc
  rw [he] at hf
  have hn := Mod3GrowingDegree.feasible_size_bound n (2*r^H) hf
  convert hn using 1 <;> ring

end
end PvsNPCartography.RootBudget
