n = int(input())
m = int(input())
Matrix = [ [str(i * j).ljust(3) for i in range (m)] for j in range(n) ]
for i in Matrix:
    print(*i)
print()