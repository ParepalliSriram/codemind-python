a=str(input())
a=a.lower()
m=set(a)
a=str(m)
c=0
s=''
for i in a:
    for j in a:
        if i==j:
            c+=1
    if c==1:
        s+=str(i)
    c=0
s=sorted(s)
for i in s:
    if i=='{' or i=='}':
        continue
    else:
        print(i,end='')