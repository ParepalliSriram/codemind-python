a=int(input())
arr=[]
for i in range(0,a):
    ar=list(map(int,input().split()))
    arr.append(ar)
count=0
for i in range(0,a):
    for k in range(0,a):
        if(k==i or k==a-i-1):
            count+=arr[i][k]
print(count)