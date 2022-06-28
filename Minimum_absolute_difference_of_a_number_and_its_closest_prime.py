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
for i in range(a,a+100):
    if prime(i):
        f=i
        break
for i in range(a,0,-1):
    if prime(i):
        s=i
        break
if abs(a-f)<=abs(a-s):
    print(f-a)
else:
    print(a-s)