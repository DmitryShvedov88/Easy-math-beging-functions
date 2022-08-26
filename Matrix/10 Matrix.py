#interleaving characters in a matrix
n, m = map(int,input().split())
Matrix = [["." if (i+j)%2==0 else "*" for i in range (m)] for j in range(n) ]# put your

#python code here
for i in range(n):
    print(*Matrix[i], sep=" ")