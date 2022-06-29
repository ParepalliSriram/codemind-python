a=input()
a=a.lower()
s=''
c=0
for i in a:
    for j in a:
        if i==j:
            c+=1
    if c==1:
        if i!=' ':
            s+=i
    c=0
s=sorted(s)
for i in s:
    print(i,end='')