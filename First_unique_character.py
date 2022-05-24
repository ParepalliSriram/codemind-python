a=str(input())
c=0
h=0
for i in a:
    for j in a:
        if i==j:
            c+=1
    if c==1:
        h=1
        print(i)
        break
    c=0
if h==0:
    print("-1")