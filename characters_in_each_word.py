a=str(input())
c=0
s=''
m=0
n=0
for j in a:
    m+=1
for i in a:
    n+=1
    if i!=' ':
        c+=1
    if i==' ' or n==m:
        print(c,end=' ')
        c=0
