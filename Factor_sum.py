def p_s(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=i
    return c
a=str(input())
b=[]
for i in a:
    if i!=',':
        b.append(int(i))
n=''
k=0
m=str(b)
for i in b:
    d=p_s(i)
    if str(d) in m:
        k+=1
        n+=str(i)
    d=0
if k==0:
    print("-1")
else:
    n=sorted(n)
    print(*n)
