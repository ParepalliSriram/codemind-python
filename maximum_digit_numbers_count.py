def cou(a):
    c=0
    d=1
    if a==0:
       return d
    elif a<0:
        a=a*(-1)
    while a:
        b=a%10
        a=a//10
        c+=1
    return c
a=int(input())
b=list(map(int,input().split()))
k=[]
for i in b:
    k.append(cou(i))
m=max(k)
s=[]
for i in b:
    if cou(i)==m:
        s.append(i)
p=[]
for i in s:
    if i not in p:
        p.append(i)
print(*p)