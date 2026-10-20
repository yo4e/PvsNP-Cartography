import Mathlib

namespace PvsNPCartography.BalancedAffineDualAlgebra

/-- Pure real algebra only. The Boolean-cube counting bridge is not assumed
proved by this module. The rational envelope intentionally need not be sharp. -/
theorem cubic_envelope_nonnegative {n t : ℝ} (hn : 0 ≤ n) (ht : 0 ≤ t) :
    t * (n * n - t * t) ≤ (2 / 5 : ℝ) * (n * n * n) := by
  by_cases hsmall : t ≤ 2 * n / 5
  · have h₁ := mul_nonneg (sq_nonneg n) (sub_nonneg.mpr hsmall)
    have h₂ := mul_nonneg ht (sq_nonneg t)
    nlinarith
  · have hlarge : 0 ≤ t - 2 * n / 5 := by linarith
    have h₁ := mul_nonneg (sq_nonneg (t - 3 * n / 5))
      (show 0 ≤ t + 6 * n / 5 by linarith)
    have h₂ := mul_nonneg (sq_nonneg n) hlarge
    nlinarith

/-- The interval bound also covers negative t. -/
theorem cubic_envelope {n t : ℝ} (hn : 0 ≤ n) (hlo : -n ≤ t) (hhi : t ≤ n) :
    t * (n * n - t * t) ≤ (2 / 5 : ℝ) * (n * n * n) := by
  by_cases ht : 0 ≤ t
  · exact cubic_envelope_nonnegative hn ht
  · have ht' : t ≤ 0 := by linarith
    have hf₀ := mul_nonneg (sub_nonneg.mpr hhi)
      (show 0 ≤ n + t by linarith)
    have hf : 0 ≤ n * n - t * t := by nlinarith
    have hp : t * (n * n - t * t) ≤ 0 := mul_nonpos_of_nonpos_of_nonneg ht' hf
    have hr : 0 ≤ (2 / 5 : ℝ) * (n * n * n) := by positivity
    exact hp.trans hr

/-- Algebraic candidate for an equal-half layer-one/layer-three affine score.
This definition alone is not the finite Boolean-cube score identity. -/
noncomputable def score (n k : ℝ) : ℝ :=
  1 / 2 + ((n - 2 * k) * (n * n - (n - 2 * k) * (n - 2 * k))) /
    (4 * n * (n - 1) * (n - 2))

theorem score_complement (n k : ℝ) : score n (n - k) = 1 - score n k := by
  unfold score
  ring

/-- Uniform strict bound for the algebraic score, for all real n>=7 and
0<=k<=n. No finite enumeration is used in this proof. -/
theorem score_lt_two_thirds {n k : ℝ} (hn : 7 ≤ n) (hk : 0 ≤ k) (hkn : k ≤ n) :
    score n k < (2 / 3 : ℝ) := by
  have hn0 : 0 < n := by linarith
  have hn1 : 0 < n - 1 := by linarith
  have hn2 : 0 < n - 2 := by linarith
  have hden : 0 < 4 * n * (n - 1) * (n - 2) := by positivity
  have henv := cubic_envelope (le_of_lt hn0)
    (show -n ≤ n - 2 * k by linarith) (show n - 2 * k ≤ n by linarith)
  have hprod := mul_nonneg (show 0 ≤ n - 7 by linarith)
    (show 0 ≤ 2 * n - 1 by linarith)
  have hgap0 : 0 < 2 * n * n - 15 * n + 10 := by nlinarith
  have hgap := mul_pos hn0 hgap0
  have hstrict : (2 / 5 : ℝ) * (n * n * n) <
      (1 / 6 : ℝ) * (4 * n * (n - 1) * (n - 2)) := by nlinarith
  have hdiv : ((n - 2 * k) * (n * n - (n - 2 * k) * (n - 2 * k))) /
      (4 * n * (n - 1) * (n - 2)) < (1 / 6 : ℝ) :=
    (div_lt_iff₀ hden).mpr (lt_of_le_of_lt henv hstrict)
  unfold score
  linarith

theorem score_gt_one_third {n k : ℝ} (hn : 7 ≤ n) (hk : 0 ≤ k) (hkn : k ≤ n) :
    (1 / 3 : ℝ) < score n k := by
  have h := score_lt_two_thirds hn
    (show 0 ≤ n - k by linarith) (show n - k ≤ n by linarith)
  rw [score_complement] at h
  linarith

/-- A boundary witness: extending this strict bound down to n=6 is false. -/
theorem six_is_tight : score 6 1 = (2 / 3 : ℝ) := by
  norm_num [score]

end PvsNPCartography.BalancedAffineDualAlgebra
