a=int(input())
l=1
for i in range(1,a+1):
    for j in range(a,0,-1):
        if i==j or i==a-j+1:
            print("x",end='')
        else:
            print("0",end='')
    print()
    l+=1
