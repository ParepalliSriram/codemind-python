a=input()
b=a.split()
c='aeiouAEIOU'
k=0
for i in b:
    l=len(i)
    p=1
    co=0
    for j in range(0,l//2):
        if i[j] in c and i[0-p] not in c or i[j] not in c and i[0-p] in c:
            co+=1
        p+=1
    k+=co
print(k)