import math
a=int(input())
b=math.sqrt(a)
c=round(b)
if c*c==a:
    print(True)
else:
    print(False)