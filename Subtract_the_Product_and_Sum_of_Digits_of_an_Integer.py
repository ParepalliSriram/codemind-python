a=int(input())
c=0
p=1
while a!=0:
    b=a%10
    a=a//10
    c+=b
    p*=b
print(p-c)