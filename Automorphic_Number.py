a=int(input())
b=a
c=0
while a:
   d=a%10
   a=a//10
   c+=1
e=b*b
f=0
h=0
while e:
    f+=1
    g=e%10
    e=e//10
    h=h*10+g
    if f==c:
        break
i=0
while h:
    j=h%10
    h=h//10
    i=i*10+j
if i==b:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")