a=int(input())
for i in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=(b*(b+1))/2
    print(int(c-sum(arr)))
    