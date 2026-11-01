# Environment notes

The archive's `ENVIRONMENT.md` is the full reference. This page summarizes it, adds what the runs of record showed,
and lists the known maintenance items for later versions. The setup recipe for verifying on Linux is in `docs/verify.md`
section 0b.

## The environment of the runs of record (Linux)

| Component | Version | Used by |
|---|---|---|
| Operating system | Ubuntu 24.04 under WSL 2 (kernel 6.18), private mount namespace without Windows drives | everything |
| Python | 3.12.16, in a venv with `--system-site-packages`, never optimized | every job and the verifier |
| psutil | 7.2.2 | the process-tree guards and the environment record |
| SymPy | 1.14.0 | some producers and archived replays; never the standard-library certificate consumers |
| NumPy | 2.5.4 | one engine step |
| PARI/GP | 2.17.3, pinned by sha256 (binary, libpari, libgmp) | exact theta series, isometry tests, minima, genus closures |
| z3 | 5.3.3.0: the bundled Python bindings with the Linux `libz3.so` of the same release | the nonroutine audits (rows C4, C3-02, C3G1-A3b, C1C0-ST2, PORTABLE-C0) and the supporting C1-SEG segment check, which loads z3 but made no solver query |
| Compatibility layer | x3compat r4, installed as `sitecustomize`, pinned by sha256 in the manifest | every job |

Sage is not needed. The conda environment that supplied the interpreter also holds Sage, but no job imports it.

## What the Linux run adds, and what it does not change
- **Nothing is patched.** Every job runs the archive's own bytes, checked by hash in its mirror.
- **One file is added to the data:** the Linux build of z3, `libz3.so`, from the portability table. It is copied into
  the mirror of each of the 17 jobs that load z3: 16 in the release manifest and the C1-SEG check in the regeneration
  manifest.
- **The environment**, not the data, adds:
  - the compatibility layer;
  - two links to the pinned PARI/GP. One has the fixed Windows path that nineteen sealed scripts name as its file
    name; the other is `gp`.
- **The compatibility layer** reproduces the Windows behaviour that sealed scripts rely on:
  - "\r\n" text-mode line endings;
  - the Windows default text encodings;
  - spawn as the start method of process pools;
  - the priority, CPU-affinity and memory calls that some scripts make.

  Its header states its scope exactly. It is not a complete emulation of Windows.

## Windows
The jobs were developed and first run on Windows 11 with Python 3.11.9 and PARI/GP 2.17.4.
- **Two jobs run on Linux only** (`T19.portable57_54`, `T19.portable_predicates`). Their deepest files exceed the
  Windows path-length limit inside a verifier mirror.
- **The two archived replays of an earlier review** (`AG.restoration`, `AG.replay34`) are part of the Linux release
  route.

So a complete verification of this release is a Linux run.

## Resources
- **Memory:** every job declares `limit_mb`, and the guard stops a job whose whole process tree exceeds it. The largest
  jobs need about 5 GB.
- **Time:** the longest jobs take up to about 90 minutes. Measured headroom is in
  `docs/execution-evidence-2026-10-31.md` §3.
- **CPUs:** the verifier's self-test needs at least four CPUs in the process affinity (its case N1).

## Trust
- **z3:** its exact decisions in the nonroutine audits are trusted. No independently checked solver trace is
  supplied. Its queries settle 35,539 of the 71,509 nonroutine branch presentations, and a predeclared sample of
  routine decisions.
- **The verifier** isolates each job's inputs and guards its resources. It is not a sandbox for hostile code.

## Known maintenance items for later versions
These do not affect the frozen archive or its runs of record.
- **Windows teardown of the guard (R-W1).** On Windows, a new guard version waits for the job object to empty before
  it writes its receipt; it passed review for future Windows use. The runs of record used the Linux backend.
- **The C1 segment checker's cache key.** The sealed checker is sound as written: its only cache insertion is in the
  branch for non-identity, non-point cases, so identity and closed-point verdicts are never cached. A new version adds
  the matrix to the cache key, as defensive hardening against later edits, not as a repair; it reproduces all 276,972
  certificates.
- **The self-test's precondition.** A new version should check the four-CPU precondition before case N1 and report
  it as unmet, rather than failing the case.
- **A quick-mode rule (optional):** when a job has display command text, validate that it agrees with the
  command the verifier constructs from `argv`, including the Python interpreter prefix. The fields need not have
  the same representation: `command` may be absent or text, while `argv` is an argument list.
- **Wording:** the docstring of `examples/small_example.py` names an earlier verifier (`verify_r6.py`). The release
  verifier is `verify_r18.py`.
