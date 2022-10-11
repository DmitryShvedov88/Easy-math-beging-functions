n, m = map(int,input().split())
matrixA=[[int(i) for i in input().split()] for _ in range(n)]
input()
a, s = map(int,input().split())
matrixB=[[int(i) for i in input().split()] for _ in range(a)]# put your python code here
matrixD=[[0]*s for i in range (n)]
for i in range(n):
    for j in range(s):
        k = 0
        for r in range(a):
            k += matrixA[i][r] * matrixB[r][j]
        matrixD[i][j] = k
for i in matrixD:
    print(*i)