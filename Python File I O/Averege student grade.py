with open('dataset_3363_4.txt') as t:
    a=[i.strip().split(";") for i in t]
for i in a:
  print((int(i[1])+int(i[2])+int(i[3]))/3)
mid1=0
mid2=0
mid3=0
lenght=0

for i in a:
  lenght+=1
  mid1+=int(i[1])
  mid2+=int(i[2])
  mid3+=int(i[3])

print(mid1/lenght, mid2/lenght, mid3/lenght, sep=" ")