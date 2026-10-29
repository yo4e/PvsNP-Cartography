import Mathlib

namespace PvsNPCartography.CentralBinomialBound
noncomputable section

/-- Normalized even central binomial coefficient. -/
def central (s : ℕ) : ℝ := (Nat.centralBinom s : ℝ) / (4 : ℝ)^s

/-- Maximum atom of the fair binomial distribution, for either parity. -/
def peak (m : ℕ) : ℝ := (m.choose (m/2) : ℝ) / (2 : ℝ)^m

theorem central_nonneg (s : ℕ) : 0 ≤ central s := by
  unfold central
  positivity

theorem peak_nonneg (m : ℕ) : 0 ≤ peak m := by
  unfold peak
  positivity

/-- Exact recurrence, with denominators cleared. -/
theorem central_step (s : ℕ) :
    central (s+1) * (2*(s : ℝ)+2) = central s * (2*s+1) := by
  have h : ((s : ℝ)+1) * (Nat.centralBinom (s+1) : ℝ) =
      2*(2*s+1)*(Nat.centralBinom s : ℝ) := by
    exact_mod_cast Nat.succ_mul_centralBinom_succ s
  unfold central
  rw [pow_succ]
  have hp : (4 : ℝ)^s ≠ 0 := by positivity
  field_simp
  nlinarith [h]

/-- An all-s induction, not a table or asymptotic estimate. -/
theorem central_square (s : ℕ) : (3*(s : ℝ)+1) * (central s)^2 ≤ 1 := by
  induction s with
  | zero => norm_num [central]
  | succ s ih =>
    have hs : (0 : ℝ) ≤ s := Nat.cast_nonneg s
    have hc : (3*(s : ℝ)+4)*(2*s+1)^2 ≤ (3*s+1)*(2*s+2)^2 := by
      nlinarith
    have hr : (central (s+1))^2 * (2*(s : ℝ)+2)^2 =
        (central s)^2 * (2*s+1)^2 := by
      calc
        _ = (central (s+1)*(2*(s : ℝ)+2))^2 := by ring
        _ = (central s*(2*s+1))^2 := by rw [central_step]
        _ = _ := by ring
    have hmul := mul_le_mul_of_nonneg_right hc (sq_nonneg (central s))
    have hi := mul_le_mul_of_nonneg_right ih (sq_nonneg (2*(s : ℝ)+2))
    have hgoal : (3*(s : ℝ)+4)*(central (s+1))^2*(2*s+2)^2 ≤ (2*s+2)^2 := by
      calc
        _ = (3*(s : ℝ)+4)*((central s)^2*(2*s+1)^2) := by
          rw [mul_assoc, hr]
        _ ≤ (3*(s : ℝ)+1)*(central s)^2*(2*s+2)^2 := by
          nlinarith [hmul]
        _ ≤ _ := by simpa only [one_mul] using hi
    have hp : (0 : ℝ) < (2*(s : ℝ)+2)^2 := by positivity
    have hfinal := (mul_le_mul_right hp).mp hgoal
    push_cast
    nlinarith [hfinal]

theorem peak_even (s : ℕ) : peak (2*s) = central s := by
  unfold peak central
  rw [Nat.mul_div_cancel_left s (by decide)]
  norm_num [Nat.centralBinom, pow_mul]

/-- Adjacent odd and even rows have the same normalized maximum atom. -/
theorem peak_odd (s : ℕ) : peak (2*s+1) = central (s+1) := by
  have hi : (2*s+1)/2 = s := by omega
  have hc : Nat.centralBinom (s+1) = 2*(2*s+1).choose s := by
    rw [Nat.centralBinom, show 2*(s+1) = (2*s+1)+1 by omega,
      Nat.choose_succ_succ', Nat.choose_symm_half]
    omega
  unfold peak central
  rw [hi, hc]
  push_cast
  simp only [pow_succ, pow_mul]
  ring

/-- Uniform maximum-atom estimate; m=0 is also valid without division by m. -/
theorem peak_square (m : ℕ) : (m : ℝ)*(peak m)^2 ≤ 1 := by
  have he : m = 2*(m/2) ∨ m = 2*(m/2)+1 := by omega
  rcases he with he | he
  · rw [he, peak_even]
    have h := central_square (m/2)
    have hnon := sq_nonneg (central (m/2))
    push_cast
    nlinarith [mul_nonneg (show (0 : ℝ) ≤ (m/2 : ℕ) + 1 by positivity) hnon]
  · rw [he, peak_odd]
    have h := central_square (m/2+1)
    have hnon := sq_nonneg (central (m/2+1))
    push_cast at h ⊢
    nlinarith [mul_nonneg (show (0 : ℝ) ≤ (m/2 : ℕ) + 3 by positivity) hnon]

theorem coefficient_le_peak (m j : ℕ) :
    (m.choose j : ℝ) ≤ peak m * (2 : ℝ)^m := by
  have h : (m.choose j : ℝ) ≤ (m.choose (m/2) : ℝ) := by
    exact_mod_cast Nat.choose_le_middle j m
  have hp : (2 : ℝ)^m ≠ 0 := by positivity
  simpa [peak, hp] using h

end
end PvsNPCartography.CentralBinomialBound
