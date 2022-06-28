a=int(input())
b=[]
c=0
while a:
    d=a%10
    a=a//10
    b.append(d)
for i in b:
    for j in b:
        if i==j:
            c+=1
    if c>1:
        print("Not Unique Number")
        break
    c=0
else:
    print("Unique Number")
