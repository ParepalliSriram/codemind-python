a=int(input())
c=0
for i in range(1,a+1):
    if i*i==a:
        print("True")
        c+=1
if c==0:
    print("False")