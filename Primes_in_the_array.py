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
b=[a]
b=list(map(int,input().split()))
c=0
for i in b:
    if prime(i):
        c+=1
print(c)