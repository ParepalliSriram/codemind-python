a=int(input())
d=a
c=0
if a<0:
    a=a*(-1)
while a!=0:
    b=a%10
    a=a//10
    c=c*10+b
if d>0:
    print(c)
else:
    print(c*-1)