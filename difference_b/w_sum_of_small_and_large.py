a=str(input())
c=0
d=0
l=len(a)
s=''
p1=''
p2=''
ma=0
mi=0
for i in a:
    c+=1
    if i!=' ':
        s+=str(i)
    if i==' ' or c==l:
        p1+=min(s)
        p2+=max(s)
        s=''
for j in p1:
    ma+=ord(j)
for k in p2:
    mi+=ord(k)
print(abs(ma-mi))