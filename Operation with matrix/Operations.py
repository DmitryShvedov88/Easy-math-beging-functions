
print("Введите матрице А")
n, m = map(int,input().split())
matrixA=[[int(input()) for i in range (m)] for j in range(n)]
print("Matrix A")
for i in range(n):
    print(*matrixA[i], sep=" ")


print("Введите матрице Б")
a, s = map(int,input().split())
matrixB=[[int(input()) for i in range (s)] for j in range(a)]
print("Matrix Б")
for i in range(a):
    print(*matrixB[i], sep=" ")


matrixC=[[matrixA[j][i]+matrixB[j][i] for i in range (m)] for j in range(n)]
print("сумма матриц")
for i in range(n):
    print(*matrixC[i], sep=" ")

print("произведение")
matrixD=[[0]*s for i in range (n)]
for i in range(n):
    for j in range(s):
        k = 0
        for r in range(a):
            k += matrixA[i][r] * matrixB[r][j]
        matrixD[i][j] = k
for i in matrixD:
    print(*i)