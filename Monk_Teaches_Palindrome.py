def check(a):
    b=len(a)
    if b%2==0:
        s='EVEN'
    else:
        s='ODD'
    p=''
    for i in a[::-1]:
        p+=i
    if p==a:
        print("YES",s,end='')
        print()
    else:
        print("NO")
a=int(input())
s=''
for i in range(0,a):
    b=str(input())
    check(b)