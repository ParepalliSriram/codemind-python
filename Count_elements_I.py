a,b=map(int,input().split())
b=[a]
c=[b]
b=list(map(int,input().split()))
c=list(map(int,input().split()))
s=set(b)
b=list(s)
d=0
e=0
for i in b:
    for j in c:
        if i==j:
            d+=1
    if d>0:
        e+=1
    d=0
print(e)