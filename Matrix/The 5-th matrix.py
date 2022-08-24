#Determine if a matrix is symmetric
n = int(input())
k=0
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if Matrix[i][j]!=Matrix[j][i]:
            k+=1
if k==0:
    print("YES")
else:
    print("NO")