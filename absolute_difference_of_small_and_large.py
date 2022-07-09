a=str(input())
l=len(a)
b=''
c=1
for i in a:
    if i!=' ':
        b+=i
    if i==' ' or c==l-1:
        d=ord(min(b))
        k=ord(max(b))
        print(abs(d-k),end=' ')
        b=''
    c+=1