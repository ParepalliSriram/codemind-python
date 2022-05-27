a=int(input())
b=[a]
b=list(map(int,input().split()))
l=[]
c=0
t=len(b)
n=0
for i in range(0,a):
    n+=1
    if b[i]!=0:
        c+=1
    if b[i]==0 or n==t:
        l.append(c)
        c=0
print(max(l))