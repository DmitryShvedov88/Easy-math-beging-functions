#A program that transposes a square matrix.
n = int(input())
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    print()
    for j in range(n):
        print(Matrix[j][i], end=(" "))