n = int(input())
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
power = int(input())
matrixD = matrixA[:]

for i in range(power - 1):
    matrixD = [[sum([matrixA[h][i] * matrixD[i][j] for i in range(n)]) for j in range(n)] for h in range(n)]

for i in matrixD:
    print(*i)