import PvsNPCartography.LayerCertificates
import PvsNPCartography.SymmetryApplications

open scoped BigOperators

namespace PvsNPCartography.Mod3Nine

open Symmetrization

set_option maxRecDepth 100000
set_option maxHeartbeats 32000000

abbrev target : BooleanCube 9 → ZMod 2 := @SmallSupportMod3.target 9

/-- Lexicographic unordered coordinate pairs, aligned with Python certificate. -/
def pairs : Fin 36 → Fin 9 × Fin 9 :=
  ![(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),
    (0,7),(0,8),(1,2),(1,3),(1,4),(1,5),
    (1,6),(1,7),(1,8),(2,3),(2,4),(2,5),
    (2,6),(2,7),(2,8),(3,4),(3,5),(3,6),
    (3,7),(3,8),(4,5),(4,6),(4,7),(4,8),
    (5,6),(5,7),(5,8),(6,7),(6,8),(7,8)]

/-- Exactly ONE quadratic seed. Full permutation averaging, not the raw seed,
is the pointwise probability distribution. -/
def rows : Fin 1 → SmallSupportMod3.Row := ![(1,127,36505001791)]

/-- Triple tickets avoid fractions in the concrete upper-layer kernel bound. -/
def weights : Fin 1 → ℕ := ![3]

def tickets (x : BooleanCube 9) : ℕ :=
  ∑ r, weights r * SmallSupportMod3.correct pairs (rows r) x

/-- Equal half-mass on Hamming layers one and three:
28*choose(9,1)+3*choose(9,3)=504. -/
def mass (x : BooleanCube 9) : ℕ :=
  match hammingWeight x with
  | 1 => 28 | 3 => 3 | _ => 0

theorem weights_sum : (∑ r, weights r) = 3 := by decide +kernel

theorem mass_sum : (∑ x, mass x) = 504 := by decide +kernel

def affineScore (p : SmallSupportMod3.Affine 9) : ℕ :=
  ∑ x, mass x * SmallSupportMod3.affineCorrect p x

/-- A full-cube bijection; this is not a layer or a sampled input list. -/
noncomputable def cubePermutation (e : Perm 9) : BooleanCube 9 ≃ BooleanCube 9 where
  toFun := permuteInput e
  invFun := permuteInput e.symm
  left_inv x := by funext i; simp [permuteInput]
  right_inv x := by funext i; simp [permuteInput]

theorem mass_permute (e : Perm 9) (x : BooleanCube 9) :
    mass (permuteInput e x) = mass x := by
  unfold mass hammingWeight
  rw [permute_weight]

/-- Renaming the coefficient positions is dual to inverse input pullback. -/
theorem affineValue_coefficients_permute (e : Perm 9)
    (p : SmallSupportMod3.Affine 9) (x : BooleanCube 9) :
    SmallSupportMod3.affineValue (p.1, permuteInput e p.2) x =
      SmallSupportMod3.affineValue p (permuteInput e.symm x) := by
  have h : (∑ i : Fin 9, (p.2 (e i)).val * (x i).val) =
      ∑ i : Fin 9, (p.2 i).val * (x (e.symm i)).val := by
    simpa only [Equiv.symm_apply_apply] using
      (Equiv.sum_comp e (fun i : Fin 9 => (p.2 i).val * (x (e.symm i)).val))
  exact congrArg (fun z : ℕ => (p.1.val : ZMod 2) + (z : ZMod 2)) h

theorem affineCorrect_coefficients_permute (e : Perm 9)
    (p : SmallSupportMod3.Affine 9) (x : BooleanCube 9) :
    SmallSupportMod3.affineCorrect (p.1, permuteInput e p.2) x =
      SmallSupportMod3.affineCorrect p (permuteInput e.symm x) := by
  unfold SmallSupportMod3.affineCorrect
  rw [affineValue_coefficients_permute, mod3_symmetric 9 e.symm x]

theorem affineScore_permute (e : Perm 9) (p : SmallSupportMod3.Affine 9) :
    affineScore (p.1, permuteInput e p.2) = affineScore p := by
  classical
  unfold affineScore
  simp_rw [affineCorrect_coefficients_permute]
  calc
    _ = ∑ x, mass (permuteInput e.symm x) *
        SmallSupportMod3.affineCorrect p (permuteInput e.symm x) := by
      apply Finset.sum_congr rfl
      intro x _
      rw [mass_permute]
    _ = _ := Equiv.sum_comp (cubePermutation e.symm)
      (fun x => mass x * SmallSupportMod3.affineCorrect p x)

def canonicalCoefficients (w : Fin 10) : BooleanCube 9 :=
  fun i => if i.val < w.val then 1 else 0

theorem canonical_weight : ∀ w : Fin 10,
    hammingWeight (canonicalCoefficients w) = w.val := by decide +kernel

/-- Only twenty cases are computed; the general row coverage is proved below. -/
theorem canonical_affine_bound : ∀ (c : Fin 2) (w : Fin 10),
    affineScore (c, canonicalCoefficients w) ≤ 322 := by decide +kernel

