"""Small example for reviewers: the three tensor-triple lattices of one generic seed (Claude, round 40).

    python -B examples/small_example.py [a b c]          (default: 3 1 4, so D = ac - b^2 = 11)

For integers 0 < 2b < a < c this builds the Gram matrices of L0, L1, L2 (the formulas of
results/rank4-tensor-proof-package/TENSOR_TRIPLE_PROOF_PACKAGE.md, as recorded in verify_package.json), and checks:
  1. each is positive definite, even, with determinant 729 D^2;
  2. their theta series agree through the Sturm bound of their common level (weight 2, trivial character), which by
     Sturm's theorem proves equality of the full theta series for this seed (Theorem A, which holds for every M);
  3. they are pairwise non-isometric (PARI qfisom), as Theorem B states for every generic M.
It does not prove the main theorem (that no fourth class exists); that is the content of the package, whose complete
verification is `python -B results/rank4-tensor-proof-package/v2/verify_r6.py full`. Needs PARI/GP 2.17.x: the sealed
default path, or EXACT3_GP, or gp on PATH."""
import os, shutil, subprocess, sys, tempfile
from fractions import Fraction as F
from math import gcd

GP_DEFAULT = r'C:\Program Files (x86)\Pari64-2-17-4\gp.exe'


def grams(a, b, c):
    L0 = [[2*a - 2*b + 2*c, a - c, 6*b - 3*c, 3*b - 6*c], [a - c, 2*a + 2*b + 2*c, 3*b + 6*c, 6*b + 3*c],
          [6*b - 3*c, 3*b + 6*c, 18*c, 9*c], [3*b - 6*c, 6*b + 3*c, 9*c, 18*c]]
    L1 = [[2*a + 6*b + 6*c, a + 5*b + 3*c, 6*b + 9*c, 3*b + 9*c], [a + 5*b + 3*c, 2*a + 2*b + 2*c, 3*b + 6*c, 6*b + 3*c],
          [6*b + 9*c, 3*b + 6*c, 18*c, 9*c], [3*b + 9*c, 6*b + 3*c, 9*c, 18*c]]
    L2 = [[2*a - 2*b + 2*c, a + 3*b - c, 6*b - 3*c, 3*b + 3*c], [a + 3*b - c, 2*a + 2*b + 2*c, 3*b + 6*c, 6*b + 3*c],
          [6*b - 3*c, 3*b + 6*c, 18*c, 9*c], [3*b + 3*c, 6*b + 3*c, 9*c, 18*c]]
    return [L0, L1, L2]


def det(M):
    M = [[F(x) for x in r] for r in M]
    n, d = len(M), F(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return F(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    return d


def minors_positive(G):
    return all(det([row[:k] for row in G[:k]]) > 0 for k in range(1, 5))


def level(G):
    """Least N with N * G^-1 integral with even diagonal (the level of the even lattice with Gram G)."""
    n, D = 4, det(G)
    inv = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[G[r][c] for c in range(n) if c != j] for r in range(n) if r != i]
            inv[j][i] = (-1) ** (i + j) * det(minor) / D
    N = 1
    for row in inv:
        for x in row:
            N = N * x.denominator // gcd(N, x.denominator)
    while not all((N * inv[i][i]).denominator == 1 and int(N * inv[i][i]) % 2 == 0 for i in range(n)):
        N *= 2
    return N


def sturm(N):
    m, k, p, idx = N, N, 2, F(N)
    while p * p <= k:
        if k % p == 0:
            idx *= F(p + 1, p)
            while k % p == 0:
                k //= p
        p += 1
    if k > 1:
        idx *= F(k + 1, k)
    return int(2 * idx / 12)


def gp_binary():
    if os.path.isfile(GP_DEFAULT):
        return GP_DEFAULT
    g = os.environ.get('EXACT3_GP') or shutil.which('gp') or shutil.which('gp.exe')
    if not g:
        sys.exit('PARI/GP not found: set EXACT3_GP or put gp on PATH')
    return g


def main():
    a, b, c = (int(x) for x in sys.argv[1:4]) if len(sys.argv) >= 4 else (3, 1, 4)
    if not (0 < 2 * b < a < c):
        sys.exit('need integers with 0 < 2b < a < c (the generic family)')
    D = a * c - b * b
    G = grams(a, b, c)
    ok = True
    for k, M in enumerate(G):
        d = det(M)
        even = all(M[i][i] % 2 == 0 for i in range(4)) and all(M[i][j] == M[j][i] for i in range(4) for j in range(4))
        print(f'L{k}: positive definite {minors_positive(M)}, even {even}, det {d} (729 D^2 = {729 * D * D})')
        ok &= minors_positive(M) and even and d == 729 * D * D
    lv = sorted({level(M) for M in G})
    B = max(sturm(N) for N in lv)
    print(f'levels {lv}; Sturm bound for weight 2 on Gamma0(N): {B}')
    mat = lambda M: 'matrix(4,4,i,j,[' + ','.join(str(x) for r in M for x in r) + '][(i-1)*4+j])'
    script = ''.join(f'G{k}={mat(M)};\n' for k, M in enumerate(G)) + (
        f't0=Vec(qfrep(G0,{B},1));t1=Vec(qfrep(G1,{B},1));t2=Vec(qfrep(G2,{B},1));\n'
        'print("THETA ",t0==t1," ",t1==t2);\n'
        'print("ISOM ",qfisom(G0,G1)!=0," ",qfisom(G0,G2)!=0," ",qfisom(G1,G2)!=0);\n'
        'print("PREFIX ",concat([1],2*t0[1..min(12,#t0)]));\nquit;\n')
    with tempfile.TemporaryDirectory() as t:
        p = os.path.join(t, 'small_example.gp')
        open(p, 'w').write(script)
        out = subprocess.run([gp_binary(), '-q', p], capture_output=True, text=True, timeout=600).stdout
    lines = {ln.split()[0]: ln.split()[1:] for ln in out.splitlines() if ln.strip()}
    theta_equal = lines.get('THETA') == ['1', '1']
    isom = lines.get('ISOM')
    print('theta series equal through the Sturm bound:', theta_equal)
    print('theta prefix of L0 (coefficients of q^0..q^12):', ' '.join(lines.get('PREFIX', [])))
    print('isometric pairs (L0,L1), (L0,L2), (L1,L2):', isom)
    ok &= theta_equal and isom == ['0', '0', '0']
    print('SMALL EXAMPLE OK' if ok else 'SMALL EXAMPLE FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
