import PvsNPCartography.BalancedAffineDualAlgebra

namespace PvsNPCartography.BalancedAffineCounting

noncomputable section

/-- Polynomial identities proved by Pascal induction, including n=0 and n=1. -/
theorem choose_two_cast (n : ℕ) :
    (n.choose 2 : ℝ) = (n : ℝ) * (n - 1) / 2 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
    rw [Nat.choose_succ_succ, Nat.choose_one_right]
    push_cast
    rw [ih]
    ring

theorem choose_three_cast (n : ℕ) :
    (n.choose 3 : ℝ) = (n : ℝ) * (n - 1) * (n - 2) / 6 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
    rw [Nat.choose_succ_succ]
    push_cast
    rw [choose_two_cast, ih]
    ring

theorem six_mul_choose_three (n : ℕ) :
    6 * (n.choose 3 : ℝ) = (n : ℝ) * (n - 1) * (n - 2) := by
  rw [choose_three_cast]
  ring

/-- Binomial expression from the singleton and odd triple intersections. -/
def countedScore (n k : ℕ) : ℝ :=
  ((n - k : ℕ) : ℝ) / (2 * n) +
    ((k : ℝ) * ((n - k).choose 2 : ℝ) + (k.choose 3 : ℝ)) / (2 * (n.choose 3 : ℝ))

theorem countedScore_eq {n k : ℕ} (hn : 3 ≤ n) (hk : k ≤ n) :
    countedScore n k = BalancedAffineDualAlgebra.score n k := by
  have hnr : (3 : ℝ) ≤ n := by exact_mod_cast hn
  have hn0 : (n : ℝ) ≠ 0 := by linarith
  have hn1 : (n : ℝ) - 1 ≠ 0 := by linarith
  have hn2 : (n : ℝ) - 2 ≠ 0 := by linarith
  unfold countedScore BalancedAffineDualAlgebra.score
  simp only [choose_two_cast, choose_three_cast, Nat.cast_sub hk]
  field_simp [hn0, hn1, hn2]
  ring

end
end PvsNPCartography.BalancedAffineCounting
