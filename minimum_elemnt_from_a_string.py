a=input()
b=a.split()
for i in range(len(b)-1,-1,-1):
    m=min(b[i])
    break
if m.isupper():
    j=m
    l=m.lower()
    if l in a:
        print(l)
    else:
        print(j)
else:
    print(m)