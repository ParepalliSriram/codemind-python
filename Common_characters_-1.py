a=input()
a=a.lower()
b=a.split()
c=b[0]
co=0
k=0
for j in c:
    for i in b:
        if j in i:
            co+=1
    if co==len(b):
        k+=1
        print(j,end='')
    co=0
if k==0:
    print("-1")