a=int(input())
b=[a]
b=list(map(int,input().split()))
s=sum(b)
c=0
avg=s//a
for i in b:
    if i<=avg:
        c+=1
print(c)