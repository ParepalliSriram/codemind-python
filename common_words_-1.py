s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=s1.split()
b=s2.split()
c=0
if len(a)>len(b):
    for i in a:
        if i in b:
            c+=1
else:
    for i in b:
        if i in a:
            c+=1
print(c)