a=int(input())
b=[a]
b=list(map(int,input().split()))
c=set(b)
ans=0
for i in c:
    if i%2==0:
        ans+=1
print(ans)