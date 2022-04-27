a=int(input())
c=0
p=0
l=0
while a!=0:
    b=a%10
    a=a//10
    c+=b
if c>=10:
    while c!=0:
        d=c%10
        c=c//10
        p+=d
    if p>=10:
        while p!=0:
            e=p%10
            p=p//10
            l+=e
        print(l)
    else:
        print(p)
else:
    print(c)