a=str(input())
b=str(input())
c=0
for i in a:
    c+=1
    if i==b:
        print(True)
        print(c-1)
        break
else:
    print(False)