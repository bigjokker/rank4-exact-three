# Verifying the release

Verification needs the evidence archive (`docs/evidence-archive.md`). Section 0 checks, decompresses and extracts it; after
section 0, run the commands from the extracted tree's root.

**On Linux, do the setup of section 0b first,** before quick or full verification. A stock Python interpreter is
refused: `verify_r18` requires the manifest-pinned x3compat r4 layer even in quick mode. The archive's
`VERIFY.md` and `ENVIRONMENT.md` describe the frozen interface; section 0b supplies the environment those
commands require. Environment details are in `docs/environment.md`.

**Never run Python optimized.** `-O` and `PYTHONOPTIMIZE` are refused, because the proof checks rely on `assert`.

## 0. Check the archive
The record holds the archive compressed as `release_tree.tar.xz`. Decompressing it restores `release_tree.tar`
byte for byte; `xz -dk` keeps the compressed file.

    sha256sum release_tree.tar.xz
    # d8a281e5a374411a0f006e081d1e5ffe7cd0b003c9aaa2b9ac9b5329cd1f1fa8
    xz -dk release_tree.tar.xz
    sha256sum release_tree.tar
    # ba42fe97adb4202a445d60f34d5b47d5c632ecc4f770790cb911acfc53ba572f
    mkdir tree && tar -xf release_tree.tar -C tree && cd tree

The archive has 4,906 files (4.7 GB), and its root holds `README.md`, `VERIFY.md` and `ENVIRONMENT.md`.

## 0b. Linux environment setup
Do this once on Linux before quick or full verification.
- **Python:** use an existing installation with the dependencies listed in `docs/environment.md`. The runs of record
  used Python 3.12.16.
- **Paths:** set `BASE_PY` and `GP_BIN` to absolute paths on your machine, with `GP_BIN` naming PARI/GP 2.17.x.
- **The venv:** `RUN_VENV` must be a new directory outside the extracted evidence tree.

This direct-verifier recipe preserves the archive's programs and manifests. It does not create the private mount
namespace of the runs of record (section 5).

```bash
BASE_PY=/absolute/path/to/python
GP_BIN=/absolute/path/to/gp
RUN_VENV=/absolute/path/to/new-venv
"$BASE_PY" -m venv --system-site-packages --without-pip "$RUN_VENV"
SP=$("$RUN_VENV/bin/python" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
cp results/rank4-r42-release/portable/x3compat/r4/sitecustomize.py "$SP/sitecustomize.py"
printf '%s  %s\n' f2742102b646aeeb828f4b671f835a4cef224f9db19fcc10800dde6938962b88 "$SP/sitecustomize.py" | sha256sum -c -
GP_LITERAL='C:\Program Files (x86)\Pari64-2-17-4\gp.exe'
ln -s "$GP_BIN" "$RUN_VENV/bin/$GP_LITERAL"
ln -s "$GP_BIN" "$RUN_VENV/bin/gp"
export PATH="$RUN_VENV/bin:$PATH"
export EXACT3_GP="$GP_BIN"
unset PYTHONOPTIMIZE
```

Then run the commands below with `"$RUN_VENV/bin/python"`.
- **What the verifier checks:** the layer's exact hash, and that the fixed GP file name resolves to version 2.17.x.
  The namespace runner of section 5 additionally checks the recorded hashes of the GP binary, libpari and libgmp.
- **z3:** the verifier itself adds the bundled Linux z3 library to each declared mirror. Do not replace the bundled
  Python bindings.

## 1. The small example (seconds)
    python -B examples/small_example.py            # the seed (3, 1, 4), D = 11
    python -B examples/small_example.py 5 2 7      # any integers with 0 < 2b < a < c

It needs Python 3.11 or later and PARI/GP 2.17.x, found through the sealed default path, `EXACT3_GP`, or `gp` on
`PATH`. The expected output is in `docs/worked-example.md`. It illustrates Theorems A and B for one seed; it does not
prove the main theorem.

## 2. Quick check (minutes; no mathematics is rerun)
    python -B results/rank4-tensor-proof-package/v2/verify_r18.py quick

It checks:
- every sealed marker and every file each marker lists, by SHA-256, and every pinned file;
- every recorded mathematical final status, with type-strict values;
- that the coverage map gives every computational step at least one executable route.

The closing line names the manifest and its sha256. Without `--deps`, the release manifest
`RELEASE_MANIFEST.json` beside the verifier is used.

## 3. Complete verification: re-execute the release manifest (hours)
The runs of record used Linux (section 5). From the tree root, with that environment:

    python -B results/rank4-tensor-proof-package/v2/verify_r18.py full --mirror-root SHORT_EMPTY_DIR \
        --limit-mb 500 --parallel 14 --aggregate-mb 14000 --aggregate-cpu 22 --cpus 0-21

**What each job must do.** Every one of the 170 jobs is copied into a fresh mirror holding only its declared inputs,
checked by hash, and run under a fail-closed memory guard on its whole process tree. It passes only if:
- it exits with its declared code;
- every final-status predicate holds;
- every declared output equals the sealed one under its comparison rule.

**The result.** Only a run of the whole manifest prints `COMPLETE MANIFEST VERIFIED: all 170 jobs, quick checks and
coverage OK | manifest RELEASE_MANIFEST.json sha256 4491cd09…`. A run with `--jobs` is labelled as a selection.

