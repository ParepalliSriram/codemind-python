a=int(input())
b=[]
while a:
    c=a%10
    a=a//10
    b.append(c)
b=b[::-1]
for i in range(0,len(b)):
    if b[i]==6:
        b[i]=9
        break
for i in b:
    print(i,end='')