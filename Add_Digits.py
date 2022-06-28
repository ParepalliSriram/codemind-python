a=int(input())
while a>10:
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c+=b
    if c<10:
        print(c)
        break
    else:
        a=c