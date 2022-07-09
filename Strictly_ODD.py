a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in range(1,a):
    if i%2==0:
        if b[i]%2!=0:
            print(False)
            break
else:
    print(True)