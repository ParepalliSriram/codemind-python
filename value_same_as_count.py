a=int(input())
b=[]
b=list(map(int,input().split()))
c=[]
co=0
s=[]
for i in b:
    if b.count(i)==i:
        c.append(i)
for i in c:
    if i not in s:
        s.append(i)
        co+=1
print(co)