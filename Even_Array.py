a=int(input())
b=[a]
b=list(map(int,input().split()))
for i in b:
    if i%2!=0:
        print(False)
        break
else:
    print(True)