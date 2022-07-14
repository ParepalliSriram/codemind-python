a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,len(b)-2,2):
    if b[i]<b[i+1] and b[i+1]>b[i+2]:
        c+=1
    else:
        d+=1
        print("-1")
        break
if d==0:
    print(c)