a=input()
a=a.lower()
b=a.split()
c=0
s=''
d=b[0]
for i in d:
    for j in b:
        if i in j:
            c+=1
    if c==len(b):
        s+=i
    c=0
if len(s)==0:
    print("-1")
else:
    print(min(s))