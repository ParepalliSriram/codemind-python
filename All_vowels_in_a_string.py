a=str(input())
c=0
d=0
e=0
f=0
g=0
if 'a' in a:
    c+=1
if 'e' in a:
    d+=1
if 'i' in a:
    e+=1
if 'o' in a:
    f+=1
if 'u' in a:
    g+=1
if c>0 and d>0 and e>0 and f>0 and g>0:
    print(True)
else:
    print(False)
