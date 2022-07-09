a=int(input())
b=[a]
b=list(map(int,input().split()))
c=int(input())
co=0
for i in b:
    if i==c:
        co+=1
print(co)