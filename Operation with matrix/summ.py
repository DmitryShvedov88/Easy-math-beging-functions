#summ 2 matrix
n, m = map(int,input().split())
#print(n, m)
matrixA =[[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB=[[int(i) for i in input().split()] for _ in range(n)]

matrixC=[[matrixA[j][i]+matrixB[j][i] for i in range (m)] for j in range(n)]
for i in range(n):
    print(*matrixC[i], sep=" ")
