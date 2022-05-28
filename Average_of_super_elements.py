a=int(input())
b=[a]
b=list(map(int,input().split()))
add=0
m=0
c=0
l=0
s=[]
for i in range(0,a):
    for j in range(0,a):
        if b[i]==b[j]:
            c+=1
    if c==b[i]:
        s.append(b[i])
        l+=1
    c=0
if l>0:
    p=set(s)
    for i in p:
        add+=i
        m+=1
    ans=add/m
    print(format(ans,".2f"))
else:
    print("-1")