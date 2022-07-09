a=int(input())
b=[]
b.append(0)
b.append(1)
for i in range(2,31):
    b.append(b[i-1]+b[i-2])
for i in b:
    if i>a:
        g=i
        break
    else:
        m=i
if abs(a-g)==abs(a-m):
    print(m,g)
elif abs(a-g)>abs(a-m):
    print(m)
else:
    print(g)