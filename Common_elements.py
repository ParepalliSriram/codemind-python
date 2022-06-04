a,b=map(int,input().split())
c=[a]
d=[b]
c=list(map(int,input().split()))
d=list(map(int,input().split()))
s=[]
p=[]
m=[]
for i in c:
    s.append(i)
for i in s:
    if i not in p:
        p.append(i)
for i in p:
    m.append(i)
c=list(m)
s=[]
p=[]
m=[]
for i in d:
    s.append(i)
for i in s:
    if i not in p:
        p.append(i)
for i in p:
    m.append(i)
d=list(m)
g=0
h=[]
k=0
for p in c:
    for q in d:
        if p==q:
            g+=1
    if g==1:
        h.append(p)
    g=0

print(*h)