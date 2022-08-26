#n order magic square
n = int(input())
summ=0
summ1=0
summ2=0
summ3=0
counter_copy=[]
Matrix = [[int(i) for i in input().split()] for _ in range(n)]
digits = [i for i in range(1, n ** 2 + 1)]

for i in range(n):
    summ+=Matrix[i][i]
    summ1+=Matrix[n-i-1][i]
if summ==summ1:
    flag=True
else:
    flag=False
#print("summ", summ)
#print("summ1", summ1)
#print(flag)

for i in range(n):
    summ2=0
    for j in range(n):
        summ2+=Matrix[j][i]
    #print(i, "summ2", summ2)
    if summ==summ2:
        flag1=True
    else:
        flag1=False
        break
#print(flag1)
for i in range(n):
    summ3=0
    for j in range(n):
        summ3+=Matrix[i][j]
    #print(i, "summ3", summ3)
    if summ==summ3:
        flag2=True
    else:
        flag2=False
        break
#print(flag2)

for i in range(n):
    for j in range(n):
            if Matrix[i][j] in digits:
                digits.remove(Matrix[i][j])
                flag3=True
            else:
                flag3=False
                break
#print(flag3)
if flag==True and flag1==True and flag2==True and flag3==True:
    print("YES")
else:
    print("NO")
