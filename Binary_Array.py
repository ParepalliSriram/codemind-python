a=int(input())
b=input()
for i in b:
    if i not in '01 ':
        print(False)
        break
else:
    print(True)