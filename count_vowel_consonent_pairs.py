a=input()
l=len(a)
l=l//2
c='aeiouAEIOU'
co=0
p=1
for i in range(0,l):
    if a[i] in c and a[0-p] not in c and a[0-p]!=' ' or a[i] not in c and a[0-p] in c and a[i]!=' ':
        co+=1
    p+=1
print(co)