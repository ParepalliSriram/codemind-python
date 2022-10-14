import math
def prime(a):
    if a<2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            return 0
    return 1
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if(prime(i)):
        count+=1
print(count)