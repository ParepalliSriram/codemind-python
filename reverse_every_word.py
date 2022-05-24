a=str(input())
l=0
k=0
for i in a:
    l+=1
s=''
c=0
for i in a:
    k+=1
    if i!=' ':
       s+=str(i)
    if i==' ' or k==l:
        print(s[::-1],end=' ')
        s=''
