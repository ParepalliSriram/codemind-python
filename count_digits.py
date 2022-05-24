def pal(a):
    c=0
    if a==0:
        c=1
    else:
        while(a!=0):
            b=a%10
            a=a//10
            c+=1
    return c
a=int(input())
b=[a]
b=list(map(int,input().split()))
d=0
for i in range(0,a):
    if b[i]<0:
        b[i]=b[i]*(-1)
    print(pal(b[i]),end=' ')
