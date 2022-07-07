a=int(input())
b=[a]
b=list(map(int,input().split()))
c=[]
d=[]
co=0
cou=0
for i in b:
    if b.count(i)==i:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
        co+=i
        cou+=1
if cou>0:
    ans=co/cou
    print(format(ans,".2f"))
else:
    print("-1")