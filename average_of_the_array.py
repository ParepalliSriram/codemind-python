a=int(input())
b=[a]
b=list(map(int,input().split()))
s=sum(b)
avg=s/a
print(format(avg,".2f"))