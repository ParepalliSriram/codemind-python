a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
s=''
for i in range(0,a):
    s+=str(b[i])
p=''
for i in s:
    if i not in p:
        p+=i
for i in p:
    print(i,end=' ')