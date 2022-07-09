def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=[]
for i in range(1,a):
    if a%i==0:
        b.append(i)
p=[]
for i in b:
    if prime(i):
        p.append(i)
co=0
for i in range(0,len(p)-1):
    if p[i]*p[i+1]==a:
        co+=1
        print(p[i],p[i+1])
        break
if co==0:
    print("-1")