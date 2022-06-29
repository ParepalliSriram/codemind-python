def rev(a):
    c=0
    while a:
        b=a%10
        a=a//10
        c=c*10+b
    return c
a=int(input())
b=a*a
r_g=rev(a)
s_r_g=(r_g)**2
if rev(s_r_g)==b:
    print(True)
else:
    print(False)