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
if pal(a):
    print(True)
else:
    print(False)