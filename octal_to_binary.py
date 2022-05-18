def dec(a):
    b=len(str(a))
    l=0
    d=0
    while a!=0:
        c=a%10
        d+=c*(8**l)
        a=a//10
        l+=1
        if l==b:
            break
    return d
a=int(input())
ans=dec(a)
print(bin(ans)[2:])