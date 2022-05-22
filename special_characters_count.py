a=str(input())
c=0
for i in a:
    if i.isalpha():
        continue
    if i.isnumeric():
        continue
    if i==' ':
        continue
    else:
        c+=1
print(c)