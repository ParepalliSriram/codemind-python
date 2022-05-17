a=int(input())
b=[a]
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=''
l=0
for i in range(0,a):
    if b[i]>=c and b[i]<=d:
        s+=str(b[i])
        l+=1
if l>0:
    print(max(s))
else:
    print('-1')
