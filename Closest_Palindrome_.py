def pal(a):
    b=a
    c=0
    while a:
        d=a%10
        a=a//10
        c=c*10+d
    if c==b:
        return 1
    else:
        return 0
a=int(input())
for i in range(a+1,a+1000):
    if pal(i):
        f=i
        break
for i in range(a-1,-1,-1):
    if pal(i):
        s=i
        break
if abs(a-f)==abs(a-s):
    print(s,f)
elif abs(a-f)<abs(a-s):
    print(f)
else:
    print(s)