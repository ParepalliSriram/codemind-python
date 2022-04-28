a=int(input())
if a<=100 and a>=3:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print('*',end="")
        print()
    for k in range(a-1,0,-1):
        for l in range(k,0,-1):
            print('*',end="")
        print()
else:
    print('The pattern is not possible')