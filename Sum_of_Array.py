a=int(input())
b=[a]
b=list(map(int,input().split()))
f=0
for i in range(0,a):
    f+=b[i]
print(f)