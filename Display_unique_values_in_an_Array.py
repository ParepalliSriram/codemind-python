a=int(input())
b=[a]
b=list(map(int,input().split()))
l=[]
c=0
m=0
for i in b:
    for j in b:
        if i==j:
            c+=1
    if c==1:
        m+=1
        l.append(i)
    c=0
if m>0:
    for i in l:
        print(i,end=' ')
else:
    print('-1')