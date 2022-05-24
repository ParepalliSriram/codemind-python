a=str(input())
s=''
ma=0
mi=0
for i in a:
    if i!=' ':
        s+=str(i)
for i in a:
    if i==min(s):
        ma+=1
    if i==max(s):
        mi+=1
print(min(s),ma,max(s),mi,end=' ')