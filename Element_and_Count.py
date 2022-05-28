a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
s=''
for i in b:
    if str(i) not in s:
        for j in b:
            if i==j:
                s+=str(i)
                c+=1
        print(i,c,end=' ')
    c=0
