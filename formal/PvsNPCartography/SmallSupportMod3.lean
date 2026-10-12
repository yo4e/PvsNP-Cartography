import PvsNPCartography.DegreeOneNormalForm
import PvsNPCartography.ProbabilisticDegree

open scoped BigOperators

namespace PvsNPCartography.SmallSupportMod3

set_option maxRecDepth 100000
set_option maxHeartbeats 16000000

/-- The actual field-valued MOD3 target, on the entire Boolean cube. -/
def target {n : ℕ} (x : BooleanCube n) : ZMod 2 :=
  if (∑ i, (x i).val) % 3 = 0 then 1 else 0

abbrev Affine (n : ℕ) := Fin 2 × BooleanCube n

def affineValue {n : ℕ} (p : Affine n) (x : BooleanCube n) : ZMod 2 :=
  (p.1.val : ZMod 2) + ∑ i, (p.2 i).val * (x i).val

def affineCorrect {n : ℕ} (p : Affine n) (x : BooleanCube n) : ℕ :=
  if affineValue p x = target x then 1 else 0

noncomputable def affinePolynomial {n : ℕ} (p : Affine n) : BinaryPolynomial n :=
  MvPolynomial.C (p.1.val : ZMod 2) +
    ∑ i, MvPolynomial.C ((p.2 i).val : ZMod 2) * MvPolynomial.X i

noncomputable def coefficientRow {n : ℕ} (P : BinaryPolynomial n) : Affine n :=
  (P.coeff 0, fun i => P.coeff (Finsupp.single i 1))

theorem degree_one_eq_affine {n : ℕ} (P : BinaryPolynomial n)
    (hP : P.totalDegree ≤ 1) : P = affinePolynomial (coefficientRow P) := by
  change P = MvPolynomial.C (((P.coeff 0).val : ℕ) : ZMod 2) +
    ∑ i, MvPolynomial.C (((P.coeff (Finsupp.single i 1)).val : ℕ) : ZMod 2) *
      MvPolynomial.X i
  simp only [ZMod.natCast_zmod_val]
  exact degree_one_normal_form P hP

theorem affine_polynomial_correct {n : ℕ} (p : Affine n) (x : BooleanCube n) :
    (affineCorrect p x : ℝ) =
      if MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (affinePolynomial p) =
        target x then 1 else 0 := by
  simp [affineCorrect, affineValue, affinePolynomial]

/-- Generic certificate bridge. The mass and exhaustive row bound are hypotheses
HERE, and are discharged by kernel computation in each concrete application. -/
theorem no_degree_one_family {n : ℕ}
    (mass : BooleanCube n → ℕ) (D B : ℕ) (hD : 0 < D)
    (hmass : ∑ x, mass x = D)
    (hbound : ∀ p : Affine n, (∑ x, mass x * affineCorrect p x) ≤ B)
    (hgap : (B : ℝ) / D < (2 : ℝ) / 3)
    {I : Type} [Fintype I] (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hd : ∀ i, (P i).totalDegree ≤ 1) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) :
    ¬ (∀ x : BooleanCube n, (2 : ℝ) / 3 ≤ ∑ i, mu i *
      (if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) =
        target x then 1 else 0)) := by
  classical
  let q : BooleanCube n → ℝ := fun x => (mass x : ℝ) / D
  have hDr : (0 : ℝ) < D := by exact_mod_cast hD
  have hqnonneg : ∀ x, 0 ≤ q x := by intro x; dsimp [q]; positivity
  have hqsum : ∑ x, q x = 1 := by
    have hm : (∑ x, (mass x : ℝ)) = D := by exact_mod_cast hmass
    simp only [q, ← Finset.sum_div, hm]
    exact div_self (ne_of_gt hDr)
  have hb (p : Affine n) :
      (∑ x, q x * (affineCorrect p x : ℝ)) ≤ (B : ℝ) / D := by
    have h : (∑ x, (mass x : ℝ) * (affineCorrect p x : ℝ)) ≤ B := by
      exact_mod_cast hbound p
    calc
      _ = (∑ x, (mass x : ℝ) * (affineCorrect p x : ℝ)) / D := by
        simp only [q, div_mul_eq_mul_div, Finset.sum_div]
      _ ≤ (B : ℝ) / D := div_le_div_of_nonneg_right h (le_of_lt hDr)
  have h := finite_dual_obstruction
    (fun i x => (affineCorrect (coefficientRow (P i)) x : ℝ)) mu q
    ((B : ℝ) / D) ((2 : ℝ) / 3) hn hs hqnonneg hqsum
    (fun i => hb (coefficientRow (P i))) hgap
  have heq : ∀ i x, (affineCorrect (coefficientRow (P i)) x : ℝ) =
      if MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) (P i) =
        target x then 1 else 0 := by
    intro i x
    rw [affine_polynomial_correct, ← degree_one_eq_affine (P i) (hd i)]
  simpa only [heq] using h

