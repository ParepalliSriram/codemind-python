a=input()
b=a.split()
c=0
d=[]
for i in b:
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    d.append(c)
    c=0
m=min(d)
print(d.count(m))