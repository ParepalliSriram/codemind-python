a=input()
b=a.split()
for i in range(0,len(b)):
    print(min(b[i]),end=' ')
    break
for i in range(len(b)-1,-1,-1):
    print(max(b[i]))
    break