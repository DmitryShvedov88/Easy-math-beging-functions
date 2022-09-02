
print("Введите матрице А")
n, m = map(int,input().split())
matrix=[[int(input()) for i in range (m)] for j in range(n)]
print("Matrix A")
for i in range(n):
    print(*matrix[i], sep=" ")

print("Введите матрице Б")
a, s = map(int,input().split())
matrix=[[int(input()) for i in range (s)] for j in range(a)]
print("Matrix Б")
for i in range(a):
    print(*matrix[i], sep=" ")

print("сумма матриц")

print("произведение")