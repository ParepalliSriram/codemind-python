a=int(input())
s=''
for i in range(0,a):
    b=str(input())
    if(any(chr.isdigit() for chr in b)):
        print("Yes")
    else:
        print("No")