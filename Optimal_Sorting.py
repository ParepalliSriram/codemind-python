a=int(input())
for i in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    ar2=arr
    ar2=sorted(ar2)
    if(arr==ar2):
        print("0")
    else:
        print(max(arr)-min(arr))
    