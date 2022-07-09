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
if a<0:
    print("Not Ugly Number")
else:
    for i in range(1,a+1):
        if a%i==0:
            if prime(i):
                if i!=2 and i!=3 and i!=5:
                    print("Not Ugly Number")
                    break
    else:
        print("Ugly Number")