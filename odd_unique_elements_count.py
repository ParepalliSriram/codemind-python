a=int(input())
b=[a]
b=list(map(int,input().split()))
l=set(b)
b=list(l)
c=0
for i in b:
    if i%2!=0:
        if b.count(i)==1:
            c+=1
print(c)
