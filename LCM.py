a,b=map(int,input().split())
for c in range(1,b+1):
    d=c*b
    if d%a==0:
        print(d)
        break