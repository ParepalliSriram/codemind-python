a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in range(0,a):
    print(b[i],end=' ')
if a%2!=0:
    print("0",end=' ')