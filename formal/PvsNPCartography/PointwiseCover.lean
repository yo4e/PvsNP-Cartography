import PvsNPCartography.ProbabilisticDegree
import PvsNPCartography.AgreementDimension
import PvsNPCartography.RandomizedGates

open scoped BigOperators

namespace PvsNPCartography.PointwiseCover
noncomputable section
attribute [local instance] Classical.propDecidable
set_option maxHeartbeats 2400000

/-- Normalized real weights cannot hide the low row entirely in zero mass. -/
theorem positive_support_le {I : Type*} [Fintype I]
    (mu v : I → ℝ) (a : ℝ) (hn : ∀ i, 0 ≤ mu i)
    (hs : ∑ i, mu i = 1) (hv : ∑ i, mu i * v i ≤ a) :
    ∃ i, 0 < mu i ∧ v i ≤ a := by
  by_contra h
  have hbad (i : I) (hi : 0 < mu i) : a < v i := by
    by_contra hh
    exact h ⟨i, hi, le_of_not_gt hh⟩
  have hp : ∃ i, 0 < mu i := by
    by_contra hh
    have hz (i : I) : mu i = 0 := by
      have hi : ¬ 0 < mu i := fun hi => hh ⟨i, hi⟩
      exact le_antisymm (le_of_not_gt hi) (hn i)
    have : (∑ i, mu i) = 0 := by simp [hz]
    linarith
  obtain ⟨j, hj⟩ := hp
  have he : a = ∑ i, mu i * a := by rw [← Finset.sum_mul, hs, one_mul]
  have hl : (∑ i, mu i * a) < ∑ i, mu i * v i := by
    apply Finset.sum_lt_sum
    · intro i _
      by_cases hi : mu i = 0
      · simp [hi]
      · exact le_of_lt (mul_lt_mul_of_pos_left
          (hbad i (lt_of_le_of_ne (hn i) (Ne.symm hi)))
          (lt_of_le_of_ne (hn i) (Ne.symm hi)))
    · exact ⟨j, Finset.mem_univ j, mul_lt_mul_of_pos_left (hbad j hj) hj⟩
  rw [← he] at hl
  exact (not_lt_of_ge hv) hl

abbrev Truth (n : ℕ) := BooleanCube n → ZMod 2

def row {n : ℕ} (P : BinaryPolynomial n) : Truth n :=
  fun x => MvPolynomial.eval (fun j => ((x j).val : ZMod 2)) P

def errors {X : Type*} [Fintype X] (f g : X → ZMod 2) : Finset X :=
  Finset.univ.filter (fun x => f x ≠ g x)

def distance {X : Type*} [Fintype X] (f g : X → ZMod 2) : ℕ :=
  (errors f g).card

theorem distance_sum {X : Type*} [Fintype X] (f g : X → ZMod 2) :
    (distance f g : ℝ) = ∑ x, if f x ≠ g x then (1 : ℝ) else 0 := by
  unfold distance errors
  rw [← Finset.sum_filter]
  simp

/-- The pointwise hypothesis uses the original input-independent real weights. -/
theorem mean_error {n : ℕ} {I : Type*} [Fintype I]
    (f : Truth n) (P : I → BinaryPolynomial n) (mu : I → ℝ) (epsilon : ℝ)
    (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1-epsilon ≤ ∑ i, mu i * (if row (P i) x = f x then 1 else 0)) :
    (∑ i, mu i * (distance (row (P i)) f : ℝ)) ≤ epsilon * (2^n : ℕ) := by
  have hx (x : BooleanCube n) :
      (∑ i, mu i * (if row (P i) x ≠ f x then (1 : ℝ) else 0)) ≤ epsilon := by
    have hc :
        (∑ i, mu i * (if row (P i) x ≠ f x then (1 : ℝ) else 0)) +
        (∑ i, mu i * (if row (P i) x = f x then (1 : ℝ) else 0)) = 1 := by
      rw [← Finset.sum_add_distrib]
      convert hs using 1
      apply Finset.sum_congr rfl
      intro i _
      by_cases h : row (P i) x = f x <;> simp [h]
    linarith [hp x]
  calc
    _ = ∑ x : BooleanCube n, ∑ i, mu i *
        (if row (P i) x ≠ f x then (1 : ℝ) else 0) := by
      simp_rw [distance_sum, Finset.mul_sum]
      exact Finset.sum_comm
    _ ≤ ∑ _x : BooleanCube n, epsilon := Finset.sum_le_sum (fun x _ => hx x)
    _ = epsilon * (2^n : ℕ) := by simp [BooleanCube, mul_comm]

