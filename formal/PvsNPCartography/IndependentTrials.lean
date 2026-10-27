import Mathlib

open scoped BigOperators

namespace PvsNPCartography.IndependentTrials
noncomputable section
attribute [local instance] Classical.propDecidable

/-- At least k failures in r independent Bernoulli trials. -/
def tail (p : ℝ) : ℕ → ℕ → ℝ
  | 0, k => if k = 0 then 1 else 0
  | _ + 1, 0 => 1
  | r + 1, k + 1 => p * tail p r k + (1-p) * tail p r (k+1)

@[simp] theorem tail_zero (p : ℝ) (r : ℕ) : tail p r 0 = 1 := by
  cases r <;> simp [tail]

theorem tail_bounds (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) (r k : ℕ) :
    0 ≤ tail p r k ∧ tail p r k ≤ 1 := by
  induction r generalizing k with
  | zero => simp only [tail]; split_ifs <;> norm_num
  | succ r ih =>
    cases k with
    | zero => simp
    | succ k =>
      have h0 := ih k
      have h1 := ih (k+1)
      simp only [tail]
      constructor
      · exact add_nonneg (mul_nonneg hp h0.1)
          (mul_nonneg (sub_nonneg.mpr hp1) h1.1)
      · nlinarith [mul_nonneg hp (sub_nonneg.mpr h0.2),
          mul_nonneg (sub_nonneg.mpr hp1) (sub_nonneg.mpr h1.2)]

theorem tail_antitone (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) (r k : ℕ) :
    tail p r (k+1) ≤ tail p r k := by
  induction r generalizing k with
  | zero => cases k <;> simp [tail]
  | succ r ih =>
    cases k with
    | zero => simpa using (tail_bounds p hp hp1 (r+1) 1).2
    | succ k =>
      simp only [tail]
      exact add_le_add (mul_le_mul_of_nonneg_left (ih k) hp)
        (mul_le_mul_of_nonneg_left (ih (k+1)) (sub_nonneg.mpr hp1))

theorem tail_mono (p q : ℝ) (hp : 0 ≤ p) (hpq : p ≤ q) (hq : q ≤ 1)
    (r k : ℕ) : tail p r k ≤ tail q r k := by
  have hp1 : p ≤ 1 := hpq.trans hq
  have hq0 : 0 ≤ q := hp.trans hpq
  induction r generalizing k with
  | zero => exact le_rfl
  | succ r ih =>
    cases k with
    | zero => simp
    | succ k =>
      simp only [tail]
      calc
        _ ≤ p * tail q r k + (1-p) * tail q r (k+1) :=
          add_le_add (mul_le_mul_of_nonneg_left (ih k) hp)
            (mul_le_mul_of_nonneg_left (ih (k+1)) (sub_nonneg.mpr hp1))
        _ ≤ _ := by
          have ht := tail_antitone q hq0 hq r k
          nlinarith [mul_nonneg (sub_nonneg.mpr hpq) (sub_nonneg.mpr ht)]

/-- Explicit splitting of a tuple; this is not diagonal repetition. -/
def headTail (I : Type*) (r : ℕ) : (Fin (r+1) → I) ≃ I × (Fin r → I) where
  toFun v := (v 0, fun j => v j.succ)
  invFun v := Fin.cons v.1 v.2
  left_inv v := by funext j; refine Fin.cases rfl (fun _ => rfl) j
  right_inv v := by cases v; rfl

theorem sum_tuples {I : Type*} [Fintype I] (r : ℕ)
    (f : (Fin (r+1) → I) → ℝ) :
    (∑ v, f v) = ∑ i, ∑ v : Fin r → I, f (Fin.cons i v) := by
  rw [← (headTail I r).symm.sum_comp f]
  exact Fintype.sum_prod_type _

/-- All coordinates are sampled independently from the SAME fixed distribution. -/
def mass {I : Type*} (mu : I → ℝ) {r : ℕ} (v : Fin r → I) : ℝ :=
  ∏ j, mu (v j)

@[simp] theorem mass_cons {I : Type*} (mu : I → ℝ) {r : ℕ} (i : I)
    (v : Fin r → I) : mass mu (Fin.cons i v) = mu i * mass mu v := by
  simp [mass, Fin.prod_univ_succ]

theorem mass_nonneg {I : Type*} (mu : I → ℝ) (hn : ∀ i, 0 ≤ mu i)
    {r : ℕ} (v : Fin r → I) : 0 ≤ mass mu v :=
  Finset.prod_nonneg (fun j _ => hn (v j))

