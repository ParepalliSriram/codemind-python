a,b=map(int,input().split())
c=[a]
d=[b]
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=0
for i in range(0,a):
    for j in range(0,b):
        if c[i]==d[j]:
            e+=1
    if e==0:
        print(c[i],end=' ')
    e=0
for j in range(0,b):
    for i in range(0,a):
        if d[j]==c[i]:
            e+=1
    if e==0:
        print(d[j],end=' ')
    e=0