/-- Constant, linear mask, quadratic mask. Pairs are supplied explicitly. -/
abbrev Row := ℕ × ℕ × ℕ

def linear {n : ℕ} (r : Row) (i : Fin n) : ℕ := r.2.1 / 2^i.val % 2

def quadratic {k : ℕ} (r : Row) (j : Fin k) : ℕ := r.2.2 / 2^j.val % 2

def value {n k : ℕ} (pairs : Fin k → Fin n × Fin n)
    (r : Row) (x : BooleanCube n) : ZMod 2 :=
  (r.1 : ZMod 2) + (∑ i, (linear r i : ZMod 2) * (x i).val) +
    ∑ j, (quadratic r j : ZMod 2) * (x (pairs j).1).val * (x (pairs j).2).val

def correct {n k : ℕ} (pairs : Fin k → Fin n × Fin n)
    (r : Row) (x : BooleanCube n) : ℕ := if value pairs r x = target x then 1 else 0

noncomputable def polynomial {n k : ℕ} (pairs : Fin k → Fin n × Fin n)
    (r : Row) : BinaryPolynomial n :=
  MvPolynomial.C (r.1 : ZMod 2) +
    (∑ i, MvPolynomial.C (linear r i : ZMod 2) * MvPolynomial.X i) +
    ∑ j, MvPolynomial.C (quadratic r j : ZMod 2) *
      MvPolynomial.X (pairs j).1 * MvPolynomial.X (pairs j).2

theorem polynomial_eval {n k : ℕ} (pairs : Fin k → Fin n × Fin n)
    (r : Row) (x : BooleanCube n) :
    MvPolynomial.eval (fun i => ((x i).val : ZMod 2)) (polynomial pairs r) =
      value pairs r x := by
  simp [polynomial, value]

theorem polynomial_degree {n k : ℕ} (pairs : Fin k → Fin n × Fin n) (r : Row) :
    (polynomial pairs r).totalDegree ≤ 2 := by
  have hlin (c : ZMod 2) (i : Fin n) :
      (MvPolynomial.C c * MvPolynomial.X i).totalDegree ≤ 1 := by
    simpa using MvPolynomial.totalDegree_mul (MvPolynomial.C c)
      (MvPolynomial.X i : BinaryPolynomial n)
  have hquad (c : ZMod 2) (i j : Fin n) :
      (MvPolynomial.C c * MvPolynomial.X i * MvPolynomial.X j).totalDegree ≤ 2 := by
    calc
      _ ≤ (MvPolynomial.C c * MvPolynomial.X i).totalDegree +
          (MvPolynomial.X j : BinaryPolynomial n).totalDegree :=
        MvPolynomial.totalDegree_mul _ _
      _ ≤ 1 + 1 := Nat.add_le_add (hlin c i) (by simp)
  unfold polynomial
  apply (MvPolynomial.totalDegree_add _ _).trans
  apply max_le
  · apply (MvPolynomial.totalDegree_add _ _).trans
    apply max_le
    · simp
    · exact (MvPolynomial.totalDegree_finsetSum_le fun i _ => hlin _ i).trans (by decide)
  · exact MvPolynomial.totalDegree_finsetSum_le fun j _ => hquad _ _ _

