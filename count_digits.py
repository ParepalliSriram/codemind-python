def leng(a):
    d=1
    if a==0:
        return d
    if a<0:
        a=a*(-1)
    c=0
    while a:
        b=a%10
        a=a//10
        c+=1
    return c
a=int(input())
c=list(map(int,input().split()))
cou=0
m=max(c)
for i in c:
    print(leng(i),end=' ')