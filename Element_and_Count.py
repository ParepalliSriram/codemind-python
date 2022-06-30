a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
d=[]
for i in b:
    if i not in d:
        d.append(i)
        for j in b:
            if i==j:
                c+=1
        print(i,c,end=' ')
        c=0
        