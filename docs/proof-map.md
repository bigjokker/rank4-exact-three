# Proof dependency map

Every step of the proof has a stable identifier, a status and its verification route. This table is generated from
the archive's dependency file `results/rank4-tensor-proof-package/v2/DEPENDENCIES_r9_r4.json` (sha256 `77a17af1c332cd5e8b186c846921c786922a220b13ab4ed91702ccdd7f3673fa`). The manuscript's dependency appendix gives the same rows.

**Kinds:**
- *computational*: a step whose proof uses an exact computation. It names at least one required job.
- *hand*: a written proof accepted in review; no job re-proves it.
- *supporting*: a check that the proof does not use.
- *record*: a recorded acceptance or count.

A status COMPUTED on a computational row is a complete exact computation that the proof uses within its stated
scope. The bounded checks (C4-200, and the a ≤ 20 consistency check C3G1-A3c) are supporting: the proof does not
use them. `THM-AB` is proved by hand; its finitely many M-independent facts (the coset table and orbit counts) are
checked by the required job `THMAB.verify_package`, hence its kind computational.

**Job roles:** the 287 jobs are 170 required, 64 supporting, 50 regeneration, 3 provenance.
- *Required* jobs form the release manifest, one necessary route per obligation.
- *Regeneration* jobs rebuild the certificate streams and run the pilots and controls.
- *Supporting* jobs are further checks.
- *Provenance* jobs re-derive recorded history.

Both manifests ran completely in the runs of record (`docs/execution-evidence-2026-10-31.md`).

**Review letters.** Letters in a status, such as AG or AN, name the review in which the step was accepted. The
reviews are Astra's, a Codex review session; "Sol" in `PORTABLE-C0` is another Codex session (see the manuscript's
"Authorship and contributions"). The archive contains the review notes AG to AN (`RANK4-HANDOFF-AG-REVIEW-ASTRA.md`
to `RANK4-HANDOFF-AN-REVIEW-ASTRA.md`, at its root) and the audit folders
`results/rank4-handoff-{o,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,aq}-review-astra/`. The other reviews cited here
are not in the archive: the notes for Q to AF and for AO, AP and AQ, and the audit folders for Q to AA and for AP.

