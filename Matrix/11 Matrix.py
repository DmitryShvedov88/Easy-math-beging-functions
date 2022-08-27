#0 0 1
#0 1 2
#1 2 2

n = int(input())
Matrix = [["0" for i in range (n)] for j in range(n) ]# put your python code here
for i in range(n):
    Matrix[n-i-1][i]=1
    for j in range(n-i-1):
        Matrix[n-i-1][n-j-1]=2
for i in range(n):
    print(*Matrix[i], sep=" ")