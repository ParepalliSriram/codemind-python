a=input()
b=a.split()
d=[]
c=0
for i in b:
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')
    c=0
