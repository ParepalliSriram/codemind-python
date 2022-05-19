a=str(input())
c=0
for element in a:
    if element>=chr(97) and element<=chr(122):
        c+=1
print(c)