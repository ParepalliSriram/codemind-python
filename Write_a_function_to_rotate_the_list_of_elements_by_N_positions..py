a=int(input())
l=list(map(int,input().split()))
b=int(input())
if(b>a):
    b=b%a
l1=l[a-b:]
for i in range(0,a-b):
    l1.append(l[i])
print(*l1)