#Swap matrix diagonals
n = int(input())
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    Matrix[i][i], Matrix[n-1-i][i]=Matrix[n-1-i][i], Matrix[i][i]
for i in range(n):
    print(*Matrix[i], sep=(" "))