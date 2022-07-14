a=int(input())
b=list(map(int,input().split()))
c=0
if a<3:
    print("no")
else:
    for i in range(2,a):
        if b[i]!=b[i-1]+b[i-2]:
            print("no")
            break
    else:
        print("yes")