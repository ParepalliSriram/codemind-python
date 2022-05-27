a=int(input())
b=[a]
b=list(map(int,input().split()))
l=[]
for i in b:
    if i<0:
        i=i*(-1)
    l.append(i)
m=[]
k=sorted(l)
for i in k:
    m.append(i*i)
for i in m:
    print(i,end=' ')