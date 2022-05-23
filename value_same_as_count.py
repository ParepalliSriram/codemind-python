a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
l=0
do=0
p=''
s=''
for i in range(0,a):
    for j in range(0,a):
        if b[i]==b[j]:
            c+=1
    if c==b[i]:
        l+=1
        s+=str(b[i])
    c=0
for d in s:
    if d not in p:
        p=p+d
for j in p:
    do+=1
print(do)
    