/-- All 1024 affine rows are covered by a proved permutation reduction, rather
than placing their whole repeated computation in one large kernel term. -/
theorem affine_bound : ∀ p : SmallSupportMod3.Affine 9,
    (∑ x, mass x * SmallSupportMod3.affineCorrect p x) ≤ 322 := by
  intro p
  let w : Fin 10 := ⟨hammingWeight p.2, by have h := hammingWeight_le p.2; omega⟩
  have hw : hammingWeight p.2 = hammingWeight (canonicalCoefficients w) :=
    (canonical_weight w).symm
  obtain ⟨e, he⟩ := exists_permutation_of_weight_eq p.2 (canonicalCoefficients w) hw
  have hs := affineScore_permute e p
  rw [he] at hs
  change affineScore p ≤ 322
  rw [← hs]
  exact canonical_affine_bound p.1 w

/-- All ten layer bounds are checked, without sampling inputs.
The general theorem converts uniform Hamming-layer averages to one fixed
distribution over polynomial permutations. -/
theorem upper_layer_bound : ∀ w : Fin 10,
    2 * Nat.choose 9 w.val ≤ ∑ x : BooleanCube 9,
      if hammingWeight x = w.val then tickets x else 0 := by
  decide +kernel

/-- Diagnostic: do not silently omit full symmetrization. -/
theorem raw_seed_counterexample :
    tickets (![0,0,0,0,0,0,0,1,0] : BooleanCube 9) = 0 := by decide +kernel

noncomputable def seedPolynomial (r : Fin 1) : BinaryPolynomial 9 :=
  SmallSupportMod3.polynomial pairs (rows r)

noncomputable def seedWeights (r : Fin 1) : ℝ := (weights r : ℝ) / 3

theorem seed_correct (r : Fin 1) (x : BooleanCube 9) :
    correct target (seedPolynomial r) x =
      (SmallSupportMod3.correct pairs (rows r) x : ℝ) := by
  unfold correct seedPolynomial SmallSupportMod3.correct
  rw [SmallSupportMod3.polynomial_eval]
  split_ifs <;> norm_num

theorem seed_success (x : BooleanCube 9) :
    success target seedPolynomial seedWeights x = (tickets x : ℝ) / 3 := by
  unfold success
  simp_rw [seed_correct]
  simp only [seedWeights, div_mul_eq_mul_div, ← Finset.sum_div, tickets,
    Nat.cast_sum, Nat.cast_mul]

theorem seed_layer_bound (w : ℕ) (hw : w ≤ 9) :
    1 - (1 / 3 : ℝ) ≤ layerAverage (success target seedPolynomial seedWeights) w := by
  have hn : 2 * Nat.choose 9 w ≤ ∑ y : Layer 9 w, tickets y.1 := by
    rw [sum_layer_eq_filter]
    exact upper_layer_bound ⟨w, by omega⟩
  have hr : (2 : ℝ) * Nat.choose 9 w ≤ ∑ y : Layer 9 w, (tickets y.1 : ℝ) := by
    exact_mod_cast hn
  have hc : (0 : ℝ) < Nat.choose 9 w := by exact_mod_cast Nat.choose_pos hw
  unfold layerAverage
  simp_rw [seed_success]
  rw [← Finset.sum_div, layer_card]
  apply (le_div_iff₀ hc).mpr
  nlinarith

/-- The final witness is the product with ALL permutations, supplied by the
verified layer bridge. It has genuine totalDegree <=2 and normalized REAL mass. -/
theorem degree_two_feasible : HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) 2 := by
  apply feasible_of_layer_bounds (mod3_symmetric 9) seedPolynomial seedWeights
  · intro r
    exact SmallSupportMod3.polynomial_degree pairs (rows r)
  · intro r
    unfold seedWeights
    positivity
  · have hs : (∑ r, (weights r : ℝ)) = 3 := by exact_mod_cast weights_sum
    simp only [seedWeights, ← Finset.sum_div, hs]
    norm_num
  · exact seed_layer_bound

/-- Structural coverage plus a fully exhausted dual excludes arbitrary
finite real mixtures of degree-at-most-one polynomial objects. -/
theorem degree_one_impossible : ¬ HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) 1 := by
  rintro ⟨m, P, mu, hd, hn, hs, hp⟩
  apply SmallSupportMod3.no_degree_one_family mass 504 322 (by decide)
    mass_sum affine_bound (by norm_num) P mu hd hn hs
  have ht : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simpa only [ht] using hp

theorem feasible_degree_iff (d : ℕ) :
    HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) d ↔ 2 ≤ d := by
  constructor
  · intro h
    by_contra hsmall
    exact degree_one_impossible (h.mono (by omega))
  · intro h
    exact degree_two_feasible.mono h

theorem degree_exists : ∃ d, HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) d :=
  ⟨2, degree_two_feasible⟩

theorem least_feasible_degree :
    IsLeast {d : ℕ | HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) d} 2 :=
  ⟨degree_two_feasible, fun _ h => (feasible_degree_iff _).mp h⟩

theorem pdeg_eq_two : probabilisticDegree target (1 / 3 : ℝ) degree_exists = 2 := by
  classical
  unfold probabilisticDegree
  apply le_antisymm
  · exact Nat.find_min' degree_exists degree_two_feasible
  · exact (feasible_degree_iff _).mp (Nat.find_spec degree_exists)

/-- A formal failure of the unsymmetrized single-seed shortcut. -/
theorem raw_seed_mixture_is_not_pointwise :
    ∃ x : BooleanCube 9, success target seedPolynomial seedWeights x < (2 : ℝ) / 3 := by
  refine ⟨![0,0,0,0,0,0,0,1,0], ?_⟩
  rw [seed_success, raw_seed_counterexample]
  norm_num

end PvsNPCartography.Mod3Nine
