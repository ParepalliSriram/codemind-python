a=str(input())
c=0
for element in a:
    if element>=chr(65) and element<=chr(90):
        c+=1
print(c)