a=str(input())
s=''
d=0
c=0
for i in a:
    if i>='A' and i<='Z':
        b=ord(i)
        i=chr(b+32)
    s+=str(i)
p=''
l=len(s)
for j in s:
    c+=1
    if j!=' ':
        p+=str(j)
    if j==' ' or c==l:
        if p==p[::-1]:
            d+=1
            p=''
        else:
            p=''
print(d)