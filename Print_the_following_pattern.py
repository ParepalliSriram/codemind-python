a=int(input())
b=a
for i in range(1,a+1):
    for k in range(1,a+1):
        if k==i or k==a-i+1:
            print(b,end=" ")
        else:
            print(" ",end="");
    print()
    b-=1;