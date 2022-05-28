a=int(input())
b=[a]
b=list(map(int,input().split()))
j=0
k=len(b)
s=[]
c=0
for i in range(0,a):
    c+=1
    s.append(b[j])
    s.append(b[k-1])
    j+=1
    k-=1
    if c==k:
        break
p=''
if a%2==0:
    print(*s)
else:
    for i in s:
        if str(i) not in p:
            p+=str(i)
    for i in p:
        print(i,end=' ')
    print("0",end=' ')
