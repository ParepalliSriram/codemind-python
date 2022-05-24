a=str(input())
s=''
l=len(a)
c=0
p1=0
p2=0
for i in a:
    c+=1
    if i!=' ':
        s+=str(i)
    if i==' ' or c==l:
        p1=ord(min(s))
        p2=ord(max(s))
        print(abs(p1-p2),end=' ')
        s=''