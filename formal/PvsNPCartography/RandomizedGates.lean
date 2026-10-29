import PvsNPCartography.IndependentTrials
import PvsNPCartography.PermutationTransport

open scoped BigOperators

namespace PvsNPCartography.RandomizedGates
open IndependentTrials Symmetrization
noncomputable section
attribute [local instance] Classical.propDecidable
set_option maxHeartbeats 1600000

abbrev Mask (k : ℕ) := Fin k → ZMod 2
abbrev Matrix (k r : ℕ) := Fin r → Mask k

def bit_cases (a : ZMod 2) : a = 0 ∨ a = 1 := by
  have ha := a.isLt
  have hv : a.val = 0 ∨ a.val = 1 := by omega
  rcases hv with h | h
  · exact Or.inl (Fin.ext h)
  · exact Or.inr (Fin.ext h)

/-- Uniform mask weights, fixed before the input. The zero-arity space is inhabited. -/
def maskWeight (k : ℕ) (_a : Mask k) : ℝ := 1 / Fintype.card (Mask k)

theorem maskWeight_nonneg (k : ℕ) (a : Mask k) : 0 ≤ maskWeight k a := by
  unfold maskWeight
  positivity

theorem maskWeight_sum (k : ℕ) : (∑ a : Mask k, maskWeight k a) = 1 := by
  have hc : (Fintype.card (Mask k) : ℝ) ≠ 0 := by
    exact_mod_cast (Fintype.card_ne_zero : Fintype.card (Mask k) ≠ 0)
  simp [maskWeight, hc]

/-- Product distribution: r distinct sample coordinates, not repetition of one mask. -/
def matrixWeight (k : ℕ) {r : ℕ} (A : Matrix k r) : ℝ := mass (maskWeight k) A

theorem matrixWeight_nonneg (k r : ℕ) (A : Matrix k r) : 0 ≤ matrixWeight k A :=
  mass_nonneg _ (maskWeight_nonneg k) A

theorem matrixWeight_sum (k r : ℕ) : (∑ A : Matrix k r, matrixWeight k A) = 1 :=
  mass_sum _ (maskWeight_sum k) r

def linear {k : ℕ} (a z : Mask k) : ZMod 2 := ∑ j, a j * z j

theorem linear_add {k : ℕ} (a b z : Mask k) :
    linear (a+b) z = linear a z + linear b z := by
  simp [linear, Pi.add_apply, add_mul, Finset.sum_add_distrib]

theorem linear_single {k : ℕ} (j : Fin k) (z : Mask k) :
    linear (Pi.single j 1) z = z j := by
  simp [linear, Pi.single_apply, ite_mul]

/-- Pair all masks by translation in an active coordinate. No assumed unbiasedness. -/
theorem linear_zero_mass {k : ℕ} (z : Mask k) (hz : z ≠ 0) :
    (∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 1 else 0)) = 1/2 := by
  have hactive : ∃ j, z j ≠ 0 := by
    by_contra h
    push_neg at h
    exact hz (funext h)
  obtain ⟨j, hj⟩ := hactive
  have hj1 : z j = 1 := (bit_cases (z j)).resolve_left hj
  let delta : Mask k := Pi.single j 1
  let E : Mask k ≃ Mask k :=
    { toFun := fun a => a + delta
      invFun := fun a => a - delta
      left_inv := by intro a; simp
      right_inv := by intro a; simp }
  have hshift (a : Mask k) : linear (E a) z = linear a z + 1 := by
    change linear (a+delta) z = _
    rw [linear_add, linear_single, hj1]
  have hpair :
      (∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 1 else 0)) =
      ∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 0 else 1) := by
    rw [← E.sum_comp (fun a => maskWeight k a * (if linear a z = 0 then (1:ℝ) else 0))]
    apply Finset.sum_congr rfl
    intro a _
    rw [hshift]
    rcases bit_cases (linear a z) with h | h <;> norm_num [h, maskWeight]
  have htotal :
      (∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 1 else 0)) +
      (∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 0 else 1)) = 1 := by
    rw [← Finset.sum_add_distrib]
    convert maskWeight_sum k using 1
    apply Finset.sum_congr rfl
    intro a _
    by_cases h : linear a z = 0 <;> simp [h]
  linarith