theorem mass_sum {I : Type*} [Fintype I] (mu : I → ℝ)
    (hs : ∑ i, mu i = 1) (r : ℕ) : (∑ v : Fin r → I, mass mu v) = 1 := by
  induction r with
  | zero => simp [mass]
  | succ r ih =>
    rw [sum_tuples]
    simp only [mass_cons, ← Finset.mul_sum, ih, mul_one, hs]

def failures {I : Type*} (e : I → Bool) {r : ℕ} (v : Fin r → I) : ℕ :=
  ∑ j, if e (v j) then 1 else 0

@[simp] theorem failures_cons {I : Type*} (e : I → Bool) {r : ℕ} (i : I)
    (v : Fin r → I) : failures e (Fin.cons i v) =
      (if e i then 1 else 0) + failures e v := by
  simp only [failures, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]

def errorMass {I : Type*} [Fintype I] (mu : I → ℝ) (e : I → Bool) : ℝ :=
  ∑ i, if e i then mu i else 0

theorem complement_mass {I : Type*} [Fintype I] (mu : I → ℝ) (e : I → Bool)
    (hs : ∑ i, mu i = 1) :
    (∑ i, if e i then 0 else mu i) = 1 - errorMass mu e := by
  have h : errorMass mu e + (∑ i, if e i then 0 else mu i) = 1 := by
    rw [errorMass, ← Finset.sum_add_distrib]
    convert hs using 1
    apply Finset.sum_congr rfl
    intro i _
    cases e i <;> simp
  linarith

theorem errorMass_bounds {I : Type*} [Fintype I] (mu : I → ℝ) (e : I → Bool)
    (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1) :
    0 ≤ errorMass mu e ∧ errorMass mu e ≤ 1 := by
  constructor
  · apply Finset.sum_nonneg
    intro i _
    cases e i <;> simp [hn]
  · have hnon : 0 ≤ ∑ i, if e i then 0 else mu i := by
      apply Finset.sum_nonneg
      intro i _
      cases e i <;> simp [hn]
    rw [complement_mass mu e hs] at hnon
    linarith

/-- Exact law derived from product weights, with no independence assumption
left for the caller to discharge. It holds even for signed normalized weights;
positivity is imposed separately when comparing tail probabilities. -/
theorem failure_law {I : Type*} [Fintype I] (mu : I → ℝ) (e : I → Bool)
    (hs : ∑ i, mu i = 1) (r k : ℕ) :
    (∑ v : Fin r → I, mass mu v * (if k ≤ failures e v then 1 else 0)) =
      tail (errorMass mu e) r k := by
  induction r generalizing k with
  | zero =>
    cases k <;> simp [mass, failures, tail]
  | succ r ih =>
    cases k with
    | zero => simpa using mass_sum mu hs (r+1)
    | succ k =>
      rw [sum_tuples]
      have hrow (i : I) :
          (∑ v : Fin r → I, mass mu (Fin.cons i v) *
            (if k+1 ≤ failures e (Fin.cons i v) then 1 else 0)) =
          if e i then mu i * tail (errorMass mu e) r k
          else mu i * tail (errorMass mu e) r (k+1) := by
        cases he : e i
        · simp only [mass_cons, failures_cons, he, Bool.false_eq_true, ite_false,
            zero_add, mul_assoc, ← Finset.mul_sum, ih]
        · simp only [mass_cons, failures_cons, he, ite_true]
          have ht (v : Fin r → I) : (k+1 ≤ 1+failures e v) ↔ k ≤ failures e v := by omega
          simp_rw [ht, mul_assoc]
          rw [← Finset.mul_sum, ih]
      simp_rw [hrow]
      have hsplit :
          (∑ i, if e i then mu i * tail (errorMass mu e) r k
            else mu i * tail (errorMass mu e) r (k+1)) =
          errorMass mu e * tail (errorMass mu e) r k +
            (1-errorMass mu e) * tail (errorMass mu e) r (k+1) := by
        rw [← complement_mass mu e hs, errorMass, Finset.sum_mul, Finset.sum_mul,
          ← Finset.sum_add_distrib]
        apply Finset.sum_congr rfl
        intro i _
        cases e i <;> simp
      exact hsplit

/-- Generic real-weighted amplification, not a rational-grid calculation. -/
theorem failure_bound {I : Type*} [Fintype I] (mu : I → ℝ) (e : I → Bool)
    (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1)
    (q : ℝ) (hq : q ≤ 1) (hp : errorMass mu e ≤ q) (r k : ℕ) :
    (∑ v : Fin r → I, mass mu v * (if k ≤ failures e v then 1 else 0)) ≤
      tail q r k := by
  rw [failure_law mu e hs]
  exact tail_mono _ q (errorMass_bounds mu e hn hs).1 hp hq r k

end
end PvsNPCartography.IndependentTrials
