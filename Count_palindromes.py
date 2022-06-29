def rev(a):
    c=0
    d=a
    while a:
        b=a%10
        a=a//10
        c=c*10+b
    if c==d:
        return 1
    else:
        return 0
a=int(input())
b=[a]
b=list(map(int,input().split()))
count=0
for i in b:
    if rev(i):
        count+=1
print(count)