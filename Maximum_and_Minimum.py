a=int(input())
b=[a]
b=list(map(int,input().split()))
c=[]
count=0
for i in b:
    if b.count(i)==i:
        count+=1
        c.append(i)
if count==0:
    print("-1")
else:
    print(min(c),max(c),end=' ')