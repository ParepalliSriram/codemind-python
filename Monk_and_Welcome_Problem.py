a=int(input())
m=[a]
b=[a]
m=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(0,a):
    for j in range(i,a):
        l.append(m[i]+b[j])
        break
for n in l:
    print(n,end=' ')