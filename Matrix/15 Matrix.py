#splitting a list into nested lists
n = input().split()
parts=int(input())
list=[[n[i] for i in range(m,len(n), parts)] for m in range(parts)]
print(list)