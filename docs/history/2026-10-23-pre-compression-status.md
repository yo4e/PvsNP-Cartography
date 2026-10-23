# Current checkpoint: real mixtures, sharp restricted obstruction, source bridge

Approved 2026-10-22 JST night session, completed after midnight on2026-10-23 JST.
Research lead: 月野テンプレクス. This records that one approved session only.
Read live Issues and [research direction](RESEARCH_DIRECTION.md); older dated
snapshots remain historical. **Issue16 is CLOSED; Issue17 is the next frontier.**

## Accepted formal result

ProfileMixtures connects ACTUAL polynomial correctness-layer profiles to arbitrary
finite REAL mixtures, reusing existing full symmetrization. Its linearity permits
signed coefficients; actual probabilistic certificates require nonnegative mass1.
Input distributions are chosen before inputs. Empty-layer totalization is not
mistaken for a probability measure.

RestrictedCliqueObstruction defines precisely zero/all q_A with |A|=9/all r_B
with |B|=8 at n12. It derives actual scores9/14 and241/462 under total layer
masses5/14 at weight6 and9/14 at weight10. It proves no normalized nonnegative
finite real mixture in that support has pointwise success>=2/3. The support
restriction is IN the theorem. A genuine degree2 q8 polynomial scores5/6 under
this dual; that counterexample is also Lean accepted. Thus this particular dual
is NOT an unrestricted quadratic lower bound.

Accepted code9410fa952ad4b92f09237bfc09be5ad200413db3,
tree d71346655c0012faa1c6b70991322ddf6cd5052f, completed SUCCESS
run39800322628/job119898840545. Pinned Lean4.35.0-rc4/Mathlib9e6b3aac,
whole-root --wfail9054 jobs;741 namespace declarations within
[propext,Classical.choice,Quot.sound], all24 new explicit target reports.
Actual full decoded log, completed steps, source and Git commit/tree re-fetched.
See Expedition023/axiom-report.txt, ci-evidence.md and statement-audit.md.
This is production Lean acceptance, not an independent second kernel/reviewer.

## Exact finite sharpness and hostile controls

The restricted game's optimum is EXACTLY9/14: give zero mass3/14 and every one
of220 q9 polynomials mass1/280; all495 r8 have mass0. Its minimum over4096
inputs is180/280. All716 actual polynomial truth tables were checked against
independent profiles, covering2,932,736 polynomial/input pairs and9308 means.
This matching primal is a finite computational certificate, not a new Lean
sharpness theorem or a support/denominator minimality result.

Exact code772b0eac985aeea4266d099482cba6759820a789 passed completed
run39799669199/job119896456402. Normal/-O outputs and both saved/actual JSONs
match. Full output, scripts, results and ancestry were inspected/re-fetched.
Graveyard033 preserves support/quantifier/normalization attacks. Graveyard034
and035 preserve two actual failed formal builds, repaired without changing the
mathematical statement or relaxing the proof/warning policy.

## Next substantive frontier: #17

A primary-source bridge was actually worked, not just scheduled. Expedition023/
source-bridge.md compares our definitions with Srinivasan, Tripathi, Venkitesh,
arXiv:1910.02465v1 Definition1, Fact6, Lemma9. Its smaller-error requirement and
existential residue are repaired by17 independent samples followed by majority,
then two-coordinate padding. Error<=1082987/14348907<1/12, degree<=17d, all three
residues on n-2 inputs. This derives a KNOWN Omega(sqrt(n)) consequence from an
IMPORTED source theorem. No explicit finite threshold or n12 conclusion follows.
Finite controls verify all131072 majority inputs, an exact derivative identity,
and24573 padding cases; they do not replace the generic mathematical argument.

#17 asks for a precise growing-degree low-degree agreement/dimension lemma from
an accessible primary source and a substantive proof reconstruction or refutation.
The difficult Smolensky ingredient remains unproved here. Formal adapters should
serve that concrete proof, not become another open-ended framework. No automatic
n13 search; no new result obtained by assuming the desired lower bound.

## Preserved scope, review and environment

Numerical exact degree2 remains n5..11; generic degree<=1 exclusion remains n>=7.
The new results do not establish unrestricted n12 degree, all-n degree2 success,
new circuit lower bounds, novelty, barrier escape or any P-versus-NP conclusion.
Gemini #15 covers OLD checkpoint0e30b5b7 only; #8 external human review remains
separate and nonblocking. New-code independent semantic review and a second
kernel remain absent. Novelty is unknown, not inferred from a passing build.

No write-permission blocker or unapplied research patch remains. Local Lean is
absent; accepted formal execution used Actions. The original ACM1987 PDF was
inaccessible; the specified accessible primary paper and its PDF pages were read.
Historical ledgers/status/README are preserved under dated archive paths.
Session record: logs/2026-10-22-night-real-mixtures.md.
