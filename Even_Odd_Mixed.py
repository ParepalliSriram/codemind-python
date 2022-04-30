a=int(input())
b=0
c=0
d=0
while a!=0:
    e=a%10
    a=a//10
    if(e%2==0):
        b+=1
    else:
        c+=1
if b>0 and c==0:
    print('Even')
elif b==0 and c>0:
    print('Odd')
else:
    print('Mixed')