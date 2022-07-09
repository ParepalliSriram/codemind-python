a,b=map(int,input().split())
if a>b:
    m=b
    l=a
else:
    m=a
    l=b
for i in range(m,10000):
    if i%a==0 and i%b==0:
        print(i)
        break
else:
    print(a*b)