/-- Converts exact integer pointwise counts into one normalized real distribution
on actual degree-two polynomial objects. No symmetry hypothesis is used. -/
theorem quadratic_feasible {n k m : ℕ} (pairs : Fin k → Fin n × Fin n)
    (rows : Fin m → Row) (weights : Fin m → ℕ) (D T : ℕ)
    (hD : 0 < D) (hsum : ∑ r, weights r = D)
    (hpoint : ∀ x : BooleanCube n, T ≤ ∑ r, weights r * correct pairs (rows r) x)
    (hthreshold : (2 : ℝ) / 3 ≤ (T : ℝ) / D) :
    HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) 2 := by
  have hDr : (0 : ℝ) < D := by exact_mod_cast hD
  refine ⟨m, (fun r => polynomial pairs (rows r)), (fun r => (weights r : ℝ) / D),
    (fun r => polynomial_degree pairs (rows r)), ?_, ?_, ?_⟩
  · intro r; positivity
  · have h : (∑ r, (weights r : ℝ)) = D := by exact_mod_cast hsum
    rw [← Finset.sum_div, h]
    exact div_self (ne_of_gt hDr)
  · intro x
    have h : (T : ℝ) ≤ ∑ r, (weights r : ℝ) * (correct pairs (rows r) x : ℝ) := by
      exact_mod_cast hpoint x
    have heq : ∀ r, (correct pairs (rows r) x : ℝ) =
        if MvPolynomial.eval (fun i => ((x i).val : ZMod 2))
          (polynomial pairs (rows r)) = target x then 1 else 0 := by
      intro r
      rw [polynomial_eval]
      simp [correct]
    calc
      (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
      _ ≤ (T : ℝ) / D := hthreshold
      _ ≤ (∑ r, (weights r : ℝ) * (correct pairs (rows r) x : ℝ)) / D :=
        div_le_div_of_nonneg_right h (le_of_lt hDr)
      _ = ∑ r, ((weights r : ℝ) / D) * (correct pairs (rows r) x : ℝ) := by
        simp only [div_mul_eq_mul_div, Finset.sum_div]
      _ = _ := by simp_rw [heq]

def weights : Fin 18 → ℕ := ![2,4,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

theorem weights_sum : (∑ r, weights r) = 24 := by decide +kernel

namespace Six

def pairs : Fin 15 → Fin 6 × Fin 6 :=
  ![(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),
    (2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]

def rows : Fin 18 → Row :=
  ![(0,0,0),(0,0,32767),(0,63,0),(1,63,32767),
    (1,43,25951),(1,45,12246),(1,53,27838),(1,21,7514),
    (1,22,9710),(1,26,15573),(1,42,11226),(1,43,15829),
    (1,45,10943),(1,53,24347),(1,21,18382),(1,22,27813),
    (1,26,7160),(1,42,29038)]

def mass (x : BooleanCube 6) : ℕ :=
  match ∑ i, (x i).val with
  | 1 => 55 | 3 => 21 | 4 => 16 | 5 => 15 | _ => 0

theorem mass_sum : (∑ x, mass x) = 1080 := by decide +kernel

theorem affine_bound :
    ∀ p : Affine 6, (∑ x, mass x * affineCorrect p x) ≤ 660 := by decide +kernel

theorem upper_bound :
    ∀ x : BooleanCube 6, 16 ≤ ∑ r, weights r * correct pairs (rows r) x := by
  decide +kernel

theorem degree_one_impossible :
    ¬ HasProbabilisticDegreeAtMost (@target 6) (1 / 3 : ℝ) 1 := by
  rintro ⟨m, P, mu, hd, hn, hs, hp⟩
  apply no_degree_one_family mass 1080 660 (by decide) mass_sum affine_bound
    (by norm_num) P mu hd hn hs
  have ht : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simpa only [ht] using hp

theorem degree_two_feasible :
    HasProbabilisticDegreeAtMost (@target 6) (1 / 3 : ℝ) 2 :=
  quadratic_feasible pairs rows weights 24 16 (by decide) weights_sum upper_bound (by norm_num)

end Six

namespace Seven

def pairs : Fin 21 → Fin 7 × Fin 7 :=
  ![(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,4),(1,5),(1,6),
    (2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]

def rows : Fin 18 → Row :=
  ![(0,0,0),(0,0,2097151),(0,127,0),(1,127,2097151),
    (1,43,480927),(1,45,621494),(1,53,996702),(1,85,718522),
    (1,86,1660878),(1,90,783765),(1,106,1781658),(1,43,1176501),
    (1,45,1780063),(1,53,458267),(1,85,1858478),(1,86,1013093),
    (1,90,700408),(1,106,1558222)]

def mass (x : BooleanCube 7) : ℕ :=
  match ∑ i, (x i).val with
  | 1 => 20 | 2 => 5 | 3 => 13 | 4 => 1 | 5 => 15 | _ => 0

theorem mass_sum : (∑ x, mass x) = 1050 := by decide +kernel

theorem affine_bound :
    ∀ p : Affine 7, (∑ x, mass x * affineCorrect p x) ≤ 595 := by decide +kernel

theorem upper_bound :
    ∀ x : BooleanCube 7, 16 ≤ ∑ r, weights r * correct pairs (rows r) x := by
  decide +kernel

theorem degree_one_impossible :
    ¬ HasProbabilisticDegreeAtMost (@target 7) (1 / 3 : ℝ) 1 := by
  rintro ⟨m, P, mu, hd, hn, hs, hp⟩
  apply no_degree_one_family mass 1050 595 (by decide) mass_sum affine_bound
    (by norm_num) P mu hd hn hs
  have ht : (1 : ℝ) - 1 / 3 = 2 / 3 := by norm_num
  simpa only [ht] using hp

theorem degree_two_feasible :
    HasProbabilisticDegreeAtMost (@target 7) (1 / 3 : ℝ) 2 :=
  quadratic_feasible pairs rows weights 24 16 (by decide) weights_sum upper_bound (by norm_num)

end Seven

/-- A joint statement, with n=6 and n=7 explicitly bounded. It has no general-n claim. -/
theorem feasible_degree_iff (n : ℕ) (hn : n = 6 ∨ n = 7) (d : ℕ) :
    HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) d ↔ 2 ≤ d := by
  have hlo : ¬ HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) 1 := by
    rcases hn with rfl | rfl
    · exact Six.degree_one_impossible
    · exact Seven.degree_one_impossible
  have hup : HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) 2 := by
    rcases hn with rfl | rfl
    · exact Six.degree_two_feasible
    · exact Seven.degree_two_feasible
  constructor
  · intro h
    by_contra hsmall
    exact hlo (h.mono (by omega))
  · intro h
    exact hup.mono h

theorem degree_exists (n : ℕ) (hn : n = 6 ∨ n = 7) :
    ∃ d, HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) d :=
  ⟨2, (feasible_degree_iff n hn 2).mpr (by decide)⟩

theorem least_feasible_degree (n : ℕ) (hn : n = 6 ∨ n = 7) :
    IsLeast {d : ℕ | HasProbabilisticDegreeAtMost (@target n) (1 / 3 : ℝ) d} 2 :=
  ⟨(feasible_degree_iff n hn 2).mpr (by decide),
    fun _ h => (feasible_degree_iff n hn _).mp h⟩

theorem pdeg_eq_two (n : ℕ) (hn : n = 6 ∨ n = 7) :
    probabilisticDegree (@target n) (1 / 3 : ℝ) (degree_exists n hn) = 2 := by
  classical
  unfold probabilisticDegree
  apply le_antisymm
  · exact Nat.find_min' (degree_exists n hn) ((feasible_degree_iff n hn 2).mpr (by decide))
  · exact (feasible_degree_iff n hn _).mp (Nat.find_spec (degree_exists n hn))

end PvsNPCartography.SmallSupportMod3
