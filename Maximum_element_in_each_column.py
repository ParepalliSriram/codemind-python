a,b=map(int,input().split())
arr=[]
for i in range(0,a):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(0,a):
    ma=0
    for k in range(0,b):
        if(arr[k][i]>ma):
            ma=arr[k][i]
    print(ma)