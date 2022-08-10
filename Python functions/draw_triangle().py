def draw_triangle():
    n = 8
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (i * 2 - 1))
draw_triangle()