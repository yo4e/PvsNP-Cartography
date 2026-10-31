import PvsNPCartography.RandomizedGates

open scoped BigOperators

namespace PvsNPCartography.SharedDAG
open RandomizedGates Symmetrization
noncomputable section
attribute [local instance] Classical.propDecidable
set_option maxHeartbeats 2400000

/-- External inputs or references to the already constructed table. -/
abbrev Wire (n m : ℕ) := Fin n ⊕ Fin m
/-- Argument positions, not wire identities. None is neutral padding. -/
abbrev Slots (n m K : ℕ) := Fin K → Option (Wire n m)

def read {n m : ℕ} {T : Type*} (x : Fin n → T) (v : Fin m → T) : Wire n m → T :=
  Sum.elim x v

def args {n m K : ℕ} {T : Type*} (b : T) (x : Fin n → T) (v : Fin m → T)
    (ws : Slots n m K) (j : Fin K) : T := (ws j).elim b (read x v)

inductive Gate (n m K : ℕ) where
  | constant (b : ZMod 2)
  | negate (w : Wire n m)
  | parity (ws : Slots n m K)
  | disj (ws : Slots n m K)
  | conj (ws : Slots n m K)

def Gate.cost {n m K : ℕ} : Gate n m K → ℕ
  | .disj _ | .conj _ => 1
  | _ => 0

def Gate.eval {n m K : ℕ} (g : Gate n m K) (x : Fin n → ZMod 2)
    (v : Fin m → ZMod 2) : ZMod 2 :=
  match g with
  | .constant b => b
  | .negate w => 1 + read x v w
  | .parity ws => ∑ j, args 0 x v ws j
  | .disj ws => orValue (args 0 x v ws)
  | .conj ws => andValue (args 1 x v ws)

def Gate.approx {n m K r : ℕ} (g : Gate n m K) (A : Matrix K r)
    (x : Fin n → ZMod 2) (v : Fin m → ZMod 2) : ZMod 2 :=
  match g with
  | .constant b => b
  | .negate w => 1 + read x v w
  | .parity ws => ∑ j, args 0 x v ws j
  | .disj ws => gateValue A (args 0 x v ws)
  | .conj ws => andGateValue A (args 1 x v ws)

def Gate.poly {n m K r : ℕ} (g : Gate n m K) (A : Matrix K r)
    (v : Fin m → BinaryPolynomial n) : BinaryPolynomial n :=
  match g with
  | .constant b => MvPolynomial.C b
  | .negate w => 1 + read MvPolynomial.X v w
  | .parity ws => ∑ j, args 0 MvPolynomial.X v ws j
  | .disj ws => orPoly A (args 0 MvPolynomial.X v ws)
  | .conj ws => andPoly A (args 1 MvPolynomial.X v ws)

def height {n m K : ℕ} (d : Fin m → ℕ) (ws : Slots n m K) : ℕ :=
  Finset.univ.sup (args 0 (fun _ => 0) d ws)

def Gate.depth {n m K : ℕ} (g : Gate n m K) (d : Fin m → ℕ) : ℕ :=
  match g with
  | .constant _ => 0
  | .negate w => read (fun _ => 0) d w
  | .parity ws => height d ws
  | .disj ws | .conj ws => height d ws + 1

/-- One prefix is stored per node, not one copied subtree per edge.
The newest table entry is index0; earlier entries shift by Fin.succ. -/
inductive Program (n K : ℕ) : ℕ → Type where
  | nil : Program n K 0
  | step {m : ℕ} (p : Program n K m) (g : Gate n m K) : Program n K (m+1)

def values {n K : ℕ} (x : Fin n → ZMod 2) : {m : ℕ} → Program n K m → Fin m → ZMod 2
  | _, .nil => Fin.elim0
  | _, .step p g => Fin.cons (g.eval x (values x p)) (values x p)

def approximations {n K r : ℕ} (A : Matrix K r) (x : Fin n → ZMod 2) :
    {m : ℕ} → Program n K m → Fin m → ZMod 2
  | _, .nil => Fin.elim0
  | _, .step p g => Fin.cons (g.approx A x (approximations A x p)) (approximations A x p)

def polynomials {n K r : ℕ} (A : Matrix K r) :
    {m : ℕ} → Program n K m → Fin m → BinaryPolynomial n
  | _, .nil => Fin.elim0
  | _, .step p g => Fin.cons (g.poly A (polynomials A p)) (polynomials A p)

def depths {n K : ℕ} : {m : ℕ} → Program n K m → Fin m → ℕ
  | _, .nil => Fin.elim0
  | _, .step p g => Fin.cons (g.depth (depths p)) (depths p)

