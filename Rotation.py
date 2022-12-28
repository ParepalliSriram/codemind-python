z=int(input())
for i in range(0,z):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for k in range(0,b):
        m=l[a-1]
        l=l[:-1]
        l1=[]
        l1.append(m)
        l1=l1+l
        l=l1
    print(*l1)