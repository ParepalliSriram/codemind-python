a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==j or j==1 or i==a:
            print("*",end='')
        else:
            print(" ",end='')
    print()
