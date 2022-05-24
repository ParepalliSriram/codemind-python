a=str(input())
l=len(a)

c=0
s=0
p=''
for i in a:
    c+=1
    if i!=' ':
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            s+=1
    if i==' ' or c==l:
        p+=str(s)
        s=0
print(min(p))
    
