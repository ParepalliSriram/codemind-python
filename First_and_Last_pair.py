a=int(input())
b=[a]
b=list(map(int,input().split()))
c=len(b)
d=[]
for i in range(0,len(b)):
    for j in range(c-1,-1,-1):
        d.append(b[i])
        d.append(b[j])
        break
    c=c-1
    if c==len(b)//2:
        break
if a%2!=0:
    del d[a-1]
    d.append(0)
    print(*d)
    
else:
    print(*d)