a=input()
b=a.split()
for i in b[::-1]:
    for j in range(0,len(i)):
        print(i[0])
        break
    break