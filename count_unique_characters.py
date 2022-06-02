a=str(input())
a=a.lower()
c=0
s=0
for i in a:
    
    for j in a:
        if i==' ':
            break
        elif i==j:
            c+=1
    if c==1:
        s+=1
    c=0
print(s)