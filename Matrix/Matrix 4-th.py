#crumple matrix columns in places
n, m=int(input()), int(input())
z=0
ma=0
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
c1,c2=input().split()
for i in range(n):
    Matrix[i][int(c1)], Matrix[i][int(c2)] = Matrix[i][int(c2)], Matrix[i][int(c1)]
for i in range(n):
    print()
    for j in range(m):
        print(Matrix[i][j], end=' ')