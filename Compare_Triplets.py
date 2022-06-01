a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
alice=0
bob=0
if a>d:
    alice+=1
elif a<d:
    bob+=1
if b>e:
    alice+=1
elif b<e:
    bob+=1
if c>f:
    alice+=1
elif c<f:
    bob+=1
print(alice,bob)