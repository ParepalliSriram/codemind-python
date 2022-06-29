def r_v(a):
    c=0
    while a:
        b=a%10
        a=a//10
        c+=b
    return c
a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in b:
    if i>10:
        c+=r_v(i)
    else:
        c+=i
print(c)