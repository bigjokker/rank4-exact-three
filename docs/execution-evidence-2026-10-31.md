# Execution evidence: the runs of record of 31 October 2026

This note records what was executed for the exact-three release, on which bytes, and what was checked afterwards. It
is dated 31 October 2026 and lives outside the frozen evidence archive, which it does not change. The figures of
sections 1–4 come from the sealed run records and the archive, and those of section 5 from the reviewers'
sealed results; section 7 says which were extracted by script.

## 1. The bytes that were executed

| Item | Identity |
|---|---|
| Evidence archive | `release_tree.tar`, sha256 `ba42fe97adb4202a445d60f34d5b47d5c632ecc4f770790cb911acfc53ba572f`, 4,678,256,640 bytes, 4,906 files; built 31 October 2026, 16:02:42 EDT |
| Tree manifest inside it | `RELEASE_TREE_MANIFEST.json`, sha256 `db1d09742cec1fc48a3a603506707e09fe7277d16f49d5057ce193ed899dd590` |
| Runner (frozen copy) | `x3_ns_run_frozen.sh`, sha256 `a4724fa27c590c6af1000e47c3aa3611902a62570308f38b7c7514b86fa11a31` (equal to its source `results/rank4-r42-release/final/x3_ns_run.sh` in the tree) |
| Verifier | `results/rank4-tensor-proof-package/v2/verify_r18.py`, sha256 `1df421096d990372714a9934cbf000517e0321d513fca111256cd6fac8413640` |
| Compatibility layer | x3compat r4, sha256 `f2742102b646aeeb828f4b671f835a4cef224f9db19fcc10800dde6938962b88` |
| Process guard | `sol/r42/portable/grun_r4_r2.py`, sha256 `428131429af75a30bbe3069d4029937165af73959d06e108051c8b58b71017d7`, with the two helpers whose hashes it embeds |

Both runs started from this archive, extracted to the Linux file system. They ran inside a private mount namespace,
in which no Windows drive was mounted. The run records show a mount namespace different from the host's, and no
drvfs, 9p or Windows-drive mount inside it.

**Environment of both runs:**
- Ubuntu 24.04 under WSL 2 (kernel 6.18);
- Python 3.12.16, not optimized (optimize 0; the assert probe exited 1, so asserts were active);
- psutil 7.2.2;
- PARI/GP 2.17.3, pinned by hash (binary, libpari, libgmp);
- z3 5.3.3.0, through the Linux `libz3.so` added from the pinned portability table;
- the compatibility layer above.

**Schedule:** up to 14 jobs at once, 14,000 MB aggregate memory limit, 22 CPUs, default timeout 21,600 s per job.

## 2. The two runs of record

| Run | Manifest in the archive | sha256 | Jobs | Verifier ran (EDT) | Result |
|---|---|---|---|---|---|
| finalR2 | `results/rank4-tensor-proof-package/v2/RELEASE_MANIFEST.json` (required routes) | `4491cd09d81bed2ff7e57a3e2052cad72257ac5718458592c7cd1c324414fbeb` | 170 of 170 passed | 16:03:58 – 17:50:16 | `COMPLETE MANIFEST VERIFIED: all 170 jobs, quick checks and coverage OK`; exit 0 |
| finalG3 | `results/rank4-tensor-proof-package/v2/REGENERATION_MANIFEST.json` (64 supporting, 50 regeneration and 3 provenance jobs) | `44c0c84b565bc329af7eec80302b32aabd3e497fe360b54be12a87f21c1ad89b` | 117 of 117 passed | 17:55:23 – 19:37:23 | `COMPLETE MANIFEST VERIFIED: all 117 jobs, quick checks and coverage OK`; exit 0 |

**What "passed" means.** A job passed only if:
- it exited with its declared code;
- every mathematical final-status predicate held;
- every declared output equalled the sealed output under its comparison rule.

A zero exit code alone was never accepted.

