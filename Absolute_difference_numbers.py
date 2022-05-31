a,b=map(int,input().split())
c=0
m=''
s=''
p=''
m=str(a)
for i in m:
    c+=1
    s+=str(i)
    if c==b:
        break
c=0
for i in m[::-1]:
    c+=1
    p+=str(i)
    if c==b:
        break
p=p[::-1]
f=int(s)
s=int(p)
print(abs(f-s))
