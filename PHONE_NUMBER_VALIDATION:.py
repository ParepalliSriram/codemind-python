a=int(input())
c=0
while a!=0:
    b=a%10
    a=a//10
    c+=1
if c==10:
    print('Valid')
else:
    print('Invalid')