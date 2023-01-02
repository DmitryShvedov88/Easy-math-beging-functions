word_list=list(map(str, input().lower().split()))
word_list=[i.strip(':,.!?();') for i in word_list]
result={}
for i in word_list:
    if i in result:
        result[i] = result.get(i, 0) +1
    else:
        result[i] = result.get(i, 1)
Min=[]
for i in result:
    if result[i]==min(result.values()):
        Min.append(i)
    else:
        continue
print(min(Min))