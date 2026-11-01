# The evidence archive and the run records

The proof's data, programs and manuscript sources are in one frozen archive, kept outside normal source browsing. The
archive is identified by its hash, and that hash is what the runs of record executed. Do not rely on any copy whose
hash differs.

## The archive

| Field | Value |
|---|---|
| File | `release_tree.tar` |
| sha256 | `ba42fe97adb4202a445d60f34d5b47d5c632ecc4f770790cb911acfc53ba572f` |
| Size | 4,678,256,640 bytes (4.7 GB) |
| Files | 4,906 |
| Tree manifest | `RELEASE_TREE_MANIFEST.json`, sha256 `db1d09742cec1fc48a3a603506707e09fe7277d16f49d5057ce193ed899dd590` (one row, with size and sha256, for each of the other 4,904 files; it does not list itself or `checksums.sha256`) |
| Published as | `release_tree.tar.xz`, xz-compressed: 809,738,804 bytes, sha256 `d8a281e5a374411a0f006e081d1e5ffe7cd0b003c9aaa2b9ac9b5329cd1f1fa8`. Decompressing it restores `release_tree.tar` byte for byte |
| Where | this release's Zenodo record, [doi:10.5281/zenodo.23853936](https://doi.org/10.5281/zenodo.23853936), file `release_tree.tar.xz` |

**Check, decompress and extract** (`xz -dk` keeps the compressed file):

    sha256sum release_tree.tar.xz    # d8a281e5a374411a0f006e081d1e5ffe7cd0b003c9aaa2b9ac9b5329cd1f1fa8
    xz -dk release_tree.tar.xz       # writes release_tree.tar
    sha256sum release_tree.tar       # ba42fe97adb4202a445d60f34d5b47d5c632ecc4f770790cb911acfc53ba572f
    mkdir tree && tar -xf release_tree.tar -C tree

**Start reading the tree at:**
- `README.md`: the theorem, the manuscript and the verification commands;
- `VERIFY.md` and `ENVIRONMENT.md`;
- `results/rank4-tensor-proof-package/v2/`: the manifests, the verifier `verify_r18.py`, the dependency file and the
  manuscript (`manuscript_r8_r6/` sources and `manuscript_r8_r6_build/main.pdf`);
- `PUBLIC_PROVENANCE.json`: the release copies (see below).

**Release copies.** Some sealed files had recorded absolute paths of the machine they were produced on. In the
archive those strings are replaced by `<WORKSPACE>`, `<USERPROFILE>` or `<ACCOUNT>`, and embedded hashes are updated
to match.
- `PUBLIC_PROVENANCE.json` lists each such file with its original and released sha256: 1,030 of the 4,896 files
  it covers. The archive's other ten files were written for the release: `README.md`, `VERIFY.md`,
  `ENVIRONMENT.md`, `requirements.txt`, the two manifests under their release names, the small example,
  `PUBLIC_PROVENANCE.json`, the tree manifest and `checksums.sha256`.
- The archive's bytes are these released bytes, and they are what the runs of record executed.

## Files copied from the archive into this repository
These copies are byte-identical to the archive members; their hashes are in the archive's tree manifest.

| Copy here | Archive member | sha256 |
|---|---|---|
| `paper/exact-three-manuscript.pdf` | `results/rank4-tensor-proof-package/v2/manuscript_r8_r6_build/main.pdf` | `5dcf22c244db8c54aaaff258f3a01afd117af20ef4c28e772dc6e63cd5b3269e` |
| `examples/small_example.py` | `examples/small_example.py` | `834e7a97bbf645b258a9129b1d12b23c54247945437a016ef43fbf3cb202a2d1` |

## The run records
The two runs of record (`docs/execution-evidence-2026-10-31.md`) left 891 files: reports, console logs, job logs,
guard receipts, environment and mount records, about 4.4 MB in all (4,398,046 bytes). They are published beside the archive, outside
it, because they were made after it was frozen.

**Where and in what form:** the same Zenodo record, file `run_records_2026-10-31.tar` (sha256
`2689ce88024f9dc7a2e242f629290e0254d5bd00d790b8150e97663ae576ddf8`, 6,205,440 bytes). It holds the 891 record files
under `runs/`, exactly as collected (no record was sanitized), and their seal `DONE_RUNS_OF_RECORD.json` (sha256
`562c9ee18acd2e3b5d541bd7340871ef7ffc228d0c3445905d54fb39af821a68`), which lists every file's sha256 under its path
in the producing workspace, `results/rank4-r42-release/final/runs/`.

**Check and extract** (the last command prints `891 files, 0 mismatches`):

    sha256sum run_records_2026-10-31.tar
    mkdir records && tar -xf run_records_2026-10-31.tar -C records && cd records
    python3 -c "import hashlib,json; m=json.load(open('DONE_RUNS_OF_RECORD.json')); p='results/rank4-r42-release/final/'; bad=[k for k,h in m['files'].items() if hashlib.sha256(open(k[len(p):],'rb').read()).hexdigest()!=h]; print(len(m['files']),'files,',len(bad),'mismatches')"
