"""Round 43 (Claude, lead), version r3: extract the run figures quoted by the execution-evidence note.
r3 (Sol review C5): the producing workspace is an explicit argument; r2 located it from the script's own path.

Reads only the sealed record copies collected by DONE_RUNS_OF_RECORD (results/rank4-r42-release/final/runs/) and the
archive's own two manifests (RELEASE_MANIFEST.json and REGENERATION_MANIFEST.json, from the extracted tree
mirrors/rd/tree, whose tree manifest db1d0974... is the frozen archive's). r1 read the workspace copies
RELEASE_MANIFEST_r9_r4.json / REGENERATION_MANIFEST_r9_r4.json instead (same jobs and argv; review R9).
Environment text files are never read; from report.json only named fields are taken, never `platform` or
`executable`. It runs only in the producing workspace (its paths are relative to it); it is published to show how the
figures were obtained.
    python -B evidence/extract_run_facts.py PRODUCING_WORKSPACE NEW_OUT_JSON
Requires the original producing-workspace record/manifest layout; the repository alone is insufficient."""
import hashlib, json, re, sys
from pathlib import Path

W7 = None
RUNS = None
V2 = 'mirrors/rd/tree/results/rank4-tensor-proof-package/v2/'
MANIFESTS = {'finalR2': V2 + 'RELEASE_MANIFEST.json', 'finalG3': V2 + 'REGENERATION_MANIFEST.json'}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def txt(p):
    return (RUNS / p).read_text(encoding='utf-8', errors='replace').strip()


def inner_seconds(argv):
    s = ' '.join(argv) if isinstance(argv, list) else str(argv)
    m = re.search(r'--seconds[ =](\d+)', s)
    return int(m.group(1)) if m else None


def main():
    global W7, RUNS
    if len(sys.argv) != 3:
        sys.exit('usage: extract_run_facts.py PRODUCING_WORKSPACE NEW_OUT_JSON')
    W7 = Path(sys.argv[1]).resolve()
    RUNS = W7 / 'results/rank4-r42-release/final/runs'
    out = Path(sys.argv[2])
    if out.exists():
        sys.exit(f'{out} exists; refusing to overwrite')
    seal = W7 / 'results/rank4-r42-release/final/DONE_RUNS_OF_RECORD.json'
    facts = dict(source_seal=dict(path=seal.relative_to(W7).as_posix(), sha256=sha(seal)),
                 archives=json.loads((RUNS / 'ARCHIVES.json').read_text(encoding='utf-8')), runs={})
    for run, man_path in MANIFESTS.items():
        rep = json.loads((RUNS / run / 'report.json').read_text(encoding='utf-8'))
        man = json.loads((W7 / man_path).read_text(encoding='utf-8'))
        mjobs = {j['id']: j for s in man['steps'] for j in s['jobs']}
        env = rep['environment']
        jobs = rep['jobs']
        peak = max(jobs, key=lambda j: (j['guard'].get('peak_MB') or 0) / j['limit_mb'])
        timed = [j for j in jobs if j.get('timeout_s')]
        slow = max(timed, key=lambda j: (j['guard'].get('seconds') or 0) / j['timeout_s'])
        inner, inner_only, both, manifest_smaller = [], 0, 0, []
        for j in jobs:
            lim = inner_seconds(mjobs.get(j['id'], {}).get('argv') or mjobs.get(j['id'], {}).get('command'))
            if lim:
                mt = mjobs.get(j['id'], {}).get('timeout_s')
                if mt is None:
                    inner_only += 1
                else:
                    both += 1
                    if mt < lim:
                        manifest_smaller.append(dict(job=j['id'], inner_limit_s=lim, manifest_timeout_s=mt))
                inner.append((j['guard'].get('seconds') or 0) / lim)
                if inner[-1] == max(inner):
                    inner_max = dict(job=j['id'], seconds=round(j['guard']['seconds'], 1), inner_limit_s=lim,
                                     ratio=round(inner[-1], 2))
        nonzero = [dict(job=j['id'], exit=j['guard'].get('exit'), expect_exit=j['guard'].get('expect_exit'),
                        ok=j['ok']) for j in jobs if (j['guard'].get('expect_exit') or 0) != 0]
        console = txt(f'{run}/verify_console.txt').splitlines()
        closing = [ln for ln in console if ln.startswith('COMPLETE MANIFEST VERIFIED')]
        facts['runs'][run] = dict(
            manifest=dict(path=man_path, sha256=sha(W7 / man_path)),
            report_manifest_identity=rep['manifest_identity'], report_dependencies_sha256=rep['dependencies_sha256'],
            verifier_sha256=rep['verifier_sha256'], mode=rep['mode'], scope=rep['scope'], ok=rep['ok'],
            started=rep['started'], finished=rep['finished'],
            verify_started=txt(f'{run}/verify_started.txt'), verify_finished=txt(f'{run}/verify_finished.txt'),
            verify_exit=txt(f'{run}/verify_exit.txt'), closing_line=closing,
            jobs_selected=rep['jobs_selected'], jobs_in_manifest=rep['jobs_in_manifest'],
            jobs_ok=sum(1 for j in jobs if j['ok']), schedule=rep['schedule'], portability_table=rep['portability_table'],
            environment=dict(python=env.get('python', '').split(' ')[0], optimize=env.get('optimize'),
                             assert_probe_exit=env.get('assert_probe_exit'), psutil=env.get('psutil'),
                             gp_version=env.get('gp_version'), guard_sha256=env.get('guard_sha256'),
                             x3compat=env.get('x3compat')),
            jobs_with_linux_additions=sum(1 for j in jobs if j.get('linux_additions')),
            max_peak_over_limit=dict(job=peak['id'], peak_MB=round(peak['guard']['peak_MB']), limit_mb=peak['limit_mb'],
                                     ratio=round(peak['guard']['peak_MB'] / peak['limit_mb'], 2)),
            jobs_with_timeout_s=len(timed),
            max_seconds_over_timeout=dict(job=slow['id'], seconds=round(slow['guard']['seconds'], 1),
                                          timeout_s=slow['timeout_s'],
                                          ratio=round(slow['guard']['seconds'] / slow['timeout_s'], 2)),
            jobs_with_inner_seconds=len(inner), inner_without_manifest_timeout=inner_only, inner_and_manifest_timeout=both,
            manifest_timeout_smaller_than_inner=manifest_smaller,
            max_seconds_over_inner_limit=inner_max if inner else None,
            nonzero_expected_exits=nonzero)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(facts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    for run, f in facts['runs'].items():
        print(run, f['jobs_ok'], '/', f['jobs_in_manifest'], 'ok', f['ok'], f['max_peak_over_limit'],
              f['max_seconds_over_timeout'], f['max_seconds_over_inner_limit'], f['nonzero_expected_exits'])


if __name__ == '__main__':
    main()
