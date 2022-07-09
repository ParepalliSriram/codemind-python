a=int(input())
b=[a]
b=list(map(int,input().split()))
s=sum(b)
avg=s//a
if avg not in b:
    print(False)
else:
    print(True)