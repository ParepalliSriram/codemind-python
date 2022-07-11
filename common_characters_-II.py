a=input()
b=input()
a=a.lower()
b=b.lower()
s=''
for i in a:
    if i==' ':
        continue
    else:
        if i in b:
            s+=i
for i in b:
    if i==' ':
        continue
    else:
        if i in a:
            s+=i
s=sorted(s)
p=''
for i in s:
    if i not in p:
        p+=i
print(len(p))