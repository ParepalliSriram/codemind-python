def lenght(a):
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c+=1
    return c
a=int(input())
b=[a]
b=list(map(int,input().split()))
c=min(b)
m=0
l=0
while c!=0:
    d=c%10
    c=c//10
    l+=1
for i in range(0,a):
        s=lenght(b[i])
        if s==l:
            m+=1
print(m)
