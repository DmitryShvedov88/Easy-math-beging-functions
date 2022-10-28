text = input().lower()
result = {}
for i in text:
    if i.isalpha():
        if i in result:
            result[i] = result.get(i, 0) +1
        else:
            result[i] = result.get(i, 1)
    else:
        continue
print(result)