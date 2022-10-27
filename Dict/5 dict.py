keys = [str(i) for i in range(10)]
values = [' ', ".,?!:", 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
d = dict(zip(keys, values))
s = input()
for c in s:
    for key, value in d.items():
        if c.upper() in value:
            print(key * (value.index(c.upper()) + 1), end='')