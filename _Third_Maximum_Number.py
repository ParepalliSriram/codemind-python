a=int(input())
m=[a]
m=list(map(int,input().split()))
b=set(m)
if a<=2:
    print(max(b))
else:
    c=max(b)
    b.remove(c)
    d=max(b)
    b.remove(d)
    print(max(b))