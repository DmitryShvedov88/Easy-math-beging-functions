#We write the non-even row of the matrix in ascending order, the even row in descending order
n, m=map(int,input().split())
Matrix=[[str((1+i)+(j*m)).ljust(3) if j%2==0 else str((j*m)+(m-i)).ljust(3) for i in range (m)] for j in range(n) ]
for i in range(n):
    print(*Matrix[i], sep=" ")