a,b=map(int,input().split())
c=[a]
d=[b]
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=set(c)
f=set(d)
c=list(e)
d=list(f)
g=0
h=0
k=0
l=0
for i in c:
    for j in d:
        if i==j:
            g+=1
    if g==0:
        h+=1
    g=0
for i in d:
    for j in c:
        if i==j:
            k+=1
    if k==0:
        l+=1
    k=0
print(h+l)