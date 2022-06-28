def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=a
c=0
if prime(a):
    while a:
        d=a%10
        a=a//10
        c=c*10+d
    if prime(c):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")