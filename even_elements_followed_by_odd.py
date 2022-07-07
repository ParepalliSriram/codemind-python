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
print(*e,end=' ')
print(*o)