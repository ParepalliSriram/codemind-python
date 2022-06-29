def rev(a):
    c=0
    b=a
    while a:
        d=a%10
        a=a//10
        c=c*10+d
    return c
a=int(input())
b=[a]
b=list(map(int,input().split()))
for i in b:
    print(rev(i),end=' ')