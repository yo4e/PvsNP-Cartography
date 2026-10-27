import PvsNPCartography.Mod3ProductBound

namespace PvsNPCartography.GF4Transport

noncomputable section
attribute [local instance] Classical.propDecidable

/-- Forward grid map, paired with the decoder actually used in the proof. -/
def encode {m : ℕ} (x : BooleanCube m) : Fin m → K :=
  fun j => if x j = 0 then 1 else omega

theorem encode_grid {m : ℕ} (x : BooleanCube m) :
    encode x ∈ AgreementDimension.grid (1 : K) omega m := by
  classical
  apply Fintype.mem_piFinset.mpr
  intro j
  change (if x j = 0 then (1 : K) else omega) ∈ ({1, omega} : Finset K)
  split_ifs <;> simp

theorem decode_encode {m : ℕ} (x : BooleanCube m) : decode (encode x) = x := by
  funext j
  have hj : x j = 0 ∨ x j = 1 := by
    have hlt := (x j).isLt
    have hv : (x j).val = 0 ∨ (x j).val = 1 := by omega
    rcases hv with h | h
    · exact Or.inl (Fin.ext h)
    · exact Or.inr (Fin.ext h)
  rcases hj with h | h <;> simp [decode, encode, h, omega_ne_one]

theorem encode_decode {m : ℕ} (y : Fin m → K)
    (hy : ∀ j, y j = 1 ∨ y j = omega) : encode (decode y) = y := by
  funext j
  rcases hy j with h | h <;> simp [encode, decode, h, omega_ne_one]

end
end PvsNPCartography.GF4Transport

namespace PvsNPCartography.Mod3ProductBound

/-- A closed numerical use of the actual MOD3 bridge, not a rank hypothesis.
This is error 1/12, NOT the previously studied error 1/3 and not an optimum claim. -/
theorem seven_small_error_impossible :
    ¬ HasProbabilisticDegreeAtMost (@SmallSupportMod3.target 7) (1 / 12 : ℝ) 2 := by
  apply no_mod3_approximation 5 2 (1 / 12 : ℝ)
  norm_num [AgreementConsequences.bound, Finset.sum_range_succ, Nat.choose]

end PvsNPCartography.Mod3ProductBound