def cost {n K : ℕ} : {m : ℕ} → Program n K m → ℕ
  | _, .nil => 0
  | _, .step p g => cost p + g.cost

/-- Every local event uses TRUE values, never corrupted sample-dependent children. -/
def bad {n K r : ℕ} (A : Matrix K r) (x : Fin n → ZMod 2) :
    {m : ℕ} → Program n K m → Prop
  | _, .nil => False
  | _, .step p g => bad A x p ∨ g.approx A x (values x p) ≠ g.eval x (values x p)

theorem eval_read {n m : ℕ} (x : Fin n → ZMod 2) (v : Fin m → BinaryPolynomial n)
    (w : Wire n m) : MvPolynomial.eval x (read MvPolynomial.X v w) =
      read x (fun i => MvPolynomial.eval x (v i)) w := by
  cases w <;> simp [read]

theorem eval_args {n m K : ℕ} (b : ZMod 2) (x : Fin n → ZMod 2)
    (v : Fin m → BinaryPolynomial n) (ws : Slots n m K) :
    (fun j => MvPolynomial.eval x (args (MvPolynomial.C b) MvPolynomial.X v ws j)) =
      args b x (fun i => MvPolynomial.eval x (v i)) ws := by
  funext j
  cases h : ws j <;> simp [args, h, eval_read]

theorem Gate.poly_eval {n m K r : ℕ} (g : Gate n m K) (A : Matrix K r)
    (x : Fin n → ZMod 2) (v : Fin m → BinaryPolynomial n) :
    MvPolynomial.eval x (g.poly A v) =
      g.approx A x (fun i => MvPolynomial.eval x (v i)) := by
  have h0 := eval_args (K := K) 0 x v
  have h1 := eval_args (K := K) 1 x v
  simp only [map_zero, map_one] at h0 h1
  cases g <;> simp [Gate.poly, Gate.approx, orPoly_eval, andPoly_eval, eval_read, h0, h1]

theorem polynomial_eval {n m K r : ℕ} (A : Matrix K r) (x : Fin n → ZMod 2)
    (p : Program n K m) : ∀ i,
    MvPolynomial.eval x (polynomials A p i) = approximations A x p i := by
  induction p with
  | nil => intro i; exact Fin.elim0 i
  | step p g ih =>
    intro i
    refine Fin.cases ?_ (fun j => ?_) i
    · change MvPolynomial.eval x (g.poly A (polynomials A p)) =
        g.approx A x (approximations A x p)
      rw [Gate.poly_eval, funext ih]
    · exact ih j

/-- A nonnegative base >=1 is necessary when exact skip wires are retained. -/
theorem pow_mono {r a b : ℕ} (hr : 1 ≤ r) (hab : a ≤ b) : r^a ≤ r^b := by
  induction b with
  | zero =>
    have ha : a = 0 := by omega
    simp [ha]
  | succ b ih =>
    by_cases h : a ≤ b
    · have hi := ih h
      rw [pow_succ]
      nlinarith [Nat.mul_le_mul_left (r^b) hr]
    · have ha : a = b+1 := by omega
      simp [ha]

theorem read_degree {n m r : ℕ} (v : Fin m → BinaryPolynomial n) (d : Fin m → ℕ)
    (hv : ∀ i, (v i).totalDegree ≤ r^(d i)) (w : Wire n m) :
    (read MvPolynomial.X v w).totalDegree ≤ r^(read (fun _ => 0) d w) := by
  cases w with
  | inl i => simp [read]
  | inr i => exact hv i

theorem args_degree {n m K r : ℕ} (b : ZMod 2) (hr : 1 ≤ r)
    (v : Fin m → BinaryPolynomial n) (d : Fin m → ℕ)
    (hv : ∀ i, (v i).totalDegree ≤ r^(d i)) (ws : Slots n m K) :
    ∀ j, (args (MvPolynomial.C b) MvPolynomial.X v ws j).totalDegree ≤ r^(height d ws) := by
  intro j
  have hj : args 0 (fun _ => 0) d ws j ≤ height d ws :=
    Finset.le_sup (Finset.mem_univ j)
  cases h : ws j with
  | none => simp [args, h]
  | some w =>
    have hh : read (fun _ => 0) d w ≤ height d ws := by simpa [args, h] using hj
    simpa [args, h] using (read_degree v d hv w).trans (pow_mono hr hh)

