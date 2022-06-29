a=input()
a=a.lower()
s=''
c=0
for i in a:
    for j in a:
        if i==j:
            c+=1
    if c==1:
        print(i)
        break
    c=0
else:
    print("-1")