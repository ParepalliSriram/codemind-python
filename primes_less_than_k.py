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
c=[a]
c=list(map(int,input().split()))
l=int(input())
b=0
d=0
for i in c:
    if prime(i):
        if i<=l:
            b+=1
print(b)