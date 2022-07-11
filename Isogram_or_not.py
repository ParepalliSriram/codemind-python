a=input()
for i in a:
    if a.count(i)!=1:
        print(False)
        break
else:
    print(True)