a=int(input())
b=[a]
b=list(map(int,input().split()))
s=[]
for i in b:
    if i not in s:
        s.append(i)
print(*s)
