a=int(input())
l=list(map(int,input().split()))
p=0
s=set(l)
s1=list(s)
l1=[]
l2=[]
for i in range(0,len(s1)):
    l1.append(s1[i])
    l2.append(l.count(s1[i]))
m=max(l2)
k=l2.index(m)
print(l1[k])