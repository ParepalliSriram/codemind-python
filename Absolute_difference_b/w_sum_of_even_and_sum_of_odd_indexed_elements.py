a=int(input())
b=[a]
b=list(map(int,input().split()))
f=0
s=0
for i in range(0,a):
    if i%2==0:
        f+=b[i]
    else:
        s+=b[i]
print(abs(f-s))