a=int(input())
l=list(map(int,input().split()))
for i in range(0,a-1):
    l1=l[i+1:]
    m=max(l1)
    l[i]=m
l[len(l)-1]=-1
print(*l)