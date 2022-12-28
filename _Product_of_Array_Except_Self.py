a=int(input())
l=list(map(int,input().split()))
p=1
for i in range(0,a):
    p*=l[i]
for i in range(0,a):
    print(p//l[i],end=" ")