**Resources.** Lower `--parallel`, `--aggregate-mb`, `--aggregate-cpu` and `--cpus` to fit your machine.
- `--limit-mb` is a floor for each job's memory limit, and each job's own `limit_mb` applies above it.
- **Keep `--aggregate-mb` at least as large as the largest effective per-job limit** in the chosen manifest.
  With `--limit-mb 500`, the largest declared limits are 4,000 MB in the release manifest and 5,200 MB in
  regeneration. A job whose limit exceeds the aggregate budget is refused, not run with a smaller limit.
- Every CPU in `--cpus` must already be in the verifier process's affinity.
- The runs of record took 1 h 46 min (release) and 1 h 42 min (regeneration) on 22 CPUs.

## 4. Regeneration (hours; optional)
    python -B results/rank4-tensor-proof-package/v2/verify_r18.py full \
        --deps results/rank4-tensor-proof-package/v2/REGENERATION_MANIFEST.json --mirror-root SHORT_EMPTY_DIR_2 \
        --limit-mb 500 --parallel 14 --aggregate-mb 14000 --aggregate-cpu 22 --cpus 0-21

**What it reruns** (117 jobs; roles as in `docs/proof-map.md`):
- the 64 supporting checks;
- the 50 regeneration jobs: the producers of the certificate streams, compared by decompressed content, and the
  pilots and controls;
- the 3 provenance jobs, which re-derive recorded history.

**What it does not do.** It is not needed to verify the proof: the release manifest of section 3 holds one necessary
route per obligation. One job, `SOL40.C4_ORIGINAL_INTENTIONAL_STOP`, must exit 78. It is a deliberate stop kept as
history, and it is never counted as a completion.

## 5. Reproducing the runs of record exactly
The runs of record executed `results/rank4-r42-release/final/x3_ns_run.sh`, through a frozen copy with the same
sha256 (`a4724fa2…`):

**Staging.** Start in the extracted tree. STAGE is an absolute Windows-backed staging directory (the runs of
record used WSL 2). It contains:
- the unchanged `release_tree.tar`, decompressed as in section 0;
- the published run record `runs/ARCHIVES.json`, copied as `STAGE/ARCHIVES.json`. It is a run-record artifact,
  not an archive member, and its archive entry must name `release_tree.tar` with the hash listed above.

Create the frozen runner from the archive member, verify its hash, and run it:

```bash
STAGE=/mnt/c/path/to/stage
cp results/rank4-r42-release/final/x3_ns_run.sh "$STAGE/x3_ns_run_frozen.sh"
printf '%s  %s\n' a4724fa27c590c6af1000e47c3aa3611902a62570308f38b7c7514b86fa11a31 "$STAGE/x3_ns_run_frozen.sh" | sha256sum -c -
sudo bash "$STAGE/x3_ns_run_frozen.sh" "$STAGE" NEW_TAG \
  results/rank4-tensor-proof-package/v2/RELEASE_MANIFEST.json \
  --parallel 14 --aggregate-mb 14000 --aggregate-cpu 22 --cpus 0-21 --limit-mb 500
```

**Requirements of the runner:**
- NEW_TAG must be unused under `/root/x3`.
- It needs Linux root privileges, or equivalent permission to write there plus CAP_SYS_ADMIN for mount
  namespaces and unmounting.
- The schedule shown requires CPUs 0–21 in the process affinity; adjust the resource options to the machine.

**Regeneration and output.** To repeat the regeneration run, use a different NEW_TAG and replace
`RELEASE_MANIFEST.json` with `REGENERATION_MANIFEST.json`. The exported report and logs appear in
`STAGE/out/NEW_TAG/`.

**What the script does:**
1. It copies the archive and checks it against `ARCHIVES.json`.
2. It extracts the archive onto the Linux file system.
3. It builds a venv with the pinned compatibility layer as its `sitecustomize` module, and links the pinned PARI/GP.
4. It runs the verifier inside a private mount namespace, in which no Windows drive is mounted.
5. It exports the logs and the report.

**Site-specific paths.** The frozen runner fixes `BASEPY` and `GPBIN` to the producing machine's
`/opt/miniforge/envs/sage` paths, and requires the three GP files pinned in the portability table. Exact use of
this runner needs that layout and those bytes. For a different installation:
- use the direct-verifier setup of section 0b and record the new environment; or
- publish a separately named runner, with any changed portability table and manifests, and their new hashes and
  provenance.

Do not edit the frozen table's GP pins in place: its hash is itself pinned by the manifests. A direct
`verify_r18` run accepts GP 2.17.x behind the required file name. It does not enforce the runner's three
native-file hashes or its mount isolation.

## 6. The verifier's own self-test
    python -B results/rank4-r42-release/verifier_r18/verify_r18_selftest.py

It runs 155 adversarial cases (path aliases, root normalization, malformed manifests, CPU sets, timeouts and earlier
review findings). It writes fixtures, mirrors and its report beside the script.
- **Use a fresh extracted working copy** in which `results/rank4-r42-release/verifier_r18/fixtures` and
  `mirrors` do not exist.
- **Keep the script at its original path in that tree.** It resolves the verifier and its other fixtures
  relative to the tree root, so copying only the `verifier_r18` folder elsewhere is not enough.

The four-CPU precondition below still applies.
- **Precondition: at least four CPUs in the process's affinity.** Case N1 runs two jobs at once with two CPUs each.
  With fewer CPUs, N1 fails for lack of resources; that is not a verifier defect.
- An independent review run with two CPUs passed the other 154 cases, and N1 passed when it was repeated with four.
