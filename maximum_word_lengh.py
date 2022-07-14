a=input()
b=a.split()
s=[]
for i in b:
    s.append(len(i))
print(max(s))