**The one expected nonfinal outcome.** In the regeneration manifest, `SOL40.C4_ORIGINAL_INTENTIONAL_STOP` declares
exit 78, and it exited 78.
- It is the deliberate stop of the original C4 certificate emitter, made by its author, Sol (a Codex session),
  during development; the emitter was replaced by a new emission.
- It is kept as history under its own contract and never counted as a completion.
- Every other job declares and returned exit 0.

**The z3 jobs:** the Linux build of z3 was added to the 16 release jobs that load it, and to one job of the
regeneration run, the supporting C1-SEG segment check `SOL38.B6_SEGMENT_ALL_r2`. It loads z3 but made no solver
query: all 276,972 of its branches have exact certificates.

## 3. Headroom

**Memory** (peak of the whole process tree against the job's limit):
- finalR2: at most 0.74 (`C2.regress.regfull`, 1,846 of 2,500 MB);
- finalG3: at most 0.81 (`DIAG.diag`, 4,026 of 5,000 MB).

**Time against the manifest's limits:**
- finalR2: at most 0.21 (`T19.stream_10_main`, 1,426 of 6,766 s);
- finalG3: at most 0.21 (`F38.A3b.run.wall`, 1,189 of 5,761 s).

**Time against the inner limits** (`guard.py --seconds`). 86 jobs carry one (46 release, 40 regeneration), all
of them SOL* jobs. For 76 of them, which have no `timeout_s` in the manifest (so the 21,600 s default applies),
the inner limit is the operative one. Ten carry both, and for four of these (`SOL40.C1_CHECK`,
`SOL39.A2_VERIFY_r3`, `SOL40.C1_EMIT`, `SOL39.A2_EMIT`) the manifest limit is the smaller. The highest ratios:
- finalR2: at most 0.41 (`SOL40.C4_VALUE_CHECK`, 4,302 of 10,500 s);
- finalG3: at most 0.35 (`SOL40.C4_PARALLEL_EMIT`, 3,675 of 10,500 s).

These are observations on one machine, not guarantees. In the nonroutine audits, a z3 query that reaches its time
limit makes the job fail closed, and the comparison is exact in both directions. On a much slower or much faster
machine the set of queries that reach the limit could change, and such a job would then fail closed. That is a
refusal, not a wrong result.

## 4. Attempts that are not runs of record
- **Rehearsal runs on an earlier archive** (`release_tree.tar` sha256 `39b858816a31834e…`, map r9_r3). They found
  one defect, a comparison rule for a recorded wall-clock field, which was repaired before the frozen archive was
  built. They were stopped when that archive was ready. Their records are kept and marked as rehearsal.
- **A first regeneration attempt on the frozen archive.** It was stopped at its start, after one job, by the host
  session's memory-pressure protection: unpacking a second copy of the archive had filled the memory of the Linux
  virtual machine. None of its results is used. It was restarted with the same settings, and that restart is finalG3.

## 5. What was checked after the runs, and by whom

| Check | By | Scope | Result |
|---|---|---|---|
| Collection of both run records: 891 files, each hashed and sealed; a scan for the account name | Claude (the lead Claude session, which ran both runs) | The seal `DONE_RUNS_OF_RECORD` (sha256 `562c9ee18acd2e3b…`) | Both runs complete; no account-name hits |
| Static check of each run record: chain to the archive, identities, report, manifest, every receipt against its declared exit code, isolation, times | Fable (a Claude Opus 5.5 review session; "Fable" is its project name) | Its own checker, on the sealed copies | 0 problems in each run |
| z3 and environment check of each run | Opus (a Claude review session) | z3 loading and its trust scope, the environment against the manuscript's description | CHECKED in both runs |
| Independent archive and record audit | Astra (a Codex review session, which did not run the jobs) | 19,009 checks: all 891 record pins, all 4,906 archive members, the 32 dependency rows and all 287 jobs (the 170/117 partition), 453 output comparisons and 1,076 status predicates recorded | All pass. **This is an audit of the archive, hashes and record contracts, not a new execution of the 287 jobs.** |
| The verifier's adversarial self-test, 155 cases | Claude; Astra | `verify_r18_selftest.py` | 155 of 155 (Claude). Astra: 154 of 155 on two CPUs; the remaining case, N1, needs four CPUs and passed when repeated with four |

Every checker named here is an AI session, as described in the manuscript's "Authorship and contributions"
paragraph. These are AI-assisted checks with independent computational replication, not peer review.

The runs themselves are the lead session's recorded executions. The reviewers checked their records; they did not
execute the manifests again.

## 6. Notes on the wording of the frozen manuscript, checked against the runs
The manuscript inside the archive is frozen. These notes refine four of its statements in the light of the runs; none
changes a mathematical claim.
1. **"Linux, where every sealed file runs unchanged."** Confirmed by execution: every one of the 287 jobs ran from the
   archive's own bytes, and nothing was patched. What the Linux run adds is listed in note 2 and in section 1.
2. **"It is the one file added on Linux"** (of z3's `libz3.so`). It is the one file added to the *data*. The
   compatibility layer and the two links to PARI/GP are part of the environment, not of the data.
3. **"The few sampled routine queries that reached it"** (the z3 time limit) are 29 of the 896 sampled routine
   queries. They are closed by exact Bernstein certificates.
4. **z3's users.** The environment file's z3 row names the inherited nonroutine audits, in rows C4, C3-02, C3G1-A3b,
   C1C0-ST2 and PORTABLE-C0. To these add the supporting C1-SEG segment check, which loads z3 but made no solver
   query. This accounts for the file's own count of 17 jobs that load z3.

## 7. Where the records are
- The run records, as collected and sealed: `runs/finalR2/` and `runs/finalG3/`, with `runs/ARCHIVES.json` and
  `runs/RUNS_SUMMARY.json` (891 files in all).
- **Published exactly as collected:** no record was sanitized. The 891 files and their seal are the file
  `run_records_2026-10-31.tar` of this release's Zenodo record (`docs/evidence-archive.md`).
- The run figures of sections 1–3 (identities, times, job counts, schedule, the Python, psutil and PARI/GP
  versions, headroom, the expected exit 78) were extracted by `evidence/extract_run_facts.py` into
  `evidence/run_facts.json`.
  - It ran in the producing workspace. It reads only the sealed record copies under
    `results/rank4-r42-release/final/runs/` and the archive's two manifests (`RELEASE_MANIFEST.json` 4491cd09…,
    `REGENERATION_MANIFEST.json` 44c0c84b…), taken from the extracted tree.
  - It never reads the environment text files.
  - It needs an explicit path to that producing-workspace layout and a fresh output file name. It is not a tool
    for running the proof, and the repository alone does not contain its input records and manifests.
- The operating system, kernel, PARI/GP pins and mount facts of section 1 come from the runs' `environment.txt`,
  `gp_pin.txt`, `namespace.txt` and `mounts_in_namespace.txt`, and the z3 release from the archive's portability
  table and `ENVIRONMENT.md`. They are stated without quoting `environment.txt`, which records the machine's host
  name.
- The figures of section 5 come from the reviewers' sealed results (Fable's DONE_C_r2 8ea63022…, Opus's
  DONE_Z3_finalR2 cc1f8e32… and DONE_Z3_finalG3 824384c6…, Astra's audit sealed by her DONE.json 2e2056fd…);
  those of section 2 on the segment check and of section 6 come from Opus's z3 review records and the
  manuscript.

## 8. What the records do not show
- They do not re-prove the accepted hand proofs that the computations rely on.
- z3's exact decisions in the nonroutine audits are trusted. No independently checked solver trace is supplied.
- Hash checks show that data are unchanged; they decide nothing mathematical.
- The records describe the archive with the hash in section 1 and nothing else.
