a=input()
c=0
d=0
ans=0
a=a.lower()
b=a.split()
for i in range(0,len(b)):
    for j in b[i]:
        if j in 'aeiou':
            c=1
        break
    if c==1:
        for j in b[::-1]:
            if j not in 'aeiou':
                d=1
            break
        if d==1:
            ans+=1
    c=0
    d=0
print(ans)
        
    