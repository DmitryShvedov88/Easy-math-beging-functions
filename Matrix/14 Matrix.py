#fill the matrix with diagonals
n, m = map(int, input().split())
mt = [[''] * m for i in '1'* n]
d = 1
for k in range(1, n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j + 1 == k:
                mt[i][j] = str(d).ljust(3)
                d += 1
[print(*r, sep='') for r in mt]