a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
for i in range(1,a):
    if i+1>a-1:
        break
    if b[i-1]%2==0 and b[i+1]%2==0:
        if b[i]%2==0:
            c+=1
print(c)