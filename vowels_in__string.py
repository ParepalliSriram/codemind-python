a=str(input())
c=0
s=''
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c+=1
        s+=i
if c>0:
    p=''
    for m in s:
        if m not in p:
            p+=m
    for n in p:
        print(n,end=' ')
else:
    print("-1")
