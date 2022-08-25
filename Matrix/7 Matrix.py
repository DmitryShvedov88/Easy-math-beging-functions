#Swap matrix rows
n = int(input())
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n//2):
    Matrix[i], Matrix[n-1-i]=Matrix[n-1-i], Matrix[i]
for i in range(n):
    print(*Matrix[i], sep=(" "))