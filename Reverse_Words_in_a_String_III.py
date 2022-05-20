a=str(input())
s=''

for i in a:
    if i!=' ':
        s+=i
    if i==' ':
        print(s[::-1],end=' ')
        s=''
        continue
print('',end='')
for j in a[::-1]:
    if j==' ':
        break
    else:
        print(j,end='')