a=int(input())
b=[2]
for n in range(0,a):
    b=list(map(int,input().split()))
    d=0
    e=0
    for i in range(0,2):
        d+=b[i]
    print(d)
