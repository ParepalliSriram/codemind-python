a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
j=0
for i in b[::-1]:
    c+=i*pow(2,j)
    j+=1
print(c)