l=''
s=''
s+=str(chr(91))
s+=str(chr(46))
s+=str(chr(93))
d=s
a=str(input())
for i in a:
    if i=='.':
        i=d
    l+=i
print(l)