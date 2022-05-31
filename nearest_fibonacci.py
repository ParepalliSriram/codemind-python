a=int(input())
b=0
c=1
m=[]
m.append(b)
m.append(c)
for i in range(2,50):
    ans=b+c
    m.append(ans)
    b=c
    c=ans
for i in range(0,50):
    if m[i]>=a:
        d=m[i]
        break
for i in range(0,50):
    if m[i]<=a:
        s=m[i]
if abs(a-d)<abs(a-s):
    print(d)
elif abs(a-d)==abs(a-s):
    print(s,d)
else:
    print(s)
