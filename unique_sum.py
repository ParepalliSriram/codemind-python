a=int(input())
b=[a]
b=list(map(int,input().split()))
c=set(b)
ans=sum(c)
print(ans)