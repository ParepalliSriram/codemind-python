z=int(input())
for i in range(0,z):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    n=0
    for k in range(0,a):
        for m in range(0,a):
            if(sum(l[k:m+1])==b):
                n+=1
                print(k+1,m+1)
                break
        if(n!=0):
            break
    if(n==0):
        print("-1")