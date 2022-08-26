#Draw a chess knight according to the entered coordinates and mark the "*" fields where the knight can go.
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])

chess=[["." for _ in range(8)] for _ in range(8)]
chess[y][x]="N"
for i in range(8):
    for j in range(8):
        if (y - i) * (x - j) in [-2, 2]: chess[i][j] = "*"
for i in range(8):
    print(*chess[i], sep=" ")