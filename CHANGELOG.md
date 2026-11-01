# Changelog

## 1.0.0 (2026-11-01)

- **The exact-three theorem.** For every generic integer seed 0 < 2b < a < c, every positive definite rank-four lattice
  with the theta series of L₀(a, b, c) is isometric to exactly one of the three tensor-triple lattices L₀, L₁, L₂.
  PROVED (computer-assisted); `docs/theorem-and-scope.md`.
- **The evidence archive** `release_tree.tar` (sha256 `ba42fe97…`, 4,906 files) holds the manuscript, the data, the
  programs and the verifier `verify_r18.py`. It is linked by hash, not stored in the repository, and is published in
  this release's Zenodo record (doi:10.5281/zenodo.23853936), compressed as `release_tree.tar.xz`.
- **The runs of record** of 31 October 2026 re-executed both manifests completely: 170 of 170 required jobs, and 117
  of 117 regeneration, supporting and provenance jobs. `docs/execution-evidence-2026-10-31.md` states what was
  executed and what was checked. Their 891 record files are published, exactly as collected, in the same record.
- **New reader-facing pages:**
  - the theorem guide;
  - a worked example;
  - the proof dependency map;
  - verification and environment notes.
- **Copies from the archive:** the manuscript PDF and the small example, byte-identical to their archive members.
