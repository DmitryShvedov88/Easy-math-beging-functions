l = input().lower().split()
d = {e: 0 for e in l}  # создаем словарь на основе списка с 0 значениями
max_value = 0
for key in l: d[key] += 1  # считаем повторяющиеся
for i in d.keys():
    if d[i] > max_value:
        max_value = d[i]


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(get_key(d, max_value), max_value)
