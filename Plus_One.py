a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in b:
    c=c*10+i
c=c+1
s=str(c)
for i in s:
    print(i,end=' ')