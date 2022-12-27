a=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l.reverse()
for i in range(0,len(l)-1):
    if(i%2==0):
        if(l[i]>l[i+1]):
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
    else:
        if(l[i]<l[i+1]):
            t2=l[i]
            l[i]=l[i+1]
            l[i+1]=t2
print(*l)