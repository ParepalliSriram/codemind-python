a=input()
m=max(a)
j=''
for i in a:
    if i!=' ':
        j+=i
mm=min(j)
c=a.count(m)
d=a.count(mm)
print(mm,d,m,c)