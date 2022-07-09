a=int(input())
b=[a]
b=list(map(int,input().split()))
c=int(input())
for i in b:
    if i==c:
        print(True)
        break
else:
    print(False)