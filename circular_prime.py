a=int(input())
c=0
ci=0
m=0
for i in range(1,a+1):
    if(a%i==0):
        c+=1
while(a!=0):
    b=a%10
    a=a//10
    ci=ci*10+b
for j in range(1,ci+1):
    if(ci%j==0):
        m+=1
if c==2 and m==2:
    print('circular prime')
elif c==2 and m!=2:
    print('prime but not a circular prime')
else:
    print('not prime')