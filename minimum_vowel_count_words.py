a=input()
b=a.split()
c='aeiouAEIOU'
co=0
s=[]
for i in b:
    for j in i:
        if j in c:
            co+=1
    s.append(co)
    co=0
m=min(s)
cou=0
for i in s:
    if i==m:
        cou+=1
print(cou)