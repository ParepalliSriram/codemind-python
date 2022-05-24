a=str(input())
l=len(a)
s=''
c=0
ans=0
v=0
u=0
for i in a:
    c+=1
    if i!=' ':
        s+=str(i)
    if i==' ' or c==l:
        for j in s:
            m=j
            break
        for j in s[::-1]:
            n=j
            break
        if m=='a' or m=='e' or m=='i' or m=='o' or m=='u' or m=='A' or m=='E' or m=='I' or m=='O' or m=='U':
            v+=1
        if n!='a' and n!='e' and n!='i' and n!='o' and n!='u' and n!='A' and n!='E' and n!='I' and n!='O' and n!='U':
            u+=1
        if u==1 and v==1:
            ans+=1
        s=''
        v=0
        u=0
print(ans)