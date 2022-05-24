a=str(input())
s=''
l=len(a)
c=0
for i in a:
    c+=1
    if i!=' ':
        s+=str(i)
    if i==' ' or c==l:
        print(min(s),max(s),end=' ')
        s=''