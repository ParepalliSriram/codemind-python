a=int(input())
b=[a]
b=list(map(int,input().split()))
c=0
co=0
if a%2!=0:
    b.append(0)
for i in range(0,a//2):
    
    c+=b[i]

for i in range((a//2),a):
    
    co+=b[i]

print(abs(c-co))