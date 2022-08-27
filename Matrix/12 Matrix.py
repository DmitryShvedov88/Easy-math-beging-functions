#Write down the dimensions of the matrix and fill it with numbers in ascending order
n, m = map(int,input().split())
Matrix = [[str((1+i)+(j*m)).ljust(3) for i in range (m)] for j in range(n) ]
for i in range(n):
    print(*Matrix[i], sep=" ")