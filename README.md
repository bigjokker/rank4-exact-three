# Exactly three theta mates for a family of rank-four lattices

A tensor construction over the Eisenstein integers gives, for every positive definite integral binary form
M = (a, b, c), three even lattices L₀, L₁, L₂ of rank four with the same theta series. For generic M
(0 < 2b < a < c) they are pairwise non-isometric. This release proves that there are no others:

> **Main theorem.** Let a, b, c be integers with 0 < 2b < a < c. Every positive definite lattice of rank four with the
> theta series of L₀(a, b, c) is isometric to exactly one of L₀, L₁, L₂.

**Status: PROVED (computer-assisted).** The computer-assisted steps are exact computations: certificates, exact isometry
tests and complete finite searches. Every one of them has an executable route, and all of them were re-executed in
complete runs of record on 31 October 2026.

**Scope:**
- Every generic integer seed is covered, with no bound on a, b, c and no residue condition.
- The theorem concerns this constructed family only. It gives no upper bound for rank-four theta fibres in general, and
  it does not treat b = 0, 2b = a or a = c.
- About the invariant ♭₄ the release says only: ♭₄ ≥ 3, contradicting the conjecture as stated in
  arXiv:2412.16709v1. This follows from Theorems A and B; no upper bound for ♭₄ is proved.
- No priority or novelty claim is made.

## Read
- **The manuscript:** [`paper/exact-three-manuscript.pdf`](paper/exact-three-manuscript.pdf), a byte copy of the
  archive's `manuscript_r8_r6_build/main.pdf`.
- **[The theorem, its hypotheses and its scope](docs/theorem-and-scope.md)**, with the labels used in this release.
- **[A small worked example](docs/worked-example.md):** the seed (3, 1, 4), with its expected output.
- **[The proof dependency map](docs/proof-map.md):** every step, its status and the jobs that verify it.

## Verify
The evidence is one frozen archive, `release_tree.tar`, sha256
`ba42fe97adb4202a445d60f34d5b47d5c632ecc4f770790cb911acfc53ba572f`. It is in this release's Zenodo record,
[doi:10.5281/zenodo.23853936](https://doi.org/10.5281/zenodo.23853936), compressed as `release_tree.tar.xz`; decompressing it restores the
archive byte for byte ([how to get and check it](docs/evidence-archive.md)).
From the root of the extracted tree (on Linux, first do the setup in section 0b of the
[verification guide](docs/verify.md): quick mode also needs the pinned x3compat r4 layer; the example needs only
Python and PARI/GP):

    python -B examples/small_example.py                                  # seconds: Theorems A and B for one seed
    python -B results/rank4-tensor-proof-package/v2/verify_r18.py quick  # minutes: integrity, statuses, coverage
    python -B results/rank4-tensor-proof-package/v2/verify_r18.py full --mirror-root SHORT_EMPTY_DIR   # hours

- **[Verification guide](docs/verify.md):** quick check, complete verification, regeneration, and reproducing the runs
  of record.
- **[Environment notes](docs/environment.md):** the runs of record used Linux, Python 3.12, PARI/GP 2.17.3 and z3
  5.3.3.
- **[Execution evidence of 31 October 2026](docs/execution-evidence-2026-10-31.md):** what was executed, on which bytes,
  and what was checked.

## What a successful verification means
- **Hash checks** show that the data are unchanged; they decide nothing mathematical.
- **Re-execution** shows that the sealed computations reproduce.
- **The certificate consumers** carry the main computational checks. They are independent standard-library checkers,
  which check every routine decision: 27,515,815 of them across six branch universes.
- **The nonroutine branches** keep their independent audits. These rely on the SMT solver z3, whose exact decisions
  are trusted; no checked solver trace is supplied.
- **The accepted hand proofs** are not re-proved by any program.

## Citation, credit and license
- **Citation:** see [`CITATION.cff`](CITATION.cff). DOI: [10.5281/zenodo.23853936](https://doi.org/10.5281/zenodo.23853936), one Zenodo record holding
  this repository's snapshot, the evidence archive and the run records.
- **Credit:** released by bigjokker. The work was carried out with AI assistance; the manuscript's "Authorship and
  contributions" paragraph describes each role. The reviews are AI-assisted reviews with independent computational
  replication, not peer review.
- **License:** MIT ([LICENSE](LICENSE)).
