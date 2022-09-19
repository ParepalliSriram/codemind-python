a=int(input())
arr=list(map(int,input().split()))
ar=[]
b,c=map(int,input().split())
d=0
for i in arr:
    if(i>=b and i<=c):
        continue
    else:
        d+=1
        ar.append(i)
if(d==0):
    print("-1")
else:
    print(min(ar))