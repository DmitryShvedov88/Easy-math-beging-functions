keys = [i for i in range(10)]
values = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d = dict(zip(keys, values))
print(*[d[int(i)] for i in input()])