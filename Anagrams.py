a=str(input())
b=str(input())
l=len(a)
c=0
for i in a:
    for j in a:
        if i in b:
            c+=1
    if c<1:
        print(False)
        break
else:
    print(True)
        