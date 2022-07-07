a=int(input())
b=[a]
b=list(map(int,input().split()))
c=int(input())
s=[]
co=0
for i in b:
    if b.count(i)==c:
        if i not in s:
            s.append(i)
            co+=1
if co==0:
    print("-1")
else:
    print(*s)