/-- Exact product law derived by splitting the actual sample tuple. -/
theorem all_zero_mass {k : ℕ} (z : Mask k) (r : ℕ) :
    (∑ A : Matrix k r, matrixWeight k A *
      (if ∀ t, linear (A t) z = 0 then 1 else 0)) =
    (∑ a : Mask k, maskWeight k a * (if linear a z = 0 then 1 else 0)) ^ r := by
  induction r with
  | zero => simp [matrixWeight, mass]
  | succ r ih =>
    change (∑ A : Fin (r+1) → Mask k, mass (maskWeight k) A *
      (if ∀ t, linear (A t) z = 0 then 1 else 0)) = _
    rw [sum_tuples]
    have hterm (a : Mask k) (A : Matrix k r) :
        mass (maskWeight k) (Fin.cons a A) *
          (if ∀ t, linear (Fin.cons a A t) z = 0 then 1 else 0) =
        (maskWeight k a * (if linear a z = 0 then 1 else 0)) *
          (matrixWeight k A * (if ∀ t, linear (A t) z = 0 then 1 else 0)) := by
      rw [mass_cons]
      by_cases ha : linear a z = 0 <;>
        by_cases hA : ∀ t, linear (A t) z = 0 <;>
        simp [Fin.forall_fin_succ, ha, hA, matrixWeight]
    simp_rw [hterm, ← Finset.mul_sum, ih]
    rw [← Finset.sum_mul, pow_succ]
    ring

/-- 1+P is Boolean NOT in characteristic two. Degree is genuine totalDegree. -/
theorem complement_degree {n d : ℕ} (P : BinaryPolynomial n)
    (hd : P.totalDegree ≤ d) : (1+P).totalDegree ≤ d := by
  exact (MvPolynomial.totalDegree_add _ _).trans (by simpa using hd)

def linearPoly {n k : ℕ} (a : Mask k) (P : Fin k → BinaryPolynomial n) :
    BinaryPolynomial n := ∑ j, MvPolynomial.C (a j) * P j

def orPoly {n k r : ℕ} (A : Matrix k r) (P : Fin k → BinaryPolynomial n) :
    BinaryPolynomial n := 1 + ∏ t, (1 + linearPoly (A t) P)

def andPoly {n k r : ℕ} (A : Matrix k r) (P : Fin k → BinaryPolynomial n) :
    BinaryPolynomial n := 1 + orPoly A (fun j => 1 + P j)

theorem linearPoly_degree {n k d : ℕ} (a : Mask k)
    (P : Fin k → BinaryPolynomial n) (hd : ∀ j, (P j).totalDegree ≤ d) :
    (linearPoly a P).totalDegree ≤ d := by
  apply MvPolynomial.totalDegree_finsetSum_le
  intro j _
  exact (MvPolynomial.totalDegree_mul _ _).trans (by simpa using hd j)

/-- Actual composition, including non-multilinear P and repeated wires. -/
theorem orPoly_degree {n k r d : ℕ} (A : Matrix k r)
    (P : Fin k → BinaryPolynomial n) (hd : ∀ j, (P j).totalDegree ≤ d) :
    (orPoly A P).totalDegree ≤ r*d := by
  apply complement_degree
  calc
    _ ≤ ∑ t, (1 + linearPoly (A t) P).totalDegree := MvPolynomial.totalDegree_finsetProd _ _
    _ ≤ ∑ _t : Fin r, d := Finset.sum_le_sum (fun t _ =>
      complement_degree _ (linearPoly_degree _ P hd))
    _ = r*d := by simp

theorem andPoly_degree {n k r d : ℕ} (A : Matrix k r)
    (P : Fin k → BinaryPolynomial n) (hd : ∀ j, (P j).totalDegree ≤ d) :
    (andPoly A P).totalDegree ≤ r*d :=
  complement_degree _ (orPoly_degree A _ (fun j => complement_degree _ (hd j)))

def orValue {k : ℕ} (z : Mask k) : ZMod 2 := if z = 0 then 0 else 1

def andValue {k : ℕ} (z : Mask k) : ZMod 2 := 1 + orValue (fun j => 1 + z j)

