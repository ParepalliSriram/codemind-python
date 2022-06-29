a,b=map(int,input().split())
c=[a]
c=list(map(int,input().split()))
d=[b]
d=list(map(int,input().split()))
e=[]
f=[]
for i in c:
    if i not in e:
        e.append(i)
for i in d:
    if i not in f:
        f.append(i)
for i in e:
    if i in f:
        print(i,end=' ')