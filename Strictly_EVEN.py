a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,a):
    if i%2==0:
        if b[i]%2==0:
            c+=1
for i in b:
    if i%2==0:
        d+=1
if c==d:
    print(True)
else:
    print(False)