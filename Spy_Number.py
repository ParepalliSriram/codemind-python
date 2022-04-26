a=int(input())
tot=0
pro=1
while a>0:
    b=a%10
    a=a//10
    tot=tot+b
    pro=pro*b
if tot==pro:
    print('Spy Number')
else:
    print('Not Spy Number')