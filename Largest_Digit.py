a=int(input())
b=[]
while a:
    c=a%10
    a=a//10
    b.append(c)
print(max(b))