| Step | Statement | Status | Kind | Required | Supporting | Regeneration | Provenance |
|---|---|---|---|---:|---:|---:|---:|
| `THM-AB` | Theorems A (equal theta) and B (pairwise non-isometry), generic M | PROVED (hand); accepted earlier | computational | 1 | 0 | 0 | 0 |
| `RES-R1` | Global ambient rigidity R1, every generic integer M | PROVED; AG | computational | 1 | 0 | 0 | 0 |
| `RES-D1` | Congruence reduction, primitive D = 1 (mod 3) | PROVED; AG | computational | 2 | 0 | 0 | 0 |
| `RES-D0` | Two visible descents, primitive D = 0, 3 (mod 9) | PROVED; AG, AH | computational | 1 | 0 | 0 | 0 |
| `RES-D6` | D = 6 (mod 9): uniform ascents and R_Z (Theorem 6, Corollary 7) | PROVED (computer-assisted); AI, AJ | computational | 19 | 4 | 0 | 0 |
| `LADDER` | The tail ladder above W = 57/5: Theorems D and E, the (3,1,c) census audit, uniform (F1)/(F2), shortest shell, exact nonunit onset, shorter window, strip recovery, two-exception window, boundary, lower strip, W = 16, 15, 29/2 and 14/13/12 | PROVED (computer-assisted); accepted in handoffs Q to AB | computational | 1 | 0 | 0 | 0 |
| `TAIL19` | R(19/2): exact-three without coprimality for 4c > 17a + 6b (W = 10 and 19/2) | PROVED (computer-assisted); accepted in AD | computational | 17 | 12 | 0 | 0 |
| `TAIL` | Tail theorem, 20c > 81a + 30b (W-streamer plus coset bands) | PROVED (computer-assisted); AK | computational | 24 | 0 | 0 | 0 |
| `C4-REC` | C4 complete 4a-span recognition (no rank-four alternative) | PROVED (computer-assisted); AL | computational | 8 | 6 | 0 | 0 |
| `BASIS-BOUNDS` | Fourth-basis-vector bounds (recognized-span completions) | PROVED (hand); AM | hand | 0 | 0 | 0 | 0 |
| `C4` | Theorem C4: closed C4, wall c = a + b included | PROVED (computer-assisted); AN | computational | 9 | 4 | 10 | 2 |
| `C3-REC-HYB` | C3 recognition and the hybrid exclusion (c = 4b, c = 3a - 2b) | PROVED (computer-assisted); AL, AM | computational | 6 | 4 | 0 | 0 |
| `C3-02` | Theorem C3(0,2): closed C3, spans R0 or R2 | PROVED (computer-assisted); AN | computational | 8 | 1 | 7 | 0 |
| `C3G1-A1` | C3 graph 1, first excess and bounds | PROVED (computer-assisted: exact Bernstein certificates) + CHECKED; AN | computational | 1 | 0 | 0 | 0 |
| `C3G1-A2` | C3 graph 1, rank-three spans (66 isolated points, six residual seeds) | COMPUTED (exact); AN | computational | 1 | 1 | 0 | 0 |
| `C3G1-A3a` | C3 graph 1, the six alternative spans have no completion | COMPUTED (complete finite search); AN | computational | 2 | 0 | 0 | 0 |
| `C3G1-A3b` | C3 graph 1, completion on both cells and the tie wall | PROVED (computer-assisted); AN | computational | 25 | 4 | 15 | 0 |
| `C3G1-A3c` | C3 graph 1, end-to-end check at a <= 20 (consistency, not a dependency) | COMPUTED | supporting | 0 | 1 | 0 | 0 |
| `C2` | Theorem C2 with the boundary repair | PROVED (computer-assisted); AM | computational | 11 | 3 | 0 | 0 |
| `C1C0-S1` | C1/C0 first excess (step 1) | COMPUTED (exact envelope); AN | computational | 2 | 0 | 0 | 0 |
| `C1C0-D` | C1/C0 binary recognition (Part D) | PROVED (computer-assisted); AN | computational | 5 | 4 | 0 | 0 |
| `C1C0-E` | Lemma E2' and certified windows (Part E) | PROVED (exact envelope + interval certificates); AN | computational | 2 | 2 | 0 | 0 |
| `C1C0-ST1` | Stage 1 (M3 classification) | COMPUTED (exact symbolic); AN | computational | 4 | 2 | 0 | 0 |
| `C1C0-ST2` | Stage 2 Case I on C1 and C0 below the tail (certbox) | PROVED (computer-assisted); AN | computational | 9 | 1 | 8 | 0 |
| `C1-SEG` | The exceptional C1 segment (Case II): no completion | PROVED (computer-assisted: portable segment consumer, closed rational-root proofs); AN, AP | computational | 2 | 4 | 6 | 0 |
| `CERTBOX` | Certificate-box domain guard | accepted; AN §3 | computational | 2 | 2 | 0 | 0 |
| `ENG` | Completion engines (cgen, cgen_r2, cgen_r3, certbox, c4_run, c4_points, clib, symgen, e2lib, d2lib, poly, pari, gpstrict, memguard) | sealed | supporting | 0 | 5 | 0 | 0 |
| `UNIVERSES` | The six completion universes (27,587,324 branches) | COMPUTED | record | 0 | 0 | 0 | 0 |
| `PORTABLE-C0` | Portable solver-free certificates for all routine decisions of C0 below the tail; the (2,1,9) boundary branch is isometric to L0 | CHECKED (round 39, Sol): all 866,232 routine decisions, solver-free; (2,1,9) boundary isometry exact | computational | 4 | 0 | 3 | 0 |
| `REG` | Finite register: the 228 primitive D = 2 mod 3 rows with a <= 10 below the tail, by complete genus-envelope certificates (checked by an independent consumer) | PROVED (computer-assisted: certificate-checked genus closure); AP route | computational | 3 | 4 | 1 | 1 |
| `C4-200` | C4-200 census (152,994 seeds) | COMPUTED (bounded); AL | supporting | 0 | 0 | 0 | 0 |
| `AN` | Astra's AN acceptance | accepted | record | 0 | 0 | 0 | 0 |
| **Total** | 32 steps | | | **170** | **64** | **50** | **3** |