def gateValue {k r : ℕ} (A : Matrix k r) (z : Mask k) : ZMod 2 :=
  1 + ∏ t, (1 + linear (A t) z)

theorem orPoly_eval {n k r : ℕ} (A : Matrix k r)
    (P : Fin k → BinaryPolynomial n) (x : Fin n → ZMod 2) :
    MvPolynomial.eval x (orPoly A P) = gateValue A (fun j => MvPolynomial.eval x (P j)) := by
  simp [orPoly, linearPoly, gateValue, linear, map_sum, map_prod]

theorem gateValue_eq {k r : ℕ} (A : Matrix k r) (z : Mask k) :
    gateValue A z = if ∀ t, linear (A t) z = 0 then 0 else 1 := by
  by_cases h : ∀ t, linear (A t) z = 0
  · simp [gateValue, h]
  · have he : ∃ t, linear (A t) z ≠ 0 := by simpa only [not_forall] using h
    obtain ⟨t, ht⟩ := he
    have ht1 : linear (A t) z = 1 := (bit_cases _).resolve_left ht
    have hp : (∏ t, (1 + linear (A t) z)) = 0 :=
      Finset.prod_eq_zero (Finset.mem_univ t) (by norm_num [ht1])
    simp [gateValue, h, hp]

@[simp] theorem gateValue_zero {k r : ℕ} (A : Matrix k r) : gateValue A 0 = 0 := by
  simp [gateValue, linear]

/-- Exact pointwise error, derived from actual matrix weights. Zero input never fails. -/
theorem gate_error_exact {k r : ℕ} (z : Mask k) :
    (∑ A : Matrix k r, matrixWeight k A *
      (if gateValue A z ≠ orValue z then 1 else 0)) =
      if z = 0 then 0 else (1/2 : ℝ)^r := by
  by_cases hz : z = 0
  · subst z
    simp [orValue]
  · have hi (A : Matrix k r) :
        (if gateValue A z ≠ orValue z then (1:ℝ) else 0) =
        if ∀ t, linear (A t) z = 0 then 1 else 0 := by
      rw [gateValue_eq]
      by_cases h : ∀ t, linear (A t) z = 0 <;> simp [orValue, hz, h]
    simp_rw [hi]
    rw [all_zero_mass, linear_zero_mass z hz, if_neg hz]

theorem gate_success {k r : ℕ} (z : Mask k) :
    1 - (1/2 : ℝ)^r ≤ ∑ A : Matrix k r, matrixWeight k A *
      (if gateValue A z = orValue z then 1 else 0) := by
  have hcomp :
      (∑ A : Matrix k r, matrixWeight k A * (if gateValue A z ≠ orValue z then 1 else 0)) +
      (∑ A : Matrix k r, matrixWeight k A * (if gateValue A z = orValue z then 1 else 0)) = 1 := by
    rw [← Finset.sum_add_distrib]
    convert matrixWeight_sum k r using 1
    apply Finset.sum_congr rfl
    intro A _
    by_cases h : gateValue A z = orValue z <;> simp [h]
  rw [gate_error_exact] at hcomp
  split_ifs at hcomp <;> nlinarith [pow_nonneg (by norm_num : (0:ℝ) ≤ 1/2) r]

/-- Original quantifiers: one finite distribution of ACTUAL polynomials, then every input. -/
theorem or_feasible (k r : ℕ) :
    HasProbabilisticDegreeAtMost
      (fun x : BooleanCube k => orValue (fun j => ((x j).val : ZMod 2)))
      ((1/2 : ℝ)^r) r := by
  apply feasible_of_fintype
    (fun A : Matrix k r => orPoly A (fun j => MvPolynomial.X j)) (matrixWeight k)
  · intro A
    simpa using orPoly_degree A (fun j => MvPolynomial.X j)
      (d := 1) (fun _ => by simp)
  · exact matrixWeight_nonneg k r
  · exact matrixWeight_sum k r
  · intro x
    simpa only [success, correct, orPoly_eval, MvPolynomial.eval_X] using
      (gate_success (r := r) (fun j => ((x j).val : ZMod 2)))

end
end PvsNPCartography.RandomizedGates
