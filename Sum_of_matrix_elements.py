a=int(input())
b=int(input())
c=[]
count=0
for i in range(0,a):
    b=list(map(int,input().split()))
    c.append(b)
for i in range(0,len(c)):
    for k in range(0,len(c[i])):
        count+=(c[i][k])
print(count)