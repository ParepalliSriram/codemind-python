a=str(input())
b=str(input())
a=a.lower()
b=b.lower()
s=''
p=''
for i in a:
    if i not in s:
        s+=str(i)
for j in b:
    if j not in p:
        p+=str(j)
    
c=0
m=0
for f in s:
    for g in p:
        if f==' ':
            continue
        if f==g:
            c+=1
    if c==1:
        m+=1
    c=0
print(m)