import PvsNPCartography.LayerCertificates
import PvsNPCartography.SymmetryApplications

open scoped BigOperators

namespace PvsNPCartography.Mod3Ten

open Symmetrization

set_option maxRecDepth 100000
set_option maxHeartbeats 64000000

abbrev target : BooleanCube 10 → ZMod 2 := @SmallSupportMod3.target 10

/-- Lexicographic 45-edge encoding, independently reconstructed from block codes. -/
def pairs : Fin 45 → Fin 10 × Fin 10 :=
  ![(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
    (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
    (2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),
    (3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
    (4,5),(4,6),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(5,9),
    (6,7),(6,8),(6,9),(7,8),(7,9),(8,9)]

/-- Eight seeds from Expedition013. Some seeds have degree below two.
The pointwise witness includes ALL coordinate permutations of each seed. -/
def rows : Fin 8 → SmallSupportMod3.Row :=
  ![(0,0,0),(0,0,35184372088831),(1,960,1124998687),
    (1,1023,37700386367),(1,1023,660606975615),
    (0,255,34523765113216),(0,256,11948326354815),(0,0,28879905423616)]

/-- Triple the stored integer masses: denominator 300, not 100. -/
def weights : Fin 8 → ℕ := ![30,6,117,66,45,18,12,6]

def tickets (x : BooleanCube 10) : ℕ :=
  ∑ r, weights r * SmallSupportMod3.correct pairs (rows r) x

/-- Equal half-mass on layers one and three: 12*10 + 120 = 240. -/
def mass (x : BooleanCube 10) : ℕ :=
  match hammingWeight x with
  | 1 => 12 | 3 => 1 | _ => 0

theorem weights_sum : (∑ r, weights r) = 300 := by decide +kernel

theorem mass_sum : (∑ x, mass x) = 240 := by decide +kernel

def affineScore (p : SmallSupportMod3.Affine 10) : ℕ :=
  ∑ x, mass x * SmallSupportMod3.affineCorrect p x

noncomputable def cubePermutation (e : Perm 10) : BooleanCube 10 ≃ BooleanCube 10 where
  toFun := permuteInput e
  invFun := permuteInput e.symm
  left_inv x := by funext i; simp [permuteInput]
  right_inv x := by funext i; simp [permuteInput]

theorem mass_permute (e : Perm 10) (x : BooleanCube 10) :
    mass (permuteInput e x) = mass x := by
  unfold mass hammingWeight
  rw [permute_weight]

theorem affineValue_coefficients_permute (e : Perm 10)
    (p : SmallSupportMod3.Affine 10) (x : BooleanCube 10) :
    SmallSupportMod3.affineValue (p.1, permuteInput e p.2) x =
      SmallSupportMod3.affineValue p (permuteInput e.symm x) := by
  have h : (∑ i : Fin 10, (p.2 (e i)).val * (x i).val) =
      ∑ i : Fin 10, (p.2 i).val * (x (e.symm i)).val := by
    simpa only [Equiv.symm_apply_apply] using
      (Equiv.sum_comp e (fun i : Fin 10 => (p.2 i).val * (x (e.symm i)).val))
  exact congrArg (fun z : ℕ => (p.1.val : ZMod 2) + (z : ZMod 2)) h

theorem affineCorrect_coefficients_permute (e : Perm 10)
    (p : SmallSupportMod3.Affine 10) (x : BooleanCube 10) :
    SmallSupportMod3.affineCorrect (p.1, permuteInput e p.2) x =
      SmallSupportMod3.affineCorrect p (permuteInput e.symm x) := by
  unfold SmallSupportMod3.affineCorrect
  rw [affineValue_coefficients_permute, mod3_symmetric 10 e.symm x]

theorem affineScore_permute (e : Perm 10) (p : SmallSupportMod3.Affine 10) :
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

def canonicalCoefficients (w : Fin 11) : BooleanCube 10 :=
  fun i => if i.val < w.val then 1 else 0

theorem canonical_weight : ∀ w : Fin 11,
    hammingWeight (canonicalCoefficients w) = w.val := by decide +kernel

/-- Twenty-two computed representatives; coverage of all rows is proved next. -/
theorem canonical_affine_bound : ∀ (c : Fin 2) (w : Fin 11),
    affineScore (c, canonicalCoefficients w) ≤ 152 := by decide +kernel

/-- All 2048 affine coefficient rows, by a proved permutation reduction. -/
theorem affine_bound : ∀ p : SmallSupportMod3.Affine 10,
    (∑ x, mass x * SmallSupportMod3.affineCorrect p x) ≤ 152 := by
  intro p
  let w : Fin 11 := ⟨hammingWeight p.2, by have h := hammingWeight_le p.2; omega⟩
  have hw : hammingWeight p.2 = hammingWeight (canonicalCoefficients w) :=
    (canonical_weight w).symm
  obtain ⟨e, he⟩ := exists_permutation_of_weight_eq p.2 (canonicalCoefficients w) hw
  have hs := affineScore_permute e p
  rw [he] at hs
  change affineScore p ≤ 152
  rw [← hs]
  exact canonical_affine_bound p.1 w

/-- All eleven full-cube layer sums, independently matched to Python integers. -/
def layerTickets : Fin 11 → ℕ :=
  ![228,2142,9567,25476,44838,53820,44964,25692,9594,2298,213]

theorem layer_tickets_exact : ∀ w : Fin 11,
    (∑ x : BooleanCube 10,
      if hammingWeight x = w.val then tickets x else 0) = layerTickets w := by
  decide +kernel

theorem upper_layer_bound : ∀ w : Fin 11,
    200 * Nat.choose 10 w.val ≤ ∑ x : BooleanCube 10,
      if hammingWeight x = w.val then tickets x else 0 := by
  intro w
  rw [layer_tickets_exact]
  exact (by decide +kernel : ∀ w : Fin 11, 200 * Nat.choose 10 w.val ≤ layerTickets w) w

/-- Removing symmetrization leaves only six winning tickets out of 300. -/
theorem raw_seed_counterexample :
    tickets (![0,0,0,0,0,0,1,0,1,1] : BooleanCube 10) = 6 := by decide +kernel

noncomputable def seedPolynomial (r : Fin 8) : BinaryPolynomial 10 :=
  SmallSupportMod3.polynomial pairs (rows r)

noncomputable def seedWeights (r : Fin 8) : ℝ := (weights r : ℝ) / 300

theorem seed_correct (r : Fin 8) (x : BooleanCube 10) :
    correct target (seedPolynomial r) x =
      (SmallSupportMod3.correct pairs (rows r) x : ℝ) := by
  unfold correct seedPolynomial SmallSupportMod3.correct
  rw [SmallSupportMod3.polynomial_eval]
  split_ifs <;> norm_num

theorem seed_success (x : BooleanCube 10) :
    success target seedPolynomial seedWeights x = (tickets x : ℝ) / 300 := by
  unfold success
  simp_rw [seed_correct]
  simp only [seedWeights, div_mul_eq_mul_div, ← Finset.sum_div, tickets,
    Nat.cast_sum, Nat.cast_mul]

theorem seed_layer_bound (w : ℕ) (hw : w ≤ 10) :
    1 - (1 / 3 : ℝ) ≤ layerAverage (success target seedPolynomial seedWeights) w := by
  have hn : 200 * Nat.choose 10 w ≤ ∑ y : Layer 10 w, tickets y.1 := by
    rw [sum_layer_eq_filter]
    exact upper_layer_bound ⟨w, by omega⟩
  have hr : (200 : ℝ) * Nat.choose 10 w ≤ ∑ y : Layer 10 w, (tickets y.1 : ℝ) := by
    exact_mod_cast hn
  have hc : (0 : ℝ) < Nat.choose 10 w := by exact_mod_cast Nat.choose_pos hw
  unfold layerAverage
  simp_rw [seed_success]
  rw [← Finset.sum_div, layer_card]
  apply (le_div_iff₀ hc).mpr
  nlinarith

/-- A single input-independent REAL distribution on genuine degree <=2 polynomials. -/
theorem degree_two_feasible : HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) 2 := by
  apply feasible_of_layer_bounds (mod3_symmetric 10) seedPolynomial seedWeights
  · intro r
    exact SmallSupportMod3.polynomial_degree pairs (rows r)
  · intro r
    unfold seedWeights
    positivity
  · have hs : (∑ r, (weights r : ℝ)) = 300 := by exact_mod_cast weights_sum
    simp only [seedWeights, ← Finset.sum_div, hs]
    norm_num
  · exact seed_layer_bound

/-- Structural polynomial normal form makes the lower bound universal. -/
theorem degree_one_impossible : ¬ HasProbabilisticDegreeAtMost target (1 / 3 : ℝ) 1 := by
  rintro ⟨m, P, mu, hd, hn, hs, hp⟩
  apply SmallSupportMod3.no_degree_one_family mass 240 152 (by decide)
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

theorem raw_seed_mixture_is_not_pointwise :
    ∃ x : BooleanCube 10, success target seedPolynomial seedWeights x < (2 : ℝ) / 3 := by
  refine ⟨![0,0,0,0,0,0,1,0,1,1], ?_⟩
  rw [seed_success, raw_seed_counterexample]
  norm_num

end PvsNPCartography.Mod3Ten