/-- Positive-mass witness, with an integer radius and no rationality assumption. -/
theorem positive_support_third {n : ℕ} {I : Type*} [Fintype I]
    (f : Truth n) (P : I → BinaryPolynomial n) (mu : I → ℝ)
    (hn : ∀ i, 0 ≤ mu i) (hs : ∑ i, mu i = 1)
    (hp : ∀ x, 1-(1/3 : ℝ) ≤ ∑ i, mu i * (if row (P i) x = f x then 1 else 0)) :
    ∃ i, 0 < mu i ∧ distance (row (P i)) f ≤ 2^n/3 := by
  obtain ⟨i, hi, he⟩ := positive_support_le mu
    (fun i => (distance (row (P i)) f : ℝ)) _ hn hs (mean_error f P mu _ hs hp)
  refine ⟨i, hi, ?_⟩
  have hh : (3 : ℝ) * (distance (row (P i)) f : ℝ) ≤ (2^n : ℕ) := by linarith
  have hnat : 3 * distance (row (P i)) f ≤ 2^n := by exact_mod_cast hh
  omega

/-- The original predicate, not an assumed deterministic covering conclusion. -/
theorem feasible_has_close_row {n d : ℕ} (f : Truth n)
    (hf : HasProbabilisticDegreeAtMost f (1/3 : ℝ) d) :
    ∃ P : BinaryPolynomial n, P.totalDegree ≤ d ∧ distance (row P) f ≤ 2^n/3 := by
  obtain ⟨m, P, mu, hd, hn, hs, hp⟩ := hf
  obtain ⟨i, _, hi⟩ := positive_support_third f P mu hn hs hp
  exact ⟨P i, hd i, hi⟩

/-- Use the accepted squarefree-span reduction on the actual binary cube. -/
def fieldCube (n : ℕ) : Finset (Fin n → ZMod 2) := Finset.univ

def codebook (n d : ℕ) : Finset (Truth n) :=
  Finset.univ.image (fun u : AgreementDimension.lowSpace (fieldCube n) d =>
    fun x : BooleanCube n => u.1 ⟨(fun j => ((x j).val : ZMod 2)), Finset.mem_univ _⟩)

def dimensionBound (n d : ℕ) : ℕ :=
  ∑ j ∈ Finset.range (min n d + 1), n.choose j

theorem row_mem_codebook {n d : ℕ} (P : BinaryPolynomial n) (hd : P.totalDegree ≤ d) :
    row P ∈ codebook n d := by
  have hm := AgreementDimension.eval_mem_low (fieldCube n) (0 : ZMod 2) 1
    (by decide) (fun y i => RandomizedGates.bit_cases (y.1 i)) P d hd
  exact Finset.mem_image.mpr ⟨⟨(fun y => MvPolynomial.eval y.1 P), hm⟩,
    Finset.mem_univ _, rfl⟩

theorem codebook_card (n d : ℕ) : (codebook n d).card ≤ 2^(dimensionBound n d) := by
  have hd : Module.finrank (ZMod 2) (AgreementDimension.lowSpace (fieldCube n) d) ≤
      (AgreementDimension.supports n d).card := by
    exact (finrank_span_finset_le_card (R := ZMod 2)
      ((AgreementDimension.supports n d).image (AgreementDimension.monoValue (fieldCube n)))).trans
      Finset.card_image_le
  calc
    _ ≤ Fintype.card (AgreementDimension.lowSpace (fieldCube n) d) := Finset.card_image_le
    _ = 2^(Module.finrank (ZMod 2) (AgreementDimension.lowSpace (fieldCube n) d)) := by
      rw [Module.card_eq_pow_finrank (K := ZMod 2)]
      simp
    _ ≤ 2^((AgreementDimension.supports n d).card) := by gcongr
    _ = 2^(dimensionBound n d) := by rw [AgreementDimension.supports_card]; rfl

/-- Binary alphabet is essential for the injective error-set encoding. -/
theorem errors_injective {X : Type*} [Fintype X] (f : X → ZMod 2) :
    Function.Injective (errors f) := by
  intro g h he
  funext x
  have hx : f x ≠ g x ↔ f x ≠ h x := by
    have hh := Finset.ext_iff.mp he x
    simpa only [errors, Finset.mem_filter, Finset.mem_univ, true_and] using hh
  exact (by decide : ∀ a b c : ZMod 2, (a ≠ b ↔ a ≠ c) → b = c) _ _ _ hx

def smallSets (X : Type*) [Fintype X] (r : ℕ) : Finset (Finset X) :=
  Finset.univ.filter (fun S => S.card ≤ r)

def volume (N r : ℕ) : ℕ := ∑ j ∈ Finset.range (r+1), N.choose j

