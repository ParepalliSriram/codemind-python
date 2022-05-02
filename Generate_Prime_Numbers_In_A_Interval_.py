def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        print(a)
    else:
        return 0
a=int(input())
b=int(input())
for j in range(a,b+1):
    prime(j)