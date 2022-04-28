a=int(input())
b=a
c=0
while a!=0:
    d=a%10
    a=a//10
    c+=d
if b%c==0:
    print('True')
else:
    print('False')