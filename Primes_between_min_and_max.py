import math
def prime(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
a=int(input())
l=list(map(int,input().split()))
mi=min(l)
ma=max(l)
fi=l.index(mi)
si=l.index(ma)
if(fi<si):
    li=l[fi:si+1]
else:
    li=l[si:fi+1]
c=0
for i in li:
    if prime(i):
        c+=1
print(c)