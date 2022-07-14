a=input()
s=''
h=''
t='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'
z=0
for i in a:
    if i.isalpha():
        s+=i
    elif i==' ':
        t+=i
    else:
        h+=i
le=len(h)
s=sorted(s)
l=len(s)
j=0
p=0
for i in a:
    if i.isalpha():
        print(s[j],end='')
        j+=1
        if j>(l-1):
            break
    elif i==' ':
        print(t[z],end='')
        z+=1
    else:
        print(h[p],end='')
        p+=1
if p!=len(h)-1:
    for i in range(p,len(h)):
        print(h[i],end='')