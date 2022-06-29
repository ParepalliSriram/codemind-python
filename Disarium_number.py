a=int(input())
c=a
m=a
k=0
while a:
    b=a%10
    a=a//10
    k+=1
l=0
while c:
    d=c%10
    c=c//10
    l+=d**k
    k=k-1
if l==m:
    print(True)
else:
    print(False)