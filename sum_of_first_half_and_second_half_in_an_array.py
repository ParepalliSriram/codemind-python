a=int(input())
b=[a]
b=list(map(int,input().split()))
if a%2!=0:
    b.append(0)
f1=0
f2=0
for i in range(0,a//2):
    f1+=b[i]
for i in range(a//2,a):
    f2+=b[i]
print(f1)
print(f2)