<details>
<summary>The required jobs of each step</summary>

- `THM-AB`: `THMAB.verify_package`
- `RES-R1`: `AG.replay34`
- `RES-D1`: `WS.replay_fable`, `WS.uniform_check`
- `RES-D0`: `AG.restoration`
- `RES-D6`: `D6.ascent_lines`, `D6.ascent_hyperplanes`, `D6.iso_planes`, `D6.z_models`, `D6.stage1`, `D6.r2.ez_cert`, `D6.r2.hexZ_lines`, `D6.r2.wall_cert`, `D6.r2.hexZ_rays`, `D6.r2.bcell_sge`, `D6.r2.ez_lines_m03`, `D6.r2.ez_lines_m1`, `D6.r2.ez_lines_m2`, `D6.r2.collect_rays`, `D6.r2.census_p0`, `D6.r2.census_p1`, `D6.r2.census_p2`, `D6.r2.census_p3`, `D6.r2.summary`
- `LADDER`: `PKG.ladder`
- `TAIL19`: `T19.stream_10_main`, `T19.edges_10_main`, `T19.survivors_10`, `T19.completion_10`, `T19.terminal_10`, `T19.stream_19_2_main`, `T19.edges_19_2_main`, `T19.survivors_19_2`, `T19.completion_19_2`, `T19.terminal_19_2`, `T19.coset_10`, `T19.coset_check_10`, `T19.coset_19_2`, `T19.coset_check_19_2`, `T19.closure_5_1_23`, `T19.portable57_54`, `T19.portable_predicates`
- `TAIL`: `TAIL.stream_main`, `TAIL.stream_vec26`, `TAIL.stream_cap30`, `TAIL.edges_main`, `TAIL.edges_vec26`, `TAIL.edges_cap30`, `TAIL.controls`, `TAIL.survivors_list`, `TAIL.survivors_run`, `TAIL.terminal`, `TAIL.coset`, `TAIL.summary`, `TAIL37.stream_main`, `TAIL37.stream_vec26`, `TAIL37.stream_cap30`, `TAIL37.edges_main`, `TAIL37.edges_vec26`, `TAIL37.edges_cap30`, `TAIL37.controls`, `TAIL37.survivors_list`, `TAIL37.survivors_run`, `TAIL37.terminal`, `TAIL37.coset`, `TAIL37.summary`
- `C4-REC`: `C4R.symspan_C4`, `C4R.refine_C4`, `C4R.km_C4`, `C4R.km_refC4`, `C4R.seedspan_C4`, `C4R.frames`, `C4R.s6`, `C4R.s7`
- `C4`: `C4.points.full`, `SOL40.C4_VALIDATION`, `SOL40.C4_GENERIC_VALIDATION`, `SOL40.C4_VALUE_VALIDATION`, `SOL40.C4_VALUE_CONTROLS`, `SOL40.C4_VALUE_CHECK`, `SOL38.B4_C4`, `SOL38.B4_C4_N_CERT`, `SOL38.B4_C4_VALIDATION_r2`
- `C3-REC-HYB`: `C3R.symspan_C3`, `C3R.refine_C3`, `C3R.km_C3`, `C3R.km_refC3`, `C3R.seedspan_C3`, `HYB.a_driver`
- `C3-02`: `C3.points.full`, `C3.k1.full`, `SOL40.C3_VALIDATION`, `SOL40.C3_GENERIC_VALIDATION`, `SOL40.C3_VALUE_VALIDATION`, `SOL40.C3_VALUE_CHECK`, `SOL38.B4_C3`, `SOL38.B4_C3_N_CERT`
- `C3G1-A1`: `F38.A1.check`
- `C3G1-A2`: `F38.A2.classify`
- `C3G1-A3a`: `F38.A3a.points`, `C3G1.A2_scope`
- `C3G1-A3b`: `F38.A3b.points.lower`, `F38.A3b.points.upper`, `F38.A3b.points.wall`, `F38.A3b.check_v1`, `F38.A3b.check_r2`, `F38.A3b.check_r3`, `SOL40.C3G1_LOWER_VALIDATION`, `SOL40.C3G1_LOWER_GENERIC_VALIDATION`, `SOL40.C3G1_LOWER_VALUE_VALIDATION`, `SOL40.C3G1_LOWER_VALUE_CHECK`, `SOL40.C3G1_UPPER_VALIDATION`, `SOL40.C3G1_UPPER_GENERIC_VALIDATION`, `SOL40.C3G1_UPPER_VALUE_VALIDATION`, `SOL40.C3G1_UPPER_VALUE_CHECK`, `SOL40.C3G1_WALL_VALIDATION`, `SOL40.C3G1_WALL_GENERIC_VALIDATION`, `SOL40.C3G1_WALL_VALUE_VALIDATION`, `SOL40.C3G1_WALL_VALUE_CHECK`, `SOL38.B4_GENERIC_VALIDATION`, `SOL38.B4_FABLE_A3b_lower`, `SOL38.B4_FABLE_A3b_lower_N_CERT`, `SOL38.B4_FABLE_A3b_upper`, `SOL38.B4_FABLE_A3b_upper_N_CERT`, `SOL38.B4_FABLE_A3b_wall`, `SOL38.B4_FABLE_A3b_wall_N_CERT`
- `C2`: `C2.run.regfull`, `C2.regress.regfull`, `C2.points.regfull`, `C2S.e_step1`, `C2S.e_stage1`, `C2S.e_classify1`, `C2A.e2_alt`, `C2A.e2_alt_isom`, `C2R2.route`, `C2C.sym_w24`, `C2C.points_w24`
- `C1C0-S1`: `FX.C1`, `FX.C0`
- `C1C0-D`: `C1D.sym_C1`, `C1D.sym_C0b`, `C1D.points_C1`, `C1D.points_C0b`, `C1D.exc_w48`
- `C1C0-E`: `C1E.env`, `C1E.win`
- `C1C0-ST1`: `C1F.stage1_C1`, `C1F.classify_C1`, `C1F.stage1_C0b`, `C1F.classify_C0b`
- `C1C0-ST2`: `F2.points.C1_case1`, `F2.points_r4.C1_case1`, `F2.points.C0b_case1`, `F2.points_r4.C0b_case1`, `F2.k1`, `SOL40.C1_VALIDATION`, `SOL40.C1_CHECK`, `SOL38.B6_F2_C1`, `SOL38.B6_F2_C1_N_CERT`
- `C1-SEG`: `SOL40.C1SEG_VALIDATION`, `SOL40.C1SEG_VALUE_CHECK`
- `CERTBOX`: `V3.b`, `V3.a`
- `PORTABLE-C0`: `SOL39.A2_VERIFY_r3`, `SOL39.C_BOUNDARY_IDENTITY`, `SOL38.B6_F2_C0b`, `SOL38.B6_F2_C0b_N_CERT`
- `REG`: `SOL41.VALIDATION_LOCAL_r2`, `SOL41.VALIDATION_PILOT`, `SOL41.REG_FULL`

</details>
