def compute_binom(n, k):
    fn = 1
    fk = 1
    fnk = 1
    l = n - k
    for i in range(n + 1):
        if i <= 1:
            fn = 1
        else:
            fn *= i
    for i in range(k + 1):
        if i <= 1:
            fk = 1
        else:
            fk *= i
    for i in range(l + 1):
        if i <= 1:
            fnk = 1
        else:
            fnk *= i
    z = int(fn / (fnk * fk))
    return z
n = int(input())
k = int(input())

print(compute_binom(n, k))