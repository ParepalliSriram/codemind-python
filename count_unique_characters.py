a=str(input())
a=a.lower()
b=[]
for i in a:
    if i==' ':
        continue
    else:
        b.append(i)
s=[]
for i in b:
    co=0
    for j in b:
        if i==j:
            co+=1
    if co==1:
        s.append(i)
print(len(s))