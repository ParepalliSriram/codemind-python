a=int(input())
b=[a]
b=list(map(int,input().split()))
l=[]
c=0
for i in range(0,a):
    for j in range(0,a):
        if b[i]==b[j]:
            c+=1
    if c!=1:
        l.append(b[i])
    c=0
n=set(l)
for k in n:
    print(k)