def rev(a):
    while a!=0:
        b=a%10
        break
    if b==2 or b==3 or b==9:
        return 1
    else:
        return 0
a=int(input())
c=0
for i in range(0,a):
    b=[2]
    b=list(map(int,input().split()))
    for i in range(b[0],b[1]+1):
        if rev(i):
            c+=1
    print(c)
    c=0