theorem Gate.poly_degree {n m K r : ℕ} (g : Gate n m K) (A : Matrix K r)
    (hr : 1 ≤ r) (v : Fin m → BinaryPolynomial n) (d : Fin m → ℕ)
    (hv : ∀ i, (v i).totalDegree ≤ r^(d i)) :
    (g.poly A v).totalDegree ≤ r^(g.depth d) := by
  have h0 := args_degree (K := K) 0 hr v d hv
  have h1 := args_degree (K := K) 1 hr v d hv
  simp only [map_zero, map_one] at h0 h1
  cases g with
  | constant b => simp [Gate.poly, Gate.depth]
  | negate w => exact complement_degree _ (read_degree v d hv w)
  | parity ws => exact xor_degree _ (h0 ws)
  | disj ws =>
    simpa [Gate.poly, Gate.depth, pow_succ, Nat.mul_comm] using orPoly_degree A _ (h0 ws)
  | conj ws =>
    simpa [Gate.poly, Gate.depth, pow_succ, Nat.mul_comm] using andPoly_degree A _ (h1 ws)

theorem polynomial_degree {n m K r : ℕ} (A : Matrix K r) (hr : 1 ≤ r)
    (p : Program n K m) : ∀ i, (polynomials A p i).totalDegree ≤ r^(depths p i) := by
  induction p with
  | nil => intro i; exact Fin.elim0 i
  | step p g ih =>
    intro i
    refine Fin.cases ?_ (fun j => ?_) i
    · exact g.poly_degree A hr (polynomials A p) (depths p) ih
    · exact ih j

set_option backward.isDefEq.respectTransparency false in
theorem Gate.local_error {n m K r : ℕ} (g : Gate n m K)
    (x : Fin n → ZMod 2) (v : Fin m → ZMod 2) :
    (∑ A : Matrix K r, matrixWeight K A *
      (if g.approx A x v ≠ g.eval x v then 1 else 0)) ≤ (g.cost : ℝ)*(1/2 : ℝ)^r := by
  cases g with
  | constant b => simp [Gate.approx, Gate.eval, Gate.cost]
  | negate w => simp [Gate.approx, Gate.eval, Gate.cost]
  | parity ws => simp [Gate.approx, Gate.eval, Gate.cost]
  | disj ws =>
    have he : (∑ A : Matrix K r, matrixWeight K A *
        (if gateValue A (args 0 x v ws) ≠ orValue (args 0 x v ws) then 1 else 0)) ≤
        (1/2 : ℝ)^r := by
      rw [gate_error_exact]
      split_ifs
      · positivity
      · exact le_rfl
    simpa only [Gate.approx, Gate.eval, Gate.cost, Nat.cast_one, one_mul] using he
  | conj ws =>
    have he : (∑ A : Matrix K r, matrixWeight K A *
        (if andGateValue A (args 1 x v ws) ≠ andValue (args 1 x v ws) then 1 else 0)) ≤
        (1/2 : ℝ)^r := by
      rw [and_gate_error_exact]
      split_ifs
      · positivity
      · exact le_rfl
    simpa only [Gate.approx, Gate.eval, Gate.cost, Nat.cast_one, one_mul] using he

/-- Topological first-error argument. No independence of child errors is used. -/
theorem good_values {n m K r : ℕ} (A : Matrix K r) (x : Fin n → ZMod 2)
    (p : Program n K m) : ¬ bad A x p → approximations A x p = values x p := by
  induction p with
  | nil => intro _; funext i; exact Fin.elim0 i
  | step p g ih =>
    intro h
    have hh := not_or.mp h
    have hp := ih hh.1
    have hg : g.approx A x (values x p) = g.eval x (values x p) := not_ne_iff.mp hh.2
    funext i
    refine Fin.cases ?_ (fun j => ?_) i
    · change g.approx A x (approximations A x p) = g.eval x (values x p)
      rw [hp, hg]
    · exact congrFun hp j

theorem union_indicator (p q : Prop) :
    (if p ∨ q then (1 : ℝ) else 0) ≤ (if p then 1 else 0) + (if q then 1 else 0) := by
  by_cases hp : p <;> by_cases hq : q <;> simp [hp, hq]

