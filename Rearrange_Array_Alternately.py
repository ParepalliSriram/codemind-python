a=int(input())
for i in range(0,a):
    b=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    l1=[]
    for k in range(0,b//2):
        l1.append(l[b-k-1])
        l1.append(l[k])
    if(b%2!=0):
        l1.append(l[b//2])
    print(*l1)