a=int(input())
j=a
b=a*a
c=0
f=0
g=0
i=0
while a!=0:
    d=a%10
    a=a//10
    c+=1
while b!=0:
    e=b%10
    b=b//10
    f+=1
    g=g*10+e
    if f==c:
        break
while g!=0:
    h=g%10
    g=g//10
    i=i*10+h
if i==j:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")