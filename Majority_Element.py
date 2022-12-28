a=int(input())
l=list(map(int,input().split()))
m=l[0]
for i in range(0,a):
    if(l.count(l[i])>a//2):
        m=l[i]
print(m)