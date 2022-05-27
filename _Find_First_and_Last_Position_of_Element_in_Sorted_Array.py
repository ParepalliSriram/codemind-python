a=int(input())
b=[a]
b=list(map(int,input().split()))
n=int(input())
l=[]
c=0
for i in range(0,a):
    if b[i]==n:
        c+=1
        l.append(i)
if c>0:
    for i in l:
        print(i,end=' ')
        break
    for i in l[::-1]:
        print(i,end=' ')
        break
else:
    print("-1 -1")