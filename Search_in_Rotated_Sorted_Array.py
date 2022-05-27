a=int(input())
b=[a]
b=list(map(int,input().split()))
n=int(input())
l=[]
c=0
for i in range(0,a):
    if b[i]==n:
        c+=1
        print(i)
        break
if c==0:
    print("-1")