a=int(input())
b=[a]
b=list(map(int,input().split()))
n=int(input())
c=0
l=0
p=''
s=''
for i in range(0,a):
    for j in range(0,a):
        if b[i]==b[j]:
            c+=1
    if c==n:
        l+=1
        s+=str(b[i])
    c=0
if l==0:
    print("-1")
else:
    for d in s:
        if d not in p:
            p=p+d
    for j in p:
        print(j,end=' ')
    