a,b=map(int,input().split())
c=[]
c=list(map(int,input().split()))
cou=0
for i in c:
    if i%b!=0:
        cou+=1
print(cou)