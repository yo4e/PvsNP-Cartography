import PvsNPCartography.FiniteDual

open scoped BigOperators

namespace PvsNPCartography.Mod3Five

-- Kernel reduction is used for the closed finite arithmetic, never native_decide.
set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

/-- All five-bit inputs, not a sampled subset or a list of layer representatives. -/
abbrev Cube := Fin 5 → Fin 2
/-- Every constant bit and every vector of five linear coefficients. -/
abbrev Affine := Fin 2 × Cube

def weight (x : Cube) : ℕ := ∑ i, (x i).val

def target (x : Cube) : ℕ := if weight x % 3 = 0 then 1 else 0

/-- Integer representatives of addition and multiplication in GF(2). -/
def affineValue (p : Affine) (x : Cube) : ℕ :=
  (p.1.val + ∑ i, (p.2 i).val * (x i).val) % 2

def affineCorrect (p : Affine) (x : Cube) : ℕ :=
  if affineValue p x = target x then 1 else 0

/-- Per-input integer masses. Dividing by 180 recovers Expedition 002's q. -/
def mass (x : Cube) : ℕ :=
  match weight x with
  | 1 => 12
  | 2 => 3
  | 3 => 7
  | 4 => 2
  | 5 => 10
  | _ => 0

theorem cube_card : Fintype.card Cube = 32 := by decide +kernel

theorem affine_card : Fintype.card Affine = 64 := by decide +kernel

theorem mass_sum : (∑ x : Cube, mass x) = 180 := by decide +kernel

/-- This is exhaustive over all 64 affine coefficient choices and 32 inputs. -/
theorem affine_integer_bound :
    ∀ p : Affine, (∑ x : Cube, mass x * affineCorrect p x) ≤ 110 := by
  decide +kernel

/-- The modular evaluator is explicitly checked against actual GF(2) arithmetic. -/
theorem affine_gf2_semantics :
    ∀ (p : Affine) (x : Cube),
      (affineValue p x : ZMod 2) =
        (p.1.val : ZMod 2) + ∑ i, (p.2 i).val * (x i).val := by
  decide +kernel

noncomputable def inputProb (x : Cube) : ℝ := (mass x : ℝ) / 180

noncomputable def payoff (p : Affine) (x : Cube) : ℝ := affineCorrect p x

theorem inputProb_nonneg (x : Cube) : 0 ≤ inputProb x := by
  unfold inputProb
  positivity

theorem inputProb_sum : (∑ x : Cube, inputProb x) = 1 := by
  have h : (∑ x : Cube, (mass x : ℝ)) = 180 := by exact_mod_cast mass_sum
  calc
    (∑ x : Cube, inputProb x) = (∑ x : Cube, (mass x : ℝ)) / 180 := by
      simp only [inputProb, Finset.sum_div]
    _ = 1 := by rw [h]; norm_num

theorem deterministic_bound (p : Affine) :
    (∑ x : Cube, inputProb x * payoff p x) ≤ (11 : ℝ) / 18 := by
  have h : (∑ x : Cube, (mass x : ℝ) * (affineCorrect p x : ℝ)) ≤ 110 := by
    exact_mod_cast affine_integer_bound p
  calc
    (∑ x : Cube, inputProb x * payoff p x) =
        (∑ x : Cube, (mass x : ℝ) * (affineCorrect p x : ℝ)) / 180 := by
      simp only [inputProb, payoff, div_mul_eq_mul_div, Finset.sum_div]
    _ ≤ (11 : ℝ) / 18 := by linarith

/-- No arbitrary real probability distribution on the COMPLETE affine class
has correctness at least 2/3 at every five-bit input. The deterministic bound
is discharged above, not assumed as an input to this theorem. -/
theorem no_affine_approximation
    (mu : Affine → ℝ) (hmu_nonneg : ∀ p, 0 ≤ mu p)
    (hmu_sum : ∑ p, mu p = 1) :
    ¬ (∀ x : Cube, (2 : ℝ) / 3 ≤ ∑ p, mu p * payoff p x) := by
  exact PvsNPCartography.finite_dual_obstruction payoff mu inputProb
    ((11 : ℝ) / 18) ((2 : ℝ) / 3) hmu_nonneg hmu_sum
    inputProb_nonneg inputProb_sum deterministic_bound (by norm_num)

end PvsNPCartography.Mod3Five
