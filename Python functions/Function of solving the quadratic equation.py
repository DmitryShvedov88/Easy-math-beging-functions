from math import *
def solve(a, b, c):
    d = pow(b, 2) - 4 * a * c
    x1 = 0
    x2 = 0
    if d == 0:
        x1 += -b / (2 * a)
        return x1, x1
    elif d > 0:
        x1 += (-b + sqrt(d)) / (2 * a)
        x2 += (-b - sqrt(d)) / (2 * a)
        if x1 < x2:
            return x1, x2
        else:
            return x2, x1
    pass
a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)