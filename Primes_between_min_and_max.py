def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=list(map(int,input().split()))
ma=max(b)
mi=min(b)
count=0
for i in range(0,a):
    if b[i]==ma:
        f=i
        break
for i in range(0,a):
    if b[i]==mi:
        s=i
        break
if f>s:
    t=f
    h=s
else:
    t=s
    h=f
c=[]
c.extend(b[h:t+1])
for i in c:
    if prime(i):
        count+=1
print(count)
