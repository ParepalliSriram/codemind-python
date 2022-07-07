a=int(input())
b=[a]
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        c.append(i)
s=[]
cou=0
for i in c:
    if i not in s:
        s.append(i)
        cou+=1
if cou==0:
    print("-1")
else:
    print(*s)