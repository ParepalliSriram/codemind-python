a=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,a,2):
    for k in range(0,l[i+1]):
        l1.append(l[i])
print(*l1)