theorem smallSets_card (X : Type*) [Fintype X] (r : ℕ) :
    (smallSets X r).card = volume (Fintype.card X) r := by
  have hf := Finset.card_eq_sum_card_fiberwise (f := fun S : Finset X => S.card)
    (s := smallSets X r) (t := Finset.range (r+1)) (by
      intro S hS
      have hs : S.card ≤ r := by simpa [smallSets] using hS
      simpa only [Finset.mem_coe, Finset.mem_range, Nat.lt_succ_iff] using hs)
  rw [hf]
  unfold volume
  apply Finset.sum_congr rfl
  intro j hj
  have hjr : j ≤ r := by simpa only [Finset.mem_range, Nat.lt_succ_iff] using hj
  have he : (smallSets X r).filter (fun S => S.card = j) =
      (Finset.univ : Finset X).powersetCard j := by
    ext S
    simp only [smallSets, Finset.mem_filter, Finset.mem_univ, true_and,
      Finset.mem_powersetCard, Finset.subset_univ]
    omega
  rw [he, Finset.card_powersetCard]
  simp

def ball {X : Type*} [Fintype X] (f : X → ZMod 2) (r : ℕ) : Finset (X → ZMod 2) :=
  Finset.univ.filter (fun g => distance f g ≤ r)

theorem ball_card_le {X : Type*} [Fintype X] (f : X → ZMod 2) (r : ℕ) :
    (ball f r).card ≤ volume (Fintype.card X) r := by
  let e : ball f r → smallSets X r := fun g =>
    ⟨errors f g.1, by simpa only [smallSets, Finset.mem_filter, Finset.mem_univ,
      true_and, distance] using (Finset.mem_filter.mp g.2).2⟩
  have hinj : Function.Injective e := by
    intro g h he
    apply Subtype.ext
    exact errors_injective f (congrArg Subtype.val he)
  have hc := Fintype.card_le_of_injective e hinj
  simpa only [Fintype.card_coe, smallSets_card] using hc

def covered (n d r : ℕ) : Finset (Truth n) :=
  (codebook n d).biUnion (fun f => ball f r)

theorem covered_card (n d r : ℕ) :
    (covered n d r).card ≤ 2^(dimensionBound n d) * volume (2^n) r := by
  calc
    _ ≤ ∑ f ∈ codebook n d, (ball f r).card := by apply Finset.card_biUnion_le
    _ ≤ ∑ _f ∈ codebook n d, volume (2^n) r := by
      apply Finset.sum_le_sum
      intro f _
      simpa [BooleanCube] using ball_card_le f r
    _ = (codebook n d).card * volume (2^n) r := by simp
    _ ≤ _ := Nat.mul_le_mul_right _ (codebook_card n d)

def feasibleTargets (n d : ℕ) : Finset (Truth n) :=
  Finset.univ.filter (fun f => HasProbabilisticDegreeAtMost f (1/3 : ℝ) d)

theorem feasible_subset_covered (n d : ℕ) : feasibleTargets n d ⊆ covered n d (2^n/3) := by
  intro f hf
  obtain ⟨P, hd, he⟩ := feasible_has_close_row f (Finset.mem_filter.mp hf).2
  apply Finset.mem_biUnion.mpr
  refine ⟨row P, row_mem_codebook P hd, ?_⟩
  simpa only [ball, Finset.mem_filter, Finset.mem_univ, true_and] using he

/-- Full finite counting endpoint: actual degree and arbitrary REAL mixtures. -/
theorem feasible_count (n d : ℕ) :
    (feasibleTargets n d).card ≤ 2^(dimensionBound n d) * volume (2^n) (2^n/3) :=
  (Finset.card_le_card (feasible_subset_covered n d)).trans (covered_card n d _)

def farTargets (n d : ℕ) : Finset (Truth n) := Finset.univ \ covered n d (2^n/3)

theorem far_not_feasible {n d : ℕ} {f : Truth n} (hf : f ∈ farTargets n d) :
    ¬ HasProbabilisticDegreeAtMost f (1/3 : ℝ) d := by
  intro h
  have hm : f ∈ feasibleTargets n d :=
    Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩
  exact (Finset.mem_sdiff.mp hf).2 (feasible_subset_covered n d hm)

/-- Nonvacuity has an explicit arithmetic obligation; it is not silently assumed. -/
theorem large_of_bound (n d : ℕ)
    (hb : 2^(dimensionBound n d) * volume (2^n) (2^n/3) < 2^(2^n-1)) :
    2^(2^n-1) < (farTargets n d).card := by
  have hc := covered_card n d (2^n/3)
  have hn : 0 < 2^n := by positivity
  have ht : (Finset.univ : Finset (Truth n)).card = 2^(2^n) := by
    simp [Truth, BooleanCube]
  have he : 2^(2^n) = 2 * 2^(2^n-1) := by
    have hh : 2^n = (2^n-1)+1 := by omega
    calc
      _ = 2^((2^n-1)+1) := by rw [← hh]
      _ = _ := by rw [pow_succ]; omega
  have hs : (farTargets n d).card =
      (Finset.univ : Finset (Truth n)).card - (covered n d (2^n/3)).card := by
    simp only [farTargets, Finset.card_sdiff, Finset.inter_univ]
  rw [ht, he] at hs
  omega

end
end PvsNPCartography.PointwiseCover