set_option backward.isDefEq.respectTransparency false in
/-- Union bound over original nodes, not the number of occurrences in an unrolled formula. -/
theorem bad_mass {n m K r : ℕ} (x : Fin n → ZMod 2) (p : Program n K m) :
    (∑ A : Matrix K r, matrixWeight K A * (if bad A x p then 1 else 0)) ≤
      (cost p : ℝ)*(1/2 : ℝ)^r := by
  induction p with
  | nil => simp [bad, cost]
  | step p g ih =>
    calc
      _ ≤ ∑ A : Matrix K r, matrixWeight K A *
          ((if bad A x p then 1 else 0) +
          (if g.approx A x (values x p) ≠ g.eval x (values x p) then 1 else 0)) := by
        apply Finset.sum_le_sum
        intro A _
        apply mul_le_mul_of_nonneg_left _ (matrixWeight_nonneg K r A)
        simpa only [bad] using union_indicator (bad A x p)
          (g.approx A x (values x p) ≠ g.eval x (values x p))
      _ = (∑ A : Matrix K r, matrixWeight K A * (if bad A x p then 1 else 0)) +
          (∑ A : Matrix K r, matrixWeight K A *
          (if g.approx A x (values x p) ≠ g.eval x (values x p) then 1 else 0)) := by
        simp only [mul_add, Finset.sum_add_distrib]
      _ ≤ (cost p : ℝ)*(1/2 : ℝ)^r + (g.cost : ℝ)*(1/2 : ℝ)^r :=
        add_le_add ih (g.local_error x (values x p))
      _ = _ := by simp [cost, Nat.cast_add, add_mul]

def output {n m K : ℕ} (p : Program n K m) (w : Wire n m) (x : Fin n → ZMod 2) :
    ZMod 2 := read x (values x p) w

def outputPoly {n m K r : ℕ} (p : Program n K m) (w : Wire n m) (A : Matrix K r) :
    BinaryPolynomial n := read MvPolynomial.X (polynomials A p) w

def outputDepth {n m K : ℕ} (p : Program n K m) (w : Wire n m) : ℕ :=
  read (fun _ => 0) (depths p) w

theorem output_degree {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (A : Matrix K r) (hr : 1 ≤ r) :
    (outputPoly p w A).totalDegree ≤ r^(outputDepth p w) :=
  read_degree _ _ (polynomial_degree A hr p) w

theorem output_error {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (x : Fin n → ZMod 2) :
    (∑ A : Matrix K r, matrixWeight K A *
      (if MvPolynomial.eval x (outputPoly p w A) ≠ output p w x then 1 else 0)) ≤
      (cost p : ℝ)*(1/2 : ℝ)^r := by
  apply le_trans ?_ (bad_mass x p)
  apply Finset.sum_le_sum
  intro A _
  apply mul_le_mul_of_nonneg_left _ (matrixWeight_nonneg K r A)
  by_cases hb : bad A x p
  · simp only [ite_eq_left hb]
    split_ifs <;> norm_num
  · have hc : MvPolynomial.eval x (outputPoly p w A) = output p w x := by
      unfold outputPoly output
      rw [eval_read, funext (polynomial_eval A x p), good_values A x p hb]
    simp [hb, hc]

def target {n m K : ℕ} (p : Program n K m) (w : Wire n m) (x : BooleanCube n) :
    ZMod 2 := output p w (fun j => ((x j).val : ZMod 2))

theorem output_success {n m K r : ℕ} (p : Program n K m) (w : Wire n m)
    (x : BooleanCube n) :
    1 - (cost p : ℝ)*(1/2 : ℝ)^r ≤
      success (target p w) (outputPoly p w) (matrixWeight K (r := r)) x := by
  have he := output_error (r := r) p w (fun j => ((x j).val : ZMod 2))
  have hc :
      (∑ A : Matrix K r, matrixWeight K A *
        (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (outputPoly p w A) ≠
          target p w x then 1 else 0)) +
      success (target p w) (outputPoly p w) (matrixWeight K (r := r)) x = 1 := by
    unfold success correct
    rw [← Finset.sum_add_distrib]
    convert matrixWeight_sum K r using 1
    apply Finset.sum_congr rfl
    intro A _
    by_cases h : MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (outputPoly p w A) =
      target p w x <;> simp [h]
  change (∑ A : Matrix K r, matrixWeight K A *
    (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (outputPoly p w A) ≠
      target p w x then 1 else 0)) ≤ (cost p : ℝ)*(1/2 : ℝ)^r at he
  linarith

/-- Closed bridge: no approximability, correctness or error bound is assumed.
One input-independent finite matrix family supplies actual polynomials. -/
theorem feasible {n m K r : ℕ} (p : Program n K m) (w : Wire n m) (hr : 1 ≤ r) :
    HasProbabilisticDegreeAtMost (target p w) ((cost p : ℝ)*(1/2 : ℝ)^r)
      (r^(outputDepth p w)) := by
  apply feasible_of_fintype (outputPoly p w) (matrixWeight K (r := r))
  · intro A; exact output_degree p w A hr
  · exact matrixWeight_nonneg K r
  · exact matrixWeight_sum K r
  · exact output_success p w

end
end PvsNPCartography.SharedDAG
