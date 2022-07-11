a=input()
b=a.split()
for i in range(0,len(b)):
    print(min(b[i]),max(b[i]),end=' ')