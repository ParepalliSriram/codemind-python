a=int(input())
b=[a]
b=list(map(int,input().split()))
c=int(input())
count=0
for i in b:
    if i!=c:
        count+=i
    else:
        count+=i
        break
print(count)