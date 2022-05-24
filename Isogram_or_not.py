a=str(input())
c=0
for i in a:
    for j in a:
        if i==j:
            c+=1
    if c>1:
        print(False)
        break
    c=0
else:
    print(True)