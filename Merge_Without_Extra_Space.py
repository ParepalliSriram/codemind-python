a=int(input())
for i in range(0,a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    e=list(map(int,input().split()))
    f=d+e
    f=sorted(f)
    print(*f)