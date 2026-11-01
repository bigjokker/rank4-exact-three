# The theorem, its hypotheses and its scope

This guide states the result of the release and what it does and does not claim. The authoritative text is the
manuscript in the evidence archive: `results/rank4-tensor-proof-package/v2/manuscript_r8_r6_build/main.pdf`, a copy of
which is `paper/exact-three-manuscript.pdf` here (see `docs/evidence-archive.md` for its hash).

## The construction
Let E = Z[ω] with ω² = ω − 1, with norm N and trace Tr. For a positive definite integral binary form
M = (a, b, c), with D = ac − b², put on E²

    Q(z₁, z₂) = a·N(z₁) + c·N(z₂) + b·Tr(z̄₁ z₂).

For the three matrices

    Φ₀ = [[0, 1], [−1, 0]],   Φ₁ = [[1, 1], [1, 0]],   Φ₂ = [[−1, 1], [1, 0]],

acting on the coordinates of z₁ in the basis (1, ω), define

    Lᵢ = Lᵢ(M) = { (z₁, z₂) ∈ E² : z₂ ≡ Φᵢ z₁ (mod 3) },   i = 0, 1, 2.

Each Lᵢ is an even lattice of rank four, of index 9 in E² and determinant (27D)². The seed M is **generic** if
0 < 2b < a < c.

**Theorems A–C** (the tensor construction; proved by hand, with M-independent finite facts checked by a
required job; accepted earlier):
- **A.** For every positive definite integral M, L₀, L₁ and L₂ have the same theta series.
- **B.** For every generic M they are pairwise non-isometric.
- **C.** For M = (3, 1, c), c ≥ 4, the triples lie in infinitely many similarity classes: lattices from
  different c are never similar.

Consequently ♭₄ ≥ 3, contradicting the conjecture as stated in arXiv:2412.16709v1. No upper bound for ♭₄ is proved.

## The main theorem
> Let a, b, c be integers with 0 < 2b < a < c. Every positive definite lattice of rank four with the theta series of
> L₀(a, b, c) is isometric to exactly one of L₀, L₁, L₂.

**Status: PROVED (computer-assisted).** The proof combines hand proofs, accepted in review, with exact computations:
certificates, exact isometry tests and complete finite searches.

**Theta equality and isometry are kept apart.** For even lattices of rank four with square determinant and level
dividing N, the theta series lie in M₂(Γ₀(N)), so agreement of two of them through the Sturm bound proves the two
series equal (Sturm's theorem); `docs/worked-example.md` checks Theorem A for one seed this way. Isometry is never
inferred from theta coefficients, through any bound: a lattice is identified with L₀, L₁ or L₂ only by an explicit
integral isometry or an exact isometry test.

**Hypotheses and scope:**
- Every generic integer seed is covered. There is no bound on a, b, c or D, and no residue or coprimality condition.
- The theorem concerns this constructed family only. It does not bound the size of rank-four theta fibres in general.
- It does not treat the non-generic parameters b = 0, 2b = a or a = c.
- No priority or novelty claim is made.

## How the proof is organized
The proof splits by the residue of D and by position in the parameter plane. The labels are those of the manuscript's
dependency table.
1. **Primitive D ≢ 2 (mod 3):**
   - global ambient rigidity, PROVED (the exact finite reduction in its proof is computer-assisted);
   - the congruence reduction for D ≡ 1 (mod 3), with a within-seed classification certificate;
   - two visible descents for D ≡ 0, 3 (mod 9);
   - uniform ascents and the rigidity statement R_Z for D ≡ 6 (mod 9).
2. **Primitive D ≡ 2 (mod 3):** the normalized plane (β, γ) = (b/a, c/a) is split into chambers C4, C3, C2, C1, C0,
   each with its walls assigned. In each chamber, every possible fourth class is reduced to a finite symbolic branch
   universe. Each branch is then excluded by an exact certificate, identified with a known Lᵢ by an explicit basis, or
   settled by exact theta differences and isometry tests. The six universes have 27,587,324 branches, and none is
   left unresolved.
3. **The tail** (20c > 81a + 30b), by a separate tail theorem and its certificate ladder. The boundary
   20c = 81a + 30b itself belongs to the C0 computation of item 2.
4. **The finite register:** the 228 primitive seeds with D ≡ 2 (mod 3), a ≤ 10 and below the tail that the chamber
   arguments set aside, each closed by a complete genus-closure certificate.
5. **Common scalings** reduce every seed to a primitive one.

`docs/proof-map.md` lists every step, its status and the jobs that verify it.

## Labels used in this release
- **PROVED (hand):** a written proof, accepted in review; no program re-proves it.
- **PROVED (computer-assisted):** a written reduction plus exact computations, every one with an executable route in
  the release manifest.
- **COMPUTED:** an exact finite computation with the stated scope. On a step of the proof
  (`docs/proof-map.md`) it is a complete computation over the finite set to which the written reduction leads,
  and it is part of the proof. A bounded census, such as C4-200, is marked COMPUTED (bounded) or used only as a
  supporting check; it is never presented as a proof beyond its range.
- **Supporting:** checks and history that the proof does not depend on, kept for reproducibility.

## What this release does not contain
These are separate research lines with their own status, outside the release claim:
- the tilted triples in every dimension n ≥ 4 (accepted in review, separate material);
- the arithmetic of the D = 127 pair;
- the isolated level-837 pairs and their four-coset relation;
- the GF(4) code controls.

None of them is needed for the main theorem.
