a=str(input())
a=a.lower()
b=[]
for i in a:
    if i==' ':
        continue
    else:
        b.append(i)
s=set(b)
b=list(s)
print(len(b))