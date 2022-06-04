a=int(input())
b=[a]
b=list(map(int,input().split()))
for i in (0,a):
    b.append(b[i])
    b.append(b[i+1])
    break
c=0
for i in range(1,len(b)-1):
    if b[i-1]%2==0 and b[i+1]%2!=0 or b[i-1]%2!=0 and b[i+1]%2==0:
        c+=1
print(c)
