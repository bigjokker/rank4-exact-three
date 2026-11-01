# A small worked example: the seed (3, 1, 4)

The smallest generic seed is M = (a, b, c) = (3, 1, 4), with D = ac − b² = 11. The archive's script
`examples/small_example.py` builds its three lattices and checks Theorems A and B for this one seed. A copy of the
script, byte-identical to the archive member, is `examples/small_example.py` here. It needs Python 3.11 or later and
PARI/GP 2.17.x, found through the sealed default path, `EXACT3_GP`, or `gp` on `PATH`.

## The three lattices
In the basis the construction uses (`docs/theorem-and-scope.md`), the Gram matrices of the bilinear form are:

    L₀ = [[ 12, −1, −6, −21], [ −1, 16, 27, 18], [ −6, 27, 72, 36], [−21, 18, 36, 72]]
    L₁ = [[ 36, 20, 42,  39], [ 20, 16, 27, 18], [ 42, 27, 72, 36], [ 39, 18, 36, 72]]
    L₂ = [[ 12,  2, −6,  15], [  2, 16, 27, 18], [ −6, 27, 72, 36], [ 15, 18, 36, 72]]

Each is positive definite and even, with determinant 729·D² = 88,209, and the common level is 297.

## Run it
    python -B examples/small_example.py

Expected output (produced on Windows with PARI/GP 2.17.4 on 31 October 2026, and reproduced independently in a
fresh copy; this script is not a job of the runs of record):

    L0: positive definite True, even True, det 88209 (729 D^2 = 88209)
    L1: positive definite True, even True, det 88209 (729 D^2 = 88209)
    L2: positive definite True, even True, det 88209 (729 D^2 = 88209)
    levels [297]; Sturm bound for weight 2 on Gamma0(N): 72
    theta series equal through the Sturm bound: True
    theta prefix of L0 (coefficients of q^0..q^12): [1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2]
    isometric pairs (L0,L1), (L0,L2), (L1,L2): ['0', '0', '0']
    SMALL EXAMPLE OK

## What each line shows
- **Positive definite, even, determinant 729·D²:** as the construction predicts.
- **Equal theta series through the Sturm bound.** The three theta series are modular forms of weight 2 for Γ₀(297)
  with trivial character. For such forms, equality of the coefficients through q^72 implies equality of the whole
  series (Sturm's theorem). So this line *proves* Theorem A for this seed.
- **Pairwise non-isometric:** PARI's `qfisom` returns 0, meaning no isometry exists, for each of the three pairs. This
  is Theorem B for this seed.

## Any other generic seed
    python -B examples/small_example.py 5 2 7

For (5, 2, 7), D = 31: the determinant is 700,569, the level 837 and the Sturm bound 192. The checks pass in the same
way.

## What the example does not show
It does not prove the main theorem, which says that no fourth isometry class has this theta series. That is the
content of the proof and of the verification in `docs/verify.md`.

**A wording note on the frozen script:** its docstring names an earlier verifier (`verify_r6.py`). The release
verifier is `verify_r18.py`.
