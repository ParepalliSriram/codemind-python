a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
l=0
for i in range(0,a):
    for j in range(i,a):
        if b[i]==b[j]:
            c+=1
    if c==1:
        l+=b[i]
    c=0
print(l)
        