a=int(input())
b=a
c=0
if a<0:
    a=a*(-1)
while a:
    d=a%10
    a=a//10
    c=c*10+d
if b<0:
    print(c*(-1))
else:
    print(c)
