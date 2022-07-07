a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
s=sum(b)
avg=s//a
for i in b:
    if i>=avg:
        c+=1
print(c)