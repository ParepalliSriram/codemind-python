a=int(input())
c=0
while a>=10:
    while a:
        b=a%10
        a=a//10
        c+=b**2
    if c<10:
        break
    else:
        a=c
        c=0
if c==1 or c==7:
    print(True)
else:
    print(False)