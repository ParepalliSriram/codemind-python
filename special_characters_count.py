a=input()
a=a.lower()
c=0
for i in a:
    if i.isalpha() or i==' ':
        continue
    else:
        c+=1
print(c)