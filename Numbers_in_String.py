a=str(input())
c=0
for i in a:
    if i.isnumeric():
        c+=int(i)
print(c)