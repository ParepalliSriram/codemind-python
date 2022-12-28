a=input()
v='aeiou'
s=''
for i in range(0,len(a)):
    if a[i] in v:
        s+='V'
    else:
        s+='C'
s1=''
for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
        s1+='0'
    else:
        s1+=s[i]
s1+=s[len(s)-1]
for i in range(0,len(s1)):
    if(s1[i]!='0'):
        print(s1[i],end='')