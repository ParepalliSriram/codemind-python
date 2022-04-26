import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
d=math.sqrt(ar)
print(format(d,".2f"))