#Find the column and row number of the largest element of a matrix
n, m=int(input()), int(input())
z=0
ma=0
#print(n)
#print(m)
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
#for i in range(n):
 #   print()
  #  for j in range(m):
  #      print(Matrix[i][j], end=' ')
#print()
z=max(max(Matrix, key=max))
#print(z)
for i in range (n):
    if ma>0:
        #print(ma)
        break
    else:
        for j in range (m):
            if Matrix[i][j]==z:
                print(i, j)
                ma+=1
                break