a,b=map(int,input().split())
c=[a]
c=list(map(int,input().split()))
d=[b]
d=list(map(int,input().split()))
e=[]
f=[]
count=0
for i in c:
    if i not in e:
        e.append(i)
for i in d:
    if i not in f:
        f.append(i)
for i in e:
    if i not in f:
        count+=1
for i in f:
    if i not in e:
        count+=1
print(count)