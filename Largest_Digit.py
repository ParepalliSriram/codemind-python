a=int(input())
m=0
while a!=0:
    b=a%10
    a=a//10
    if b>m:
        m=b
print(m)