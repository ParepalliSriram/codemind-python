a=int(input())
c=0
p=1
while a:
    b=a%10
    a=a//10
    c+=b
    p=p*b
if c==p:
    print("Spy Number")
else:
    print("Not Spy Number")