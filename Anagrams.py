a=input()
b=input()
a=a.lower()
b=b.lower()
for i in a:
    if a.count(i)!=b.count(i):
        print(False)
        break
else:
    print(True)