a=int(input())
b=[a]
b=list(map(int,input().split()))
b.append(b[0])
b.append(b[1])
c=0
for i in range(1,a+1):
    if b[i-1]%2==0 and b[i+1]%2!=0 or b[i-1]%2!=0 and b[i+1]%2==0:
        c+=1
print(c)