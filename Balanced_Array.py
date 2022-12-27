z=int(input())
for i in range(0,z):
    a=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    count=0
    p=0
    for k in range(0,a):
        if(s-l[k]-count==count):
            print("YES")
            p+=1
            break
        count+=l[k]
    if(p==0):
        print("NO")