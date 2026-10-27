import PvsNPCartography.IndependentTrials
import PvsNPCartography.Mod3ProductBound

open scoped BigOperators

namespace PvsNPCartography.MajorityNumerics
open IndependentTrials
noncomputable section

set_option maxRecDepth 100000
set_option maxHeartbeats 16000000

/-- Exact integer tail at error1/3: one failure ticket, two success tickets. -/
def tickets : ℕ → ℕ → ℕ
  | 0, k => if k = 0 then 1 else 0
  | r + 1, 0 => 3^(r+1)
  | r + 1, k + 1 => tickets r k + 2*tickets r (k+1)

theorem tail_tickets (r k : ℕ) :
    tail (1/3) r k * (3 : ℝ)^r = (tickets r k : ℝ) := by
  induction r generalizing k with
  | zero => cases k <;> simp [tail, tickets]
  | succ r ih =>
    cases k with
    | zero => simp [tail, tickets]
    | succ k =>
      simp only [tail, tickets, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat, pow_succ]
      linear_combination ih k + 2 * ih (k+1)

def deltaStar : ℝ := 422009 / 4782969

theorem tail15_exact : tail (1/3) 15 8 = deltaStar := by
  have ht : tickets 15 8 = 1266027 := by decide +kernel
  have h := tail_tickets 15 8
  rw [ht] at h
  norm_num [deltaStar] at h ⊢
  linarith

/-- A linear-depth evaluator. Its equality with Nat.choose is proved below;
no external numerical table or native evaluator is admitted as an axiom. -/
def fastChoose (n : ℕ) : ℕ → ℕ
  | 0 => 1
  | k + 1 => fastChoose n k * (n-k) / (k+1)

theorem fastChoose_eq (n k : ℕ) : fastChoose n k = n.choose k := by
  induction k with
  | zero => simp [fastChoose]
  | succ k ih =>
    rw [fastChoose, ih, ← Nat.choose_succ_right_eq]
    simp

/-- This is a finite integer identity; the generic obstruction is elsewhere. -/
theorem bound297_exact : AgreementConsequences.bound 297 16 =
    209660394993883821947535023324611441185492248181130328034971979979928832110669599839817888 := by
  change (∑ j ∈ Finset.range 157, Nat.choose 297 j) = _
  simp_rw [← fastChoose_eq]
  decide +kernel

/-- The strict gap is checked over exact integers/rationals, not rounded floats. -/
theorem strict_gap : (AgreementConsequences.bound 297 16 : ℝ) <
    (1-2*deltaStar) * (2^297 : ℝ) := by
  rw [bound297_exact]
  norm_num [deltaStar]

end
end PvsNPCartography.MajorityNumerics
