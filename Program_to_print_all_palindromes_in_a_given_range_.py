def pol(a):
    c=0
    d=a
    while(a!=0):
        b=a%10
        a=a//10
        c=c*10+b
    if c==d:
        print(c,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    pol(i)