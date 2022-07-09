def rev(a):
    c=0
    if a<0:
        a=a*(-1)
    while a:
        b=a%10
        a=a//10
        c+=1
    return c
a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in b:
    if rev(i)>c:
        c=rev(i)
for i in b:
    if rev(i)==c:
        print(i,end=' ')