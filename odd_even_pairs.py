a=int(input())
b=[a]
b=list(map(int,input().split()))
e=[]
o=[]
for i in b:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)>len(o):
    c=0
    for i in range(0,len(o)):
        c+=1
        print(o[i],e[i],end=' ')
    for i in range(c,len(e)):
        print(e[i],end=' ')
else:
    c=0
    for i in range(0,len(e)):
        c+=1
        print(o[i],e[i],end=' ')
    for i in range(c,len(o)):
        print(o[i],end=' ')
if a%2!=0:
    print("0")