a=int(input())
b=a*a
c=0
while b!=0:
    d=b%10
    b=b//10
    c+=d
if c==a:
    print('Neon Number')
else:
    print('Not Neon Number')