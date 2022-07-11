a=input()
s=''
for i in a:
    if i in 'aeiouAEIOU':
        s+=i
d=''
for i in s:
    if i not in d:
        d+=i
print(*d)